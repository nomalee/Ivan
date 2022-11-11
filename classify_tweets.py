from googletrans import Translator
import torch
import torch.nn as nn
import transformers
from transformers import AutoModel, BertTokenizerFast
from transformers import logging
import numpy as np
logging.set_verbosity_error()

class BERT_Arch(nn.Module):

    def __init__(self, bert):
      super(BERT_Arch, self).__init__()
      self.bert = bert 
      # dropout layer
      self.dropout = nn.Dropout(0.1)
      # relu activation function
      self.relu =  nn.ReLU()
      # dense layer 1
      self.fc1 = nn.Linear(768,512)
      # dense layer 2 (Output layer)
      self.fc2 = nn.Linear(512,2)
      #softmax activation function
      self.softmax = nn.LogSoftmax(dim=1)

    #define the forward pass
    def forward(self, sent_id, mask):
      #pass the inputs to the model  
      _, cls_hs = self.bert(sent_id, attention_mask=mask, return_dict=False)
      x = self.fc1(cls_hs)
      x = self.relu(x)
      x = self.dropout(x)
      # output layer
      x = self.fc2(x)
      # apply softmax activation
      x = self.softmax(x)
      return x

def classify_mil_text(tweet_text):

	# specify GPU
	device = torch.device("cpu")

	# import BERT-base pretrained model
	bert = AutoModel.from_pretrained('bert-base-uncased')
	tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")

	# pass the pre-trained BERT to our define architecture
	model = BERT_Arch(bert)

	# push the model to GPU
	model = model.to(device)

	#load weights of best model
	path = 'saved_weights.pt'
	model.load_state_dict(torch.load(path))

	translator = Translator()
	if translator.detect(tweet_text).lang != 'en':
		#print('Non-English language detected...traslating')
		tweet_text = translator.translate(tweet_text, dest='en').text

	tokens_test_one = tokenizer.batch_encode_plus(
		[tweet_text],
		max_length = 25,
		#pad_to_max_length=True,
		truncation=True
	)

	## convert lists to tensors
	test_seq_one = torch.tensor(tokens_test_one['input_ids'])
	test_mask_one = torch.tensor(tokens_test_one['attention_mask'])

	# get predictions for test data
	with torch.no_grad():
		#preds = model(test_seq.to(device), test_mask.to(device))
		preds = model(test_seq_one.to(device), test_mask_one.to(device))
		probs = torch.nn.functional.softmax(preds, dim=1)
		preds = preds.detach().cpu().numpy()
		#print(probs)

	preds = np.argmax(preds, axis = 1)

	if preds[0] == 0:
		return {'pred':'military', 'prob_mil': probs[0][0], 'prob_non_mil': probs[0][1]}
	else:
		return {'pred':'non-military', 'prob_mil': probs[0][0], 'prob_non_mil': probs[0][1]}


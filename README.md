# Ivan

Ivan is a Twitter agent that collects and analyzes live tweets, automatically recognizing tweets relevant to the Russo-Ukrainian war.

Forked from [tankbuster](https://github.com/thiippal/tankbuster), a deep learning engine trained to detect Russia-made MBTs (such as the T-72) and BMTs, Ivan also collects tweet texts and identifies whether they are related to the military domain using NLP (Natural Language Processing) technology. As well as English, Ivan supports 133 different languages including Russian and Ukrainan as Google Translate does.

## Installation

Ivan can be installed by cloning the repository. To do so, enter the following command:

<code>git clone https://github.com/nomalee/Ivan.git</code>

Ivan requires the following libraries to run the code.

- PyTorch v1.13.0
- BERT v4.24.0
- tweepy v4.12.1
- googletrans v3.1.0a0
- numpy v1.23.4
- pandas v1.5.1

Other libraries may be required. You can refer to the [tankbuster](https://github.com/thiippal/tankbuster) repository for checking out the libraries required by [tankbuster](https://github.com/thiippal/tankbuster).

## Usage

Please note that Ivan uses Twitter API v2, therefore, all the names and syntax related to Twitter API hereafter are applied accordingly. Before running Ivan, you need to edit the configuration part in twitter_streaming.py. A bearer token can be claimed from Twitter.

<code>BEARER_TOKEN = 'Put Your BEAR_TOKEN here'</code>

In addition, it is recommended to edit the filtering rule in the same configuration part for better results in the initial filtering phase:

<code>filtering_rule = 'has:media Ukraine OR Kherson OR War OR tank OR танк'</code>

A paid subscription to Twitter provides a wider range of filtering options. You can cansult [Twitter API Documentation](https://developer.twitter.com/en/docs/twitter-api) for a better understanding of Twitter's subscription plans and filtering options. Then, you can run Ivan with the following commend on CLI.

<code>python ./twitter_streaming.py</code>

## Results

Tweets that passed final determination are archived in tweet_data.csv (the file name can be edited in the configuration part) with mata-data including user id, user name, tweet address, tweet text, image url and GPS coordinates (if any). The following are some screeshots of tweets collected by the Ivan agent.

<img src="https://github.com/nomalee/Ivan/blob/master/images/IMG_6611.jpg" width="260">

<img src="https://github.com/nomalee/Ivan/blob/master/images/IMG_6613.jpg" width="260">

<img src="https://github.com/nomalee/Ivan/blob/master/images/IMG_6615.jpg" width="260">

<img src="https://github.com/nomalee/Ivan/blob/master/images/IMG_6617.jpg" width="260">

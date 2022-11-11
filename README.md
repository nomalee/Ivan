# Ivan

Ivan is a twitter agent that collects and analyzes live tweets, recognizying tweets relavent to the Russo-Ukraine war in an automated manner.

Forked from tankbuster, which is a deep learning engine trained to detect Russia-made MBTs (e.g., T-72) and BMTs, Ivan also collects tweet texts and identify whether they are related to the military domain based on NLP (Natural Language Processing) technology.

## Installation

Ivan can be installed by cloning the repository. To do so, enter the following command:

<code>git clone https://github.com/nomalee/Ivan.git</code>

Ivan requires the following libraries to run the code.

- PyTorch v1.13.0
- BERT v4.24.0
- googletrans v3.1.0a0
- numpy v1.23.4
- pandas v1.5.1

Other libaries may be required. You can refer to the [tankbuster]([url](https://github.com/thiippal/tankbuster)) repository for checking out the libraries required by tankbuster.

## Usage

Before running Ivan, you need to edit the configuration part in twitter_streaming.py. A bearer token can be claimed from Twitter.

<code>
  BEARER_TOKEN = 'Put Your BEAR_TOKEN here'
</code>

Then, you can run Ivan with the following commend on CLI.

<code>python ./twitter_streaming.py</code>

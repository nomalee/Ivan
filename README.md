# Ivan

Ivan is a Twitter agent that collects and analyzes live tweets, automatically recognizing tweets relevant to the Russo-Ukrainian war.

Forked from tankbuster, a deep learning engine trained to detect Russia-made MBTs (such as the T-72) and BMTs, Ivan also collects tweet texts and identifies whether they are related to the military domain using NLP (Natural Language Processing) technology.

## Installation

Ivan can be installed by cloning the repository. To do so, enter the following command:

<code>git clone https://github.com/nomalee/Ivan.git</code>

Ivan requires the following libraries to run the code.

- PyTorch v1.13.0
- BERT v4.24.0
- googletrans v3.1.0a0
- numpy v1.23.4
- pandas v1.5.1

Other libraries may be required. You can refer to the [tankbuster]([url](https://github.com/thiippal/tankbuster)) repository for checking out the libraries required by tankbuster.

## Usage

Before running Ivan, you need to edit the configuration part in twitter_streaming.py. A bearer token can be claimed from Twitter.

<code>
  BEARER_TOKEN = 'Put Your BEAR_TOKEN here'
</code>

Then, you can run Ivan with the following commend on CLI.

<code>python ./twitter_streaming.py</code>

## Results

<iframe><blockquote class="twitter-tweet"><p lang="en" dir="ltr"><a href="https://twitter.com/hashtag/Ukrainian?src=hash&amp;ref_src=twsrc%5Etfw">#Ukrainian</a> Paratroopers won a <a href="https://twitter.com/hashtag/T80BVM?src=hash&amp;ref_src=twsrc%5Etfw">#T80BVM</a> tank.<br><br>Glory to the <a href="https://twitter.com/hashtag/DSHV?src=hash&amp;ref_src=twsrc%5Etfw">#DSHV</a>, Glory to the <a href="https://twitter.com/hashtag/ZSU?src=hash&amp;ref_src=twsrc%5Etfw">#ZSU</a>!!!<br><br>Video: <a href="https://twitter.com/hashtag/OleksandrPogrebyskyi?src=hash&amp;ref_src=twsrc%5Etfw">#OleksandrPogrebyskyi</a> <a href="https://t.co/vJFdQZBiL4">pic.twitter.com/vJFdQZBiL4</a></p>&mdash; Lientjie 👑 (@news_globally) <a href="https://twitter.com/news_globally/status/1588905709714169856?ref_src=twsrc%5Etfw">November 5, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script></iframe>

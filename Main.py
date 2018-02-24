import tweepy

TWITTER_CLIENT = "kwykBA0bYzMqcHoFl29zK1OQa"
TWITTER_SECRET = "xyR4hegGMoQxCiDPrqmr4CLGm41DqG1rQDDDMrQRLJwRXBYd3O"
TWITTER_ACCESS = "967433840183709696-DRyKObUSKI7WbOmoePl0O3GBff8DYxV"
TWITTER_ACCESS_SECRET = "Veyq0L0SKkByptUD1CYlR2XkgjYDhJObzwbigbFrTe76A"

auth = tweepy.OAuthHandler(TWITTER_CLIENT, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS, TWITTER_ACCESS_SECRET)

api = tweepy.API(auth)

try:
    api.update_status("Hello, world!")
except TweepyError:
    print "Could not tweet"
    
    def main():
  # Open and read corpus
  corpus = open("simple-corpus.txt", "r")
  word_lines = corpus.readlines()
  corpus.close()

if __name__ == '__main__':
  main()

sentence_starters = []

# Create map of words
# word_lines is a list of strings that represents our file
def create_word_map(word_lines):
  word_map = dict()

  # Go through each line in our corpus
  for line in word_lines:
    
    # Split each line into a list of words
    words = line.split()

    end_of_sentence = True
    
    # Go through each word in our corpus line
    for index in range(0,len(words)-2):
      
      # If we're at the end of a sentence, add the start of the next sentence
      # to our array of sentence starters
      if end_of_sentence:
        sentence_starters.append((words[index], words[index + 1]))
        end_of_sentence = False

      # Check if at the end of sentence
      if words[index + 1] == "?" or words[index + 1] == "." or words[index + 1] == "!":
        end_of_sentence = True

      # Add word pairings to our word_map
      if (words[index], words[index + 1]) in word_map.keys():
        word_map[(words[index], words[index + 1])].append(words[index + 2])
      else:
        word_map[(words[index], words[index + 1])] = [words[index + 2]]

  return word_map

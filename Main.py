import random
from nltk.tokenize import RegexpTokenizer


# VARIABLES TO READ IN SENTENCES FROM TEXT
sentences = open("Sentences.txt").readlines()  # reads from the Sentences.txt file
random.shuffle(sentences)                      # shuffles the sentences
number_of_sentences = len(sentences)           # counts the number of sentences


# MAIN METHOD
def main():

    sentence_index = 0  # indicates which sentence is being pulled from the .txt file
    score = 0           # keeps track of the current score
    is_running = True   # maintains that the game is running

    print("Can you identify the verbs in each sentence? Let's find out!\n")

    while is_running:

        # separates the words in the sentence
        tokenizer = RegexpTokenizer(r'\w+')
        words = tokenizer.tokenize(sentences[sentence_index])

        # identifies the verb
        first_word_to_identify = words[1]

        # reads user input
        print(' '.join(words) + "\n")
        answer = input("In the sentence above, identify the verb.\n")

        # checks if the user input matches the verb
        words[1] = str.upper(first_word_to_identify)
        if str.lower(answer) == first_word_to_identify:
            print("You are right!\n" + ' '.join(words) + "\n\n")
            score += 1
        else:
            print("Mmm, sorry. That isn't correct.\n" + ' '.join(words) + "\n\n")
        sentence_index += 1

        # prints the user score at the end of the game
        if sentence_index == 10:
            is_running = False
            if score == 10:
                print("You got a perfect score out of 10! Wow! Great job!\n")
            if 8 <= score <= 9:
                print("Your score is " + str(score) + " of 10. Nice job!\n")
            elif 5 <= score <= 7:
                print("Your score is " + str(score) + " of 10. You did okay, but try harder next time!\n")
            elif score <= 4:
                print("Your score is " + str(score) + " of 10. Looks like you need to brush up on some grammar.\n")


# RUNS MAIN METHOD
main()

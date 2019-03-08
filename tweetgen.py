import random

def histogram(list_of_words):
    '''returns histogram, list of lists.'''
    hist_lol = []
    for word in list_of_words:
        found = False
        for list in hist_lol:
            if word in list:
                list[1] += 1
                found = True
        if not found:
            hist_lol.append([word, 1])
    # print(hist_lol)
    return hist_lol

def hist_probability_distribution(histogram):
    '''takes a histogram and returns an array of the probabilty distribution'''
    # takes in a dictogram (list of lists)
    sample_size = 0
    for element in histogram:
        sample_size += element[1]
    # print(sample_size)
    range = 0
    list_of_values = []
    for pair in histogram:
        range += float(pair[1]) /float(sample_size)
        list_of_values.append(range)
    return list_of_values

def sample_word(histogram, probability_distribution):
    '''takes a histogram and its probability distribution and returns a random word '''
    rando = random.random()
    for i in range(len(probability_distribution)):
        if probability_distribution[i] > rando:
            return histogram[i][0]

def sample_words_by_frequency(histogram, n = 1):
    '''takes in a histogram and creates a probability distribution.
        Also takes in n, number of words outputted'''
    probability_distribution = hist_probability_distribution(histogram)
    output_string = ''
    for i in range(n):
        random_word = sample_word(histogram, probability_distribution)
        if random_word:
            output_string += random_word + ' '
    return output_string


f = open('frankenstein.txt' , 'r')
file = [word for line in f.read().split('\n') for word in line.split(' ')]
f.close()

hist = histogram(file)
text = sample_words_by_frequency(hist, 10)
print(text)
# print(len(file))

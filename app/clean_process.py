# from textblob import TextBlob
import re
from langdetect import detect


def SentenceCleaner(line):
    line = re.sub(r"(')(\w+)(')", r" ", line)
    line = re.sub(r'[.?!]$', ' ', line)
    line = re.sub(r'[)]', '  ', line)
    line = re.sub(r'[(]', '  ', line)
    line = re.sub(r'["]', '  ', line)
    line = re.sub(r'[“]', '  ', line)
    line = re.sub(r'[!]', '  ', line)
    line = re.sub(r',[^\d\w]', '  ', line)
    line = re.sub(r'[,]', '  ', line)
    line = re.sub(r'\s+', ' ', line)
    line = re.sub(r'[-]', '  ', line)
    return line


def tokenizer(data):
    textData = re.sub("[?]", "  END", data)
    textData = re.sub("[।] [\"]", " END", textData)
    textData = re.sub("[।]", " END", textData)
    textData = re.sub("[|]", " END", textData)
    textData = re.sub("[\n]", " END", textData)
    textData = re.sub("\r\n", " END", textData)
    textData = re.sub("[.]", " END", textData)
    Sen = re.split("END", textData)
    sentences = '\n'.join([SentenceCleaner(i)
                           for i in Sen if len(i.strip()) > 1])
    return sentences


def clean(data):
    output = tokenizer(' '.join([i for i in list(data)]))
    return output

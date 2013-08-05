#!/usr/bin/env python

import nltk.data
from nltk import word_tokenize
from nltk.corpus import stopwords

def content_to_sentences(text):
    """
    Converts passed text into a list of sentences.
    """
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    return tokenizer.tokenize(text)

def sentence_to_words(sentence):
    """
    Converts passed sentences into a list of words.
    Returns all words but stop words.
    """
    #all_words = word_tokenize(sentence)
    #return [word for word in all_words if word not in stopwords.words('english')]
    return word_tokenize(sentence)


if __name__ == '__main__':
    # partial content from http://www.nytimes.com/2013/07/08/opinion/immigration-in-the-house.html
    text = """
    Four immigration bills have passed the House Judiciary Committee, each with 
    its own nonanswers. The SAFE Act doubles down on the failed strategy of trying 
    to force millions of immigrants to self-deport. It would free states to write 
    their own immigration laws, give state and local law enforcement more power to
    make immigration arrests, and remove the discretion for the Homeland Security
    Department to defer the deportations of harmless immigrants in favor of all-out,
    indiscriminate enforcement. The Ag Act would make it easier to exploit cheap
    emporary workers, who would be deported when their jobs were done. The Legal
    orkforce Act would vastly expand the use of federal electronic databases to
    screen job applicants, an invitation to discrimination. And the Skills Visa
    Act would create an immigration path for thousands of entrepreneurs and workers
    in science, technology, engineering and math fields - a worthwhile goal but a
    very narrow one.

    A bipartisan gang of House members has been working on a broader bill, but nobody
    has seen it yet and it may go nowhere because it is said to include a path to
    citizenship. About all that can be safely predicted is that we are in for a
    summer of heat and pressure, with immigrant advocates loudly demanding a bill
    and defiant Republicans digging in to make sure that reform collapses.

    If only enough House Republicans could see that the bill is one that embraces
    many of their own priorities. It shrinks the deficit and satisfies big-business
    interests with more visas for agricultural and information-technology workers.
    It ushers millions of shadow workers into the higher-earning, taxpaying,
    aboveground economy, a sure recipe for jobs and growth. And it heaps billions on
    defense contractors to supply the surveillance tools and weaponry to fortify
    the border.

    The coalition behind comprehensive reform is large. It includes evangelicals
    and Catholics, law-enforcement and business groups, and Republicans like Jeb
    Bush and former President George W. Bush. Immigrant-rights advocates and
    Democrats are solidly lined up, too, even those who want a shorter path to
    citizenship and less money thrown at the border buildup.

    Mr. Boehner has a choice. He can let reform go forward with bipartisan
    support - House Republicans and Democrats together could pass a good bill.
    This would infuriate the hotheads in his caucus but save the Republican Party
    from itself. Or he can stand back and let his party kill reform. As the issue
    festers, a nation is watching to see whether the Republicans can work out their
    Steve King problem and do something difficult for their own good, and the
    country's.
    """
    
    sentences = content_to_sentences(text) # split into list of sentences
    #print "total sentences = %d" % len(sentences) # debug
    
    sentences = list(set(sentences)) # remove duplicate sentences
    #print "unique sentences = %d" % len(sentences) # debug
    
    all_sentence_words = [] # nested list to hold list of words of a sentence
    
    for s in sentences:
        all_sentence_words.append(sentence_to_words(s)) # split into list of words
        
    print all_sentence_words # debug
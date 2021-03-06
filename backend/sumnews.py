import os,re,nltk
import operator
import pandas as pd
import numpy as np
import gensim.models.keyedvectors as word2vec
import os
import pandas as pd
import string
from pyvi import ViTokenizer
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
from deepai_nlp.tokenization.crf_tokenizer import CrfTokenizer
from deepai_nlp.tokenization.utils import preprocess_text
from readData import readExcelFile, readCsvFile
from preProcessData import *
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import pairwise_distances_argmin_min
import multiprocessing
from sklearn.model_selection import train_test_split


def makesentences(rawtext):
    models = []
    models.append([Word2Vec.load('word2vec_Education.model'),0])
    models.append([Word2Vec.load('word2vec_Technology.model'),1])
    models.append([Word2Vec.load('word2vec_Sport.model'),2])

    models.append([Word2Vec.load('word2vec_Covid19.model'),3])
    models.append([Word2Vec.load('word2vec_Politic.model'),4])
    # models.append([Word2Vec.load('word2vec_Entertainment.model'),5])
    # models.append([Word2Vec.load('word2vec_Film.model'),6])
    models.append([Word2Vec.load('word2vec_Law.model'),5])
    models.append([Word2Vec.load('word2vec_Economy.model'),6])
    X = []
    Y = []
    new_values = []
    # tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=250, random_state=5)
    for model in models:
        for word in model[0].wv.vocab:
            X.append(model[0][word])
            Y.append(model[1])
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.15)
  
# new_values = tsne_model.fit_transform(tokens)
    # sdasdasd
    cores = multiprocessing.cpu_count()
    knn = KNeighborsClassifier(n_neighbors = 5, p = 2,weights="distance") 
    knn.fit(X_train, y_train)
    sentences = nltk.sent_tokenize(rawtext)
    tokenizer = CrfTokenizer()
    stopWordLst = stopWordsLst()
    data = []
    for sentence in sentences:
        documents = preprocess_text([sentence], tokenizer=tokenizer) # Tách từ và clean
        if len(documents) == 0:
            continue
        sents = removeStopWord(documents,stopWordLst)
        data.append(sents)
    # model = Word2Vec(data, size=100, window=20, min_count=2, workers=4, sg=0)
    model = Word2Vec(data,min_count=2,
                        window=5,
                        size=150,
                        sample=6e-5, 
                        alpha=0.03, 
                        min_alpha=0.0007,
                        negative=20,
                        workers=cores-1)
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
    data_covid = []
    data_edu = []
    data_tech = []
    data_sport = []
    data_polictic = []
    # data_entertainment = []
    # data_film = []
    data_law = []
    data_economy = []
    for word in model.wv.vocab:
        if knn.predict([model[word]]) == 0:
            data_edu.append(word)
        if knn.predict([model[word]]) == 1:
            data_tech.append(word)
        if knn.predict([model[word]]) == 2:
            data_sport.append(word)
        if knn.predict([model[word]]) == 3:
            data_covid.append(word)
        if knn.predict([model[word]]) == 4:
            data_polictic.append(word)
        # if knn.predict([model[word]]) == 5:
        #   data_entertainment.append(word)
        # if knn.predict([model[word]]) == 6:
        #   data_film.append(word)
        if knn.predict([model[word]]) == 5:
            data_law.append(word)
        if knn.predict([model[word]]) == 6:
            data_economy.append(word)
    out = {
        'education' : len(data_edu),
        'technology': len(data_tech),
        'sport': len(data_sport),
        'covid': len(data_covid),
        'polictic': len(data_polictic),
        # 'entertainment': len(data_entertainment),
        # 'film': len(data_film),
        'law': len(data_law),
        'economy': len(data_economy)
    }
    return model,data_covid,("The news belong to category:{}".format(max(out.items(), key=operator.itemgetter(1))[0]))

def kmean_model(sentences):
    sentences = nltk.sent_tokenize(sentences)

    model=Word2Vec.load('word2vec_Covid19.model')
    vocab = model.wv.vocab
    X = []
    for sentence in sentences:
        sentence_tokenized = ViTokenizer.tokenize(sentence)
        words = sentence_tokenized.split(" ")
        sentence_vec = np.zeros((150))
        for word in words:
            if word in vocab:
                sentence_vec+=model.wv[word]
        X.append(sentence_vec)
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans = kmeans.fit(X)
    avg = []
    for j in range(n_clusters):
        idx = np.where(kmeans.labels_ == j)[0]
        avg.append(np.mean(idx))
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])
    summary = ' '.join([sentences[closest[idx]] for idx in ordering])
    return summary
def knn_model(sentences):
    model,vocab,belongto = makesentences(sentences)
    sentences = nltk.sent_tokenize(sentences)
    # model=model
    # vocab = data_test
    model1 = Word2Vec.load('word2vec_Covid19.model')
    vocal1 = model1.wv.vocab
    X = []
    for sentence in sentences:
        sentence_tokenized = ViTokenizer.tokenize(sentence)
        words = sentence_tokenized.split(" ")
        sentence_vec = np.zeros((150))
        for word in words:
            if word in vocab:
                sentence_vec+=model.wv[word]
            # if word in vocal1:
            #     sentence_vec+=model1.wv[word]
        X.append(sentence_vec)
    n_clusters = 4
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans = kmeans.fit(X)
    avg = []
    for j in range(n_clusters):
        idx = np.where(kmeans.labels_ == j)[0]
        avg.append(np.mean(idx))
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])
    summary = ' '.join([sentences[closest[idx]] for idx in ordering])
    return summary
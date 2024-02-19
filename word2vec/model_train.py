import io
import re
import string
import tqdm
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers
SEED = 42
AUTOTUNE = tf.data.AUTOTUNE
import os
import pickle
#define the number of negative samples for every positive sample
num_ns = 4


# load in vocab.pkl
with open('./word2vec/vocab.pkl', 'rb') as f:
    vocab = pickle.load(f)

#load labels, targets, contexts using numpy
labels = np.load('./word2vec/labels.npy')
targets = np.load('./word2vec/targets.npy')
contexts = np.load('./word2vec/contexts.npy')

#set the vocab size
vocab_size = len(vocab) + 1  # Adding 1 because vocab does not contain 0 which is used as a padding value. this is accounted for later.

print(vocab_size)

BATCH_SIZE = 1024
BUFFER_SIZE = 10000
dataset = tf.data.Dataset.from_tensor_slices(((targets, contexts), labels))
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)
print(dataset)



class Word2Vec(tf.keras.Model):
  def __init__(self, vocab_size, embedding_dim):
    super(Word2Vec, self).__init__()
    self.target_embedding = layers.Embedding(vocab_size,
                                      embedding_dim,
                                      input_length=1,
                                      name="w2v_embedding")
    self.context_embedding = layers.Embedding(vocab_size,
                                       embedding_dim,
                                       input_length=num_ns+1)

  def call(self, pair):
    target, context = pair
    # target: (batch, dummy?)  # The dummy axis doesn't exist in TF2.7+
    # context: (batch, context)
    if len(target.shape) == 2:
      target = tf.squeeze(target, axis=1)
    # target: (batch,)
    word_emb = self.target_embedding(target)
    # word_emb: (batch, embed)
    context_emb = self.context_embedding(context)
    # context_emb: (batch, context, embed)
    dots = tf.einsum('be,bce->bc', word_emb, context_emb)
    # dots: (batch, context)
    return dots
  


embedding_dim = 128
word2vec = Word2Vec(vocab_size, embedding_dim)
word2vec.compile(optimizer='adam',
                 loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
                 metrics=['accuracy'])


tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="logs")

word2vec.fit(dataset, epochs=20, callbacks=[tensorboard_callback])


weights = word2vec.get_layer('w2v_embedding').get_weights()[0]

# save the weights to a file
np.save('./word2vec/chord_embeddings.npy', weights)


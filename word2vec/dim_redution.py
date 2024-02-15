import numpy as np
import pickle
import pandas as pd

#load chord embeddings
chord_embeddings = np.load('./word2vec/chord_embeddings.npy')

# load in vocab.pkl
with open('./word2vec/vocab.pkl', 'rb') as f:
    vocab = pickle.load(f)
#load inverse vocab
with open('./word2vec/inv_vocab.pkl', 'rb') as f:
    inv_vocab = pickle.load(f)


#import t-sne
from sklearn.manifold import TSNE

#reduce the dimensionality of the chord embeddings to 3 dimensions
tsne = TSNE(n_components=3, random_state=42)
chord_embeddings_3d = tsne.fit_transform(chord_embeddings)

# add another key:value pair to inv_vocab to account for the 0th index. make the value 'no chord'
inv_vocab[0] = 'no chord'


chord_names = [inv_vocab[i] for i in range(len(inv_vocab))]
df = pd.DataFrame({'chord': chord_names, 'x': chord_embeddings_3d[:,0], 'y': chord_embeddings_3d[:,1], 'z': chord_embeddings_3d[:,2]})

print(df.head())

# filter the dataframe to grab just C, D, E, F, G,
# and their relative minor chords:
# Amin, Emin, Bmin, Fmin, Cmin
df = df[df['chord'].isin(['C', 'D', 'E', 'F', 'G', 'Am', 'Em', 'Bm', 'Fm', 'Cm', 'G5', 'C5', 'F5', 'G7', 'C7', 'F7', 'Gmaj7', 'Cmaj7', 'Fmaj7'])]

#use plotly to create an interactive 3d scatter plot of df
import plotly.express as px
fig = px.scatter_3d(df, x='x', y='y', z='z', text='chord')
fig.update_traces(textposition='top center')
fig.show()
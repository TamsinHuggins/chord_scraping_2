import numpy as np
import pickle
import pandas as pd
import plotly
import plotly.express as px

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

# extract the 3D coordinates from the dataframe. 
# use t-sne to reduce to 1 dimension
#append the 1D to the dataframe, in a column called 'color'
tsne1d = TSNE(n_components=1, random_state=42)
df['color'] = tsne1d.fit_transform(chord_embeddings)

# again use t-sne on the chord_embeddings, this time reducing to 2 dimensions
tsne2d = TSNE(n_components=2, random_state=42)
chord_embeddings_2d = tsne2d.fit_transform(chord_embeddings)

# create a new dataframe
# the chord column will contain the chord names
# the x and y columns will contain the 2D coordinates
# the color column will contain the 1D coordinates
df_2d = pd.DataFrame({'chord': chord_names, 'x': chord_embeddings_2d[:,0], 'y': chord_embeddings_2d[:,1], 'color': df['color']})

print(df_2d.head(10))

#drop the first row of df_2d, as it contains the 'no chord' entry
df_2d = df_2d.drop(0)
#save the dataframe to a csv file without the index
df_2d.to_csv('chord_embeddings_2d.csv', index=False)




#save the dataframe to a csv file without the index
#df.to_csv('chord_embeddings_3d.csv', index=False)


# chords_of_interest = ['C', 'D', 'E', 'F', 'G', 
#                       'Am', 'Em', 'Bm', 'Fm', 'Cm',
#                       'C7', 'D7', 'E7', 'F7', 'G7',
#                       'Cmaj7', 'Dmaj7', 'Emaj7', 'Fmaj7', 'Gmaj7',
#                       'C5', 'D5', 'E5', 'F5', 'G5']


# df = df[df['chord'].isin(chords_of_interest)]

# #use plotly to create an interactive 3d scatter plot of df
# # label the points with their chord
# # use the 'color' column to colour the points
# fig = px.scatter_3d(df, x='x', y='y', z='z', color='color', text='chord')
# fig.update_traces(marker=dict(size=5))
# fig.update_layout(
#     plot_bgcolor='white',
# )
# fig.update_scenes(
#     xaxis=dict(showgrid=False, backgroundcolor='white'),
#     yaxis=dict(showgrid=False, backgroundcolor='white'),
#     zaxis=dict(showgrid=False, backgroundcolor='white')
# )
# fig.show()
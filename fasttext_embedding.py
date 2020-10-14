# Make sure to install the specific version of gensim before
# pip install gensim==3.6.0

import gensim
model = gensim.models.Word2Vec.load('model_dir/model_name')

# Get embedding
print(model['Fix the null pointer exception.'])

# Find similar words in vector space
print(model.wv.most_similar("pointer"))

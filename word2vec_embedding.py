# Make sure to install the specific version of gensim before
# pip install gensim==3.6.0

from gensim.models import Word2Vec

model = Word2Vec.load("model_dir/model_name")

# Get vector
print(model.wv['Handle exception.'])

# Make sure to install the specific version of gensim before
# pip install gensim==3.6.0

import gensim
model = gensim.models.Word2Vec.load('fasttext_code_comment/fasttext_code_comment')

print(model['Fix the null pointer exception.'])
print(model.wv.most_similar("pointer"))

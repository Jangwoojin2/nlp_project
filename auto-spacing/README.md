# auto spacing
This is about auto-sapcing model based on CRF(Conditional Random Field)

# comment
this is for only baemin review due to the vocaburary distribution of training data.
it may not work on other text data.

#usage
import pycrfsuite_spacing
from pycrfsuite_spacing import CharacterFeatureTransformer
from pycrfsuite_spacing import TemplateGenerator
from pycrfsuite_spacing import PyCRFSuiteSpacing

to_feature = CharacterFeatureTransformer(
    TemplateGenerator(begin=-2, 
    end=2,
    min_range_length=3,
    max_range_length=3)
)


correct = PyCRFSuiteSpacing(
    to_feature = to_feature,
    feature_minfreq=3, # default = 0
    max_iterations=100,
    l1_cost=1.0,
    l2_cost=1.0
)
model_path = './review_space.crfsuite'  #pre-trained model using review data
correct = PyCRFSuiteSpacing(to_feature)
correct.load_tagger(model_path)

#result example
correct('너무빡쳐서쓰는데요머리카락나왔어요더러워죽겠네')
output: '너무 빡쳐서 쓰는데요 머리카락 나왔어요 더러워 죽겠네'
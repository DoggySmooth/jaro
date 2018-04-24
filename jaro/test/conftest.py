from hypothesis import settings

import os

settings.register_profile('ci', max_examples=10)
settings.register_profile('dev', max_examples=50)
settings.register_profile('max', max_examples=100)

settings.load_profile(os.getenv('HYPOTHESIS_PROFILE', 'dev'))

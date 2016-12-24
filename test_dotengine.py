

import dotengine



dotengine.dot_engine_api_url = 'http://localhost:8000/api/'


dot = dotengine.DotEngine('dotcc','dotcc')


print dot.createToken('room','userid')



import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()
api.model_list_cli()


"""
Next Page Token = [...]
[...]
"""

# ubicación del dataset
# https://www.kaggle.com/datasets/NUFORC/ufo-sightings

data_url='NUFORC/ufo-sightings'

kaggle.api.authenticate()

kaggle.api.dataset_download_files(data_url,path= '.', unzip=True )


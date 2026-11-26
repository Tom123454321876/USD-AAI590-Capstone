# Shared paths and dataset metadata

KAGGLE_DATASET_PAGE = "https://www.kaggle.com/datasets/joniarroba/noshowappointments"
KAGGLE_DATASET_SLUG = "joniarroba/noshowappointments"

# Team 2 shared Databricks Unity Catalog Volume
TEAM_VOLUME = "/Volumes/workspace/default/eye_style_team2"

# Shared project directories
RAW_DATA_DIR = f"{TEAM_VOLUME}/raw"
CLEAN_DATA_DIR = f"{TEAM_VOLUME}/clean"
RAG_DATA_DIR = f"{TEAM_VOLUME}/rag"
MODEL_ARTIFACT_DIR = f"{TEAM_VOLUME}/models"

# Team 2 source dataset
NO_SHOW_CSV = f"{RAW_DATA_DIR}/KaggleV2-May-2016.csv"
CLEAN_NO_SHOW_CSV = f"{CLEAN_DATA_DIR}/cleaned_appointments_features.csv"




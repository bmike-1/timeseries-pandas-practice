# Script from https://www.kaggle.com/datasets/amruthayenikonda/dirty-dataset-to-practice-data-cleaning/data

# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "my_file (1).csv"

# Load the latest version
df = kagglehub.load_dataset(
    KaggleDatasetAdapter.PANDAS,
    "amruthayenikonda/dirty-dataset-to-practice-data-cleaning",
    file_path,
    # Provide any additional arguments like
    # sql_query or pandas_kwargs. See the
    # documenation for more information:
    # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

# df.head()

df.to_csv("input_data/tour_data.csv", index=False)

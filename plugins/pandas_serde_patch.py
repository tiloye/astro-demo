# plugins/patch_pandas_serde.py
import pandas as pd
from airflow.plugins_manager import AirflowPlugin

# Enforce the legacy string representation Airflow 3.2 expects
pd.DataFrame.__qualname__ = "core.frame.DataFrame"

class PatchPandasSerdePlugin(AirflowPlugin):
    name = "patch_pandas_serde_plugin"

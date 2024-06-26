import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def convert_week_to_datetime(data, *args, **kwargs):
    data["Week"] = pd.to_datetime(data["Week"])
    return data


@test
def test_output(output, *args) -> None:
    # Test if the Week column is a datetime object
    assert output["Week"].dtype == "datetime64[ns]"

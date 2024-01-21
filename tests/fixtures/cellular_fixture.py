import pandas as pd
from io import StringIO

import pytest


@pytest.fixture(scope="module")
def cellular_fixtures() -> pd.DataFrame:
    return pd.read_csv(
        StringIO(
            """radio,mcc,net,area,cell,unit,lon,lat,range,samples,changeable,created,updated,averageSignal
        GSM,270,99,12,22222,0,6.120712,49.54384,11109,144,1,1309988245,1443599522,0
        GSM,270,77,3,373,0,6.117069,49.538568,8810,1999,1,1309988245,1549544159,0
        GSM,270,1,1010,15396,0,6.114561,49.536516,11764,2000,1,1309988245,1384491026,0
        GSM,270,77,3,10373,0,6.115696,49.539976,21609,1068,1,1309988245,1328105111,0
        GSM,270,77,3,10372,0,6.116469,49.542106,21646,1083,1,1309988245,1328105021,0
    """
        )
    )

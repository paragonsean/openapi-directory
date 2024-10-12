

# WcdmaNmr

WCDMA Network measurement

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cid** | **Integer** | UTRAN Cell Identifier (UC-Id), 28 bits (12 bits RNC and 16 bits Cell ID). MCC + MNC + CID uniquely identifies the WCDMA cell, LAC is optional.  |  [optional] |
|**pathloss** | **Integer** | UTRAN pathloss (dBm) |  [optional] |
|**psc** | **Integer** | Primary Scrambling Code (PSC, Primary CPICH, Primary Control Pilot Channel). |  |
|**rscp** | **Integer** | Received Signal Code Power (RSCP) in dBm. Power less than -120dBm should be mapped to -120. Power greater than -25dBm should be mapped to -25.  |  [optional] |
|**uarfcndl** | **Integer** | UTRAN Absolute Radio Frequency Downlink (UARFCN-DL) |  |




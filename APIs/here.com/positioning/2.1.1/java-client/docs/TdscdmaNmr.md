

# TdscdmaNmr

TD-SCDMA Network measurement

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cellParams** | **Integer** | Cell Parameters ID (CDMA Spreading Code ID) |  |
|**cid** | **Integer** | UTRAN Cell Identifier (UC-Id), 28 bits (12 bits RNC and 16 bits Cell ID). MCC + MNC + CID uniquely identifies the WCDMA cell, LAC is optional.  |  [optional] |
|**pathloss** | **Integer** | UTRAN pathloss (dBm) |  [optional] |
|**rscp** | **Integer** | Received Signal Code Power (RSCP) in dBm. Power less than -120dBm should be mapped to -120. Power greater than -25dBm should be mapped to -25.  |  [optional] |
|**uarfcn** | **Integer** | UTRAN Absolute Radio Frequency (U-ARFCN) |  |




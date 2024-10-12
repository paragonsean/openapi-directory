

# Wcdma

WCDMA measurement

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cid** | **Integer** | UTRAN Cell Identifier (UC-Id), 28 bits (12 bits RNC and 16 bits Cell ID). MCC + MNC + CID uniquely identifies the WCDMA cell, LAC is optional.  |  |
|**lac** | **Integer** | Location Area Code (LAC). Note, value 65534 is invalid. |  [optional] |
|**localId** | [**WcdmaLocalId**](WcdmaLocalId.md) |  |  [optional] |
|**mcc** | **Integer** | Mobile Country Code (MCC). Note: 0xx is for test networks, 1xx and 8xx are not used  |  |
|**mnc** | **Integer** | Mobile Network Code (MNC). |  |
|**nmr** | [**List&lt;WcdmaNmr&gt;**](WcdmaNmr.md) | WCDMA Network measurements. Maximum of 8 distinct uarfcndl frequencies. |  [optional] |
|**pathloss** | **Integer** | UTRAN pathloss (dBm) |  [optional] |
|**rscp** | **Integer** | Received Signal Code Power (RSCP) in dBm. Power less than -120dBm should be mapped to -120. Power greater than -25dBm should be mapped to -25.  |  [optional] |




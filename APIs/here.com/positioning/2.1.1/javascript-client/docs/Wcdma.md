# HereNetworkPositioningApiV2.Wcdma

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **Number** | UTRAN Cell Identifier (UC-Id), 28 bits (12 bits RNC and 16 bits Cell ID). MCC + MNC + CID uniquely identifies the WCDMA cell, LAC is optional.  | 
**lac** | **Number** | Location Area Code (LAC). Note, value 65534 is invalid. | [optional] 
**localId** | [**WcdmaLocalId**](WcdmaLocalId.md) |  | [optional] 
**mcc** | **Number** | Mobile Country Code (MCC). Note: 0xx is for test networks, 1xx and 8xx are not used  | 
**mnc** | **Number** | Mobile Network Code (MNC). | 
**nmr** | [**[WcdmaNmr]**](WcdmaNmr.md) | WCDMA Network measurements. Maximum of 8 distinct uarfcndl frequencies. | [optional] 
**pathloss** | **Number** | UTRAN pathloss (dBm) | [optional] 
**rscp** | **Number** | Received Signal Code Power (RSCP) in dBm. Power less than -120dBm should be mapped to -120. Power greater than -25dBm should be mapped to -25.  | [optional] 



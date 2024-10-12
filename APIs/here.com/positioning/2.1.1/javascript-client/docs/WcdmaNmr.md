# HereNetworkPositioningApiV2.WcdmaNmr

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **Number** | UTRAN Cell Identifier (UC-Id), 28 bits (12 bits RNC and 16 bits Cell ID). MCC + MNC + CID uniquely identifies the WCDMA cell, LAC is optional.  | [optional] 
**pathloss** | **Number** | UTRAN pathloss (dBm) | [optional] 
**psc** | **Number** | Primary Scrambling Code (PSC, Primary CPICH, Primary Control Pilot Channel). | 
**rscp** | **Number** | Received Signal Code Power (RSCP) in dBm. Power less than -120dBm should be mapped to -120. Power greater than -25dBm should be mapped to -25.  | [optional] 
**uarfcndl** | **Number** | UTRAN Absolute Radio Frequency Downlink (UARFCN-DL) | 



# HereNetworkPositioningApiV2.Gsm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **Number** | Cell identifier (GERAN CID) | 
**lac** | **Number** | Location Area Code (LAC). Note, value 65534 is invalid. | 
**localId** | [**GsmLocalId**](GsmLocalId.md) |  | [optional] 
**mcc** | **Number** | Mobile Country Code (MCC). Note: 0xx is for test networks, 1xx and 8xx are not used  | 
**mnc** | **Number** | Mobile Network Code (MNC). | 
**nmr** | [**[GsmNmr]**](GsmNmr.md) | GSM Network measurements | [optional] 
**rxLevel** | **Number** | Received Signal power (dBm). Power less than -110dBm should be mapped to -110. Power greater than -25dBm should be mapped to -25.  | [optional] 
**ta** | **Number** | Timing advance (TA). Expressed in the units of GSM bits equaling to 48/13 μs ~ 1107 meters. | [optional] 



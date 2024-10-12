# HereNetworkPositioningApiV2.Tdscdma

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **Number** | UTRAN Cell Identifier (UC-Id), 28 bits (12 bits RNC and 16 bits Cell ID). MCC + MNC + CID uniquely identifies the WCDMA cell, LAC is optional.  | 
**lac** | **Number** | Location Area Code (LAC). Note, value 65534 is invalid. | [optional] 
**localId** | [**TdscdmaLocalId**](TdscdmaLocalId.md) |  | [optional] 
**mcc** | **Number** | Mobile Country Code (MCC). Note: 0xx is for test networks, 1xx and 8xx are not used  | 
**mnc** | **Number** | Mobile Network Code (MNC). | 
**nmr** | [**[TdscdmaNmr]**](TdscdmaNmr.md) | TD-SCDMA Network measurements. Maximum of 8 distinct uarfcn frequencies. | [optional] 
**pathloss** | **Number** | UTRAN pathloss (dBm) | [optional] 
**rscp** | **Number** | Received Signal Code Power (RSCP) in dBm. Power less than -120dBm should be mapped to -120. Power greater than -25dBm should be mapped to -25.  | [optional] 
**ta** | **Number** | Timing advance (TA). Round-Trip distance presented in the units of 4*c/7.68e6 ~156 meters. That is, the scaling factor is 4 times the chip length at chip rate of 7.68 Mchips/s. Note that at chip rates 1.28 Mchips/s and 3.84 Mchips/s you need to scale according to chip length of 7.68 Mchips/s, that is, multiply by 6 or 2 if needed.  | [optional] 



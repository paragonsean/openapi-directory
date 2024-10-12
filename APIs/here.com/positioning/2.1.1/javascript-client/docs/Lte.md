# HereNetworkPositioningApiV2.Lte

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cid** | **Number** | E-UTRA Cell Identifier (UC-Id), 28 bits (20 bits eNodeB and 8 bits Cell ID). MCC + MNC + CID uniquely identifies the LTE cell, TAC is optional.  | 
**localId** | [**LteLocalId**](LteLocalId.md) |  | [optional] 
**mcc** | **Number** | Mobile Country Code (MCC). Note: 0xx is for test networks, 1xx and 8xx are not used  | 
**mnc** | **Number** | Mobile Network Code (MNC). | 
**nmr** | [**[LteNmr]**](LteNmr.md) | LTE Network measurements | [optional] 
**rsrp** | **Number** | Reference Signal Received Power (RSRP) in dBm. Power less than -140dBm should be mapped to -140. Power greater than -44dBm should be mapped to -44.  | [optional] 
**rsrq** | **Number** | Reference Signal Received Quality (RSRQ) in dBm. Values less than -19.5dB should be mapped to -19.5, and values greater than -3dB should be mapped to -3dB.  | [optional] 
**ta** | **Number** | Timing Advance. Expressed in the units of 16*Ts (16 Basic time units) &#x3D; 16/(15000*2048) seconds ~ 156meters. For reference see 3GPP TS 36.213 and 36.211.  | [optional] 
**tac** | **Number** | Tracking Area Code (TAC) | [optional] 



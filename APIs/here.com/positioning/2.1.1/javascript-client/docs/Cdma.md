# HereNetworkPositioningApiV2.Cdma

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseLat** | **Number** | Base station latitude | [optional] 
**baseLng** | **Number** | Base station longitude | [optional] 
**bsid** | **Number** | Base Station ID (CDMA BSID, BID) | 
**localId** | [**CdmaLocalId**](CdmaLocalId.md) |  | [optional] 
**nid** | **Number** | Network ID (NID) | 
**nmr** | [**[CdmaNmr]**](CdmaNmr.md) | CDMA Network measurements | [optional] 
**pilotPower** | **Number** | Pilot Power (dBm). If Pilot Power is not available directly, it needs to be calculated from Total Power in the band and Pilot Strength with respect to the Total Power. Pilot power less than -142dBm should be mapped to -142. Pilot power greater than -49dBm should be mapped to -49.  | [optional] 
**rz** | **Number** | CDMA Registration Zone (RZ) | [optional] 
**sid** | **Number** | System ID (SID) | 





# Cdma

CDMA measurement

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseLat** | **BigDecimal** | Base station latitude |  [optional] |
|**baseLng** | **BigDecimal** | Base station longitude |  [optional] |
|**bsid** | **Integer** | Base Station ID (CDMA BSID, BID) |  |
|**localId** | [**CdmaLocalId**](CdmaLocalId.md) |  |  [optional] |
|**nid** | **Integer** | Network ID (NID) |  |
|**nmr** | [**List&lt;CdmaNmr&gt;**](CdmaNmr.md) | CDMA Network measurements |  [optional] |
|**pilotPower** | **Integer** | Pilot Power (dBm). If Pilot Power is not available directly, it needs to be calculated from Total Power in the band and Pilot Strength with respect to the Total Power. Pilot power less than -142dBm should be mapped to -142. Pilot power greater than -49dBm should be mapped to -49.  |  [optional] |
|**rz** | **Integer** | CDMA Registration Zone (RZ) |  [optional] |
|**sid** | **Integer** | System ID (SID) |  |




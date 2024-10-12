# HereNetworkPositioningApiV2.CdmaNmr

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bsid** | **Number** | Base Station ID (CDMA BSID, BID) | [optional] 
**channel** | **Number** | CDMA channel frequency | 
**pilotPower** | **Number** | Pilot Power (dBm). If Pilot Power is not available directly, it needs to be calculated from Total Power in the band and Pilot Strength with respect to the Total Power. Pilot power less than -142dBm should be mapped to -142. Pilot power greater than -49dBm should be mapped to -49.  | [optional] 
**pnOffset** | **Number** | Pseudonoise offset. This field and CDMA channel frequency together allow for the locally unique identification of the cell.  | 



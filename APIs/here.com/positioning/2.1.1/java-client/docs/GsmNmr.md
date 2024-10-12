

# GsmNmr

GSM Network measurements. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bcch** | **Integer** | Broadcast Control Channel (BCCH, synonymous to ARFCN &#x3D; Absolute Radio Frequency Channel) |  |
|**bsic** | **Integer** | Base Station Identity Code (BSIC, for instance, color code) |  |
|**globalIdentity** | [**GsmNmrGlobalId**](GsmNmrGlobalId.md) |  |  [optional] |
|**rxLevel** | **Integer** | Received Signal power (dBm). Power less than -110dBm should be mapped to -110. Power greater than -25dBm should be mapped to -25.  |  [optional] |






# StoresList200ResponseInner

ExternalStoreResponse

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdBy** | **String** | The ID of the principal that created the store. |  [optional] |
|**createdByPrincipalType** | **String** | The type of the principal that created the store. |  [optional] |
|**id** | **String** | Store id |  [optional] |
|**intuneDetails** | [**StoresList200ResponseInnerIntuneDetails**](StoresList200ResponseInnerIntuneDetails.md) |  |  [optional] |
|**name** | **String** | Store Name |  [optional] |
|**serviceConnectionId** | **String** | Id for the shared service connection. In case of Apple / GooglePlay stores, this connection will be used to connect to the Apple / Google stores in App Center. |  [optional] |
|**track** | [**TrackEnum**](#TrackEnum) | Store track |  [optional] |
|**type** | **String** | Store Type |  [optional] |



## Enum: TrackEnum

| Name | Value |
|---- | -----|
| PRODUCTION | &quot;production&quot; |
| ALPHA | &quot;alpha&quot; |
| BETA | &quot;beta&quot; |
| TESTFLIGHT_INTERNAL | &quot;testflight-internal&quot; |
| TESTFLIGHT_EXTERNAL | &quot;testflight-external&quot; |






# StoresCreateRequest

ExternalStoreRequest

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intuneDetails** | [**StoresCreateRequestIntuneDetails**](StoresCreateRequestIntuneDetails.md) |  |  [optional] |
|**name** | **String** | name of the store. In case of googleplay, and Apple store this is fixed to Production. |  [optional] |
|**serviceConnectionId** | **String** | Id for the shared service connection. In case of Apple AppStore, this connection will be used to create and connect to the Apple AppStore in Mobile Center. |  [optional] |
|**track** | [**TrackEnum**](#TrackEnum) | track of the store. Can be production, alpha &amp; beta for googleplay. Can be production, testflight-internal &amp; testflight-external for Apple Store. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | store Type |  [optional] |



## Enum: TrackEnum

| Name | Value |
|---- | -----|
| PRODUCTION | &quot;production&quot; |
| ALPHA | &quot;alpha&quot; |
| BETA | &quot;beta&quot; |
| TESTFLIGHT_INTERNAL | &quot;testflight-internal&quot; |
| TESTFLIGHT_EXTERNAL | &quot;testflight-external&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| GOOGLEPLAY | &quot;googleplay&quot; |
| APPLE | &quot;apple&quot; |
| INTUNE | &quot;intune&quot; |




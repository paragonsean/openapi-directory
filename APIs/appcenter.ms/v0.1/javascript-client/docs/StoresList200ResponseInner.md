# AppCenterClient.StoresList200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdBy** | **String** | The ID of the principal that created the store. | [optional] 
**createdByPrincipalType** | **String** | The type of the principal that created the store. | [optional] 
**id** | **String** | Store id | [optional] 
**intuneDetails** | [**StoresList200ResponseInnerIntuneDetails**](StoresList200ResponseInnerIntuneDetails.md) |  | [optional] 
**name** | **String** | Store Name | [optional] 
**serviceConnectionId** | **String** | Id for the shared service connection. In case of Apple / GooglePlay stores, this connection will be used to connect to the Apple / Google stores in App Center. | [optional] 
**track** | **String** | Store track | [optional] 
**type** | **String** | Store Type | [optional] 



## Enum: TrackEnum


* `production` (value: `"production"`)

* `alpha` (value: `"alpha"`)

* `beta` (value: `"beta"`)

* `testflight-internal` (value: `"testflight-internal"`)

* `testflight-external` (value: `"testflight-external"`)





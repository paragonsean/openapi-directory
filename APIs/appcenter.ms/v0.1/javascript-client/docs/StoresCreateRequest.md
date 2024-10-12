# AppCenterClient.StoresCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intuneDetails** | [**StoresCreateRequestIntuneDetails**](StoresCreateRequestIntuneDetails.md) |  | [optional] 
**name** | **String** | name of the store. In case of googleplay, and Apple store this is fixed to Production. | [optional] 
**serviceConnectionId** | **String** | Id for the shared service connection. In case of Apple AppStore, this connection will be used to create and connect to the Apple AppStore in Mobile Center. | [optional] 
**track** | **String** | track of the store. Can be production, alpha &amp; beta for googleplay. Can be production, testflight-internal &amp; testflight-external for Apple Store. | [optional] 
**type** | **String** | store Type | [optional] 



## Enum: TrackEnum


* `production` (value: `"production"`)

* `alpha` (value: `"alpha"`)

* `beta` (value: `"beta"`)

* `testflight-internal` (value: `"testflight-internal"`)

* `testflight-external` (value: `"testflight-external"`)





## Enum: TypeEnum


* `googleplay` (value: `"googleplay"`)

* `apple` (value: `"apple"`)

* `intune` (value: `"intune"`)





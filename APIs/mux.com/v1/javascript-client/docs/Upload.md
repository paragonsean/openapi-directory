# MuxApi.Upload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetId** | **String** | Only set once the upload is in the &#x60;asset_created&#x60; state. | [optional] 
**corsOrigin** | **String** | If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers. | [optional] 
**error** | [**UploadError**](UploadError.md) |  | [optional] 
**id** | **String** | Unique identifier for the Direct Upload. | [optional] 
**newAssetSettings** | [**Asset**](Asset.md) |  | [optional] 
**status** | **String** |  | [optional] 
**test** | **Boolean** | Indicates if this is a test Direct Upload, in which case the Asset that gets created will be a &#x60;test&#x60; Asset. | [optional] 
**timeout** | **Number** | Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked &#x60;timed_out&#x60; | [optional] [default to 3600]
**url** | **String** | The URL to upload the associated source media to. | [optional] 



## Enum: StatusEnum


* `waiting` (value: `"waiting"`)

* `asset_created` (value: `"asset_created"`)

* `errored` (value: `"errored"`)

* `cancelled` (value: `"cancelled"`)

* `timed_out` (value: `"timed_out"`)





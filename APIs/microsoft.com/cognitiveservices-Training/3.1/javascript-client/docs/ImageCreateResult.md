# CustomVisionTrainingClient.ImageCreateResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**Image**](Image.md) |  | [optional] 
**sourceUrl** | **String** | Source URL of the image. | [optional] [readonly] 
**status** | **String** | Status of the image creation. | [optional] [readonly] 



## Enum: StatusEnum


* `OK` (value: `"OK"`)

* `OKDuplicate` (value: `"OKDuplicate"`)

* `ErrorSource` (value: `"ErrorSource"`)

* `ErrorImageFormat` (value: `"ErrorImageFormat"`)

* `ErrorImageSize` (value: `"ErrorImageSize"`)

* `ErrorStorage` (value: `"ErrorStorage"`)

* `ErrorLimitExceed` (value: `"ErrorLimitExceed"`)

* `ErrorTagLimitExceed` (value: `"ErrorTagLimitExceed"`)

* `ErrorRegionLimitExceed` (value: `"ErrorRegionLimitExceed"`)

* `ErrorUnknown` (value: `"ErrorUnknown"`)

* `ErrorNegativeAndRegularTagOnSameImage` (value: `"ErrorNegativeAndRegularTagOnSameImage"`)





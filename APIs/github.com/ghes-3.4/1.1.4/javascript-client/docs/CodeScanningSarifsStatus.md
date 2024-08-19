# GitHubV3RestApi.CodeScanningSarifsStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysesUrl** | **String** | The REST API URL for getting the analyses associated with the upload. | [optional] [readonly] 
**errors** | **[String]** | Any errors that ocurred during processing of the delivery. | [optional] [readonly] 
**processingStatus** | **String** | &#x60;pending&#x60; files have not yet been processed, while &#x60;complete&#x60; means results from the SARIF have been stored. &#x60;failed&#x60; files have either not been processed at all, or could only be partially processed. | [optional] 



## Enum: ProcessingStatusEnum


* `pending` (value: `"pending"`)

* `complete` (value: `"complete"`)

* `failed` (value: `"failed"`)





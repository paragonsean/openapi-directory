# FilesComApi.ActionNotificationExportEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endAt** | **Date** | End date/time of export range. | [optional] 
**exportVersion** | **String** | Version of the underlying records for the export. | [optional] 
**id** | **Number** | History Export ID | [optional] 
**queryFolder** | **String** | Return notifications that were triggered by actions in this folder. | [optional] 
**queryMessage** | **String** | Error message associated with the request, if any. | [optional] 
**queryPath** | **String** | Return notifications that were triggered by actions on this specific path. | [optional] 
**queryRequestMethod** | **String** | The HTTP request method used by the webhook. | [optional] 
**queryRequestUrl** | **String** | The target webhook URL. | [optional] 
**queryStatus** | **String** | The HTTP status returned from the server in response to the webhook request. | [optional] 
**querySuccess** | **Boolean** | true if the webhook request succeeded (i.e. returned a 200 or 204 response status). false otherwise. | [optional] 
**resultsUrl** | **String** | If &#x60;status&#x60; is &#x60;ready&#x60;, this will be a URL where all the results can be downloaded at once as a CSV. | [optional] 
**startAt** | **Date** | Start date/time of export range. | [optional] 
**status** | **String** | Status of export.  Valid values: &#x60;building&#x60;, &#x60;ready&#x60;, or &#x60;failed&#x60; | [optional] 



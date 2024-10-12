# FilesComApi.ActionNotificationExportResultEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Number** | When the notification was sent. | [optional] 
**folder** | **String** | The folder associated with the triggering action for this notification. | [optional] 
**id** | **Number** | Notification ID | [optional] 
**message** | **String** | A message indicating the overall status of the webhook notification. | [optional] 
**path** | **String** | The path to the actual file that triggered this notification. | [optional] 
**requestHeaders** | **String** | A JSON-encoded string with headers that were sent with the webhook. | [optional] 
**requestMethod** | **String** | The HTTP verb used to perform the webhook. | [optional] 
**requestUrl** | **String** | The webhook request URL. | [optional] 
**status** | **Number** | HTTP status code returned in the webhook response. | [optional] 
**success** | **Boolean** | &#x60;true&#x60; if the webhook succeeded by receiving a 200 or 204 response. | [optional] 



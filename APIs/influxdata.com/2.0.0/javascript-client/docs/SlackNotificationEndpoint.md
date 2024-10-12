# InfluxOssApiService.SlackNotificationEndpoint

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** |  | [optional] [readonly] 
**description** | **String** | An optional description of the notification endpoint. | [optional] 
**id** | **String** |  | [optional] 
**labels** | [**[Label]**](Label.md) |  | [optional] 
**links** | [**NotificationEndpointBaseLinks**](NotificationEndpointBaseLinks.md) |  | [optional] 
**name** | **String** |  | 
**orgID** | **String** |  | [optional] 
**status** | **String** | The status of the endpoint. | [optional] [default to &#39;active&#39;]
**type** | [**NotificationEndpointType**](NotificationEndpointType.md) |  | 
**updatedAt** | **Date** |  | [optional] [readonly] 
**userID** | **String** |  | [optional] 
**token** | **String** | Specifies the API token string. Specify either &#x60;URL&#x60; or &#x60;Token&#x60;. | [optional] 
**url** | **String** | Specifies the URL of the Slack endpoint. Specify either &#x60;URL&#x60; or &#x60;Token&#x60;. | [optional] 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)





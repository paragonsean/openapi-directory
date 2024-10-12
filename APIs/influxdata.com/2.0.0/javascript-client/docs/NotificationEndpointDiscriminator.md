# InfluxOssApiService.NotificationEndpointDiscriminator

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
**token** | **String** | Specifies the Telegram bot token. See https://core.telegram.org/bots#creating-a-new-bot . | 
**url** | **String** |  | 
**clientURL** | **String** |  | [optional] 
**routingKey** | **String** |  | 
**authMethod** | **String** |  | 
**contentTemplate** | **String** |  | [optional] 
**headers** | **{String: String}** | Customized headers. | [optional] 
**method** | **String** |  | 
**password** | **String** |  | [optional] 
**username** | **String** |  | [optional] 
**channel** | **String** | ID of the telegram channel, a chat_id in https://core.telegram.org/bots/api#sendmessage . | 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `inactive` (value: `"inactive"`)





## Enum: AuthMethodEnum


* `none` (value: `"none"`)

* `basic` (value: `"basic"`)

* `bearer` (value: `"bearer"`)





## Enum: MethodEnum


* `POST` (value: `"POST"`)

* `GET` (value: `"GET"`)

* `PUT` (value: `"PUT"`)





# DracoonApi.Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Creation date | 
**createdBy** | [**UserInfo**](UserInfo.md) |  | [optional] 
**eventTypeNames** | **[String]** | List of names of event types | 
**expireAt** | **Date** | Expiration date / time | 
**failStatus** | **Number** | Last HTTP status code when a webhook is disabled due to delivery failures | [optional] 
**id** | **Number** | ID | 
**isEnabled** | **Boolean** | Is enabled | 
**name** | **String** | Name | 
**secret** | **String** | Secret; used for event message signatures | [optional] 
**updatedAt** | **Date** | Modification date | 
**updatedBy** | [**UserInfo**](UserInfo.md) |  | [optional] 
**url** | **String** | URL | 



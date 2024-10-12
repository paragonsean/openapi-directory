# SalesLoftPlatform.CrmActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activityType** | **String** | The type of activity that is being recorded, if available. The values can change over time, but could be one of: email, phone, email reminder, inmail | [optional] 
**createdAt** | **Date** | Datetime of when the crm activity was created | [optional] 
**crmId** | **String** | The ID of the activity in your CRM, if written to your CRM | [optional] 
**customCrmFields** | **Object** | Additional fields that are logged to your CRM, if mapped by the team at the time of writing to your CRM | [optional] 
**description** | **String** | The description field of the activity in your CRM | [optional] 
**error** | **String** | Information about why this crm activity failed to sync, if it did fail to sync. Failed activities will be automatically retried and may become successful in the future | [optional] 
**id** | **Number** | CrmActivity ID | [optional] 
**person** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 
**subject** | **String** | The subject field of the activity in your CRM | [optional] 
**updatedAt** | **Date** | Datetime of when the crm activity was last updated | [optional] 
**user** | [**EmbeddedResource**](EmbeddedResource.md) |  | [optional] 



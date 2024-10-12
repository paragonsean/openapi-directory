# ThePlaidApi.Activity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity** | [**ActivityType**](ActivityType.md) |  | 
**id** | **String** | A unique identifier for the activity | 
**initiatedDate** | **String** | The date and time this activity was initiated [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format in UTC. | 
**initiator** | **String** | Application ID of the client who initiated the activity. | 
**scopes** | [**ScopesNullable**](ScopesNullable.md) |  | [optional] 
**state** | [**ActionState**](ActionState.md) |  | 
**targetApplicationId** | **String** | This field will map to the application ID that is returned from /item/applications/list, or provided to the institution in an oauth redirect. | [optional] 



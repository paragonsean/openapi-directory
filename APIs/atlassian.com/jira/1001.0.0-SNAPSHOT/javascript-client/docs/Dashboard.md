# TheJiraCloudPlatformRestApi.Dashboard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automaticRefreshMs** | **Number** | The automatic refresh interval for the dashboard in milliseconds. | [optional] [readonly] 
**description** | **String** |  | [optional] 
**editPermissions** | [**[SharePermission]**](SharePermission.md) | The details of any edit share permissions for the dashboard. | [optional] [readonly] 
**id** | **String** | The ID of the dashboard. | [optional] [readonly] 
**isFavourite** | **Boolean** | Whether the dashboard is selected as a favorite by the user. | [optional] [readonly] 
**isWritable** | **Boolean** | Whether the current user has permission to edit the dashboard. | [optional] [readonly] 
**name** | **String** | The name of the dashboard. | [optional] [readonly] 
**owner** | [**UserBean**](UserBean.md) | The owner of the dashboard. | [optional] [readonly] 
**popularity** | **Number** | The number of users who have this dashboard as a favorite. | [optional] [readonly] 
**rank** | **Number** | The rank of this dashboard. | [optional] [readonly] 
**self** | **String** | The URL of these dashboard details. | [optional] [readonly] 
**sharePermissions** | [**[SharePermission]**](SharePermission.md) | The details of any view share permissions for the dashboard. | [optional] [readonly] 
**systemDashboard** | **Boolean** | Whether the current dashboard is system dashboard. | [optional] [readonly] 
**view** | **String** | The URL of the dashboard. | [optional] [readonly] 



# Asana.WorkspaceMembershipResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **String** | Globally unique identifier of the resource, as a string. | [optional] [readonly] 
**resourceType** | **String** | The base type of this resource. | [optional] [readonly] 
**user** | [**UserCompact**](UserCompact.md) |  | [optional] 
**workspace** | [**WorkspaceCompact**](WorkspaceCompact.md) |  | [optional] 
**isActive** | **Boolean** | Reflects if this user still a member of the workspace. | [optional] [readonly] 
**isAdmin** | **Boolean** | Reflects if this user is an admin of the workspace. | [optional] [readonly] 
**isGuest** | **Boolean** | Reflects if this user is a guest of the workspace. | [optional] [readonly] 
**userTaskList** | [**UserTaskListCompact**](UserTaskListCompact.md) |  | [optional] 
**vacationDates** | [**WorkspaceMembershipResponseAllOfVacationDates**](WorkspaceMembershipResponseAllOfVacationDates.md) |  | [optional] 



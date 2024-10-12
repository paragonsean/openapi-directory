# PeopleApi.UpdateContactGroupRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contactGroup** | [**ContactGroup**](ContactGroup.md) |  | [optional] 
**readGroupFields** | **String** | Optional. A field mask to restrict which fields on the group are returned. Defaults to &#x60;metadata&#x60;, &#x60;groupType&#x60;, and &#x60;name&#x60; if not set or set to empty. Valid fields are: * clientData * groupType * memberCount * metadata * name | [optional] 
**updateGroupFields** | **String** | Optional. A field mask to restrict which fields on the group are updated. Multiple fields can be specified by separating them with commas. Defaults to &#x60;name&#x60; if not set or set to empty. Updated fields are replaced. Valid values are: * clientData * name | [optional] 



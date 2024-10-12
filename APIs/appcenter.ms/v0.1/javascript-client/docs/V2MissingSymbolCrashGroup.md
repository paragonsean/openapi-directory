# AppCenterClient.V2MissingSymbolCrashGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appBuild** | **String** | application build | 
**appId** | **String** | application id | 
**appVer** | **String** | application version | 
**crashCount** | **Number** | number of crashes that belong to this group | [optional] 
**errorCount** | **Number** | number of errors that belong to this group | [optional] 
**lastModified** | **Date** | last update date for the group | 
**missingSymbols** | [**[MissingSymbolGroupsList200ResponseGroupsInnerMissingSymbolsInner]**](MissingSymbolGroupsList200ResponseGroupsInnerMissingSymbolsInner.md) | list of missing symbols | 
**status** | **String** | group status | 
**symbolGroupId** | **String** | id of the symbol group | 



## Enum: StatusEnum


* `active` (value: `"active"`)

* `pending` (value: `"pending"`)

* `closed` (value: `"closed"`)





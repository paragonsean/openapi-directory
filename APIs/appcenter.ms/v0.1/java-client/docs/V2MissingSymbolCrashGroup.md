

# V2MissingSymbolCrashGroup

missing symbol crash group object

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appBuild** | **String** | application build |  |
|**appId** | **String** | application id |  |
|**appVer** | **String** | application version |  |
|**crashCount** | **Integer** | number of crashes that belong to this group |  [optional] |
|**errorCount** | **Integer** | number of errors that belong to this group |  [optional] |
|**lastModified** | **OffsetDateTime** | last update date for the group |  |
|**missingSymbols** | [**List&lt;MissingSymbolGroupsList200ResponseGroupsInnerMissingSymbolsInner&gt;**](MissingSymbolGroupsList200ResponseGroupsInnerMissingSymbolsInner.md) | list of missing symbols |  |
|**status** | [**StatusEnum**](#StatusEnum) | group status |  |
|**symbolGroupId** | **String** | id of the symbol group |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PENDING | &quot;pending&quot; |
| CLOSED | &quot;closed&quot; |




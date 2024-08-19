

# ListArchives200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The kind of the archive |  |
|**data** | [**ListArchives200ResponseData**](ListArchives200ResponseData.md) |  |  |
|**result** | [**ResultEnum**](#ResultEnum) | Result of the request |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| ARCHIVE_FULL | &quot;archiveFull&quot; |
| ARCHIVE_GROUPS | &quot;archiveGroups&quot; |
| ARCHIVE_RULES | &quot;archiveRules&quot; |
| ARCHIVE_DIRECTIVES | &quot;archiveDirectives&quot; |
| ARCHIVE_PARAMETERS | &quot;archiveParameters&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| ERROR | &quot;error&quot; |




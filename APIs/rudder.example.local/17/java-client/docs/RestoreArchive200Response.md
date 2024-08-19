

# RestoreArchive200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | The kind of the archive |  |
|**data** | [**RestoreArchive200ResponseData**](RestoreArchive200ResponseData.md) |  |  |
|**result** | [**ResultEnum**](#ResultEnum) | Result of the request |  |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| RESTORE_FULL_LATEST_ARCHIVE | &quot;restoreFullLatestArchive&quot; |
| RESTORE_GROUP_LATEST_ARCHIVE | &quot;restoreGroupLatestArchive&quot; |
| RESTORE_RULES_LATEST_ARCHIVE | &quot;restoreRulesLatestArchive&quot; |
| RESTORE_DIRECTIVES_LATEST_ARCHIVE | &quot;restoreDirectivesLatestArchive&quot; |
| RESTORE_PARAMETERS_LATEST_ARCHIVE | &quot;restoreParametersLatestArchive&quot; |
| RESTORE_FULL_LATEST_COMMIT | &quot;restoreFullLatestCommit&quot; |
| RESTORE_GROUP_LATEST_COMMIT | &quot;restoreGroupLatestCommit&quot; |
| RESTORE_RULES_LATEST_COMMIT | &quot;restoreRulesLatestCommit&quot; |
| RESTORE_DIRECTIVES_LATEST_COMMIT | &quot;restoreDirectivesLatestCommit&quot; |
| RESTORE_PARAMETERS_LATEST_COMMIT | &quot;restoreParametersLatestCommit&quot; |
| ARCHIVE_FULL_DATE_RESTORE | &quot;archiveFullDateRestore&quot; |
| ARCHIVE_GROUP_DATE_RESTORE | &quot;archiveGroupDateRestore&quot; |
| ARCHIVE_RULES_DATE_RESTORE | &quot;archiveRulesDateRestore&quot; |
| ARCHIVE_DIRECTIVES_DATE_RESTORE | &quot;archiveDirectivesDateRestore&quot; |
| ARCHIVE_PARAMETERS_DATE_RESTORE | &quot;archiveParametersDateRestore&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| ERROR | &quot;error&quot; |




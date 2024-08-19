

# FindingTypeStats

A FindingTypeStats resource represents stats regarding a specific FindingType of Findings under a given ScanRun.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**findingCount** | **Integer** | The count of findings belonging to this finding type. |  [optional] |
|**findingType** | [**FindingTypeEnum**](#FindingTypeEnum) | The finding type associated with the stats. |  [optional] |



## Enum: FindingTypeEnum

| Name | Value |
|---- | -----|
| FINDING_TYPE_UNSPECIFIED | &quot;FINDING_TYPE_UNSPECIFIED&quot; |
| MIXED_CONTENT | &quot;MIXED_CONTENT&quot; |
| OUTDATED_LIBRARY | &quot;OUTDATED_LIBRARY&quot; |
| ROSETTA_FLASH | &quot;ROSETTA_FLASH&quot; |
| XSS_CALLBACK | &quot;XSS_CALLBACK&quot; |
| XSS_ERROR | &quot;XSS_ERROR&quot; |
| CLEAR_TEXT_PASSWORD | &quot;CLEAR_TEXT_PASSWORD&quot; |
| INVALID_CONTENT_TYPE | &quot;INVALID_CONTENT_TYPE&quot; |
| XSS_ANGULAR_CALLBACK | &quot;XSS_ANGULAR_CALLBACK&quot; |
| INVALID_HEADER | &quot;INVALID_HEADER&quot; |
| MISSPELLED_SECURITY_HEADER_NAME | &quot;MISSPELLED_SECURITY_HEADER_NAME&quot; |
| MISMATCHING_SECURITY_HEADER_VALUES | &quot;MISMATCHING_SECURITY_HEADER_VALUES&quot; |
| ACCESSIBLE_GIT_REPOSITORY | &quot;ACCESSIBLE_GIT_REPOSITORY&quot; |
| ACCESSIBLE_SVN_REPOSITORY | &quot;ACCESSIBLE_SVN_REPOSITORY&quot; |
| ACCESSIBLE_ENV_FILE | &quot;ACCESSIBLE_ENV_FILE&quot; |




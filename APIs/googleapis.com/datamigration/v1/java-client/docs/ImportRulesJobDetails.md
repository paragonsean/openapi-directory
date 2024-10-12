

# ImportRulesJobDetails

Details regarding an Import Rules background job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fileFormat** | [**FileFormatEnum**](#FileFormatEnum) | Output only. The requested file format. |  [optional] [readonly] |
|**files** | **List&lt;String&gt;** | Output only. File names used for the import rules job. |  [optional] [readonly] |



## Enum: FileFormatEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPORT_RULES_FILE_FORMAT_UNSPECIFIED&quot; |
| HARBOUR_BRIDGE_SESSION_FILE | &quot;IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE&quot; |
| ORATOPG_CONFIG_FILE | &quot;IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE&quot; |




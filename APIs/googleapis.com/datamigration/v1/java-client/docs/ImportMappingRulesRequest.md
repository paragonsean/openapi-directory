

# ImportMappingRulesRequest

Request message for 'ImportMappingRules' request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCommit** | **Boolean** | Required. Should the conversion workspace be committed automatically after the import operation. |  [optional] |
|**rulesFiles** | [**List&lt;RulesFile&gt;**](RulesFile.md) | Required. One or more rules files. |  [optional] |
|**rulesFormat** | [**RulesFormatEnum**](#RulesFormatEnum) | Required. The format of the rules content file. |  [optional] |



## Enum: RulesFormatEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;IMPORT_RULES_FILE_FORMAT_UNSPECIFIED&quot; |
| HARBOUR_BRIDGE_SESSION_FILE | &quot;IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE&quot; |
| ORATOPG_CONFIG_FILE | &quot;IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE&quot; |




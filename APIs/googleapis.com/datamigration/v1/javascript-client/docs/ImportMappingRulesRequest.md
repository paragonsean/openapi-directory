# DatabaseMigrationApi.ImportMappingRulesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoCommit** | **Boolean** | Required. Should the conversion workspace be committed automatically after the import operation. | [optional] 
**rulesFiles** | [**[RulesFile]**](RulesFile.md) | Required. One or more rules files. | [optional] 
**rulesFormat** | **String** | Required. The format of the rules content file. | [optional] 



## Enum: RulesFormatEnum


* `UNSPECIFIED` (value: `"IMPORT_RULES_FILE_FORMAT_UNSPECIFIED"`)

* `HARBOUR_BRIDGE_SESSION_FILE` (value: `"IMPORT_RULES_FILE_FORMAT_HARBOUR_BRIDGE_SESSION_FILE"`)

* `ORATOPG_CONFIG_FILE` (value: `"IMPORT_RULES_FILE_FORMAT_ORATOPG_CONFIG_FILE"`)





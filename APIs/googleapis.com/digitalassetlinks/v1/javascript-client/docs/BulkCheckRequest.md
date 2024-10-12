# DigitalAssetLinksApi.BulkCheckRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowGoogleInternalDataSources** | **Boolean** | Same configuration as in Check request, all statements checks will use same configurations. | [optional] 
**defaultRelation** | **String** | If specified, will be used in any given template statement that doesn’t specify a relation. | [optional] 
**defaultSource** | [**Asset**](Asset.md) |  | [optional] 
**defaultTarget** | [**Asset**](Asset.md) |  | [optional] 
**skipCacheLookup** | **Boolean** | Same configuration as in Check request, all statements checks will use same configurations. | [optional] 
**statements** | [**[StatementTemplate]**](StatementTemplate.md) | List of statements to check. For each statement, you can omit a field if the corresponding default_* field below was supplied. Minimum 1 statement; maximum 1,000 statements. Any additional statements will be ignored. | [optional] 



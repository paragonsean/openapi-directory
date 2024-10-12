# CustomerInsightsManagementClient.ConnectorMapping

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectorMappingName** | **String** | The connector mapping name | [optional] [readonly] 
**connectorName** | **String** | The connector name. | [optional] [readonly] 
**connectorType** | [**ConnectorType**](ConnectorType.md) |  | [optional] 
**created** | **Date** | The created time. | [optional] [readonly] 
**dataFormatId** | **String** | The DataFormat ID. | [optional] [readonly] 
**description** | **String** | The description of the connector mapping. | [optional] 
**displayName** | **String** | Display name for the connector mapping. | [optional] 
**entityType** | **String** | Defines which entity type the file should map to. | 
**entityTypeName** | **String** | The mapping entity name. | 
**lastModified** | **Date** | The last modified time. | [optional] [readonly] 
**mappingProperties** | [**ConnectorMappingProperties**](ConnectorMappingProperties.md) |  | 
**nextRunTime** | **Date** | The next run time based on customer&#39;s settings. | [optional] [readonly] 
**runId** | **String** | The RunId. | [optional] [readonly] 
**state** | **String** | State of connector mapping. | [optional] [readonly] 
**tenantId** | **String** | The hub name. | [optional] [readonly] 



## Enum: EntityTypeEnum


* `None` (value: `"None"`)

* `Profile` (value: `"Profile"`)

* `Interaction` (value: `"Interaction"`)

* `Relationship` (value: `"Relationship"`)





## Enum: StateEnum


* `Creating` (value: `"Creating"`)

* `Created` (value: `"Created"`)

* `Failed` (value: `"Failed"`)

* `Ready` (value: `"Ready"`)

* `Running` (value: `"Running"`)

* `Stopped` (value: `"Stopped"`)

* `Expiring` (value: `"Expiring"`)





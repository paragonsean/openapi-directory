# AirbyteConfigurationApi.ConnectionUpdate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakingChange** | **Boolean** |  | [optional] 
**connectionId** | **String** |  | 
**geography** | [**Geography**](Geography.md) |  | [optional] 
**name** | **String** | Name that will be set to this connection | [optional] 
**namespaceDefinition** | [**NamespaceDefinitionType**](NamespaceDefinitionType.md) |  | [optional] 
**namespaceFormat** | **String** | Used when namespaceDefinition is &#39;customformat&#39;. If blank then behaves like namespaceDefinition &#x3D; &#39;destination&#39;. If \&quot;${SOURCE_NAMESPACE}\&quot; then behaves like namespaceDefinition &#x3D; &#39;source&#39;. | [optional] 
**nonBreakingChangesPreference** | [**NonBreakingChangesPreference**](NonBreakingChangesPreference.md) |  | [optional] 
**notifySchemaChanges** | **Boolean** |  | [optional] 
**operationIds** | **[String]** |  | [optional] 
**prefix** | **String** | Prefix that will be prepended to the name of each stream when it is written to the destination. | [optional] 
**resourceRequirements** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**schedule** | [**ConnectionSchedule**](ConnectionSchedule.md) |  | [optional] 
**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  | [optional] 
**scheduleType** | [**ConnectionScheduleType**](ConnectionScheduleType.md) |  | [optional] 
**sourceCatalogId** | **String** |  | [optional] 
**status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**syncCatalog** | [**AirbyteCatalog**](AirbyteCatalog.md) |  | [optional] 



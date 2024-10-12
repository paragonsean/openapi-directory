# AirbyteConfigurationApi.WebBackendConnectionRead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**catalogDiff** | [**CatalogDiff**](CatalogDiff.md) |  | [optional] 
**catalogId** | **String** |  | [optional] 
**connectionId** | **String** |  | 
**destination** | [**DestinationRead**](DestinationRead.md) |  | 
**destinationId** | **String** |  | 
**geography** | [**Geography**](Geography.md) |  | [optional] 
**isSyncing** | **Boolean** |  | 
**latestSyncJobCreatedAt** | **Number** | epoch time of the latest sync job. null if no sync job has taken place. | [optional] 
**latestSyncJobStatus** | [**JobStatus**](JobStatus.md) |  | [optional] 
**name** | **String** |  | 
**namespaceDefinition** | [**NamespaceDefinitionType**](NamespaceDefinitionType.md) |  | [optional] 
**namespaceFormat** | **String** | Used when namespaceDefinition is &#39;customformat&#39;. If blank then behaves like namespaceDefinition &#x3D; &#39;destination&#39;. If \&quot;${SOURCE_NAMESPACE}\&quot; then behaves like namespaceDefinition &#x3D; &#39;source&#39;. | [optional] 
**nonBreakingChangesPreference** | [**NonBreakingChangesPreference**](NonBreakingChangesPreference.md) |  | 
**notifySchemaChanges** | **Boolean** |  | 
**operationIds** | **[String]** |  | [optional] 
**operations** | [**[OperationRead]**](OperationRead.md) |  | [optional] 
**prefix** | **String** | Prefix that will be prepended to the name of each stream when it is written to the destination. | [optional] 
**resourceRequirements** | [**ResourceRequirements**](ResourceRequirements.md) |  | [optional] 
**schedule** | [**ConnectionSchedule**](ConnectionSchedule.md) |  | [optional] 
**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  | [optional] 
**scheduleType** | [**ConnectionScheduleType**](ConnectionScheduleType.md) |  | [optional] 
**schemaChange** | [**SchemaChange**](SchemaChange.md) |  | 
**source** | [**SourceRead**](SourceRead.md) |  | 
**sourceId** | **String** |  | 
**status** | [**ConnectionStatus**](ConnectionStatus.md) |  | 
**syncCatalog** | [**AirbyteCatalog**](AirbyteCatalog.md) |  | 





# WebBackendConnectionRead


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**catalogDiff** | [**CatalogDiff**](CatalogDiff.md) |  |  [optional] |
|**catalogId** | **UUID** |  |  [optional] |
|**connectionId** | **UUID** |  |  |
|**destination** | [**DestinationRead**](DestinationRead.md) |  |  |
|**destinationId** | **UUID** |  |  |
|**geography** | **Geography** |  |  [optional] |
|**isSyncing** | **Boolean** |  |  |
|**latestSyncJobCreatedAt** | **Long** | epoch time of the latest sync job. null if no sync job has taken place. |  [optional] |
|**latestSyncJobStatus** | **JobStatus** |  |  [optional] |
|**name** | **String** |  |  |
|**namespaceDefinition** | **NamespaceDefinitionType** |  |  [optional] |
|**namespaceFormat** | **String** | Used when namespaceDefinition is &#39;customformat&#39;. If blank then behaves like namespaceDefinition &#x3D; &#39;destination&#39;. If \&quot;${SOURCE_NAMESPACE}\&quot; then behaves like namespaceDefinition &#x3D; &#39;source&#39;. |  [optional] |
|**nonBreakingChangesPreference** | **NonBreakingChangesPreference** |  |  |
|**notifySchemaChanges** | **Boolean** |  |  |
|**operationIds** | **List&lt;UUID&gt;** |  |  [optional] |
|**operations** | [**List&lt;OperationRead&gt;**](OperationRead.md) |  |  [optional] |
|**prefix** | **String** | Prefix that will be prepended to the name of each stream when it is written to the destination. |  [optional] |
|**resourceRequirements** | [**ResourceRequirements**](ResourceRequirements.md) |  |  [optional] |
|**schedule** | [**ConnectionSchedule**](ConnectionSchedule.md) |  |  [optional] |
|**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  |  [optional] |
|**scheduleType** | **ConnectionScheduleType** |  |  [optional] |
|**schemaChange** | **SchemaChange** |  |  |
|**source** | [**SourceRead**](SourceRead.md) |  |  |
|**sourceId** | **UUID** |  |  |
|**status** | **ConnectionStatus** |  |  |
|**syncCatalog** | [**AirbyteCatalog**](AirbyteCatalog.md) |  |  |




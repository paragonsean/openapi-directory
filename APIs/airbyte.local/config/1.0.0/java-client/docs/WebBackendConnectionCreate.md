

# WebBackendConnectionCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**destinationId** | **UUID** |  |  |
|**geography** | **Geography** |  |  [optional] |
|**name** | **String** | Optional name of the connection |  [optional] |
|**namespaceDefinition** | **NamespaceDefinitionType** |  |  [optional] |
|**namespaceFormat** | **String** | Used when namespaceDefinition is &#39;customformat&#39;. If blank then behaves like namespaceDefinition &#x3D; &#39;destination&#39;. If \&quot;${SOURCE_NAMESPACE}\&quot; then behaves like namespaceDefinition &#x3D; &#39;source&#39;. |  [optional] |
|**nonBreakingChangesPreference** | **NonBreakingChangesPreference** |  |  [optional] |
|**operationIds** | **List&lt;UUID&gt;** |  |  [optional] |
|**operations** | [**List&lt;OperationCreate&gt;**](OperationCreate.md) |  |  [optional] |
|**prefix** | **String** | Prefix that will be prepended to the name of each stream when it is written to the destination. |  [optional] |
|**resourceRequirements** | [**ResourceRequirements**](ResourceRequirements.md) |  |  [optional] |
|**schedule** | [**ConnectionSchedule**](ConnectionSchedule.md) |  |  [optional] |
|**scheduleData** | [**ConnectionScheduleData**](ConnectionScheduleData.md) |  |  [optional] |
|**scheduleType** | **ConnectionScheduleType** |  |  [optional] |
|**sourceCatalogId** | **UUID** |  |  [optional] |
|**sourceId** | **UUID** |  |  |
|**status** | **ConnectionStatus** |  |  |
|**syncCatalog** | [**AirbyteCatalog**](AirbyteCatalog.md) |  |  [optional] |




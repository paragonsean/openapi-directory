

# DataFlowDebugPackage

Request body structure for starting data flow debug session.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFlow** | [**DataFlowDebugResource**](DataFlowDebugResource.md) |  |  [optional] |
|**datasets** | [**List&lt;DatasetDebugResource&gt;**](DatasetDebugResource.md) | List of datasets. |  [optional] |
|**debugSettings** | [**DataFlowDebugPackageDebugSettings**](DataFlowDebugPackageDebugSettings.md) |  |  [optional] |
|**linkedServices** | [**List&lt;LinkedServiceDebugResource&gt;**](LinkedServiceDebugResource.md) | List of linked services. |  [optional] |
|**sessionId** | **String** | The ID of data flow debug session. |  [optional] |
|**staging** | [**DataFlowStagingInfo**](DataFlowStagingInfo.md) |  |  [optional] |




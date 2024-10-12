

# ServiceMeshAnalysisMessage

AnalysisMessage is a single message produced by an analyzer, and it used to communicate to the end user about the state of their Service Mesh configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **Map&lt;String, Object&gt;** | A UI can combine these args with a template (based on message_base.type) to produce an internationalized message. |  [optional] |
|**description** | **String** | A human readable description of what the error means. It is suitable for non-internationalize display purposes. |  [optional] |
|**messageBase** | [**ServiceMeshAnalysisMessageBase**](ServiceMeshAnalysisMessageBase.md) |  |  [optional] |
|**resourcePaths** | **List&lt;String&gt;** | A list of strings specifying the resource identifiers that were the cause of message generation. A \&quot;path\&quot; here may be: * MEMBERSHIP_ID if the cause is a specific member cluster * MEMBERSHIP_ID/(NAMESPACE/)?RESOURCETYPE/NAME if the cause is a resource in a cluster |  [optional] |




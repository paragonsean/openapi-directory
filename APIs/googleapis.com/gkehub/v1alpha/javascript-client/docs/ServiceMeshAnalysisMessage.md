# GkeHubApi.ServiceMeshAnalysisMessage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **{String: Object}** | A UI can combine these args with a template (based on message_base.type) to produce an internationalized message. | [optional] 
**description** | **String** | A human readable description of what the error means. It is suitable for non-internationalize display purposes. | [optional] 
**messageBase** | [**ServiceMeshAnalysisMessageBase**](ServiceMeshAnalysisMessageBase.md) |  | [optional] 
**resourcePaths** | **[String]** | A list of strings specifying the resource identifiers that were the cause of message generation. A \&quot;path\&quot; here may be: * MEMBERSHIP_ID if the cause is a specific member cluster * MEMBERSHIP_ID/(NAMESPACE/)?RESOURCETYPE/NAME if the cause is a resource in a cluster | [optional] 



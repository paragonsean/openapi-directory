# CloudAssetApi.GoogleCloudAssetV1AccessControlList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accesses** | [**[GoogleCloudAssetV1Access]**](GoogleCloudAssetV1Access.md) | The accesses that match one of the following conditions: - The access_selector, if it is specified in request; - Otherwise, access specifiers reachable from the policy binding&#39;s role. | [optional] 
**conditionEvaluation** | [**ConditionEvaluation**](ConditionEvaluation.md) |  | [optional] 
**resourceEdges** | [**[GoogleCloudAssetV1Edge]**](GoogleCloudAssetV1Edge.md) | Resource edges of the graph starting from the policy attached resource to any descendant resources. The Edge.source_node contains the full resource name of a parent resource and Edge.target_node contains the full resource name of a child resource. This field is present only if the output_resource_edges option is enabled in request. | [optional] 
**resources** | [**[GoogleCloudAssetV1Resource]**](GoogleCloudAssetV1Resource.md) | The resources that match one of the following conditions: - The resource_selector, if it is specified in request; - Otherwise, resources reachable from the policy attached resource. | [optional] 



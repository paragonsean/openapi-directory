# CloudAssetApi.GoogleCloudAssetV1p4beta1IdentityList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupEdges** | [**[GoogleCloudAssetV1p4beta1Edge]**](GoogleCloudAssetV1p4beta1Edge.md) | Group identity edges of the graph starting from the binding&#39;s group members to any node of the identities. The Edge.source_node contains a group, such as \&quot;group:parent@google.com\&quot;. The Edge.target_node contains a member of the group, such as \&quot;group:child@google.com\&quot; or \&quot;user:foo@google.com\&quot;. This field is present only if the output_group_edges option is enabled in request. | [optional] 
**identities** | [**[GoogleCloudAssetV1p4beta1Identity]**](GoogleCloudAssetV1p4beta1Identity.md) | Only the identities that match one of the following conditions will be presented: - The identity_selector, if it is specified in request; - Otherwise, identities reachable from the policy binding&#39;s members. | [optional] 



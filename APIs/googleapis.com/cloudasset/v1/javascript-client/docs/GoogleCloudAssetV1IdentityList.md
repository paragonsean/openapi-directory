# CloudAssetApi.GoogleCloudAssetV1IdentityList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupEdges** | [**[GoogleCloudAssetV1Edge]**](GoogleCloudAssetV1Edge.md) | Group identity edges of the graph starting from the binding&#39;s group members to any node of the identities. The Edge.source_node contains a group, such as &#x60;group:parent@google.com&#x60;. The Edge.target_node contains a member of the group, such as &#x60;group:child@google.com&#x60; or &#x60;user:foo@google.com&#x60;. This field is present only if the output_group_edges option is enabled in request. | [optional] 
**identities** | [**[GoogleCloudAssetV1Identity]**](GoogleCloudAssetV1Identity.md) | Only the identities that match one of the following conditions will be presented: - The identity_selector, if it is specified in request; - Otherwise, identities reachable from the policy binding&#39;s members. | [optional] 



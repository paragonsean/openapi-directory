

# GoogleCloudDiscoveryengineV1alphaDocumentAclInfoAccessRestriction

AclRestriction to model complex inheritance restrictions. Example: Modeling a \"Both Permit\" inheritance, where to access a child document, user needs to have access to parent document. Document Hierarchy - Space_S --> Page_P. Readers: Space_S: group_1, user_1 Page_P: group_2, group_3, user_2 Space_S ACL Restriction - { \"acl_info\": { \"readers\": [ { \"principals\": [ { \"group_id\": \"group_1\" }, { \"user_id\": \"user_1\" } ] } ] } } Page_P ACL Restriction. { \"acl_info\": { \"readers\": [ { \"principals\": [ { \"group_id\": \"group_2\" }, { \"group_id\": \"group_3\" }, { \"user_id\": \"user_2\" } ], }, { \"principals\": [ { \"group_id\": \"group_1\" }, { \"user_id\": \"user_1\" } ], } ] } }

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principals** | [**List&lt;GoogleCloudDiscoveryengineV1alphaPrincipal&gt;**](GoogleCloudDiscoveryengineV1alphaPrincipal.md) | List of principals. |  [optional] |




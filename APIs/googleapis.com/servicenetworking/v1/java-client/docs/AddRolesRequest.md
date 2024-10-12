

# AddRolesRequest

Request for AddRoles to allow Service Producers to add roles in the shared VPC host project for them to use.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerNetwork** | **String** | Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is a project number, as in &#39;12345&#39; {network} is a network name. |  [optional] |
|**policyBinding** | [**List&lt;PolicyBinding&gt;**](PolicyBinding.md) | Required. List of policy bindings to add to shared VPC host project. |  [optional] |




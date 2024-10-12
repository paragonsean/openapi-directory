# ApigeeApi.GoogleCloudApigeeV1RoutingRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**basepath** | **String** | URI path prefix used to route to the specified environment. May contain one or more wildcards. For example, path segments consisting of a single &#x60;*&#x60; character will match any string. | [optional] 
**deploymentGroup** | **String** | Name of a deployment group in an environment bound to the environment group in the following format: &#x60;organizations/{org}/environment/{env}/deploymentGroups/{group}&#x60; Only one of environment or deployment_group will be set. | [optional] 
**envGroupRevision** | **String** | The env group config revision_id when this rule was added or last updated. This value is set when the rule is created and will only update if the the environment_id changes. It is used to determine if the runtime is up to date with respect to this rule. This field is omitted from the IngressConfig unless the GetDeployedIngressConfig API is called with view&#x3D;FULL. | [optional] 
**environment** | **String** | Name of an environment bound to the environment group in the following format: &#x60;organizations/{org}/environments/{env}&#x60;. Only one of environment or deployment_group will be set. | [optional] 
**otherTargets** | **[String]** | Conflicting targets, which will be resource names specifying either deployment groups or environments. | [optional] 
**receiver** | **String** | The resource name of the proxy revision that is receiving this basepath in the following format: &#x60;organizations/{org}/apis/{api}/revisions/{rev}&#x60;. This field is omitted from the IngressConfig unless the GetDeployedIngressConfig API is called with view&#x3D;FULL. | [optional] 
**updateTime** | **String** | The unix timestamp when this rule was updated. This is updated whenever env_group_revision is updated. This field is omitted from the IngressConfig unless the GetDeployedIngressConfig API is called with view&#x3D;FULL. | [optional] 



# ApigeeApi.GoogleCloudApigeeV1Deployment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiProxy** | **String** | API proxy. | [optional] 
**deployStartTime** | **String** | Time the API proxy was marked &#x60;deployed&#x60; in the control plane in millisconds since epoch. | [optional] 
**environment** | **String** | Environment. | [optional] 
**errors** | [**[GoogleRpcStatus]**](GoogleRpcStatus.md) | Errors reported for this deployment. Populated only when state &#x3D;&#x3D; ERROR. **Note**: This field is displayed only when viewing deployment status. | [optional] 
**instances** | [**[GoogleCloudApigeeV1InstanceDeploymentStatus]**](GoogleCloudApigeeV1InstanceDeploymentStatus.md) | Status reported by each runtime instance. **Note**: This field is displayed only when viewing deployment status. | [optional] 
**pods** | [**[GoogleCloudApigeeV1PodStatus]**](GoogleCloudApigeeV1PodStatus.md) | Status reported by runtime pods. **Note**: **This field is deprecated**. Runtime versions 1.3 and above report instance level status rather than pod status. | [optional] 
**proxyDeploymentType** | **String** | Output only. The type of the deployment (standard or extensible) Deployed proxy revision will be marked as extensible in following 2 cases. 1. The deployed proxy revision uses extensible policies. 2. If a environment supports flowhooks and flow hook is configured. | [optional] [readonly] 
**revision** | **String** | API proxy revision. | [optional] 
**routeConflicts** | [**[GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict]**](GoogleCloudApigeeV1DeploymentChangeReportRoutingConflict.md) | Conflicts in the desired state routing configuration. The presence of conflicts does not cause the state to be &#x60;ERROR&#x60;, but it will mean that some of the deployment&#39;s base paths are not routed to its environment. If the conflicts change, the state will transition to &#x60;PROGRESSING&#x60; until the latest configuration is rolled out to all instances. **Note**: This field is displayed only when viewing deployment status. | [optional] 
**serviceAccount** | **String** | The full resource name of Cloud IAM Service Account that this deployment is using, eg, &#x60;projects/-/serviceAccounts/{email}&#x60;. | [optional] 
**state** | **String** | Current state of the deployment. **Note**: This field is displayed only when viewing deployment status. | [optional] 



## Enum: ProxyDeploymentTypeEnum


* `PROXY_DEPLOYMENT_TYPE_UNSPECIFIED` (value: `"PROXY_DEPLOYMENT_TYPE_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `EXTENSIBLE` (value: `"EXTENSIBLE"`)





## Enum: StateEnum


* `RUNTIME_STATE_UNSPECIFIED` (value: `"RUNTIME_STATE_UNSPECIFIED"`)

* `READY` (value: `"READY"`)

* `PROGRESSING` (value: `"PROGRESSING"`)

* `ERROR` (value: `"ERROR"`)





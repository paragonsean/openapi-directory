# GkeHubApi.PolicyControllerHubConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditIntervalSeconds** | **String** | Sets the interval for Policy Controller Audit Scans (in seconds). When set to 0, this disables audit functionality altogether. | [optional] 
**constraintViolationLimit** | **String** | The maximum number of audit violations to be stored in a constraint. If not set, the internal default (currently 20) will be used. | [optional] 
**deploymentConfigs** | [**{String: PolicyControllerPolicyControllerDeploymentConfig}**](PolicyControllerPolicyControllerDeploymentConfig.md) | Map of deployment configs to deployments (\&quot;admission\&quot;, \&quot;audit\&quot;, \&quot;mutation&#39;). | [optional] 
**exemptableNamespaces** | **[String]** | The set of namespaces that are excluded from Policy Controller checks. Namespaces do not need to currently exist on the cluster. | [optional] 
**installSpec** | **String** | The install_spec represents the intended state specified by the latest request that mutated install_spec in the feature spec, not the lifecycle state of the feature observed by the Hub feature controller that is reported in the feature state. | [optional] 
**logDeniesEnabled** | **Boolean** | Logs all denies and dry run failures. | [optional] 
**monitoring** | [**PolicyControllerMonitoringConfig**](PolicyControllerMonitoringConfig.md) |  | [optional] 
**mutationEnabled** | **Boolean** | Enables the ability to mutate resources using Policy Controller. | [optional] 
**policyContent** | [**PolicyControllerPolicyContentSpec**](PolicyControllerPolicyContentSpec.md) |  | [optional] 
**referentialRulesEnabled** | **Boolean** | Enables the ability to use Constraint Templates that reference to objects other than the object currently being evaluated. | [optional] 



## Enum: InstallSpecEnum


* `UNSPECIFIED` (value: `"INSTALL_SPEC_UNSPECIFIED"`)

* `NOT_INSTALLED` (value: `"INSTALL_SPEC_NOT_INSTALLED"`)

* `ENABLED` (value: `"INSTALL_SPEC_ENABLED"`)

* `SUSPENDED` (value: `"INSTALL_SPEC_SUSPENDED"`)

* `DETACHED` (value: `"INSTALL_SPEC_DETACHED"`)







# PolicyControllerHubConfig

Configuration for Policy Controller

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**auditIntervalSeconds** | **String** | Sets the interval for Policy Controller Audit Scans (in seconds). When set to 0, this disables audit functionality altogether. |  [optional] |
|**constraintViolationLimit** | **String** | The maximum number of audit violations to be stored in a constraint. If not set, the internal default (currently 20) will be used. |  [optional] |
|**deploymentConfigs** | [**Map&lt;String, PolicyControllerPolicyControllerDeploymentConfig&gt;**](PolicyControllerPolicyControllerDeploymentConfig.md) | Map of deployment configs to deployments (\&quot;admission\&quot;, \&quot;audit\&quot;, \&quot;mutation&#39;). |  [optional] |
|**exemptableNamespaces** | **List&lt;String&gt;** | The set of namespaces that are excluded from Policy Controller checks. Namespaces do not need to currently exist on the cluster. |  [optional] |
|**installSpec** | [**InstallSpecEnum**](#InstallSpecEnum) | The install_spec represents the intended state specified by the latest request that mutated install_spec in the feature spec, not the lifecycle state of the feature observed by the Hub feature controller that is reported in the feature state. |  [optional] |
|**logDeniesEnabled** | **Boolean** | Logs all denies and dry run failures. |  [optional] |
|**monitoring** | [**PolicyControllerMonitoringConfig**](PolicyControllerMonitoringConfig.md) |  |  [optional] |
|**mutationEnabled** | **Boolean** | Enables the ability to mutate resources using Policy Controller. |  [optional] |
|**policyContent** | [**PolicyControllerPolicyContentSpec**](PolicyControllerPolicyContentSpec.md) |  |  [optional] |
|**referentialRulesEnabled** | **Boolean** | Enables the ability to use Constraint Templates that reference to objects other than the object currently being evaluated. |  [optional] |



## Enum: InstallSpecEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;INSTALL_SPEC_UNSPECIFIED&quot; |
| NOT_INSTALLED | &quot;INSTALL_SPEC_NOT_INSTALLED&quot; |
| ENABLED | &quot;INSTALL_SPEC_ENABLED&quot; |
| SUSPENDED | &quot;INSTALL_SPEC_SUSPENDED&quot; |
| DETACHED | &quot;INSTALL_SPEC_DETACHED&quot; |




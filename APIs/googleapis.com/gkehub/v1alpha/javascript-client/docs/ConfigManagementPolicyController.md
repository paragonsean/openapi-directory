# GkeHubApi.ConfigManagementPolicyController

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auditIntervalSeconds** | **String** | Sets the interval for Policy Controller Audit Scans (in seconds). When set to 0, this disables audit functionality altogether. | [optional] 
**enabled** | **Boolean** | Enables the installation of Policy Controller. If false, the rest of PolicyController fields take no effect. | [optional] 
**exemptableNamespaces** | **[String]** | The set of namespaces that are excluded from Policy Controller checks. Namespaces do not need to currently exist on the cluster. | [optional] 
**logDeniesEnabled** | **Boolean** | Logs all denies and dry run failures. | [optional] 
**monitoring** | [**ConfigManagementPolicyControllerMonitoring**](ConfigManagementPolicyControllerMonitoring.md) |  | [optional] 
**mutationEnabled** | **Boolean** | Enable or disable mutation in policy controller. If true, mutation CRDs, webhook and controller deployment will be deployed to the cluster. | [optional] 
**referentialRulesEnabled** | **Boolean** | Enables the ability to use Constraint Templates that reference to objects other than the object currently being evaluated. | [optional] 
**templateLibraryInstalled** | **Boolean** | Installs the default template library along with Policy Controller. | [optional] 
**updateTime** | **String** | Output only. Last time this membership spec was updated. | [optional] [readonly] 



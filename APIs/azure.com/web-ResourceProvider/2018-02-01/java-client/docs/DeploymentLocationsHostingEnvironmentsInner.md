

# DeploymentLocationsHostingEnvironmentsInner

Description of an App Service Environment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedMultiSizes** | **String** | List of comma separated strings describing which VM sizes are allowed for front-ends. |  [optional] [readonly] |
|**allowedWorkerSizes** | **String** | List of comma separated strings describing which VM sizes are allowed for workers. |  [optional] [readonly] |
|**apiManagementAccountId** | **String** | API Management Account associated with the App Service Environment. |  [optional] |
|**clusterSettings** | [**List&lt;DeploymentLocationsHostingEnvironmentsInnerClusterSettingsInner&gt;**](DeploymentLocationsHostingEnvironmentsInnerClusterSettingsInner.md) | Custom settings for changing the behavior of the App Service Environment. |  [optional] |
|**databaseEdition** | **String** | Edition of the metadata database for the App Service Environment, e.g. \&quot;Standard\&quot;. |  [optional] [readonly] |
|**databaseServiceObjective** | **String** | Service objective of the metadata database for the App Service Environment, e.g. \&quot;S0\&quot;. |  [optional] [readonly] |
|**defaultFrontEndScaleFactor** | **Integer** | Default Scale Factor for FrontEnds. |  [optional] [readonly] |
|**dnsSuffix** | **String** | DNS suffix of the App Service Environment. |  [optional] |
|**dynamicCacheEnabled** | **Boolean** | True/false indicating whether the App Service Environment is suspended. The environment can be suspended e.g. when the management endpoint is no longer available (most likely because NSG blocked the incoming traffic). |  [optional] |
|**environmentCapacities** | [**List&lt;DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner&gt;**](DeploymentLocationsHostingEnvironmentsInnerEnvironmentCapacitiesInner.md) | Current total, used, and available worker capacities. |  [optional] [readonly] |
|**environmentIsHealthy** | **Boolean** | True/false indicating whether the App Service Environment is healthy. |  [optional] [readonly] |
|**environmentStatus** | **String** | Detailed message about with results of the last check of the App Service Environment. |  [optional] [readonly] |
|**frontEndScaleFactor** | **Integer** | Scale factor for front-ends. |  [optional] |
|**hasLinuxWorkers** | **Boolean** | Flag that displays whether an ASE has linux workers or not |  [optional] |
|**internalLoadBalancingMode** | [**InternalLoadBalancingModeEnum**](#InternalLoadBalancingModeEnum) | Specifies which endpoints to serve internally in the Virtual Network for the App Service Environment. |  [optional] |
|**ipsslAddressCount** | **Integer** | Number of IP SSL addresses reserved for the App Service Environment. |  [optional] |
|**lastAction** | **String** | Last deployment action on the App Service Environment. |  [optional] [readonly] |
|**lastActionResult** | **String** | Result of the last deployment action on the App Service Environment. |  [optional] [readonly] |
|**location** | **String** | Location of the App Service Environment, e.g. \&quot;West US\&quot;. |  |
|**maximumNumberOfMachines** | **Integer** | Maximum number of VMs in the App Service Environment. |  [optional] [readonly] |
|**multiRoleCount** | **Integer** | Number of front-end instances. |  [optional] |
|**multiSize** | **String** | Front-end VM size, e.g. \&quot;Medium\&quot;, \&quot;Large\&quot;. |  [optional] |
|**name** | **String** | Name of the App Service Environment. |  |
|**networkAccessControlList** | [**List&lt;DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner&gt;**](DeploymentLocationsHostingEnvironmentsInnerNetworkAccessControlListInner.md) | Access control list for controlling traffic to the App Service Environment. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the App Service Environment. |  [optional] [readonly] |
|**resourceGroup** | **String** | Resource group of the App Service Environment. |  [optional] [readonly] |
|**sslCertKeyVaultId** | **String** | Key Vault ID for ILB App Service Environment default SSL certificate |  [optional] |
|**sslCertKeyVaultSecretName** | **String** | Key Vault Secret Name for ILB App Service Environment default SSL certificate |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Current status of the App Service Environment. |  [optional] [readonly] |
|**subscriptionId** | **String** | Subscription of the App Service Environment. |  [optional] [readonly] |
|**suspended** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if the App Service Environment is suspended; otherwise, &lt;code&gt;false&lt;/code&gt;. The environment can be suspended, e.g. when the management endpoint is no longer available  (most likely because NSG blocked the incoming traffic). |  [optional] |
|**upgradeDomains** | **Integer** | Number of upgrade domains of the App Service Environment. |  [optional] [readonly] |
|**userWhitelistedIpRanges** | **List&lt;String&gt;** | User added ip ranges to whitelist on ASE db |  [optional] |
|**vipMappings** | [**List&lt;DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner&gt;**](DeploymentLocationsHostingEnvironmentsInnerVipMappingsInner.md) | Description of IP SSL mapping for the App Service Environment. |  [optional] [readonly] |
|**virtualNetwork** | [**DeploymentLocationsHostingEnvironmentsInnerVirtualNetwork**](DeploymentLocationsHostingEnvironmentsInnerVirtualNetwork.md) |  |  |
|**vnetName** | **String** | Name of the Virtual Network for the App Service Environment. |  [optional] |
|**vnetResourceGroupName** | **String** | Resource group of the Virtual Network. |  [optional] |
|**vnetSubnetName** | **String** | Subnet of the Virtual Network. |  [optional] |
|**workerPools** | [**List&lt;DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner&gt;**](DeploymentLocationsHostingEnvironmentsInnerWorkerPoolsInner.md) | Description of worker pools with worker size IDs, VM sizes, and number of workers in each pool. |  |



## Enum: InternalLoadBalancingModeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| WEB | &quot;Web&quot; |
| PUBLISHING | &quot;Publishing&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| DELETING | &quot;Deleting&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PREPARING | &quot;Preparing&quot; |
| READY | &quot;Ready&quot; |
| SCALING | &quot;Scaling&quot; |
| DELETING | &quot;Deleting&quot; |




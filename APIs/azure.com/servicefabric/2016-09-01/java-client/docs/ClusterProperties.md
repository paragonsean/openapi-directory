

# ClusterProperties

The cluster resource properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableClusterVersions** | [**List&lt;ClusterVersionDetails&gt;**](ClusterVersionDetails.md) | The available cluster code version which the cluster can upgrade to, note that you must choose upgradeMode to manual to upgrade to |  [optional] [readonly] |
|**azureActiveDirectory** | [**AzureActiveDirectory**](AzureActiveDirectory.md) |  |  [optional] |
|**certificate** | [**CertificateDescription**](CertificateDescription.md) |  |  [optional] |
|**clientCertificateCommonNames** | [**List&lt;ClientCertificateCommonName&gt;**](ClientCertificateCommonName.md) |  List of client certificates to whitelist based on common names |  [optional] |
|**clientCertificateThumbprints** | [**List&lt;ClientCertificateThumbprint&gt;**](ClientCertificateThumbprint.md) | The client thumbprint details ,it is used for client access for cluster operation |  [optional] |
|**clusterCodeVersion** | **String** | The ServiceFabric code version running in your cluster |  [optional] |
|**clusterEndpoint** | **String** | The endpoint for the cluster connecting to servicefabric resource provider |  [optional] [readonly] |
|**clusterId** | **String** | The unique identifier for the cluster resource |  [optional] [readonly] |
|**clusterState** | [**ClusterStateEnum**](#ClusterStateEnum) | The state for the cluster |  [optional] [readonly] |
|**diagnosticsStorageAccountConfig** | [**DiagnosticsStorageAccountConfig**](DiagnosticsStorageAccountConfig.md) |  |  [optional] |
|**fabricSettings** | [**List&lt;SettingsSectionDescription&gt;**](SettingsSectionDescription.md) | List of custom fabric settings to configure the cluster. |  [optional] |
|**managementEndpoint** | **String** | The http management endpoint of the cluster |  |
|**nodeTypes** | [**List&lt;NodeTypeDescription&gt;**](NodeTypeDescription.md) | The list of node types that make up the cluster |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the cluster resource |  [optional] [readonly] |
|**reliabilityLevel** | [**ReliabilityLevelEnum**](#ReliabilityLevelEnum) | Cluster reliability level indicates replica set size of system service |  [optional] |
|**reverseProxyCertificate** | [**CertificateDescription**](CertificateDescription.md) |  |  [optional] |
|**upgradeDescription** | [**ClusterUpgradePolicy**](ClusterUpgradePolicy.md) |  |  [optional] |
|**upgradeMode** | [**UpgradeModeEnum**](#UpgradeModeEnum) | Cluster upgrade mode indicates if fabric upgrade is initiated automatically by the system or not |  [optional] |
|**vmImage** | **String** | The name of VM image VMSS has been configured with. Generic names such as Windows or Linux can be used. |  [optional] |



## Enum: ClusterStateEnum

| Name | Value |
|---- | -----|
| WAITING_FOR_NODES | &quot;WaitingForNodes&quot; |
| DEPLOYING | &quot;Deploying&quot; |
| BASELINE_UPGRADE | &quot;BaselineUpgrade&quot; |
| UPDATING_USER_CONFIGURATION | &quot;UpdatingUserConfiguration&quot; |
| UPDATING_USER_CERTIFICATE | &quot;UpdatingUserCertificate&quot; |
| UPDATING_INFRASTRUCTURE | &quot;UpdatingInfrastructure&quot; |
| ENFORCING_CLUSTER_VERSION | &quot;EnforcingClusterVersion&quot; |
| UPGRADE_SERVICE_UNREACHABLE | &quot;UpgradeServiceUnreachable&quot; |
| AUTO_SCALE | &quot;AutoScale&quot; |
| READY | &quot;Ready&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| UPDATING | &quot;Updating&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



## Enum: ReliabilityLevelEnum

| Name | Value |
|---- | -----|
| BRONZE | &quot;Bronze&quot; |
| SILVER | &quot;Silver&quot; |
| GOLD | &quot;Gold&quot; |
| PLATINUM | &quot;Platinum&quot; |



## Enum: UpgradeModeEnum

| Name | Value |
|---- | -----|
| AUTOMATIC | &quot;Automatic&quot; |
| MANUAL | &quot;Manual&quot; |




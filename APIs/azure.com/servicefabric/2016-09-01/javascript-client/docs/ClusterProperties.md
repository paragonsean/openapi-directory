# ServiceFabricManagementClient.ClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableClusterVersions** | [**[ClusterVersionDetails]**](ClusterVersionDetails.md) | The available cluster code version which the cluster can upgrade to, note that you must choose upgradeMode to manual to upgrade to | [optional] [readonly] 
**azureActiveDirectory** | [**AzureActiveDirectory**](AzureActiveDirectory.md) |  | [optional] 
**certificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**clientCertificateCommonNames** | [**[ClientCertificateCommonName]**](ClientCertificateCommonName.md) |  List of client certificates to whitelist based on common names | [optional] 
**clientCertificateThumbprints** | [**[ClientCertificateThumbprint]**](ClientCertificateThumbprint.md) | The client thumbprint details ,it is used for client access for cluster operation | [optional] 
**clusterCodeVersion** | **String** | The ServiceFabric code version running in your cluster | [optional] 
**clusterEndpoint** | **String** | The endpoint for the cluster connecting to servicefabric resource provider | [optional] [readonly] 
**clusterId** | **String** | The unique identifier for the cluster resource | [optional] [readonly] 
**clusterState** | **String** | The state for the cluster | [optional] [readonly] 
**diagnosticsStorageAccountConfig** | [**DiagnosticsStorageAccountConfig**](DiagnosticsStorageAccountConfig.md) |  | [optional] 
**fabricSettings** | [**[SettingsSectionDescription]**](SettingsSectionDescription.md) | List of custom fabric settings to configure the cluster. | [optional] 
**managementEndpoint** | **String** | The http management endpoint of the cluster | 
**nodeTypes** | [**[NodeTypeDescription]**](NodeTypeDescription.md) | The list of node types that make up the cluster | 
**provisioningState** | **String** | The provisioning state of the cluster resource | [optional] [readonly] 
**reliabilityLevel** | **String** | Cluster reliability level indicates replica set size of system service | [optional] 
**reverseProxyCertificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**upgradeDescription** | [**ClusterUpgradePolicy**](ClusterUpgradePolicy.md) |  | [optional] 
**upgradeMode** | **String** | Cluster upgrade mode indicates if fabric upgrade is initiated automatically by the system or not | [optional] 
**vmImage** | **String** | The name of VM image VMSS has been configured with. Generic names such as Windows or Linux can be used. | [optional] 



## Enum: ClusterStateEnum


* `WaitingForNodes` (value: `"WaitingForNodes"`)

* `Deploying` (value: `"Deploying"`)

* `BaselineUpgrade` (value: `"BaselineUpgrade"`)

* `UpdatingUserConfiguration` (value: `"UpdatingUserConfiguration"`)

* `UpdatingUserCertificate` (value: `"UpdatingUserCertificate"`)

* `UpdatingInfrastructure` (value: `"UpdatingInfrastructure"`)

* `EnforcingClusterVersion` (value: `"EnforcingClusterVersion"`)

* `UpgradeServiceUnreachable` (value: `"UpgradeServiceUnreachable"`)

* `AutoScale` (value: `"AutoScale"`)

* `Ready` (value: `"Ready"`)





## Enum: ProvisioningStateEnum


* `Updating` (value: `"Updating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





## Enum: ReliabilityLevelEnum


* `Bronze` (value: `"Bronze"`)

* `Silver` (value: `"Silver"`)

* `Gold` (value: `"Gold"`)

* `Platinum` (value: `"Platinum"`)





## Enum: UpgradeModeEnum


* `Automatic` (value: `"Automatic"`)

* `Manual` (value: `"Manual"`)





# ServiceFabricManagementClient.ClusterProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addOnFeatures** | [**[AddOnFeatures]**](AddOnFeatures.md) | The list of add-on features to enable in the cluster. | [optional] 
**availableClusterVersions** | [**[ClusterVersionDetails]**](ClusterVersionDetails.md) | The Service Fabric runtime versions available for this cluster. | [optional] [readonly] 
**azureActiveDirectory** | [**AzureActiveDirectory**](AzureActiveDirectory.md) |  | [optional] 
**certificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**certificateCommonNames** | [**ServerCertificateCommonNames**](ServerCertificateCommonNames.md) |  | [optional] 
**clientCertificateCommonNames** | [**[ClientCertificateCommonName]**](ClientCertificateCommonName.md) | The list of client certificates referenced by common name that are allowed to manage the cluster. | [optional] 
**clientCertificateThumbprints** | [**[ClientCertificateThumbprint]**](ClientCertificateThumbprint.md) | The list of client certificates referenced by thumbprint that are allowed to manage the cluster. | [optional] 
**clusterCodeVersion** | **String** | The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to &#39;Manual&#39;. To get list of available Service Fabric versions for new clusters use [ClusterVersion API](./ClusterVersion.md). To get the list of available version for existing clusters use **availableClusterVersions**. | [optional] 
**clusterEndpoint** | **String** | The Azure Resource Provider endpoint. A system service in the cluster connects to this  endpoint. | [optional] [readonly] 
**clusterId** | **String** | A service generated unique identifier for the cluster resource. | [optional] [readonly] 
**clusterState** | [**ClusterState**](ClusterState.md) |  | [optional] 
**diagnosticsStorageAccountConfig** | [**DiagnosticsStorageAccountConfig**](DiagnosticsStorageAccountConfig.md) |  | [optional] 
**fabricSettings** | [**[SettingsSectionDescription]**](SettingsSectionDescription.md) | The list of custom fabric settings to configure the cluster. | [optional] 
**managementEndpoint** | **String** | The http management endpoint of the cluster. | 
**nodeTypes** | [**[NodeTypeDescription]**](NodeTypeDescription.md) | The list of node types in the cluster. | 
**provisioningState** | **String** | The provisioning state of the cluster resource. | [optional] [readonly] 
**reliabilityLevel** | [**ReliabilityLevel**](ReliabilityLevel.md) |  | [optional] 
**reverseProxyCertificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**reverseProxyCertificateCommonNames** | [**ServerCertificateCommonNames**](ServerCertificateCommonNames.md) |  | [optional] 
**upgradeDescription** | [**ClusterUpgradePolicy**](ClusterUpgradePolicy.md) |  | [optional] 
**upgradeMode** | [**UpgradeMode**](UpgradeMode.md) |  | [optional] 
**vmImage** | **String** | The VM image VMSS has been configured with. Generic names such as Windows or Linux can be used. | [optional] 



## Enum: ProvisioningStateEnum


* `Updating` (value: `"Updating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)





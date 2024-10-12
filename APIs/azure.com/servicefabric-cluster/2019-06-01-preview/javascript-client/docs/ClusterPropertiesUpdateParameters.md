# ServiceFabricManagementClient.ClusterPropertiesUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addOnFeatures** | [**[AddOnFeatures]**](AddOnFeatures.md) | The list of add-on features to enable in the cluster. | [optional] 
**certificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**certificateCommonNames** | [**ServerCertificateCommonNames**](ServerCertificateCommonNames.md) |  | [optional] 
**clientCertificateCommonNames** | [**[ClientCertificateCommonName]**](ClientCertificateCommonName.md) | The list of client certificates referenced by common name that are allowed to manage the cluster. This will overwrite the existing list. | [optional] 
**clientCertificateThumbprints** | [**[ClientCertificateThumbprint]**](ClientCertificateThumbprint.md) | The list of client certificates referenced by thumbprint that are allowed to manage the cluster. This will overwrite the existing list. | [optional] 
**clusterCodeVersion** | **String** | The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to &#39;Manual&#39;. To get list of available Service Fabric versions for new clusters use [ClusterVersion API](./ClusterVersion.md). To get the list of available version for existing clusters use **availableClusterVersions**. | [optional] 
**eventStoreServiceEnabled** | **Boolean** | Indicates if the event store service is enabled. | [optional] 
**fabricSettings** | [**[SettingsSectionDescription]**](SettingsSectionDescription.md) | The list of custom fabric settings to configure the cluster. This will overwrite the existing list. | [optional] 
**nodeTypes** | [**[NodeTypeDescription]**](NodeTypeDescription.md) | The list of node types in the cluster. This will overwrite the existing list. | [optional] 
**reliabilityLevel** | [**ReliabilityLevel**](ReliabilityLevel.md) |  | [optional] 
**reverseProxyCertificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**upgradeDescription** | [**ClusterUpgradePolicy**](ClusterUpgradePolicy.md) |  | [optional] 
**upgradeMode** | [**UpgradeMode**](UpgradeMode.md) |  | [optional] 



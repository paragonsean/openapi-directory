# ServiceFabricManagementClient.ClusterPropertiesUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addOnFeatures** | [**[AddOnFeatures]**](AddOnFeatures.md) | The list of add-on features to enable in the cluster. | [optional] 
**certificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**clientCertificateCommonNames** | [**[ClientCertificateCommonName]**](ClientCertificateCommonName.md) | The list of client certificates referenced by common name that are allowed to manage the cluster. This will overwrite the existing list. | [optional] 
**clientCertificateThumbprints** | [**[ClientCertificateThumbprint]**](ClientCertificateThumbprint.md) | The list of client certificates referenced by thumbprint that are allowed to manage the cluster. This will overwrite the existing list. | [optional] 
**clusterCodeVersion** | **String** | The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to &#39;Manual&#39;. To get list of available Service Fabric versions for new clusters use [ClusterVersion API](./ClusterVersion.md). To get the list of available version for existing clusters use **availableClusterVersions**. | [optional] 
**fabricSettings** | [**[SettingsSectionDescription]**](SettingsSectionDescription.md) | The list of custom fabric settings to configure the cluster. This will overwrite the existing list. | [optional] 
**nodeTypes** | [**[NodeTypeDescription]**](NodeTypeDescription.md) | The list of node types in the cluster. This will overwrite the existing list. | [optional] 
**reliabilityLevel** | **String** | The reliability level sets the replica set size of system services. Learn about [ReliabilityLevel](https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-capacity). | [optional] 
**reverseProxyCertificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**upgradeDescription** | [**ClusterUpgradePolicy**](ClusterUpgradePolicy.md) |  | [optional] 
**upgradeMode** | **String** | The upgrade mode of the cluster. This indicates if the cluster should be automatically upgraded when new Service Fabric runtime version is available. | [optional] 



## Enum: ReliabilityLevelEnum


* `Bronze` (value: `"Bronze"`)

* `Silver` (value: `"Silver"`)

* `Gold` (value: `"Gold"`)





## Enum: UpgradeModeEnum


* `Automatic` (value: `"Automatic"`)

* `Manual` (value: `"Manual"`)





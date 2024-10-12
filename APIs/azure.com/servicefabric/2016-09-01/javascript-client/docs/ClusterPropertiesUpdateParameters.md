# ServiceFabricManagementClient.ClusterPropertiesUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**clientCertificateCommonNames** | [**[ClientCertificateCommonName]**](ClientCertificateCommonName.md) | List of client certificates to whitelist based on common names. | [optional] 
**clientCertificateThumbprints** | [**[ClientCertificateThumbprint]**](ClientCertificateThumbprint.md) | The client thumbprint details, it is used for client access for cluster operation, it will override existing collection | [optional] 
**clusterCodeVersion** | **String** | The ServiceFabric code version, if set it, please make sure you have set upgradeMode to Manual, otherwise ,it will fail, if you are using PUT new cluster, you can get the version by using ClusterVersions_List, if you are updating existing cluster, you can get the availableClusterVersions from Clusters_Get | [optional] 
**fabricSettings** | [**[SettingsSectionDescription]**](SettingsSectionDescription.md) | List of custom fabric settings to configure the cluster, Note, it will overwrite existing collection | [optional] 
**nodeTypes** | [**[NodeTypeDescription]**](NodeTypeDescription.md) | The list of node types that make up the cluster, it will override | [optional] 
**reliabilityLevel** | **String** | This level is used to set the number of replicas of the system services | [optional] 
**reverseProxyCertificate** | [**CertificateDescription**](CertificateDescription.md) |  | [optional] 
**upgradeDescription** | [**ClusterUpgradePolicy**](ClusterUpgradePolicy.md) |  | [optional] 
**upgradeMode** | **String** | Cluster upgrade mode indicates if fabric upgrade is initiated automatically by the system or not | [optional] 



## Enum: ReliabilityLevelEnum


* `Bronze` (value: `"Bronze"`)

* `Silver` (value: `"Silver"`)

* `Gold` (value: `"Gold"`)





## Enum: UpgradeModeEnum


* `Automatic` (value: `"Automatic"`)

* `Manual` (value: `"Manual"`)





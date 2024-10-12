

# ClusterPropertiesUpdateParameters

Describes the cluster resource properties that can be updated during PATCH operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addOnFeatures** | **List&lt;AddOnFeatures&gt;** | The list of add-on features to enable in the cluster. |  [optional] |
|**certificate** | [**CertificateDescription**](CertificateDescription.md) |  |  [optional] |
|**clientCertificateCommonNames** | [**List&lt;ClientCertificateCommonName&gt;**](ClientCertificateCommonName.md) | The list of client certificates referenced by common name that are allowed to manage the cluster. This will overwrite the existing list. |  [optional] |
|**clientCertificateThumbprints** | [**List&lt;ClientCertificateThumbprint&gt;**](ClientCertificateThumbprint.md) | The list of client certificates referenced by thumbprint that are allowed to manage the cluster. This will overwrite the existing list. |  [optional] |
|**clusterCodeVersion** | **String** | The Service Fabric runtime version of the cluster. This property can only by set the user when **upgradeMode** is set to &#39;Manual&#39;. To get list of available Service Fabric versions for new clusters use [ClusterVersion API](./ClusterVersion.md). To get the list of available version for existing clusters use **availableClusterVersions**. |  [optional] |
|**fabricSettings** | [**List&lt;SettingsSectionDescription&gt;**](SettingsSectionDescription.md) | The list of custom fabric settings to configure the cluster. This will overwrite the existing list. |  [optional] |
|**nodeTypes** | [**List&lt;NodeTypeDescription&gt;**](NodeTypeDescription.md) | The list of node types in the cluster. This will overwrite the existing list. |  [optional] |
|**reliabilityLevel** | [**ReliabilityLevelEnum**](#ReliabilityLevelEnum) | The reliability level sets the replica set size of system services. Learn about [ReliabilityLevel](https://docs.microsoft.com/azure/service-fabric/service-fabric-cluster-capacity). |  [optional] |
|**reverseProxyCertificate** | [**CertificateDescription**](CertificateDescription.md) |  |  [optional] |
|**upgradeDescription** | [**ClusterUpgradePolicy**](ClusterUpgradePolicy.md) |  |  [optional] |
|**upgradeMode** | [**UpgradeModeEnum**](#UpgradeModeEnum) | The upgrade mode of the cluster. This indicates if the cluster should be automatically upgraded when new Service Fabric runtime version is available. |  [optional] |



## Enum: ReliabilityLevelEnum

| Name | Value |
|---- | -----|
| BRONZE | &quot;Bronze&quot; |
| SILVER | &quot;Silver&quot; |
| GOLD | &quot;Gold&quot; |



## Enum: UpgradeModeEnum

| Name | Value |
|---- | -----|
| AUTOMATIC | &quot;Automatic&quot; |
| MANUAL | &quot;Manual&quot; |




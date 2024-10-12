# BatchService.CertificateReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storeLocation** | **String** | The default value is currentUser. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. | [optional] 
**storeName** | **String** | The default value is My. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). | [optional] 
**thumbprint** | **String** |  | 
**thumbprintAlgorithm** | **String** |  | 
**visibility** | **[String]** | The default is all accounts. | [optional] 



## Enum: StoreLocationEnum


* `currentUser` (value: `"currentUser"`)

* `localMachine` (value: `"localMachine"`)

* `unmapped` (value: `"unmapped"`)





## Enum: [VisibilityEnum]


* `startTask` (value: `"startTask"`)

* `task` (value: `"task"`)

* `remoteUser` (value: `"remoteUser"`)

* `unmapped` (value: `"unmapped"`)





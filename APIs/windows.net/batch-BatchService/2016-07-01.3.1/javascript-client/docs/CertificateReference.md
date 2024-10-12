# BatchService.CertificateReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storeLocation** | **String** | The default value is CurrentUser. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of remoteuser, a certs directory is created in the user&#39;s home directory (e.g., /home/&lt;user-name&gt;/certs) where certificates are placed. | [optional] 
**storeName** | **String** | The default value is My. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). | [optional] 
**thumbprint** | **String** |  | 
**thumbprintAlgorithm** | **String** |  | 
**visibility** | **[String]** | The default is all accounts. | [optional] 



## Enum: StoreLocationEnum


* `currentuser` (value: `"currentuser"`)

* `localmachine` (value: `"localmachine"`)

* `unmapped` (value: `"unmapped"`)





## Enum: [VisibilityEnum]


* `starttask` (value: `"starttask"`)

* `task` (value: `"task"`)

* `remoteuser` (value: `"remoteuser"`)

* `unmapped` (value: `"unmapped"`)





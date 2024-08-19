# BatchManagement.CertificateReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | 
**storeLocation** | **String** | The default value is currentUser. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. | [optional] 
**storeName** | **String** | This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). Common store names include: My, Root, CA, Trust, Disallowed, TrustedPeople, TrustedPublisher, AuthRoot, AddressBook, but any custom store name can also be used. The default value is My. | [optional] 
**visibility** | **[String]** |  | [optional] 



## Enum: StoreLocationEnum


* `CurrentUser` (value: `"CurrentUser"`)

* `LocalMachine` (value: `"LocalMachine"`)





## Enum: [VisibilityEnum]


* `StartTask` (value: `"StartTask"`)

* `Task` (value: `"Task"`)

* `RemoteUser` (value: `"RemoteUser"`)







# CertificateReference


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storeLocation** | [**StoreLocationEnum**](#StoreLocationEnum) | The default value is currentUser. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). For Linux compute nodes, the certificates are stored in a directory inside the task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the task to query for this location. For certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and certificates are placed in that directory. |  [optional] |
|**storeName** | **String** | The default value is My. This property is applicable only for pools configured with Windows nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows image reference). |  [optional] |
|**thumbprint** | **String** |  |  |
|**thumbprintAlgorithm** | **String** |  |  |
|**visibility** | [**List&lt;VisibilityEnum&gt;**](#List&lt;VisibilityEnum&gt;) | The default is all accounts. |  [optional] |



## Enum: StoreLocationEnum

| Name | Value |
|---- | -----|
| CURRENT_USER | &quot;currentUser&quot; |
| LOCAL_MACHINE | &quot;localMachine&quot; |
| UNMAPPED | &quot;unmapped&quot; |



## Enum: List&lt;VisibilityEnum&gt;

| Name | Value |
|---- | -----|
| START_TASK | &quot;startTask&quot; |
| TASK | &quot;task&quot; |
| REMOTE_USER | &quot;remoteUser&quot; |
| UNMAPPED | &quot;unmapped&quot; |




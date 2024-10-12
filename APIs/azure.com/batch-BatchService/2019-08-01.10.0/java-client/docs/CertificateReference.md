

# CertificateReference


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**storeLocation** | [**StoreLocationEnum**](#StoreLocationEnum) | The default value is currentuser. This property is applicable only for Pools configured with Windows Compute Nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows Image reference). For Linux Compute Nodes, the Certificates are stored in a directory inside the Task working directory and an environment variable AZ_BATCH_CERTIFICATES_DIR is supplied to the Task to query for this location. For Certificates with visibility of &#39;remoteUser&#39;, a &#39;certs&#39; directory is created in the user&#39;s home directory (e.g., /home/{user-name}/certs) and Certificates are placed in that directory. |  [optional] |
|**storeName** | **String** | This property is applicable only for Pools configured with Windows Compute Nodes (that is, created with cloudServiceConfiguration, or with virtualMachineConfiguration using a Windows Image reference). Common store names include: My, Root, CA, Trust, Disallowed, TrustedPeople, TrustedPublisher, AuthRoot, AddressBook, but any custom store name can also be used. The default value is My. |  [optional] |
|**thumbprint** | **String** |  |  |
|**thumbprintAlgorithm** | **String** |  |  |
|**visibility** | [**List&lt;VisibilityEnum&gt;**](#List&lt;VisibilityEnum&gt;) | You can specify more than one visibility in this collection. The default is all Accounts. |  [optional] |



## Enum: StoreLocationEnum

| Name | Value |
|---- | -----|
| CURRENTUSER | &quot;currentuser&quot; |
| LOCALMACHINE | &quot;localmachine&quot; |



## Enum: List&lt;VisibilityEnum&gt;

| Name | Value |
|---- | -----|
| STARTTASK | &quot;starttask&quot; |
| TASK | &quot;task&quot; |
| REMOTEUSER | &quot;remoteuser&quot; |




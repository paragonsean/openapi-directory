# BatchService.CertificateReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storeLocation** | **String** | The location of the certificate store on the compute node into which to install the certificate. The default value is CurrentUser. | [optional] 
**storeName** | **String** | The name of the certificate store on the compute node into which to install the certificate. The default value is My. | [optional] 
**thumbprint** | **String** | The thumbprint of the certificate. | 
**thumbprintAlgorithm** | **String** | The algorithm with which the thumbprint is associated. This must be sha1. | 
**visibility** | **[String]** | Which user accounts on the compute node should have access to the private data of the certificate. This may be any subset of the values &#39;starttask&#39;, &#39;task&#39; and &#39;remoteuser&#39;, separated by commas. The default is all accounts, corresponding to the string &#39;starttask,task,remoteuser&#39;. | [optional] 



## Enum: StoreLocationEnum


* `currentuser` (value: `"currentuser"`)

* `localmachine` (value: `"localmachine"`)

* `unmapped` (value: `"unmapped"`)





## Enum: [VisibilityEnum]


* `starttask` (value: `"starttask"`)

* `task` (value: `"task"`)

* `remoteuser` (value: `"remoteuser"`)

* `unmapped` (value: `"unmapped"`)





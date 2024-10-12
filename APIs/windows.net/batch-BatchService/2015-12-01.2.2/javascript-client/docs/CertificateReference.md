# BatchService.CertificateReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storeLocation** | **String** | Gets or sets the location of the certificate store on the compute node into which to install the certificate. The default value is CurrentUser. | [optional] 
**storeName** | **String** | Gets or sets the name of the certificate store on the compute node into which to install the certificate. The default value is My. | [optional] 
**thumbprint** | **String** | Gets or sets the thumbprint of the certificate. | 
**thumbprintAlgorithm** | **String** | Gets or sets the algorithm with which the thumbprint is associated.  This must be sha1. | 
**visibility** | **String** | Gets or sets which user accounts on the compute node should have access to the private data of the certificate. This may be any subset of the values &#39;starttask&#39;, &#39;task&#39; and &#39;rdp&#39;, separated by commas. The default is all accounts, corresponding to the string &#39;starttask,task,rdp&#39;. | [optional] 



## Enum: StoreLocationEnum


* `currentuser` (value: `"currentuser"`)

* `localmachine` (value: `"localmachine"`)

* `unmapped` (value: `"unmapped"`)





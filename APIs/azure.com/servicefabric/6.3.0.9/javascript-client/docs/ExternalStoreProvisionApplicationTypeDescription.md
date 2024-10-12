# ServiceFabricClientApis.ExternalStoreProvisionApplicationTypeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationPackageDownloadUri** | **String** | The path to the &#39;.sfpkg&#39; application package from where the application package can be downloaded using HTTP or HTTPS protocols. The application package can be stored in an external store that provides GET operation to download the file. Supported protocols are HTTP and HTTPS, and the path must allow READ access. | [optional] 
**applicationTypeName** | **String** | The application type name represents the name of the application type found in the application manifest. | [optional] 
**applicationTypeVersion** | **String** | The application type version represents the version of the application type found in the application manifest. | [optional] 



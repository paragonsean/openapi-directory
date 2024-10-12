

# ExternalStoreProvisionApplicationTypeDescription

Describes the operation to register or provision an application type using an application package from an external store instead of a package uploaded to the Service Fabric image store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationPackageDownloadUri** | **String** | The path to the &#39;.sfpkg&#39; application package from where the application package can be downloaded using HTTP or HTTPS protocols. The application package can be stored in an external store that provides GET operation to download the file. Supported protocols are HTTP and HTTPS, and the path must allow READ access. |  |
|**applicationTypeName** | **String** | The application type name represents the name of the application type found in the application manifest. |  |
|**applicationTypeVersion** | **String** | The application type version represents the version of the application type found in the application manifest. |  |




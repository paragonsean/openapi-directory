# StorageImportExport.UpdateJobParametersProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupDriveManifest** | **Boolean** | Indicates whether the manifest files on the drives should be copied to block blobs. | [optional] 
**cancelRequested** | **Boolean** | If specified, the value must be true. The service will attempt to cancel the job.  | [optional] 
**deliveryPackage** | [**PackageInfomation**](PackageInfomation.md) |  | [optional] 
**driveList** | [**[DriveStatus]**](DriveStatus.md) | List of drives that comprise the job. | [optional] 
**logLevel** | **String** | Indicates whether error logging or verbose logging is enabled. | [optional] 
**returnAddress** | [**ReturnAddress**](ReturnAddress.md) |  | [optional] 
**returnShipping** | [**ReturnShipping**](ReturnShipping.md) |  | [optional] 
**state** | **String** | If specified, the value must be Shipping, which tells the Import/Export service that the package for the job has been shipped. The ReturnAddress and DeliveryPackage properties must have been set either in this request or in a previous request, otherwise the request will fail.  | [optional] 



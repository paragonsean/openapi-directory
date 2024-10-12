

# JobDetails

Specifies the job properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupDriveManifest** | **Boolean** | Default value is false. Indicates whether the manifest files on the drives should be copied to block blobs. |  [optional] |
|**cancelRequested** | **Boolean** | Indicates whether a request has been submitted to cancel the job. |  [optional] |
|**deliveryPackage** | [**PackageInfomation**](PackageInfomation.md) |  |  [optional] |
|**diagnosticsPath** | **String** | The virtual blob directory to which the copy logs and backups of drive manifest files (if enabled) will be stored. |  [optional] |
|**driveList** | [**List&lt;DriveStatus&gt;**](DriveStatus.md) | List of up to ten drives that comprise the job. The drive list is a required element for an import job; it is not specified for export jobs. |  [optional] |
|**export** | [**Export**](Export.md) |  |  [optional] |
|**incompleteBlobListUri** | **String** | A blob path that points to a block blob containing a list of blob names that were not exported due to insufficient drive space. If all blobs were exported successfully, then this element is not included in the response. |  [optional] |
|**jobType** | **String** | The type of job |  [optional] |
|**logLevel** | **String** | Default value is Error. Indicates whether error logging or verbose logging will be enabled. |  [optional] |
|**percentComplete** | **Integer** | Overall percentage completed for the job. |  [optional] |
|**provisioningState** | **String** | Specifies the provisioning state of the job. |  [optional] |
|**returnAddress** | [**ReturnAddress**](ReturnAddress.md) |  |  [optional] |
|**returnPackage** | [**PackageInfomation**](PackageInfomation.md) |  |  [optional] |
|**returnShipping** | [**ReturnShipping**](ReturnShipping.md) |  |  [optional] |
|**shippingInformation** | [**ShippingInformation**](ShippingInformation.md) |  |  [optional] |
|**state** | **String** | Current state of the job. |  [optional] |
|**storageAccountId** | **String** | The resource identifier of the storage account where data will be imported to or exported from. |  [optional] |




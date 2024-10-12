# DataBoxManagementClient.JobDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chainOfCustodySasKey** | **String** | Shared access key to download the chain of custody logs | [optional] [readonly] 
**contactDetails** | [**ContactDetails**](ContactDetails.md) |  | 
**copyLogDetails** | [**[CopyLogDetails]**](CopyLogDetails.md) | List of copy log details. | [optional] [readonly] 
**deliveryPackage** | [**PackageShippingDetails**](PackageShippingDetails.md) |  | [optional] 
**destinationAccountDetails** | [**[DestinationAccountDetails]**](DestinationAccountDetails.md) | Destination account details. | 
**errorDetails** | [**[JobErrorDetails]**](JobErrorDetails.md) | Error details for failure. This is optional. | [optional] [readonly] 
**expectedDataSizeInTerabytes** | **Number** | The expected size of the data, which needs to be transferred in this job, in terabytes. | [optional] 
**jobDetailsType** | **String** | Indicates the type of job details. | 
**jobStages** | [**[JobStages]**](JobStages.md) | List of stages that run in the job. | [optional] [readonly] 
**preferences** | [**Preferences**](Preferences.md) |  | [optional] 
**returnPackage** | [**PackageShippingDetails**](PackageShippingDetails.md) |  | [optional] 
**reverseShipmentLabelSasKey** | **String** | Shared access key to download the return shipment label | [optional] [readonly] 
**shippingAddress** | [**ShippingAddress**](ShippingAddress.md) |  | 



## Enum: JobDetailsTypeEnum


* `DataBox` (value: `"DataBox"`)

* `DataBoxDisk` (value: `"DataBoxDisk"`)

* `DataBoxHeavy` (value: `"DataBoxHeavy"`)





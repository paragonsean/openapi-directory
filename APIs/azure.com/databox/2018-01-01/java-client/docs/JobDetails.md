

# JobDetails

Job details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**chainOfCustodySasKey** | **String** | Shared access key to download the chain of custody logs |  [optional] [readonly] |
|**contactDetails** | [**ContactDetails**](ContactDetails.md) |  |  |
|**copyLogDetails** | [**List&lt;CopyLogDetails&gt;**](CopyLogDetails.md) | List of copy log details. |  [optional] [readonly] |
|**deliveryPackage** | [**PackageShippingDetails**](PackageShippingDetails.md) |  |  [optional] |
|**destinationAccountDetails** | [**List&lt;DestinationAccountDetails&gt;**](DestinationAccountDetails.md) | Destination account details. |  |
|**errorDetails** | [**List&lt;JobErrorDetails&gt;**](JobErrorDetails.md) | Error details for failure. This is optional. |  [optional] [readonly] |
|**expectedDataSizeInTeraBytes** | **Integer** | The expected size of the data, which needs to be transferred in this job, in terabytes. |  [optional] |
|**jobDetailsType** | [**JobDetailsTypeEnum**](#JobDetailsTypeEnum) | Indicates the type of job details. |  |
|**jobStages** | [**List&lt;JobStages&gt;**](JobStages.md) | List of stages that run in the job. |  [optional] [readonly] |
|**preferences** | [**Preferences**](Preferences.md) |  |  [optional] |
|**returnPackage** | [**PackageShippingDetails**](PackageShippingDetails.md) |  |  [optional] |
|**reverseShipmentLabelSasKey** | **String** | Shared access key to download the return shipment label |  [optional] [readonly] |
|**shippingAddress** | [**ShippingAddress**](ShippingAddress.md) |  |  |



## Enum: JobDetailsTypeEnum

| Name | Value |
|---- | -----|
| DATA_BOX | &quot;DataBox&quot; |
| DATA_BOX_DISK | &quot;DataBoxDisk&quot; |
| DATA_BOX_HEAVY | &quot;DataBoxHeavy&quot; |




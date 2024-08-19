

# CheckTransferDeposit

After a check transfer is deposited, this will contain supplemental details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backImageFileId** | **String** | The ID for the File containing the image of the rear of the check. |  |
|**depositedAt** | **OffsetDateTime** | When the check was deposited. |  |
|**frontImageFileId** | **String** | The ID for the File containing the image of the front of the check. |  |
|**type** | [**TypeEnum**](#TypeEnum) | A constant representing the object&#39;s type. For this resource it will always be &#x60;check_transfer_deposit&#x60;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CHECK_TRANSFER_DEPOSIT | &quot;check_transfer_deposit&quot; |




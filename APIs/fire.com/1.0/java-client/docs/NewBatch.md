

# NewBatch


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batchName** | **String** | An optional name you give to the batch at creation time. |  [optional] |
|**callbackUrl** | **String** | An optional POST URL that all events for this batch will be sent to. |  [optional] |
|**currency** | **String** | 3 digit ISO code for the currency you wish to send - GBP, EUR, USD, CAD, etc... |  [optional] |
|**jobNumber** | **String** | An optional job number you can give to the batch to help link it to your own system. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the batch - can be one of the listed 3 |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_TRANSFER | &quot;BANK_TRANSFER&quot; |
| INTERNAL_TRANSFER | &quot;INTERNAL_TRANSFER&quot; |
| INTERNATIONAL_TRANSFER | &quot;INTERNATIONAL_TRANSFER&quot; |




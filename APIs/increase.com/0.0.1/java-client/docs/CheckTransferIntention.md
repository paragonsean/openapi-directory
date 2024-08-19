

# CheckTransferIntention

A Check Transfer Intention object. This field will be present in the JSON response if and only if `category` is equal to `check_transfer_intention`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressCity** | **String** | The city of the check&#39;s destination. |  |
|**addressLine1** | **String** | The street address of the check&#39;s destination. |  |
|**addressLine2** | **String** | The second line of the address of the check&#39;s destination. |  |
|**addressState** | **String** | The state of the check&#39;s destination. |  |
|**addressZip** | **String** | The postal code of the check&#39;s destination. |  |
|**amount** | **Integer** | The transfer amount in USD cents. |  |
|**currency** | [**CurrencyEnum**](#CurrencyEnum) | The [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code for the check&#39;s currency. |  |
|**recipientName** | **String** | The name that will be printed on the check. |  |
|**transferId** | **String** | The identifier of the Check Transfer with which this is associated. |  |



## Enum: CurrencyEnum

| Name | Value |
|---- | -----|
| CAD | &quot;CAD&quot; |
| CHF | &quot;CHF&quot; |
| EUR | &quot;EUR&quot; |
| GBP | &quot;GBP&quot; |
| JPY | &quot;JPY&quot; |
| USD | &quot;USD&quot; |




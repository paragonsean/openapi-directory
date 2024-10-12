

# OpenInvoiceDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | **String** | The address where to send the invoice. |  [optional] |
|**deliveryAddress** | **String** | The address where the goods should be delivered. |  [optional] |
|**personalDetails** | **String** | Shopper name, date of birth, phone number, and email address. |  [optional] |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **openinvoice** |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OPENINVOICE | &quot;openinvoice&quot; |
| AFTERPAY_DIRECTDEBIT | &quot;afterpay_directdebit&quot; |
| ATOME_POS | &quot;atome_pos&quot; |




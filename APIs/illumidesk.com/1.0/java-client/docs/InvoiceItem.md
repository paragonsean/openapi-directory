

# InvoiceItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | Amount the the invoice item will be billed for. |  |
|**created** | **String** | Date and time when invoice was created. |  |
|**currency** | **String** | Currency used in invoice. |  |
|**description** | **String** | Item description. |  [optional] |
|**id** | **String** | InvoiceItem unique identifier expressed as UUID. |  [optional] |
|**invoice** | **String** | Invoice unique identifier expressed as UUID. |  |
|**invoiceDate** | **String** | Date the item was added to the invoice. |  |
|**livemode** | **Boolean** | Boolean that determines whether invoice is live, or not. |  [optional] |
|**metadata** | **Object** | Optional metadata object of invoice. |  [optional] |
|**proration** | **Boolean** | Whether or not the items cost will be prorated for the billing period. |  [optional] |
|**quantity** | **Integer** | Number of units for this item. |  |
|**stripeId** | **String** | Stripe account identifier. |  |




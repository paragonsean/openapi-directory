

# InvoiceCustomField

An additional seller-defined and customer-facing field to include on the invoice. For more information,  see [Custom fields](https://developer.squareup.com/docs/invoices-api/overview#custom-fields).  Adding custom fields to an invoice requires an  [Invoices Plus subscription](https://developer.squareup.com/docs/invoices-api/overview#invoices-plus-subscription).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**label** | **String** | The label or title of the custom field. This field is required for a custom field. |  [optional] |
|**placement** | **String** | The location of the custom field on the invoice. This field is required for a custom field. |  [optional] |
|**value** | **String** | The text of the custom field. If omitted, only the label is rendered. |  [optional] |




# SquareConnectApi.UpdateInvoiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldsToClear** | **[String]** | The list of fields to clear. For examples, see [Update an invoice](https://developer.squareup.com/docs/invoices-api/overview#update-an-invoice). | [optional] 
**idempotencyKey** | **String** | A unique string that identifies the &#x60;UpdateInvoice&#x60; request. If you do not provide &#x60;idempotency_key&#x60; (or provide an empty string as the value), the endpoint treats each request as independent.  For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency). | [optional] 
**invoice** | [**Invoice**](Invoice.md) |  | 



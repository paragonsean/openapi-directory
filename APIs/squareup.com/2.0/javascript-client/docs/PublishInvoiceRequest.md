# SquareConnectApi.PublishInvoiceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idempotencyKey** | **String** | A unique string that identifies the &#x60;PublishInvoice&#x60; request. If you do not  provide &#x60;idempotency_key&#x60; (or provide an empty string as the value), the endpoint  treats each request as independent.  For more information, see [Idempotency](https://developer.squareup.com/docs/working-with-apis/idempotency). | [optional] 
**version** | **Number** | The version of the [invoice](https://developer.squareup.com/reference/square_2021-08-18/objects/Invoice) to publish. This must match the current version of the invoice; otherwise, the request is rejected. | 



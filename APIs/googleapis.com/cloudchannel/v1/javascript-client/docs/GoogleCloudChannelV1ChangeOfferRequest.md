# CloudChannelApi.GoogleCloudChannelV1ChangeOfferRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAccount** | **String** | Optional. The billing account resource name that is used to pay for this entitlement when setting up billing on a trial subscription. This field is only relevant for multi-currency accounts. It should be left empty for single currency accounts. | [optional] 
**offer** | **String** | Required. New Offer. Format: accounts/{account_id}/offers/{offer_id}. | [optional] 
**parameters** | [**[GoogleCloudChannelV1Parameter]**](GoogleCloudChannelV1Parameter.md) | Optional. Parameters needed to purchase the Offer. To view the available Parameters refer to the Offer.parameter_definitions from the desired offer. | [optional] 
**purchaseOrderId** | **String** | Optional. Purchase order id provided by the reseller. | [optional] 
**requestId** | **String** | Optional. You can specify an optional unique request ID, and if you need to retry your request, the server will know to ignore the request if it&#39;s complete. For example, you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if it received the original operation with the same request ID. If it did, it will ignore the second request. The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (&#x60;00000000-0000-0000-0000-000000000000&#x60;). | [optional] 



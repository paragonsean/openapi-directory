# AdExchangeBuyerApi.Budget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The id of the account. This is required for get and update requests. | [optional] 
**billingId** | **String** | The billing id to determine which adgroup to provide budget information for. This is required for get and update requests. | [optional] 
**budgetAmount** | **String** | The daily budget amount in unit amount of the account currency to apply for the billingId provided. This is required for update requests. | [optional] 
**currencyCode** | **String** | The currency code for the buyer. This cannot be altered here. | [optional] 
**id** | **String** | The unique id that describes this item. | [optional] 
**kind** | **String** | The kind of the resource, i.e. \&quot;adexchangebuyer#budget\&quot;. | [optional] [default to &#39;adexchangebuyer#budget&#39;]



# ThePlaidApi.InstitutionsSearchRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includeAuthMetadata** | **Boolean** | When &#x60;true&#x60;, returns metadata related to the Auth product indicating which auth methods are supported. | [optional] [default to false]
**includeOptionalMetadata** | **Boolean** | When true, return the institution&#39;s homepage URL, logo and primary brand color. | [optional] 
**includePaymentInitiationMetadata** | **Boolean** | When &#x60;true&#x60;, returns metadata related to the Payment Initiation product indicating which payment configurations are supported. | [optional] [default to false]
**oauth** | **Boolean** | Limit results to institutions with or without mandatory OAuth login flows. Note that institutions will only have &#x60;oauth&#x60; set to &#x60;true&#x60; if *all* Items associated with that institution are required to use OAuth flows; institutions in a state of migration to OAuth may have the &#x60;oauth&#x60; attribute set to &#x60;false&#x60; even if they support OAuth. | [optional] 
**paymentInitiation** | [**InstitutionsSearchPaymentInitiationOptions**](InstitutionsSearchPaymentInitiationOptions.md) |  | [optional] 



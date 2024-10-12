# AdyenRecurringApi.RecurringDetailsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchantAccount** | **String** | The merchant account identifier you want to process the (transaction) request with. | 
**recurring** | [**Recurring**](Recurring.md) | A container for the type of a recurring contract to be retrieved.  The contract value needs to match the contract value submitted in the payment transaction used to create a recurring contract. However, if &#x60;ONECLICK,RECURRING&#x60; is the original contract definition in the initial payment, then &#x60;contract&#x60; should take either &#x60;ONECLICK&#x60; or &#x60;RECURRING&#x60;, depending on whether or not you want the shopper to enter their card&#39;s security code when they finalize their purchase. | [optional] 
**shopperReference** | **String** | The reference you use to uniquely identify the shopper (e.g. user ID or account ID). | 



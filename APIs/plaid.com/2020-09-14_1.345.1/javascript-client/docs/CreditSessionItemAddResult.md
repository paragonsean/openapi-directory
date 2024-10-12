# ThePlaidApi.CreditSessionItemAddResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**institutionId** | **String** | The Plaid Institution ID associated with the Item. | [optional] 
**itemId** | **String** | The Plaid Item ID. The &#x60;item_id&#x60; is always unique; linking the same account at the same institution twice will result in two Items with different &#x60;item_id&#x60; values. Like all Plaid identifiers, the &#x60;item_id&#x60; is case-sensitive. | [optional] 
**publicToken** | **String** | Returned once a user has successfully linked their Item. | [optional] 



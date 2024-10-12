# AdyenPaymentApi.FundSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | **{String: String}** | A map of name-value pairs for passing additional or industry-specific data. | [optional] 
**billingAddress** | [**Address**](Address.md) | The address where to send the invoice. | [optional] 
**card** | [**Card**](Card.md) | Credit card data.  Optional if &#x60;shopperReference&#x60; and &#x60;selectedRecurringDetailReference&#x60; are provided. | [optional] 
**shopperEmail** | **String** | Email address of the person. | [optional] 
**shopperName** | [**Name**](Name.md) | Name of the person. | [optional] 
**telephoneNumber** | **String** | Phone number of the person | [optional] 



# AdyenRecurringApi.ScheduleAccountUpdaterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | **{String: String}** | This field contains additional data, which may be required for a particular request. | [optional] 
**card** | [**Card**](Card.md) | Credit card data.  Optional if &#x60;shopperReference&#x60; and &#x60;selectedRecurringDetailReference&#x60; are provided. | [optional] 
**merchantAccount** | **String** | Account of the merchant. | 
**reference** | **String** | A reference that merchants can apply for the call. | 
**selectedRecurringDetailReference** | **String** | The selected detail recurring reference.  Optional if &#x60;card&#x60; is provided. | [optional] 
**shopperReference** | **String** | The reference of the shopper that owns the recurring contract.  Optional if &#x60;card&#x60; is provided. | [optional] 



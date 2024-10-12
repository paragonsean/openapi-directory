# AdyenPayoutApi.SubmitRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalData** | **{String: String}** | This field contains additional data, which may be required for a particular request. | [optional] 
**amount** | [**Amount**](Amount.md) | A container object for the payable amount information of the transaction. | 
**dateOfBirth** | **Date** | The date of birth. Format: ISO-8601; example: YYYY-MM-DD  For Paysafecard it must be the same as used when registering the Paysafecard account.  &gt; This field is mandatory for natural persons.  &gt; This field is required to update the existing &#x60;dateOfBirth&#x60; that is associated with this recurring contract. | [optional] 
**entityType** | **String** | The type of the entity the payout is processed for.  Allowed values: * NaturalPerson * Company &gt; This field is required to update the existing &#x60;entityType&#x60; that is associated with this recurring contract. | [optional] 
**fraudOffset** | **Number** | An integer value that is added to the normal fraud score. The value can be either positive or negative. | [optional] 
**merchantAccount** | **String** | The merchant account identifier you want to process the transaction request with. | 
**nationality** | **String** | The shopper&#39;s nationality.  A valid value is an ISO 2-character country code (e.g. &#39;NL&#39;).  &gt; This field is required to update the existing nationality that is associated with this recurring contract. | [optional] 
**recurring** | [**Recurring**](Recurring.md) | A container for the type of recurring contract to be retrieved.  The &#x60;recurring.contract&#x60; must be set to \&quot;PAYOUT\&quot;. | 
**reference** | **String** | The merchant reference for this payout. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement. | 
**selectedRecurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; you want to use for this payout.  You can use the value LATEST to select the most recently used recurring detail. | 
**shopperEmail** | **String** | The shopper&#39;s email address. | 
**shopperName** | [**Name**](Name.md) | The shopper&#39;s name.  In case the &#x60;entityType&#x60; is &#x60;Company&#x60;, the &#x60;shopperName.lastName&#x60; must contain the company name.  &gt; This field is required to update the existing &#x60;shopperName&#x60; associated with a recurring contract. | [optional] 
**shopperReference** | **String** | The shopper&#39;s reference for the payout transaction. | 
**shopperStatement** | **String** | The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method). | [optional] 
**socialSecurityNumber** | **String** | The shopper&#39;s social security number. | [optional] 



## Enum: EntityTypeEnum


* `NaturalPerson` (value: `"NaturalPerson"`)

* `Company` (value: `"Company"`)





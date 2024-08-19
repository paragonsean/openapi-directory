

# StoreDetailAndSubmitRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **Map&lt;String, String&gt;** | This field contains additional data, which may be required for a particular request. |  [optional] |
|**amount** | [**Amount**](Amount.md) | A container object for the payable amount information of the transaction. |  |
|**bank** | [**BankAccount**](BankAccount.md) | A container for bank account data. &gt; This field is mandatory if &#x60;card&#x60; is not provided. |  [optional] |
|**billingAddress** | [**Address**](Address.md) | The billing address.  &gt; The &#x60;billingAddress&#x60; object is required for cross-border payouts to and from Canada. Include all of the fields within this object. |  [optional] |
|**card** | [**Card**](Card.md) | A container for card data. &gt; This field is mandatory if &#x60;bank&#x60; is not provided. |  [optional] |
|**dateOfBirth** | **LocalDate** | The date of birth. Format: [ISO-8601](https://www.w3.org/TR/NOTE-datetime); example: YYYY-MM-DD For Paysafecard it must be the same as used when registering the Paysafecard account. &gt; This field is mandatory for natural persons. |  |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | The type of the entity the payout is processed for. |  |
|**fraudOffset** | **Integer** | An integer value that is added to the normal fraud score. The value can be either positive or negative. |  [optional] |
|**merchantAccount** | **String** | The merchant account identifier, with which you want to process the transaction. |  |
|**nationality** | **String** | The shopper&#39;s nationality.  A valid value is an ISO 2-character country code (e.g. &#39;NL&#39;). |  |
|**recurring** | [**Recurring**](Recurring.md) | A container for the type of recurring contract to be retrieved.  The recurring.contract must be set to &#x60;PAYOUT&#x60; |  |
|**reference** | **String** | The merchant reference for this payment. This reference will be used in all communication to the merchant about the status of the payout. Although it is a good idea to make sure it is unique, this is not a requirement. |  |
|**selectedBrand** | **String** | The name of the brand to make a payout to.  For Paysafecard it must be set to &#x60;paysafecard&#x60;. |  [optional] |
|**shopperEmail** | **String** | The shopper&#39;s email address. |  |
|**shopperName** | [**Name**](Name.md) | The shopper&#39;s name.  When the &#x60;entityType&#x60; is &#x60;Company&#x60;, the &#x60;shopperName.lastName&#x60; must contain the company name. |  [optional] |
|**shopperReference** | **String** | The shopper&#39;s reference for the payment transaction. |  |
|**shopperStatement** | **String** | The description of this payout. This description is shown on the bank statement of the shopper (if this is supported by the chosen payment method). |  [optional] |
|**socialSecurityNumber** | **String** | The shopper&#39;s social security number. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| NATURAL_PERSON | &quot;NaturalPerson&quot; |
| COMPANY | &quot;Company&quot; |




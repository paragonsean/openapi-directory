# LinodeApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activePromotions** | [**[Promotion]**](Promotion.md) |  | [optional] [readonly] 
**activeSince** | **Date** | The datetime of when the account was activated. | [optional] [readonly] 
**address1** | **String** | First line of this Account&#39;s billing address. | [optional] 
**address2** | **String** | Second line of this Account&#39;s billing address. | [optional] 
**balance** | **Number** | This Account&#39;s balance, in US dollars. | [optional] [readonly] 
**balanceUninvoiced** | **Number** | This Account&#39;s current estimated invoice in US dollars. This is not your final invoice balance. Transfer charges are not included in the estimate.  | [optional] [readonly] 
**billingSource** | **String** | The source of service charges for this Account, as determined by its relationship with Akamai. Accounts that are associated with Akamai-specific customers return a value of &#x60;akamai&#x60;. All other Accounts return a value of &#x60;linode&#x60;.  | [optional] [readonly] 
**capabilities** | **[String]** | A list of capabilities your account supports.  | [optional] [readonly] 
**city** | **String** | The city for this Account&#39;s billing address. | [optional] 
**company** | **String** | The company name associated with this Account. | [optional] 
**country** | **String** | The two-letter ISO 3166 country code of this Account&#39;s billing address.  | [optional] 
**creditCard** | [**AccountCreditCard**](AccountCreditCard.md) |  | [optional] 
**email** | **String** | The email address of the person associated with this Account. | [optional] 
**euuid** | **String** | An external unique identifier for this account.  | [optional] [readonly] 
**firstName** | **String** | The first name of the person associated with this Account. | [optional] 
**lastName** | **String** | The last name of the person associated with this Account. | [optional] 
**phone** | **String** | The phone number associated with this Account. | [optional] 
**state** | **String** | If billing address is in the United States (US) or Canada (CA), only the two-letter ISO 3166 State or Province code are accepted. If entering a US military address, state abbreviations (AA, AE, AP) should be entered. If the address is outside the US or CA, this is the Province associated with the Account&#39;s billing address.  | [optional] 
**taxId** | **String** | The tax identification number associated with this Account, for tax calculations in some countries. If you do not live in a country that collects tax, this should be an empty string (&#x60;\&quot;\&quot;&#x60;).  | [optional] 
**zip** | **String** | The zip code of this Account&#39;s billing address. The following restrictions apply:  - May only consist of letters, numbers, spaces, and hyphens. - Must not contain more than 9 letter or number characters.  | [optional] 



## Enum: BillingSourceEnum


* `akamai` (value: `"akamai"`)

* `linode` (value: `"linode"`)





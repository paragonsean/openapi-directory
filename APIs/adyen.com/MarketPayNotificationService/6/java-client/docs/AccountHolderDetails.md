

# AccountHolderDetails


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**ViasAddress**](ViasAddress.md) | The address of the account holder. |  |
|**bankAccountDetails** | [**List&lt;BankAccountDetail&gt;**](BankAccountDetail.md) | Array of bank accounts associated with the account holder. For details about the required &#x60;bankAccountDetail&#x60; fields, see [Required information](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/required-information). |  [optional] |
|**bankAggregatorDataReference** | **String** | The opaque reference value returned by the Adyen API during bank account login. |  [optional] |
|**businessDetails** | [**BusinessDetails**](BusinessDetails.md) | Details about the business or nonprofit account holder. Required when creating an account holder with &#x60;legalEntity&#x60; **Business** or **NonProfit**. |  [optional] |
|**email** | **String** | The email address of the account holder. |  [optional] |
|**fullPhoneNumber** | **String** | The phone number of the account holder provided as a single string. It will be handled as a landline phone. **Examples:** \&quot;0031 6 11 22 33 44\&quot;, \&quot;+316/1122-3344\&quot;, \&quot;(0031) 611223344\&quot; |  [optional] |
|**individualDetails** | [**IndividualDetails**](IndividualDetails.md) | Details about the individual account holder. Required when creating an account holder with &#x60;legalEntity&#x60; **Individual**.  |  [optional] |
|**lastReviewDate** | **String** | Date when you last reviewed the account holder&#39;s information, in ISO-8601 YYYY-MM-DD format. For example, **2020-01-31**. |  [optional] |
|**legalArrangements** | [**List&lt;LegalArrangementDetail&gt;**](LegalArrangementDetail.md) | An array containing information about the account holder&#39;s [legal arrangements](https://docs.adyen.com/marketplaces-and-platforms/classic/verification-process/legal-arrangements). |  [optional] |
|**merchantCategoryCode** | **String** | The Merchant Category Code of the account holder. &gt; If not specified in the request, this will be derived from the platform account (which is configured by Adyen). |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | A set of key and value pairs for general use by the account holder or merchant. The keys do not have specific names and may be used for storing miscellaneous data as desired. &gt; The values being stored have a maximum length of eighty (80) characters and will be truncated if necessary. &gt; Note that during an update of metadata, the omission of existing key-value pairs will result in the deletion of those key-value pairs. |  [optional] |
|**payoutMethods** | [**List&lt;PayoutMethod&gt;**](PayoutMethod.md) | Array of tokenized card details associated with the account holder. For details about how you can use the tokens to pay out, refer to [Pay out to cards](https://docs.adyen.com/marketplaces-and-platforms/classic/payout-to-cards). |  [optional] |
|**principalBusinessAddress** | [**ViasAddress**](ViasAddress.md) | The principal business address of the account holder. |  [optional] |
|**storeDetails** | [**List&lt;StoreDetail&gt;**](StoreDetail.md) | Array of stores associated with the account holder. Required when onboarding account holders that have an Adyen [point of sale](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-pos). |  [optional] |
|**webAddress** | **String** | The URL of the website of the account holder. |  [optional] |




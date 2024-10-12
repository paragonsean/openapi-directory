

# RecurringDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **Map&lt;String, String&gt;** | This field contains additional data, which may be returned in a particular response.  The additionalData object consists of entries, each of which includes the key and value. |  [optional] |
|**alias** | **String** | The alias of the credit card number.  Applies only to recurring contracts storing credit card details |  [optional] |
|**aliasType** | **String** | The alias type of the credit card number.  Applies only to recurring contracts storing credit card details. |  [optional] |
|**bank** | [**BankAccount**](BankAccount.md) | A container for bank account data. |  [optional] |
|**billingAddress** | [**Address**](Address.md) | The billing address. |  [optional] |
|**card** | [**Card**](Card.md) | A container for card data. |  [optional] |
|**contractTypes** | **List&lt;String&gt;** | Types of recurring contracts. |  [optional] |
|**creationDate** | **OffsetDateTime** | The date when the recurring details were created. |  [optional] |
|**firstPspReference** | **String** | The &#x60;pspReference&#x60; of the first recurring payment that created the recurring detail. |  [optional] |
|**name** | **String** | An optional descriptive name for this recurring detail. |  [optional] |
|**paymentMethodVariant** | **String** | The  type or sub-brand of a payment method used, e.g. Visa Debit, Visa Corporate, etc. For more information, refer to [PaymentMethodVariant](https://docs.adyen.com/development-resources/paymentmethodvariant). |  [optional] |
|**recurringDetailReference** | **String** | The reference that uniquely identifies the recurring detail. |  |
|**shopperName** | [**Name**](Name.md) | The name of the shopper. |  [optional] |
|**socialSecurityNumber** | **String** | A shopper&#39;s social security number (only in countries where it is legal to collect). |  [optional] |
|**tokenDetails** | [**TokenDetails**](TokenDetails.md) |  |  [optional] |
|**variant** | **String** | The payment method, such as “mc\&quot;, \&quot;visa\&quot;, \&quot;ideal\&quot;, \&quot;paypal\&quot;. |  |




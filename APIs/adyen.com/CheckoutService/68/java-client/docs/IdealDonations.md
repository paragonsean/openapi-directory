

# IdealDonations


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkoutAttemptId** | **String** | The checkout attempt identifier. |  [optional] |
|**issuer** | **String** | The iDEAL issuer value of the shopper&#39;s selected bank. Set this to an **id** of an iDEAL issuer to preselect it. |  |
|**recurringDetailReference** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**storedPaymentMethodId** | **String** | This is the &#x60;recurringDetailReference&#x60; returned in the response when you created the token. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | **ideal** |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| IDEAL | &quot;ideal&quot; |




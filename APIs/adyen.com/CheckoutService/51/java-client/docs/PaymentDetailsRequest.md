

# PaymentDetailsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**details** | [**PaymentCompletionDetails**](PaymentCompletionDetails.md) | Use this collection to submit the details that were returned as a result of the &#x60;/payments&#x60; call. |  |
|**paymentData** | **String** | The &#x60;paymentData&#x60; value from the &#x60;/payments&#x60; response. Required if the &#x60;/payments&#x60; response contained &#x60;paymentData&#x60;.  |  [optional] |
|**threeDSAuthenticationOnly** | **Boolean** | Change the &#x60;authenticationOnly&#x60; indicator originally set in the &#x60;/payments&#x60; request. Only needs to be set if you want to modify the value set previously. |  [optional] |




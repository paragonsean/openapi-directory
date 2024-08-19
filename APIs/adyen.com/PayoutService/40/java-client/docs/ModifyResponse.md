

# ModifyResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **Map&lt;String, String&gt;** | This field contains additional data, which may be returned in a particular response. |  [optional] |
|**pspReference** | **String** | Adyen&#39;s 16-character string reference associated with the transaction. This value is globally unique; quote it when communicating with us about this response. |  |
|**response** | **String** | The response: * In case of success, it is either &#x60;payout-confirm-received&#x60; or &#x60;payout-decline-received&#x60;. * In case of an error, an informational message is returned. |  |




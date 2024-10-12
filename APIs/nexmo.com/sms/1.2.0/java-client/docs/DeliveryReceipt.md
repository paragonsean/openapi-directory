

# DeliveryReceipt


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiKey** | **String** | The API key that sent the SMS. This is useful when multiple accounts are sending webhooks to the same endpoint. |  [optional] |
|**clientRef** | **String** | If the &#x60;client-ref&#x60; is set when the SMS is sent, it will be included in the delivery receipt |  [optional] |
|**errCode** | **String** | The status of the request. Will be a non &#x60;0&#x60; value if there has been an error, or if the status is unknown. See the [Delivery Receipt documentation](/messaging/sms/guides/delivery-receipts#dlr-error-codes) for more details |  [optional] |
|**messageTimestamp** | **String** | The time when Vonage started to push this Delivery Receipt to your webhook endpoint. |  [optional] |
|**messageId** | **String** | The Vonage ID for this message. |  [optional] |
|**msisdn** | **String** | The number the message was sent to. Numbers are specified in E.164 format. |  [optional] |
|**networkCode** | **String** | The Mobile Country Code Mobile Network Code (MCCMNC) of the carrier this phone number is registered with. |  [optional] |
|**nonce** | **String** | A random string to be used when calculating the signature. _Only included if you have signatures enabled_ |  [optional] |
|**price** | **String** | The cost of the message |  [optional] |
|**scts** | **String** | When the DLR was received from the carrier in the following format &#x60;YYMMDDHHMM&#x60;. For example, &#x60;2001011400&#x60; is at &#x60;2020-01-01 14:00&#x60; |  [optional] |
|**sig** | **String** | The signature to enable verification of the source of this webhook. Please see the [developer documentation for validating signatures](/concepts/guides/signing-messages) for more information, or use one of our published SDKs. _Only included if you have signatures enabled_ |  [optional] |
|**status** | **String** | A code that explains where the message is in the delivery process. |  [optional] |
|**timestamp** | **String** | A timestamp in Unix (seconds since the epoch) format. _Only included if you have signatures enabled_ |  [optional] |
|**to** | **String** | The SenderID you set in &#x60;from&#x60; in your request. |  [optional] |




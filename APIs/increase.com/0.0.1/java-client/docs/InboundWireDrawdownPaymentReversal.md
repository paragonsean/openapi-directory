

# InboundWireDrawdownPaymentReversal

A Inbound Wire Drawdown Payment Reversal object. This field will be present in the JSON response if and only if `category` is equal to `inbound_wire_drawdown_payment_reversal`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** | The amount that was reversed. |  |
|**description** | **String** | The description on the reversal message from Fedwire. |  |
|**inputCycleDate** | **LocalDate** | The Fedwire cycle date for the wire reversal. |  |
|**inputMessageAccountabilityData** | **String** | The Fedwire transaction identifier. |  |
|**inputSequenceNumber** | **String** | The Fedwire sequence number. |  |
|**inputSource** | **String** | The Fedwire input source identifier. |  |
|**previousMessageInputCycleDate** | **LocalDate** | The Fedwire cycle date for the wire transfer that was reversed. |  |
|**previousMessageInputMessageAccountabilityData** | **String** | The Fedwire transaction identifier for the wire transfer that was reversed. |  |
|**previousMessageInputSequenceNumber** | **String** | The Fedwire sequence number for the wire transfer that was reversed. |  |
|**previousMessageInputSource** | **String** | The Fedwire input source identifier for the wire transfer that was reversed. |  |




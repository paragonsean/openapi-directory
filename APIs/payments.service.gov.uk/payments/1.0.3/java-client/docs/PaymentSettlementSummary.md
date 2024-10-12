

# PaymentSettlementSummary

A structure representing information about a settlement

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**captureSubmitTime** | **String** | Date and time capture request has been submitted. May be null if capture request was not immediately acknowledged by payment gateway. |  [optional] [readonly] |
|**capturedDate** | **String** | Date of the capture event. |  [optional] [readonly] |
|**settledDate** | **String** | The date that the transaction was paid into the service&#39;s account. |  [optional] [readonly] |




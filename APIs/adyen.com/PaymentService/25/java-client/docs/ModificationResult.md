

# ModificationResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalData** | **Map&lt;String, String&gt;** | This field contains additional data, which may be returned in a particular modification response. |  [optional] |
|**pspReference** | **String** | Adyen&#39;s 16-character string reference associated with the transaction/request. This value is globally unique; quote it when communicating with us about this request. |  |
|**response** | [**ResponseEnum**](#ResponseEnum) | Indicates if the modification request has been received for processing. |  |



## Enum: ResponseEnum

| Name | Value |
|---- | -----|
| CAPTURE_RECEIVED_ | &quot;[capture-received]&quot; |
| CANCEL_RECEIVED_ | &quot;[cancel-received]&quot; |
| REFUND_RECEIVED_ | &quot;[refund-received]&quot; |
| CANCEL_OR_REFUND_RECEIVED_ | &quot;[cancelOrRefund-received]&quot; |
| ADJUST_AUTHORISATION_RECEIVED_ | &quot;[adjustAuthorisation-received]&quot; |
| DONATION_RECEIVED_ | &quot;[donation-received]&quot; |
| TECHNICAL_CANCEL_RECEIVED_ | &quot;[technical-cancel-received]&quot; |
| VOID_PENDING_REFUND_RECEIVED_ | &quot;[voidPendingRefund-received]&quot; |






# WorldpayAllOfSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**delay** | **Integer** | Auto Capture delay (in hours). |  [optional] |
|**enableStoredCredentials** | **Boolean** | True to enable Stored Credentials. |  [optional] |
|**merchantInitiatedReason** | [**MerchantInitiatedReasonEnum**](#MerchantInitiatedReasonEnum) | The value of merchantInitiatedReason to send with merchant-initiated transactions. |  [optional] |



## Enum: MerchantInitiatedReasonEnum

| Name | Value |
|---- | -----|
| UNSCHEDULED | &quot;UNSCHEDULED&quot; |
| RECURRING | &quot;RECURRING&quot; |
| INSTALMENT | &quot;INSTALMENT&quot; |
| REAUTH | &quot;REAUTH&quot; |
| DELAYED | &quot;DELAYED&quot; |
| INCREMENTAL | &quot;INCREMENTAL&quot; |
| RESUBMISSION | &quot;RESUBMISSION&quot; |
| NOSHOW | &quot;NOSHOW&quot; |




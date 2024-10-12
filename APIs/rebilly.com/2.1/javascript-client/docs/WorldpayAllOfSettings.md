# RebillyRestApi.WorldpayAllOfSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay** | **Number** | Auto Capture delay (in hours). | [optional] [default to 0]
**enableStoredCredentials** | **Boolean** | True to enable Stored Credentials. | [optional] [default to false]
**merchantInitiatedReason** | **String** | The value of merchantInitiatedReason to send with merchant-initiated transactions. | [optional] [default to &#39;UNSCHEDULED&#39;]



## Enum: MerchantInitiatedReasonEnum


* `UNSCHEDULED` (value: `"UNSCHEDULED"`)

* `RECURRING` (value: `"RECURRING"`)

* `INSTALMENT` (value: `"INSTALMENT"`)

* `REAUTH` (value: `"REAUTH"`)

* `DELAYED` (value: `"DELAYED"`)

* `INCREMENTAL` (value: `"INCREMENTAL"`)

* `RESUBMISSION` (value: `"RESUBMISSION"`)

* `NOSHOW` (value: `"NOSHOW"`)





# VerifyApi.SearchErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorText** | **String** | If &#x60;status&#x60; is not &#x60;SUCCESS&#x60;, this message explains the issue encountered. | [optional] 
**requestId** | **String** | The &#x60;request_id&#x60; that you received in the response to the Verify request and used in the Verify search request. May be empty in an error situation. | [optional] 
**status** | **String** | Code | Description -- | -- IN PROGRESS | The search is still in progress. SUCCESS | Your user entered a correct verification code. FAILED | Your user entered an incorrect code more than three times. EXPIRED | Your user did not enter a code before the &#x60;pin_expiry&#x60; time elapsed. CANCELLED | The verification process was cancelled by a Verify control request. 101 | You supplied an invalid &#x60;request_id&#x60;, or the data is not available. Note that for recently-completed requests, there can be a delay of up to 1 minute before the results are available in search.  | [optional] 



## Enum: StatusEnum


* `IN PROGRESS` (value: `"IN PROGRESS"`)

* `FAILED` (value: `"FAILED"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `101` (value: `"101"`)





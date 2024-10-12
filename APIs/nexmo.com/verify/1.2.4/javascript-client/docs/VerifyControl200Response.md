# VerifyApi.VerifyControl200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **String** | The &#x60;cmd&#x60; you sent in the request. | [optional] 
**status** | **String** | Code | Text | Description -- | -- | -- 0 | Success | The request was successfully accepted by Vonage. 1 | Throttled | You are trying to send more than the maximum of 30 requests per second. 2 | Your request is incomplete and missing the mandatory parameter &#x60;$parameter&#x60; | The stated parameter is missing. 3 | Invalid value for parameter &#x60;$parameter&#x60; | Invalid value for parameter. If you see Facility not allowed in the error text, check that you are using the correct Base URL in your request. 4 | Invalid credentials were provided | The supplied API key or secret in the request is either invalid or disabled. 5 | Internal Error | An error occurred processing this request in the Cloud Communications Platform. 6 | The Vonage platform was unable to process this message for the following reason: &#x60;$reason&#x60; | The request could not be routed. 8 | The api_key you supplied is for an account that has been barred from submitting messages. | 9 | Partner quota exceeded | Your account does not have sufficient credit to process this request. 19 | For &#x60;cancel&#x60;: Either you have not waited at least 30 secs after sending a Verify request before cancelling or Verify has made too many attempts to deliver the verification code for this request and you must now wait for the process to complete. For &#x60;trigger_next_event&#x60;: All attempts to deliver the verification code for this request have completed and there are no remaining events to advance to.  | [optional] 
**errorText** | **String** | If the &#x60;status&#x60; is non-zero, this explains the error encountered. | [optional] 



## Enum: CommandEnum


* `cancel` (value: `"cancel"`)

* `trigger_next_event` (value: `"trigger_next_event"`)





## Enum: StatusEnum


* `0` (value: `"0"`)

* `1` (value: `"1"`)

* `2` (value: `"2"`)

* `3` (value: `"3"`)

* `4` (value: `"4"`)

* `5` (value: `"5"`)

* `6` (value: `"6"`)

* `8` (value: `"8"`)

* `9` (value: `"9"`)

* `19` (value: `"19"`)





# VerifyApi.VerifyCheck200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | The currency code. | [optional] 
**estimatedPriceMessagesSent** | **String** | This field may not be present, depending on your pricing model. The value indicates the cost (in EUR) of the calls made and messages sent for the verification process. This value may be updated during and shortly after the request completes because user input events can overlap with message/call events. When this field is present, the total cost of the verification is the sum of this field and the &#x60;price&#x60; field.  | [optional] 
**eventId** | **String** | The ID of the verification event, such as an SMS or TTS call. | [optional] 
**price** | **String** | The cost incurred for this request. | [optional] 
**requestId** | **String** | The &#x60;request_id&#x60; that you received in the response to the Verify request and used in the Verify check request. | [optional] 
**status** | **String** | Code | Text | Description -- | -- | -- 0 | Success | The request was successfully accepted by Vonage. 1 | Throttled | You are trying to send more than the maximum of 30 requests per second. 2 | Your request is incomplete and missing the mandatory parameter &#x60;$parameter&#x60; | The stated parameter is missing. 3 | Invalid value for parameter &#x60;$parameter&#x60; | Invalid value for parameter. If you see Facility not allowed in the error text, check that you are using the correct Base URL in your request. 4 | Invalid credentials were provided | The supplied API key or secret in the request is either invalid or disabled. 5 | Internal Error | An error occurred processing this request in the Cloud Communications Platform. 6 | The Vonage platform was unable to process this message for the following reason: &#x60;$reason&#x60; | The request could not be routed. 16 | The code inserted does not match the expected value | 17 | The wrong code was provided too many times | You can run Verify check on a specific &#x60;request_id&#x60; up to three times unless a new verification code is generated. If you check a request more than three times, it is set to FAILED and you cannot check it again.  | [optional] 
**errorText** | **String** | If the &#x60;status&#x60; is non-zero, this explains the error encountered. | [optional] 



## Enum: StatusEnum


* `0` (value: `"0"`)

* `1` (value: `"1"`)

* `2` (value: `"2"`)

* `3` (value: `"3"`)

* `4` (value: `"4"`)

* `5` (value: `"5"`)

* `6` (value: `"6"`)

* `16` (value: `"16"`)

* `17` (value: `"17"`)





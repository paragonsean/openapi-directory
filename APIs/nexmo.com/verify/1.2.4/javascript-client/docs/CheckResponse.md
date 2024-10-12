# VerifyApi.CheckResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **String** | The currency code. | [optional] 
**estimatedPriceMessagesSent** | **String** | This field may not be present, depending on your pricing model. The value indicates the cost (in EUR) of the calls made and messages sent for the verification process. This value may be updated during and shortly after the request completes because user input events can overlap with message/call events. When this field is present, the total cost of the verification is the sum of this field and the &#x60;price&#x60; field.  | [optional] 
**eventId** | **String** | The ID of the verification event, such as an SMS or TTS call. | [optional] 
**price** | **String** | The cost incurred for this request. | [optional] 
**requestId** | **String** | The &#x60;request_id&#x60; that you received in the response to the Verify request and used in the Verify check request. | [optional] 
**status** | **String** | A value of &#x60;0&#x60; indicates that your user entered the correct code. If it is non-zero, check the &#x60;error_text&#x60;. | [optional] 



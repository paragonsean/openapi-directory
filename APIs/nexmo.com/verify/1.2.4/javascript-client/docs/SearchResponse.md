# VerifyApi.SearchResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Vonage account ID the request was for. | [optional] 
**checks** | [**[SearchResponseChecksInner]**](SearchResponseChecksInner.md) | The list of checks made for this verification and their outcomes. | [optional] 
**currency** | **String** | The currency code. | [optional] 
**dateFinalized** | **String** | The date and time the verification request was completed. This response parameter is in the following format YYYY-MM-DD HH:MM:SS. | [optional] 
**dateSubmitted** | **String** | The date and time the verification request was submitted, in the following format YYYY-MM-DD HH:MM:SS. | [optional] 
**estimatedPriceMessagesSent** | **String** | This field may not be present, depending on your pricing model. The value indicates the cost (in EUR) of the calls made and messages sent for the verification process. This value may be updated during and shortly after the request completes because user input events can overlap with message/call events. When this field is present, the total cost of the verification is the sum of this field and the &#x60;price&#x60; field.  | [optional] 
**events** | [**[SearchResponseEventsInner]**](SearchResponseEventsInner.md) | The events that have taken place to verify this number, and their unique identifiers. | [optional] 
**firstEventDate** | **String** | The time the first verification attempt was made, in the following format YYYY-MM-DD HH:MM:SS. | [optional] 
**lastEventDate** | **String** | The time the last verification attempt was made, in the following format YYYY-MM-DD HH:MM:SS. | [optional] 
**number** | **String** | The phone number this verification request was used for. | [optional] 
**price** | **String** | The cost incurred for this verification request. | [optional] 
**requestId** | **String** | The &#x60;request_id&#x60; that you received in the response to the Verify request and used in the Verify search request. | [optional] 
**senderId** | **String** | The &#x60;sender_id&#x60; you provided in the Verify request. | [optional] [default to &#39;verify&#39;]
**status** | **String** | Code | Description -- | -- IN PROGRESS | The search is still in progress. SUCCESS | Your user entered a correct verification code. FAILED | Your user entered an incorrect code more than three times. EXPIRED | Your user did not enter a code before the &#x60;pin_expiry&#x60; time elapsed. CANCELLED | The verification process was cancelled by a Verify control request.  | [optional] 



## Enum: StatusEnum


* `IN PROGRESS` (value: `"IN PROGRESS"`)

* `SUCCESS` (value: `"SUCCESS"`)

* `FAILED` (value: `"FAILED"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `CANCELLED` (value: `"CANCELLED"`)





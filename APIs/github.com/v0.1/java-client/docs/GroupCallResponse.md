

# GroupCallResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**requestUUID** | **String** | Unique identifier of the Call request (UUIDv4) |  |
|**restApiServer** | **String** | API server which handled this request (an Eqivo extension) |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| GROUP_CALL_REQUEST_EXECUTED | &quot;GroupCall Request Executed&quot; |
| MANDATORY_PARAMETERS_MISSING | &quot;Mandatory Parameters Missing&quot; |
| THIS_DELIMITER_IS_NOT_ALLOWED | &quot;This Delimiter is not allowed&quot; |
| GROUP_CALL_SHOULD_BE_USED_FOR_AT_LEAST_2_NUMBERS | &quot;GroupCall should be used for at least 2 numbers&quot; |
| _TO_PARAMETER_LENGTH_DOES_NOT_MATCH_GATEWAYS_LENGTH | &quot;&#39;To&#39; parameter length does not match &#39;Gateways&#39; Length&quot; |
| ANSWER_URL_IS_NOT_VALID | &quot;AnswerUrl is not Valid&quot; |
| HANGUP_URL_IS_NOT_VALID | &quot;HangupUrl is not Valid&quot; |
| RING_URL_IS_NOT_VALID | &quot;RingUrl is not Valid&quot; |
| CONFIRM_SOUND_IS_NOT_VALID | &quot;ConfirmSound is not Valid&quot; |
| UNKNOWN_CORE_UUID | &quot;Unknown Core UUID&quot; |
| GROUP_CALL_REQUEST_FAILED | &quot;GroupCall Request Failed&quot; |






# CallResponse


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
| CALL_REQUEST_EXECUTED | &quot;Call Request Executed&quot; |
| MANDATORY_PARAMETERS_MISSING | &quot;Mandatory Parameters Missing&quot; |
| ANSWER_URL_IS_NOT_VALID | &quot;AnswerUrl is not Valid&quot; |
| HANGUP_URL_IS_NOT_VALID | &quot;HangupUrl is not Valid&quot; |
| RING_URL_IS_NOT_VALID | &quot;RingUrl is not Valid&quot; |
| UNKNOWN_CORE_UUID | &quot;Unknown Core UUID&quot; |




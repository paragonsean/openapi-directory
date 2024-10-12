

# DownloadReport200ResponseReportInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. |  [optional] |
|**clientRef** | **String** | Search for messages with this &#x60;client_ref&#x60;. |  [optional] |
|**country** | **String** | Country where the request was sent. |  [optional] |
|**countryName** | **String** | Country name where the request was sent. |  [optional] |
|**currency** | **String** | Currency of the price of the request. |  [optional] |
|**dateFinalized** | **LocalDate** | Date when the request was finalized. |  [optional] |
|**dateReceived** | **LocalDate** | Date of the request. |  [optional] |
|**direction** | **Direction** |  |  [optional] |
|**errorCode** | **String** | Error code of the message. |  [optional] |
|**errorCodeDescription** | **String** | Description of the error code of the request. |  [optional] |
|**from** | **String** | Request from this number. |  [optional] |
|**latency** | **Integer** | Latency of the request in ms. |  [optional] |
|**messageBody** | **String** | Body of the message sent. Only present if include_message parameter is set to true. |  [optional] |
|**messageId** | **String** | Id of the request. |  [optional] |
|**network** | **String** | Network of the looked up number. |  [optional] |
|**networkName** | **String** | Network name of the looked up number. |  [optional] |
|**status** | **AsrStatus** |  |  [optional] |
|**to** | **String** | Request to this number. |  [optional] |
|**totalPrice** | **String** | Total price of the request. |  [optional] |
|**callId** | **String** | UUID of the request. |  [optional] |
|**dateEnd** | **LocalDate** | Date of the end of the call. |  [optional] |
|**dateStart** | **LocalDate** | Date of the start of the call. |  [optional] |
|**duration** | **Integer** | Duration of the call in seconds. |  [optional] |
|**price** | **String** | Price of the request. |  [optional] |
|**statusDescription** | **String** | ASR error message. |  [optional] |
|**applicationId** | **String** | Search only for requests attached to a particular Application ID. |  [optional] |
|**conversationId** | **String** | Search only for events sent to this particular Conversation. This should include the \&quot;CON-\&quot; prefix. |  [optional] |
|**id** | **String** | Id of the related CDR. |  [optional] |
|**legId** | **String** | Id of the call leg. |  [optional] |
|**requestId** | **String** | UUID of the request. |  [optional] |
|**userId** | **String** | User id in the conversation. |  [optional] |
|**estimatedPrice** | **String** | Estimated price of the verify request. |  [optional] |
|**firstEventDate** | **LocalDate** | Date of the first verify event. |  [optional] |
|**lastEventDate** | **LocalDate** | Date of the last verify event. |  [optional] |
|**locale** | **String** | Locale used for the TTS. |  [optional] |
|**numberType** | **String** | Type of phone number to which requests are sent. |  [optional] |
|**pricingModel** | **String** | Pricing model used for this request. |  [optional] |
|**smsEventCount** | **Integer** | Number of sms sent for this verify request. |  [optional] |
|**ttsEventCount** | **Integer** | Number of tts sent for this verify request. |  [optional] |
|**verifyStatus** | **String** | Status of the verify request. |  [optional] |
|**firstName** | **String** | First name of the owner of the looked up number. |  [optional] |
|**lastName** | **String** | Last name of the owner of the looked up number. |  [optional] |
|**networkType** | **String** | Network type of the looked up number. |  [optional] |
|**number** | **String** | Number looked up for this request. |  [optional] |
|**ported** | **String** | Is the looked up number ported. |  [optional] |
|**productType** | **String** | Type of Number Insight request. |  [optional] |
|**reachable** | **String** | Is the looked up number reachable. |  [optional] |
|**responseCode** | **String** | Response code of the Number Insight request. |  [optional] |
|**valid** | **String** | Is the looked up number valid. |  [optional] |
|**provider** | **String** | Provider of the message. |  [optional] |
|**callDateStart** | **LocalDate** | Date of the start of the call. |  [optional] |






# CreateAsyncReport200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**LinksCreateReport**](LinksCreateReport.md) |  |  [optional] |
|**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. |  |
|**callbackUrl** | **URI** | URL to send a callback upon completion of the report. This POST callback contains the same information as the response to [Get status of report](/api/reports#get-report). |  [optional] |
|**dateEnd** | **LocalDate** | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when report should end.  It is exclusive, i.e. the provided value is strictly greater than the value in the field &#x60;date_received&#x60; in the CDR. &lt;br&gt;If unspecified, defaults to the current time.  |  [optional] |
|**dateStart** | **LocalDate** | ISO-8601 extended time zone offset or ISO-8601 UTC zone offset formatted date (format &#x60;yyyy-mm-ddThh:mm:ss[.sss]±hh:mm&#x60; or &#x60;yyyy-mm-ddThh:mm:ss[.sss]Z&#x60;) for when reports  should begin. It filters on the time the API call was received by Vonage and corresponds to the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the report file. It is inclusive, i.e. the provided value is less than or equal to the value in the field &#x60;date_received&#x60; (&#x60;date_start&#x60; for Voice) in the CDR.&lt;br&gt;If unspecified, defaults  to seven days ago.  |  [optional] |
|**includeSubaccounts** | **Boolean** | Whether to include subaccounts or not. |  [optional] |
|**product** | **ProductAsr** |  |  |
|**receiveTime** | **LocalDate** | Time at which the report request was received by the service. |  [optional] |
|**requestId** | **String** | UUID of the request. |  [optional] |
|**requestStatus** | **RequestStatusCreateReport** |  |  [optional] |
|**startTime** | **LocalDate** | Time at which the report processing of the report has started. |  [optional] |
|**accountRef** | **String** | Search for messages with this &#x60;account_ref&#x60;. |  [optional] |
|**clientRef** | **String** | Search for messages with this &#x60;client_ref&#x60;. |  [optional] |
|**direction** | **Direction** |  |  |
|**from** | **String** | Request from this number. |  [optional] |
|**includeMessage** | **Boolean** | Include the text of messages in the report. |  [optional] |
|**network** | **String** | Network used to send the request. |  [optional] |
|**showConcatenated** | **Boolean** | Indicates whether the SMS was split up into multiple parts (due to its length). |  [optional] |
|**status** | **AsrStatus** |  |  [optional] |
|**to** | **String** | Request to this number. |  [optional] |
|**conversationId** | **String** | Search only for events sent to this particular Conversation. This should include the \&quot;CON-\&quot; prefix. |  [optional] |
|**number** | **String** | Search only request for the target number. |  [optional] |
|**id** | **String** | Search only messages with the specified uuid. |  [optional] |






# CsvMessagesOutbound

Outbound Messages

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
|**from** | **String** | Request from this number. |  [optional] |
|**latency** | **Integer** | Latency of the request in ms. |  [optional] |
|**messageBody** | **String** | Body of the message sent. Only present if include_message parameter is set to true. |  [optional] |
|**messageId** | **String** | Id of the request. |  [optional] |
|**provider** | **String** | Provider of the message. |  [optional] |
|**status** | **String** | Status of the message. |  [optional] |
|**to** | **String** | Request to this number. |  [optional] |
|**totalPrice** | **String** | Total price of the request. |  [optional] |




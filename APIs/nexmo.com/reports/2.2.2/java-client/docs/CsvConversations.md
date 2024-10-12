

# CsvConversations

Conversations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | The account ID (API key) you wish to search for. This can differ from the API key in the authorization header because some accounts can request reports for other accounts, e.g. a primary account owner wants to create a report for one of its subaccounts. |  [optional] |
|**applicationId** | **String** | Search only for requests attached to a particular Application ID. |  [optional] |
|**clientRef** | **String** | Search for messages with this &#x60;client_ref&#x60;. |  [optional] |
|**conversationId** | **String** | Search only for events sent to this particular Conversation. This should include the \&quot;CON-\&quot; prefix. |  [optional] |
|**creationDate** | **LocalDate** | Date the event was created. |  [optional] |
|**currency** | **String** | Currency of the price of the request. |  [optional] |
|**id** | **String** | Id of the related CDR. |  [optional] |
|**price** | **String** | Price of the request. |  [optional] |
|**requestId** | **String** | UUID of the request. |  [optional] |
|**totalPrice** | **String** | Total price of the request. |  [optional] |
|**userId** | **String** | User id in the conversation. |  [optional] |




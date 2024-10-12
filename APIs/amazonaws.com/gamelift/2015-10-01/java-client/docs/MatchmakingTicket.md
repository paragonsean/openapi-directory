

# MatchmakingTicket

Ticket generated to track the progress of a matchmaking request. Each ticket is uniquely identified by a ticket ID, supplied by the requester, when creating a matchmaking request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ticketId** | [**String**](String.md) |  |  [optional] |
|**configurationName** | [**String**](String.md) |  |  [optional] |
|**configurationArn** | [**String**](String.md) |  |  [optional] |
|**status** | [**MatchmakingConfigurationStatus**](MatchmakingConfigurationStatus.md) |  |  [optional] |
|**statusReason** | [**String**](String.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**startTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**players** | [**List**](List.md) |  |  [optional] |
|**gameSessionConnectionInfo** | [**MatchmakingTicketGameSessionConnectionInfo**](MatchmakingTicketGameSessionConnectionInfo.md) |  |  [optional] |
|**estimatedWaitTime** | [**Integer**](Integer.md) |  |  [optional] |




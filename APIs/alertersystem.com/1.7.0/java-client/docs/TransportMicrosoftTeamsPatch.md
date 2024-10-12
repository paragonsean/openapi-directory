

# TransportMicrosoftTeamsPatch

The TransportMicrosoftTeams resource is a collection of transports that carry dispatched alerts to the external Microsoft Teams service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSegmentCode** | **String** | User-provided string on which to segment and filter data. Max 50 characters. |  [optional] |
|**microsoftTeamsPath** | **String** | The path (has the following format: &#39;webhookb2/{uuid}@{uuid}/IncomingWebhook/{id}/{uuid}&#39;) for the Microsoft Teams service. Stored in encrypted format. |  |
|**transportName** | **String** | The name of the transport. |  |




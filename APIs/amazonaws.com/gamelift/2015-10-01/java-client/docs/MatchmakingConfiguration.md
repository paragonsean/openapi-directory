

# MatchmakingConfiguration

Guidelines for use with FlexMatch to match players into games. All matchmaking requests must specify a matchmaking configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**configurationArn** | [**String**](String.md) |  |  [optional] |
|**description** | [**String**](String.md) |  |  [optional] |
|**gameSessionQueueArns** | [**List**](List.md) |  |  [optional] |
|**requestTimeoutSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**acceptanceTimeoutSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**acceptanceRequired** | [**Boolean**](Boolean.md) |  |  [optional] |
|**ruleSetName** | [**String**](String.md) |  |  [optional] |
|**ruleSetArn** | [**String**](String.md) |  |  [optional] |
|**notificationTarget** | [**String**](String.md) |  |  [optional] |
|**additionalPlayerCount** | [**Integer**](Integer.md) |  |  [optional] |
|**customEventData** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**gameProperties** | [**List**](List.md) |  |  [optional] |
|**gameSessionData** | [**String**](String.md) |  |  [optional] |
|**backfillMode** | [**BackfillMode**](BackfillMode.md) |  |  [optional] |
|**flexMatchMode** | [**FlexMatchMode**](FlexMatchMode.md) |  |  [optional] |




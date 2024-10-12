

# GameSessionQueue

Configuration for a game session placement mechanism that processes requests for new game sessions. A queue can be used on its own or as part of a matchmaking solution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**gameSessionQueueArn** | [**String**](String.md) |  |  [optional] |
|**timeoutInSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**playerLatencyPolicies** | [**List**](List.md) |  |  [optional] |
|**destinations** | [**List**](List.md) |  |  [optional] |
|**filterConfiguration** | [**CreateGameSessionQueueInputFilterConfiguration**](CreateGameSessionQueueInputFilterConfiguration.md) |  |  [optional] |
|**priorityConfiguration** | [**CreateGameSessionQueueInputPriorityConfiguration**](CreateGameSessionQueueInputPriorityConfiguration.md) |  |  [optional] |
|**customEventData** | [**String**](String.md) |  |  [optional] |
|**notificationTarget** | [**String**](String.md) |  |  [optional] |




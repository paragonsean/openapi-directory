

# Event

Carries information about events that occur during pipeline execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A human-readable description of the event. Note that these strings can change at any time without notice. Any application logic must use the information in the &#x60;details&#x60; field. |  [optional] |
|**details** | **Map&lt;String, Object&gt;** | Machine-readable details about the event. |  [optional] |
|**timestamp** | **String** | The time at which the event occurred. |  [optional] |




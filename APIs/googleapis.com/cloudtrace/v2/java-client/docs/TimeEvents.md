

# TimeEvents

A collection of `TimeEvent`s. A `TimeEvent` is a time-stamped annotation on the span, consisting of either user-supplied key:value pairs, or details of a message sent/received between Spans.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**droppedAnnotationsCount** | **Integer** | The number of dropped annotations in all the included time events. If the value is 0, then no annotations were dropped. |  [optional] |
|**droppedMessageEventsCount** | **Integer** | The number of dropped message events in all the included time events. If the value is 0, then no message events were dropped. |  [optional] |
|**timeEvent** | [**List&lt;TimeEvent&gt;**](TimeEvent.md) | A collection of &#x60;TimeEvent&#x60;s. |  [optional] |




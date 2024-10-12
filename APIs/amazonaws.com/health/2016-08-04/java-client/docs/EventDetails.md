

# EventDetails

Detailed information about an event. A combination of an <a href=\"https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html\">Event</a> object, an <a href=\"https://docs.aws.amazon.com/health/latest/APIReference/API_EventDescription.html\">EventDescription</a> object, and additional metadata about the event. Returned by the <a href=\"https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html\">DescribeEventDetails</a> operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**event** | [**EventDetailsEvent**](EventDetailsEvent.md) |  |  [optional] |
|**eventDescription** | [**EventDetailsEventDescription**](EventDetailsEventDescription.md) |  |  [optional] |
|**eventMetadata** | [**Map**](Map.md) |  |  [optional] |




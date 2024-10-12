

# DateTimeRange

The range of time. Cannot be null or negative.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**from** | **OffsetDateTime** | Start timestamp of the time range. Start timestamp is inclusive when used in time series query requests. Events that have this timestamp are included. |  |
|**to** | **OffsetDateTime** | End timestamp of the time range. End timestamp is exclusive when used in time series query requests. Events that match this timestamp are excluded. Note that end timestamp is inclusive when returned by Get Availability (meaning that there is an event with this exact \&quot;to\&quot; timestamp). |  |




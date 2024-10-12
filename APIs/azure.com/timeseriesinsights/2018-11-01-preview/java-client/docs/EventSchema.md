

# EventSchema

Event schema of all events within a given search span. Event schema is a set of property definitions. Properties are identified by both name and type. Different events can have properties with same name, but different type. Event schema may not be contain all persisted properties when there are too many properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**List&lt;EventProperty&gt;**](EventProperty.md) | A set of property definitions. When environment has no data, the returned array is empty. |  [optional] [readonly] |




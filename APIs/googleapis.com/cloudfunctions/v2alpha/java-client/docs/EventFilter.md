

# EventFilter

Filters events based on exact matches on the CloudEvents attributes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attribute** | **String** | Required. The name of a CloudEvents attribute. |  [optional] |
|**operator** | **String** | Optional. The operator used for matching the events with the value of the filter. If not specified, only events that have an exact key-value pair specified in the filter are matched. The only allowed value is &#x60;match-path-pattern&#x60;. |  [optional] |
|**value** | **String** | Required. The value for the attribute. |  [optional] |




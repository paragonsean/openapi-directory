

# Colors


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calendar** | [**Map&lt;String, ColorDefinition&gt;**](ColorDefinition.md) | A global palette of calendar colors, mapping from the color ID to its definition. A calendarListEntry resource refers to one of these color IDs in its colorId field. Read-only. |  [optional] |
|**event** | [**Map&lt;String, ColorDefinition&gt;**](ColorDefinition.md) | A global palette of event colors, mapping from the color ID to its definition. An event resource may refer to one of these color IDs in its colorId field. Read-only. |  [optional] |
|**kind** | **String** | Type of the resource (\&quot;calendar#colors\&quot;). |  [optional] |
|**updated** | **OffsetDateTime** | Last modification time of the color palette (as a RFC3339 timestamp). Read-only. |  [optional] |




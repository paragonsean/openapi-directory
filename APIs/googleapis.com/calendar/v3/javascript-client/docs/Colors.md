# CalendarApi.Colors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calendar** | [**{String: ColorDefinition}**](ColorDefinition.md) | A global palette of calendar colors, mapping from the color ID to its definition. A calendarListEntry resource refers to one of these color IDs in its colorId field. Read-only. | [optional] 
**event** | [**{String: ColorDefinition}**](ColorDefinition.md) | A global palette of event colors, mapping from the color ID to its definition. An event resource may refer to one of these color IDs in its colorId field. Read-only. | [optional] 
**kind** | **String** | Type of the resource (\&quot;calendar#colors\&quot;). | [optional] [default to &#39;calendar#colors&#39;]
**updated** | **Date** | Last modification time of the color palette (as a RFC3339 timestamp). Read-only. | [optional] 



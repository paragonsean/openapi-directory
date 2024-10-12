

# MoreHours

The time periods during which a location is open for certain types of business.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hoursTypeId** | **String** | Required. Type of hours. Clients should call {#link businessCategories:BatchGet} to get supported hours types for categories of their locations. |  [optional] |
|**periods** | [**List&lt;TimePeriod&gt;**](TimePeriod.md) | Required. A collection of times that this location is open. Each period represents a range of hours when the location is open during the week. |  [optional] |




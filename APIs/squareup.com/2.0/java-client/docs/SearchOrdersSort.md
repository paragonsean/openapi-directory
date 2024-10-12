

# SearchOrdersSort

Sorting criteria for a `SearchOrders` request. Results can only be sorted by a timestamp field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sortField** | **String** | The field to sort by.  __Important:__ When using a [DateTimeFilter](https://developer.squareup.com/reference/square_2021-08-18/objects/SearchOrdersFilter), &#x60;sort_field&#x60; must match the timestamp field that the &#x60;DateTimeFilter&#x60; uses to filter. For example, if you set your &#x60;sort_field&#x60; to &#x60;CLOSED_AT&#x60; and you use a &#x60;DateTimeFilter&#x60;, your &#x60;DateTimeFilter&#x60; must filter for orders by their &#x60;CLOSED_AT&#x60; date. If this field does not match the timestamp field in &#x60;DateTimeFilter&#x60;, &#x60;SearchOrders&#x60; returns an error.  Default: &#x60;CREATED_AT&#x60;. |  |
|**sortOrder** | **String** | The chronological order in which results are returned. Defaults to &#x60;DESC&#x60;. |  [optional] |




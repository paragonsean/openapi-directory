

# ListGiftCardActivitiesRequest

Returns a list of gift card activities. You can optionally specify a filter to retrieve a subset of activites.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beginTime** | **String** | The timestamp for the beginning of the reporting period, in RFC 3339 format. Inclusive. Default: The current time minus one year. |  [optional] |
|**cursor** | **String** | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query. If you do not provide the cursor, the call returns the first page of the results. |  [optional] |
|**endTime** | **String** | The timestamp for the end of the reporting period, in RFC 3339 format. Inclusive. Default: The current time. |  [optional] |
|**giftCardId** | **String** | If you provide a gift card ID, the endpoint returns activities that belong  to the specified gift card. Otherwise, the endpoint returns all gift card activities for  the seller. |  [optional] |
|**limit** | **Integer** | If you provide a limit value, the endpoint returns the specified number  of results (or less) per page. A maximum value is 100. The default value is 50. |  [optional] |
|**locationId** | **String** | If you provide a location ID, the endpoint returns gift card activities for that location.  Otherwise, the endpoint returns gift card activities for all locations. |  [optional] |
|**sortOrder** | **String** | The order in which the endpoint returns the activities, based on &#x60;created_at&#x60;. - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default). |  [optional] |
|**type** | **String** | If you provide a type, the endpoint returns gift card activities of this type.  Otherwise, the endpoint returns all types of gift card activities. |  [optional] |




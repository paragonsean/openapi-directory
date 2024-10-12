

# BookingStatusRequest

**note**: all items are optional, but at least one needs to be included

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bookingDateFrom** | **String** | **earliest date** for *this* booking (must be in the future) |  [optional] |
|**bookingDateTo** | **String** | **latest date** for *this* booking (must be in the future) |  [optional] |
|**distributorItemRefs** | **List&lt;String&gt;** | **array** of partner-defined distributor item reference identifiers e.g. &#x60;[&#39;refItem1&#39;,&#39;refItem2&#39;,&#39;refItem3&#39;]&#x60; |  [optional] |
|**distributorRefs** | **List&lt;String&gt;** | **array** of partner-defined distributor reference identifiers |  [optional] |
|**itemIds** | **List&lt;Integer&gt;** | **array** of item identifiers to check |  [optional] |
|**leadFirstName** | **String** | **first name** of the lead traveler |  [optional] |
|**leadSurname** | **String** | **surname** of the lead traveler |  [optional] |
|**test** | **Boolean** | **specifier**: - &#x60;true&#x60;: bypass the poll limit in the prelive environment only (recommended for testing) - &#x60;false&#x60;: (default)  |  [optional] |




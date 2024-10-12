

# DailyRate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addonServices** | [**List&lt;ServiceRate&gt;**](ServiceRate.md) | List of addon services with additional price information. |  [optional] |
|**date** | **OffsetDateTime** | Date the room rate will be charged to the folio |  [optional] |
|**excludedTax** | **Double** | The amount of extra taxes also calculated for all rooms and all persons per room. |  [optional] |
|**includedServices** | **List&lt;String&gt;** | List of codes for all services already included in the gross rate |  [optional] |
|**includedTax** | **Double** | The amount of taxes already included in the gross nightly rate also calculated for all rooms and              all persons per room. |  [optional] |
|**rate** | **Double** | The gross room rate. It is the price calculated for all rooms and all persons per room. |  [optional] |
|**roomType** | **String** | Code of the room type which is booked for that day |  [optional] |




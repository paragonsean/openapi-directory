

# CustomerFilter

Represents a set of `CustomerQuery` filters used to limit the set of customers returned by the [SearchCustomers](https://developer.squareup.com/reference/square_2021-08-18/customers-api/search-customers) endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | [**TimeRange**](TimeRange.md) |  |  [optional] |
|**creationSource** | [**CustomerCreationSourceFilter**](CustomerCreationSourceFilter.md) |  |  [optional] |
|**emailAddress** | [**CustomerTextFilter**](CustomerTextFilter.md) |  |  [optional] |
|**groupIds** | [**FilterValue**](FilterValue.md) |  |  [optional] |
|**phoneNumber** | [**CustomerTextFilter**](CustomerTextFilter.md) |  |  [optional] |
|**referenceId** | [**CustomerTextFilter**](CustomerTextFilter.md) |  |  [optional] |
|**updatedAt** | [**TimeRange**](TimeRange.md) |  |  [optional] |






# GoogleCloudRetailV2CatalogAttributeFacetConfigIgnoredFacetValues

Facet values to ignore on facets during the specified time range for the given SearchResponse.Facet.key attribute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | If start time is empty and end time is not empty, then ignore these facet values before end time. |  [optional] |
|**startTime** | **String** | Time range for the current list of facet values to ignore. If multiple time ranges are specified for an facet value for the current attribute, consider all of them. If both are empty, ignore always. If start time and end time are set, then start time must be before end time. If start time is not empty and end time is empty, then will ignore these facet values after the start time. |  [optional] |
|**values** | **List&lt;String&gt;** | List of facet values to ignore for the following time range. The facet values are the same as the attribute values. There is a limit of 10 values per instance of IgnoredFacetValues. Each value can have at most 128 characters. |  [optional] |




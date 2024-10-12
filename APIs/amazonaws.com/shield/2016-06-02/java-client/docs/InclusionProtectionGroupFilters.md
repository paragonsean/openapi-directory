

# InclusionProtectionGroupFilters

Narrows the set of protection groups that the call retrieves. You can retrieve a single protection group by its name and you can retrieve all protection groups that are configured with a specific pattern, aggregation, or resource type. You can provide up to one criteria per filter type. Shield Advanced returns the protection groups that exactly match all of the search criteria that you provide.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**protectionGroupIds** | [**List**](List.md) |  |  [optional] |
|**patterns** | [**List**](List.md) |  |  [optional] |
|**resourceTypes** | [**List**](List.md) |  |  [optional] |
|**aggregations** | [**List**](List.md) |  |  [optional] |




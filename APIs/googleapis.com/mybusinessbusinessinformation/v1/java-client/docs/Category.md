

# Category

A category describing what this business is (not what it does). For a list of valid category IDs, and the mappings to their human-readable names, see `categories.list`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Output only. The human-readable name of the category. This is set when reading the location. When modifying the location, &#x60;category_id&#x60; must be set. |  [optional] [readonly] |
|**moreHoursTypes** | [**List&lt;MoreHoursType&gt;**](MoreHoursType.md) | Output only. More hours types that are available for this business category. |  [optional] [readonly] |
|**name** | **String** | Required. A stable ID (provided by Google) for this category. The value must be specified when modifying the category (when creating or updating a location). |  [optional] |
|**serviceTypes** | [**List&lt;ServiceType&gt;**](ServiceType.md) | Output only. A list of all the service types that are available for this business category. |  [optional] [readonly] |




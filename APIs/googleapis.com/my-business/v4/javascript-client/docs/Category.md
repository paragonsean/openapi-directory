# GoogleMyBusinessApi.Category

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryId** | **String** | @OutputOnly. A stable ID (provided by Google) for this category. The &#x60;category_id&#x60; must be specified when modifying the category (when creating or updating a location). | [optional] 
**displayName** | **String** | @OutputOnly. The human-readable name of the category. This is set when reading the location. When modifying the location, &#x60;category_id&#x60; must be set. | [optional] 
**moreHoursTypes** | [**[MoreHoursType]**](MoreHoursType.md) | Output only. More hours types that are available for this business category. | [optional] [readonly] 
**serviceTypes** | [**[ServiceType]**](ServiceType.md) | @OutputOnly. A list of all the service types that are available for this business category. | [optional] 



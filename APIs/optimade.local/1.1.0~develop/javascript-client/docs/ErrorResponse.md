# OptimadeApi.ErrorResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Data**](Data.md) |  | [optional] 
**errors** | [**[OptimadeError]**](OptimadeError.md) | A list of OPTIMADE-specific JSON API error objects, where the field detail MUST be present. | 
**included** | [**[Resource]**](Resource.md) | A list of unique included resources | [optional] 
**jsonapi** | [**JsonApi**](JsonApi.md) | Information about the JSON API used | [optional] 
**links** | [**ToplevelLinks**](ToplevelLinks.md) | Links associated with the primary data or errors | [optional] 
**meta** | [**ResponseMeta**](ResponseMeta.md) | A meta object containing non-standard information | 



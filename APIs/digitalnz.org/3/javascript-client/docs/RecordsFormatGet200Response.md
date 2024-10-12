# DigitalNzApi.RecordsFormatGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facets** | **{String: {String: Number}}** | Each field you request from the list of facetable fields will be returned as separate elements. Each of those will contain a sorted list of elements that are made up of a value (eg collection name, subject, date) and the number of results associated with that value.    | [optional] 
**page** | **Number** | Current page. | [optional] 
**perPage** | **Number** | Requested amount of records shown per page of results. | [optional] 
**records** | [**[Record]**](Record.md) |  | [optional] 
**requestUrl** | **String** | The URL of current page of results. | [optional] 
**resultCount** | **Number** | Total number of matching search results. | [optional] 



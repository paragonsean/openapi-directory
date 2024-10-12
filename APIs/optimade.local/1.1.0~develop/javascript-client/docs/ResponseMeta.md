# OptimadeApi.ResponseMeta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiVersion** | **String** | Presently used full version of the OPTIMADE API. The version number string MUST NOT be prefixed by, e.g., \&quot;v\&quot;. Examples: &#x60;1.0.0&#x60;, &#x60;1.0.0-rc.2&#x60;. | 
**dataAvailable** | **Number** | An integer containing the total number of data resource objects available in the database for the endpoint. | [optional] 
**dataReturned** | **Number** | An integer containing the total number of data resource objects returned for the current &#x60;filter&#x60; query, independent of pagination. | [optional] 
**implementation** | [**Implementation**](Implementation.md) | a dictionary describing the server implementation | [optional] 
**lastId** | **String** | a string containing the last ID returned | [optional] 
**moreDataAvailable** | **Boolean** | &#x60;false&#x60; if the response contains all data for the request (e.g., a request issued to a single entry endpoint, or a &#x60;filter&#x60; query at the last page of a paginated response) and &#x60;true&#x60; if the response is incomplete in the sense that multiple objects match the request, and not all of them have been included in the response (e.g., a query with multiple pages that is not at the last page). | 
**provider** | [**Provider**](Provider.md) | information on the database provider of the implementation. | [optional] 
**query** | [**ResponseMetaQuery**](ResponseMetaQuery.md) | Information on the Query that was requested | 
**responseMessage** | **String** | response string from the server | [optional] 
**schema** | [**Schema**](Schema.md) |  | [optional] 
**timeStamp** | **Date** | A timestamp containing the date and time at which the query was executed. | [optional] 
**warnings** | [**[Warnings]**](Warnings.md) | A list of warning resource objects representing non-critical errors or warnings. A warning resource object is defined similarly to a [JSON API error object](http://jsonapi.org/format/1.0/#error-objects), but MUST also include the field &#x60;type&#x60;, which MUST have the value &#x60;\&quot;warning\&quot;&#x60;. The field &#x60;detail&#x60; MUST be present and SHOULD contain a non-critical message, e.g., reporting unrecognized search attributes or deprecated features. The field &#x60;status&#x60;, representing a HTTP response status code, MUST NOT be present for a warning resource object. This is an exclusive field for error resource objects. | [optional] 



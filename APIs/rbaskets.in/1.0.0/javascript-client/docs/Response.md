# RequestBasketsApi.Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | Content of response body | [optional] 
**headers** | **{String: [String]}** | Map of HTTP headers, key represents name, value is array of values | [optional] 
**isTemplate** | **Boolean** | If set to &#x60;true&#x60; the body is treated as [HTML template](https://golang.org/pkg/html/template) that accepts input from request parameters.  | [optional] 
**status** | **Number** | The HTTP status code to reply with | [optional] 



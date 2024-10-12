# HotelSearchApi.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **Number** | A machine-readable error code from the Amadeus Canned Messages table, that will enable the API Consumers code to handle this type of error | [optional] 
**detail** | **String** | An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized. | [optional] 
**documentation** | **String** | A link to a web page or file with further documentation to help the API consumer resolve this error | [optional] 
**source** | [**ErrorSource**](ErrorSource.md) |  | [optional] 
**status** | **Number** | The [HTTP status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) of this response. This is present only in terminal errors which cause an unsuccessful response. In the case of multiple errors, they must all have the same status. | [optional] 
**title** | **String** | An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized | [optional] 



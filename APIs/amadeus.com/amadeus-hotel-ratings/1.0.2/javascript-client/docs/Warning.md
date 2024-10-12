# HotelRatings.Warning

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **Number** | A machine-readable error code from the Canned Messages table, that will enable the API Consumers code to handle this type of error | 
**detail** | **String** | An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field’s value can be localized. | [optional] 
**documentation** | **String** | A link to a web page or file with further documentation to help the API consumer resolve this error | [optional] 
**source** | [**ErrorSource**](ErrorSource.md) |  | [optional] 
**title** | **String** | An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized | 



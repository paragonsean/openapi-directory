# HotelBooking.Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **Number** | [Integer] A machine-readable error code from the Amadeus Canned Messages table, that will enable the API Consumers code to handle this type of error | 
**detail** | **String** | [String] An easy-to-read explanation specific to this occurrence of the problem. It should give the API consumer an idea of what went wrong and how to recover from it. Like the title, this field value can be localized. | [optional] 
**status** | **Number** | [Integer] The [HTTP status code](https://www.iana.org/assignments/http-status-codes/http-status-codes.xhtml) of this response. This is present only in terminal errors which cause an unsuccessful response. In the case of multiple errors, they must all have the same status. | 
**title** | **String** | [String] An error title from the Canned Messages table with a 1:1 correspondence to the error code. This may be localized | 



# ManagementApi.RestServiceError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **String** | A human-readable explanation specific to this occurrence of the problem. | 
**errorCode** | **String** | A code that identifies the problem type. | 
**instance** | **String** | A unique URI that identifies the specific occurrence of the problem. | [optional] 
**invalidFields** | [**[InvalidField]**](InvalidField.md) | Detailed explanation of each validation error, when applicable. | [optional] 
**requestId** | **String** | A unique reference for the request, essentially the same as &#x60;pspReference&#x60;. | [optional] 
**response** | **Object** |  | [optional] 
**status** | **Number** | The HTTP status code. | 
**title** | **String** | A short, human-readable summary of the problem type. | 
**type** | **String** | A URI that identifies the problem type, pointing to human-readable documentation on this problem type. | 



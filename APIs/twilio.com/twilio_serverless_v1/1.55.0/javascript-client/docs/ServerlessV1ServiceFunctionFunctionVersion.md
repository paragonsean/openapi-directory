# TwilioServerless.ServerlessV1ServiceFunctionFunctionVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Function Version resource. | [optional] 
**dateCreated** | **Date** | The date and time in GMT when the Function Version resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] 
**functionSid** | **String** | The SID of the Function resource that is the parent of the Function Version resource. | [optional] 
**links** | **Object** |  | [optional] 
**path** | **String** | The URL-friendly string by which the Function Version resource can be referenced. It can be a maximum of 255 characters. All paths begin with a forward slash (&#39;/&#39;). If a Function Version creation request is submitted with a path not containing a leading slash, the path will automatically be prepended with one. | [optional] 
**serviceSid** | **String** | The SID of the Service that the Function Version resource is associated with. | [optional] 
**sid** | **String** | The unique string that we created to identify the Function Version resource. | [optional] 
**url** | **String** | The absolute URL of the Function Version resource. | [optional] 
**visibility** | [**FunctionVersionEnumVisibility**](FunctionVersionEnumVisibility.md) |  | [optional] 



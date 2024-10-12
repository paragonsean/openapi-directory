# BeezUpMerchantApi.LinkParameter3

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | description of the parameter | [optional] 
**_in** | [**ParameterIn**](ParameterIn.md) |  | 
**label** | **String** | The label corresponding to the link parameter. This label is automatically translated based on the Accept-Language http header. | [optional] 
**lovLink** | [**LOVLink3**](LOVLink3.md) |  | [optional] 
**lovRequired** | **Boolean** | If true, you MUST indicate a value from the list of values otherwise it&#39;s a freetext | [optional] 
**pattern** | **String** | The regular expression to validate the value | [optional] 
**properties** | [**{String: LinkParameterProperty3}**](LinkParameterProperty3.md) | If the parameter is an object with flexible properties (additionProperties/dictionary), we will describe the properties of the object. | [optional] 
**required** | **Boolean** |  | [optional] [default to false]
**schema** | **String** | schema of the parameter | [optional] 
**value** | **Object** | The value of the parameter. It can be an integer a string or an object. | [optional] 



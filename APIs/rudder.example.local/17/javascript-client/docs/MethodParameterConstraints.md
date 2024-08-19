# RudderApi.MethodParameterConstraints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowEmptyString** | **Boolean** | Can this parameter be empty? | 
**allowWhitespaceString** | **Boolean** | Can this parameter allow trailing/ending spaces, or even a full whitespace string ? | 
**maxLength** | **Number** | Maximum size of a parameter | 
**minLength** | **Number** | Minimal size of a parameter | 
**notRegex** | **String** | A regexp to invalidate this parameter | 
**regex** | **String** | A regex to validate this parameter | 
**select** | **[String]** | List of items authorized for this parameter | 



# InfermedicaApi.ParseRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conceptTypes** | **[String]** | list of concept types that should be captured | [optional] 
**context** | **[String]** | ordered list of ids of present symptoms that were already captured and can be used as context | [optional] 
**correctSpelling** | **Boolean** | correct spelling of input text before proper analysis | [optional] 
**includeTokens** | **Boolean** | include tokenization details in output | [optional] 
**text** | **String** | user text to process | 



## Enum: [ConceptTypesEnum]


* `symptom` (value: `"symptom"`)

* `risk_factor` (value: `"risk_factor"`)







# ParseRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conceptTypes** | [**List&lt;ConceptTypesEnum&gt;**](#List&lt;ConceptTypesEnum&gt;) | list of concept types that should be captured |  [optional] |
|**context** | **List&lt;String&gt;** | ordered list of ids of present symptoms that were already captured and can be used as context |  [optional] |
|**correctSpelling** | **Boolean** | correct spelling of input text before proper analysis |  [optional] |
|**includeTokens** | **Boolean** | include tokenization details in output |  [optional] |
|**text** | **String** | user text to process |  |



## Enum: List&lt;ConceptTypesEnum&gt;

| Name | Value |
|---- | -----|
| SYMPTOM | &quot;symptom&quot; |
| RISK_FACTOR | &quot;risk_factor&quot; |






# CorrectionCorrection

Object that indicates if the term was misspelled and suggests a possible correction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correction** | **Boolean** | Whether the API was able to suggest a correction (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |
|**highlighted** | **String** | The same as &#x60;text&#x60;, but it highlights the corrected word. Useful when there is more than one word. |  [optional] |
|**misspelled** | **Boolean** | Whether the term was misspelled (&#x60;true&#x60;) or not (&#x60;false&#x60;). |  [optional] |
|**text** | **String** | The corrected term. If the API was not able to correct the term, it will show the original search term. |  [optional] |




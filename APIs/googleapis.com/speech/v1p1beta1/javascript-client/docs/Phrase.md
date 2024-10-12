# CloudSpeechToTextApi.Phrase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boost** | **Number** | Hint Boost. Overrides the boost set at the phrase set level. Positive value will increase the probability that a specific phrase will be recognized over other similar sounding phrases. The higher the boost, the higher the chance of false positive recognition as well. Negative boost will simply be ignored. Though &#x60;boost&#x60; can accept a wide range of positive values, most use cases are best served with values between 0 and 20. We recommend using a binary search approach to finding the optimal value for your use case as well as adding phrases both with and without boost to your requests. | [optional] 
**value** | **String** | The phrase itself. | [optional] 



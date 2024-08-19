# RudderApi.GroupNewQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**composition** | **String** | Boolean operator to use between each  &#x60;where&#x60; criteria. | [optional] [default to &#39;and&#39;]
**select** | **String** | What kind of data we want to include. Here we can get policy servers/relay by setting &#x60;nodeAndPolicyServer&#x60;. Only used if &#x60;where&#x60; is defined. | [optional] [default to &#39;node&#39;]
**where** | [**[GroupQueryWhereInner]**](GroupQueryWhereInner.md) | List of criteria | [optional] 



## Enum: CompositionEnum


* `and` (value: `"and"`)

* `or` (value: `"or"`)





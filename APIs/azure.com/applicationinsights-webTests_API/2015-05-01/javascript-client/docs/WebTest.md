# ApplicationInsightsManagementClient.WebTest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** | The kind of web test that this web test watches. Choices are ping and multistep. | [optional] [default to &#39;ping&#39;]
**properties** | [**WebTestProperties**](WebTestProperties.md) |  | [optional] 
**id** | **String** | Azure resource Id | [optional] [readonly] 
**location** | **String** | Resource location | 
**name** | **String** | Azure resource name | [optional] [readonly] 
**tags** | **Object** | Resource tags | [optional] 
**type** | **String** | Azure resource type | [optional] [readonly] 



## Enum: KindEnum


* `ping` (value: `"ping"`)

* `multistep` (value: `"multistep"`)





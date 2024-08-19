# SvixApi.EndpointIn

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **[String]** | List of message channels this endpoint listens to (omit for all) | [optional] 
**description** | **String** |  | [optional] [default to &#39;&#39;]
**disabled** | **Boolean** |  | [optional] [default to false]
**filterTypes** | **[String]** |  | [optional] 
**metadata** | **{String: String}** |  | [optional] 
**rateLimit** | **Number** |  | [optional] 
**secret** | **String** | The endpoint&#39;s verification secret. If &#x60;null&#x60; is passed, a secret is automatically generated. Format: &#x60;base64&#x60; encoded random bytes optionally prefixed with &#x60;whsec_&#x60;. Recommended size: 24. | [optional] 
**uid** | **String** | Optional unique identifier for the endpoint | [optional] 
**url** | **String** |  | 
**version** | **Number** |  | 



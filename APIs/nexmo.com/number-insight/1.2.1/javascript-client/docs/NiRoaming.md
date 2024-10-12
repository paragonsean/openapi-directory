# NumberInsightApi.NiRoaming

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roamingCountryCode** | **String** | If &#x60;number&#x60; is &#x60;roaming&#x60;, this is the [code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country &#x60;number&#x60; is roaming in. | [optional] 
**roamingNetworkCode** | **String** | If &#x60;number&#x60; is &#x60;roaming&#x60;, this is the id of the carrier network &#x60;number&#x60; is roaming in. | [optional] 
**roamingNetworkName** | **String** | If &#x60;number&#x60; is &#x60;roaming&#x60;, this is the name of the carrier network &#x60;number&#x60; is roaming in. | [optional] 
**status** | **String** | Is &#x60;number&#x60; outside its home carrier network. | [optional] 



## Enum: StatusEnum


* `roaming` (value: `"roaming"`)

* `not_roaming` (value: `"not_roaming"`)





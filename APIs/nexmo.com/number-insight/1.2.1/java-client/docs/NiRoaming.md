

# NiRoaming

Information about the roaming status for `number`. This is applicable to mobile numbers only. If unknown, this may return a string of `unknown` instead of an object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**roamingCountryCode** | **String** | If &#x60;number&#x60; is &#x60;roaming&#x60;, this is the [code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the country &#x60;number&#x60; is roaming in. |  [optional] |
|**roamingNetworkCode** | **String** | If &#x60;number&#x60; is &#x60;roaming&#x60;, this is the id of the carrier network &#x60;number&#x60; is roaming in. |  [optional] |
|**roamingNetworkName** | **String** | If &#x60;number&#x60; is &#x60;roaming&#x60;, this is the name of the carrier network &#x60;number&#x60; is roaming in. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Is &#x60;number&#x60; outside its home carrier network. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ROAMING | &quot;roaming&quot; |
| NOT_ROAMING | &quot;not_roaming&quot; |




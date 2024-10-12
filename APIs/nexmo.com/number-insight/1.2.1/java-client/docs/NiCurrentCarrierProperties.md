

# NiCurrentCarrierProperties

Information about the network `number` is currently connected to.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | The country that &#x60;number&#x60; is associated with. This is in ISO 3166-1 alpha-2   format. |  [optional] |
|**name** | **String** | The full name of the carrier that &#x60;number&#x60; is associated with. |  [optional] |
|**networkCode** | **String** | The [https://en.wikipedia.org/wiki/Mobile_country_code](https://en.wikipedia.org/wiki/Mobile_country_code) for the carrier&#x60;number&#x60; is associated with. Unreal numbers are marked as&#x60;null&#x60; and the request is rejected altogether if the number is impossible according to the [E.164](https://en.wikipedia.org/wiki/E.164) guidelines. |  [optional] |
|**networkType** | [**NetworkTypeEnum**](#NetworkTypeEnum) | The type of network that &#x60;number&#x60; is associated with. |  [optional] |



## Enum: NetworkTypeEnum

| Name | Value |
|---- | -----|
| MOBILE | &quot;mobile&quot; |
| LANDLINE | &quot;landline&quot; |
| LANDLINE_PREMIUM | &quot;landline_premium&quot; |
| LANDLINE_TOLLFREE | &quot;landline_tollfree&quot; |
| VIRTUAL | &quot;virtual&quot; |
| UNKNOWN | &quot;unknown&quot; |
| PAGER | &quot;pager&quot; |
| NULL | &quot;null&quot; |




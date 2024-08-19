

# NetworkFeaturePartial

Polymorphic Network Feature

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressFamilies** | [**List&lt;AddressFamiliesEnum&gt;**](#List&lt;AddressFamiliesEnum&gt;) | When creating a route server feature config, remember to specify which address family or families to use:  If the route server network feature only supports &#x60;af_inet&#x60;, then the &#x60;as_set_v4&#x60; in the network feature config is required.  If only &#x60;af_inet6&#x60; is supported, then the &#x60;as_set_v6&#x60; is required.  If both &#x60;af_inet&#x60; and &#x60;af_inet6&#x60; are supported, either &#x60;as_set_v4&#x60; or &#x60;as_set_v6&#x60; is required, but both can be provided in the network service config.  |  [optional] |
|**asn** | **Integer** |  |  [optional] |
|**availableBgpSessionTypes** | [**List&lt;AvailableBgpSessionTypesEnum&gt;**](#List&lt;AvailableBgpSessionTypesEnum&gt;) | The route server provides the following session modes.  |  [optional] |
|**flags** | [**List&lt;IXPSpecificFeatureFlag&gt;**](IXPSpecificFeatureFlag.md) | A list of IXP specific feature flags. This can be used to see if e.g. RPKI hard filtering is available. |  [optional] |
|**fqdn** | **String** | The FQDN of the route server.  |  [optional] |
|**id** | **String** |  |  [optional] |
|**ipV4** | **String** | IPv4 address in [dot-decimal notation](https://en.wikipedia.org/wiki/Dot-decimal_notation) notation.  |  [optional] |
|**ipV6** | **String** | IPv6 address in hexadecimal colon separated notation.  |  [optional] |
|**lookingGlassUrl** | **String** | The url of the looking glass.  |  [optional] |
|**name** | **String** |  |  [optional] |
|**networkService** | **String** |  |  [optional] |
|**nfcRequiredContactRoles** | **List&lt;String&gt;** | The configuration will require at least one of each of the specified roles assigned to contacts.  The role assignments is associated with the network feature config through the &#x60;role_assignments&#x60; list property. |  [optional] [readonly] |
|**required** | **Boolean** |  |  [optional] |
|**sessionMode** | [**SessionModeEnum**](#SessionModeEnum) | When creating a route server feature config, remember to specify the same session_mode as the route server.  |  [optional] |
|**type** | **String** |  |  |



## Enum: List&lt;AddressFamiliesEnum&gt;

| Name | Value |
|---- | -----|
| INET | &quot;af_inet&quot; |
| INET6 | &quot;af_inet6&quot; |



## Enum: List&lt;AvailableBgpSessionTypesEnum&gt;

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PASSIVE | &quot;passive&quot; |



## Enum: SessionModeEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;public&quot; |
| COLLECTOR | &quot;collector&quot; |




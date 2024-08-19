

# AdUnitMapping

Settings to map an AdMob ad unit to a 3rd party ad unit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adUnitConfigurations** | **Map&lt;String, String&gt;** | Settings for the specified ad unit to make an ad request to 3rd party ad network. Key-value pairs with values set by the user for the keys requested by the ad network. Please see https://support.google.com/admob/answer/3245073 for details on how to configure the network settings. |  [optional] |
|**adapterId** | **String** | The ID of mediation ad source adapter used by this ad unit mapping. The adapter determines the information needed in the ad_network_settings. |  [optional] |
|**displayName** | **String** | Optional. The display name of this ad unit mapping instance. |  [optional] |
|**name** | **String** | Resource name of this ad unit mapping. Format is: accounts/{publisher_id}/adUnits/{ad_unit_id_fragment}/adUnitMappings/{ad_unit_mapping_id} Example: accounts/pub-1234567890123456/adUnits/0123456789/adUnitMappings/987654321 |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The status of this ad unit mapping. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ENABLED | &quot;ENABLED&quot; |




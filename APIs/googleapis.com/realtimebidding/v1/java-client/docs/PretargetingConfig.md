

# PretargetingConfig

Pretargeting configuration: a set of targeting dimensions applied at the pretargeting stage of the RTB funnel. These control which inventory a bidder will receive bid requests for.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedUserTargetingModes** | [**List&lt;AllowedUserTargetingModesEnum&gt;**](#List&lt;AllowedUserTargetingModesEnum&gt;) | Targeting modes included by this configuration. A bid request must allow all the specified targeting modes. An unset value allows all bid requests to be sent, regardless of which targeting modes they allow. |  [optional] |
|**appTargeting** | [**AppTargeting**](AppTargeting.md) |  |  [optional] |
|**billingId** | **String** | Output only. The identifier that corresponds to this pretargeting configuration that helps buyers track and attribute their spend across their own arbitrary divisions. If a bid request matches more than one configuration, the buyer chooses which billing_id to attribute each of their bids. |  [optional] [readonly] |
|**displayName** | **String** | The diplay name associated with this configuration. This name must be unique among all the pretargeting configurations a bidder has. |  [optional] |
|**excludedContentLabelIds** | **List&lt;String&gt;** | The sensitive content category label IDs excluded in this configuration. Bid requests for inventory with any of the specified content label IDs will not be sent. Refer to this file https://storage.googleapis.com/adx-rtb-dictionaries/content-labels.txt for category IDs. |  [optional] |
|**geoTargeting** | [**NumericTargetingDimension**](NumericTargetingDimension.md) |  |  [optional] |
|**includedCreativeDimensions** | [**List&lt;CreativeDimensions&gt;**](CreativeDimensions.md) | Creative dimensions included by this configuration. Only bid requests eligible for at least one of the specified creative dimensions will be sent. An unset value allows all bid requests to be sent, regardless of creative dimension. |  [optional] |
|**includedEnvironments** | [**List&lt;IncludedEnvironmentsEnum&gt;**](#List&lt;IncludedEnvironmentsEnum&gt;) | Environments that are being included. Bid requests will not be sent for a given environment if it is not included. Further restrictions can be applied to included environments to target only a subset of its inventory. An unset value includes all environments. |  [optional] |
|**includedFormats** | [**List&lt;IncludedFormatsEnum&gt;**](#List&lt;IncludedFormatsEnum&gt;) | Creative formats included by this configuration. Only bid requests eligible for at least one of the specified creative formats will be sent. An unset value will allow all bid requests to be sent, regardless of format. |  [optional] |
|**includedLanguages** | **List&lt;String&gt;** | The languages included in this configuration, represented by their language code. See https://developers.google.com/adwords/api/docs/appendix/languagecodes. |  [optional] |
|**includedMobileOperatingSystemIds** | **List&lt;String&gt;** | The mobile operating systems included in this configuration as defined in https://storage.googleapis.com/adx-rtb-dictionaries/mobile-os.csv |  [optional] |
|**includedPlatforms** | [**List&lt;IncludedPlatformsEnum&gt;**](#List&lt;IncludedPlatformsEnum&gt;) | The platforms included by this configration. Bid requests for devices with the specified platform types will be sent. An unset value allows all bid requests to be sent, regardless of platform. |  [optional] |
|**includedUserIdTypes** | [**List&lt;IncludedUserIdTypesEnum&gt;**](#List&lt;IncludedUserIdTypesEnum&gt;) | User identifier types included in this configuration. At least one of the user identifier types specified in this list must be available for the bid request to be sent. |  [optional] |
|**interstitialTargeting** | [**InterstitialTargetingEnum**](#InterstitialTargetingEnum) | The interstitial targeting specified for this configuration. The unset value will allow bid requests to be sent regardless of whether they are for interstitials or not. |  [optional] |
|**invalidGeoIds** | **List&lt;String&gt;** | Output only. Existing included or excluded geos that are invalid. Previously targeted geos may become invalid due to privacy restrictions. |  [optional] [readonly] |
|**maximumQps** | **String** | The maximum QPS threshold for this configuration. The bidder should receive no more than this number of bid requests matching this configuration per second across all their bidding endpoints among all trading locations. Further information available at https://developers.google.com/authorized-buyers/rtb/peer-guide |  [optional] |
|**minimumViewabilityDecile** | **Integer** | The targeted minimum viewability decile, ranging in values [0, 10]. A value of 5 means that the configuration will only match adslots for which we predict at least 50% viewability. Values &gt; 10 will be rounded down to 10. An unset value or a value of 0 indicates that bid requests will be sent regardless of viewability. |  [optional] |
|**name** | **String** | Output only. Name of the pretargeting configuration that must follow the pattern &#x60;bidders/{bidder_account_id}/pretargetingConfigs/{config_id}&#x60; |  [optional] [readonly] |
|**publisherTargeting** | [**StringTargetingDimension**](StringTargetingDimension.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of this pretargeting configuration. |  [optional] [readonly] |
|**userListTargeting** | [**NumericTargetingDimension**](NumericTargetingDimension.md) |  |  [optional] |
|**verticalTargeting** | [**NumericTargetingDimension**](NumericTargetingDimension.md) |  |  [optional] |
|**webTargeting** | [**StringTargetingDimension**](StringTargetingDimension.md) |  |  [optional] |



## Enum: List&lt;AllowedUserTargetingModesEnum&gt;

| Name | Value |
|---- | -----|
| USER_TARGETING_MODE_UNSPECIFIED | &quot;USER_TARGETING_MODE_UNSPECIFIED&quot; |
| REMARKETING_ADS | &quot;REMARKETING_ADS&quot; |
| INTEREST_BASED_TARGETING | &quot;INTEREST_BASED_TARGETING&quot; |



## Enum: List&lt;IncludedEnvironmentsEnum&gt;

| Name | Value |
|---- | -----|
| ENVIRONMENT_UNSPECIFIED | &quot;ENVIRONMENT_UNSPECIFIED&quot; |
| APP | &quot;APP&quot; |
| WEB | &quot;WEB&quot; |



## Enum: List&lt;IncludedFormatsEnum&gt;

| Name | Value |
|---- | -----|
| CREATIVE_FORMAT_UNSPECIFIED | &quot;CREATIVE_FORMAT_UNSPECIFIED&quot; |
| HTML | &quot;HTML&quot; |
| VAST | &quot;VAST&quot; |
| NATIVE | &quot;NATIVE&quot; |



## Enum: List&lt;IncludedPlatformsEnum&gt;

| Name | Value |
|---- | -----|
| PLATFORM_UNSPECIFIED | &quot;PLATFORM_UNSPECIFIED&quot; |
| PERSONAL_COMPUTER | &quot;PERSONAL_COMPUTER&quot; |
| PHONE | &quot;PHONE&quot; |
| TABLET | &quot;TABLET&quot; |
| CONNECTED_TV | &quot;CONNECTED_TV&quot; |



## Enum: List&lt;IncludedUserIdTypesEnum&gt;

| Name | Value |
|---- | -----|
| USER_ID_TYPE_UNSPECIFIED | &quot;USER_ID_TYPE_UNSPECIFIED&quot; |
| HOSTED_MATCH_DATA | &quot;HOSTED_MATCH_DATA&quot; |
| GOOGLE_COOKIE | &quot;GOOGLE_COOKIE&quot; |
| DEVICE_ID | &quot;DEVICE_ID&quot; |



## Enum: InterstitialTargetingEnum

| Name | Value |
|---- | -----|
| INTERSTITIAL_TARGETING_UNSPECIFIED | &quot;INTERSTITIAL_TARGETING_UNSPECIFIED&quot; |
| ONLY_INTERSTITIAL_REQUESTS | &quot;ONLY_INTERSTITIAL_REQUESTS&quot; |
| ONLY_NON_INTERSTITIAL_REQUESTS | &quot;ONLY_NON_INTERSTITIAL_REQUESTS&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| SUSPENDED | &quot;SUSPENDED&quot; |






# MediationGroupTargeting

Set of criteria targeted by this mediation group. For example, a mediation group can target specific ad unit IDs, platform, format and geo location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adUnitIds** | **List&lt;String&gt;** | Ad units targeted by this mediation group. Example: \&quot;ca-app-pub-1234/8790\&quot;. |  [optional] |
|**excludedRegionCodes** | **List&lt;String&gt;** | The Unicode country/region code (CLDR) of a location, such as \&quot;US\&quot;. Unset if this mediation group does not exclude any region. |  [optional] |
|**format** | **String** | Ad format targeted by this mediation group. Examples: \&quot;banner\&quot;, \&quot;native\&quot;. |  [optional] |
|**idfaTargeting** | [**IdfaTargetingEnum**](#IdfaTargetingEnum) | The parameter can be used to target ad requests based on the availability of the IDFA. If set to ALL, the mediation group applies to all ad requests (with or without IDFA). If set to AVAILABLE, the mediation group applies to ad requests with IDFA. If set to NOT_AVAILABLE, the mediation group applies to ad requests without IDFA. Doesn&#39;t need to be specified for an ANDROID device. |  [optional] |
|**platform** | **String** | Describes the platform of the app. Examples: \&quot;IOS\&quot;, \&quot;Android\&quot;. |  [optional] |
|**targetedRegionCodes** | **List&lt;String&gt;** | The Unicode country/region code (CLDR) of a location, such as \&quot;US\&quot;. Unset if this mediation group targets all available regions. For more information, see http://www.unicode.org/reports/tr35/#unicode_region_subtag. |  [optional] |



## Enum: IdfaTargetingEnum

| Name | Value |
|---- | -----|
| IDFA_TARGETING_UNSPECIFIED | &quot;IDFA_TARGETING_UNSPECIFIED&quot; |
| ALL | &quot;ALL&quot; |
| AVAILABLE | &quot;AVAILABLE&quot; |
| NOT_AVAILABLE | &quot;NOT_AVAILABLE&quot; |




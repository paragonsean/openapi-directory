# AdMobApi.MediationGroupTargeting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adUnitIds** | **[String]** | Ad units targeted by this mediation group. Example: \&quot;ca-app-pub-1234/8790\&quot;. | [optional] 
**excludedRegionCodes** | **[String]** | The Unicode country/region code (CLDR) of a location, such as \&quot;US\&quot;. Unset if this mediation group does not exclude any region. | [optional] 
**format** | **String** | Ad format targeted by this mediation group. Examples: \&quot;banner\&quot;, \&quot;native\&quot;. | [optional] 
**idfaTargeting** | **String** | The parameter can be used to target ad requests based on the availability of the IDFA. If set to ALL, the mediation group applies to all ad requests (with or without IDFA). If set to AVAILABLE, the mediation group applies to ad requests with IDFA. If set to NOT_AVAILABLE, the mediation group applies to ad requests without IDFA. Doesn&#39;t need to be specified for an ANDROID device. | [optional] 
**platform** | **String** | Describes the platform of the app. Examples: \&quot;IOS\&quot;, \&quot;Android\&quot;. | [optional] 
**targetedRegionCodes** | **[String]** | The Unicode country/region code (CLDR) of a location, such as \&quot;US\&quot;. Unset if this mediation group targets all available regions. For more information, see http://www.unicode.org/reports/tr35/#unicode_region_subtag. | [optional] 



## Enum: IdfaTargetingEnum


* `IDFA_TARGETING_UNSPECIFIED` (value: `"IDFA_TARGETING_UNSPECIFIED"`)

* `ALL` (value: `"ALL"`)

* `AVAILABLE` (value: `"AVAILABLE"`)

* `NOT_AVAILABLE` (value: `"NOT_AVAILABLE"`)





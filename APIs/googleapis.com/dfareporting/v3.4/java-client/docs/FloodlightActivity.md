

# FloodlightActivity

Contains properties of a Floodlight activity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | Account ID of this floodlight activity. This is a read-only field that can be left blank. |  [optional] |
|**advertiserId** | **String** | Advertiser ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group&#39;s advertiser or the existing activity&#39;s advertiser. |  [optional] |
|**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**attributionEnabled** | **Boolean** | Whether the activity is enabled for attribution. |  [optional] |
|**cacheBustingType** | [**CacheBustingTypeEnum**](#CacheBustingTypeEnum) | Code type used for cache busting in the generated tag. Applicable only when floodlightActivityGroupType is COUNTER and countingMethod is STANDARD_COUNTING or UNIQUE_COUNTING. |  [optional] |
|**countingMethod** | [**CountingMethodEnum**](#CountingMethodEnum) | Counting method for conversions for this floodlight activity. This is a required field. |  [optional] |
|**defaultTags** | [**List&lt;FloodlightActivityDynamicTag&gt;**](FloodlightActivityDynamicTag.md) | Dynamic floodlight tags. |  [optional] |
|**expectedUrl** | **String** | URL where this tag will be deployed. If specified, must be less than 256 characters long. |  [optional] |
|**floodlightActivityGroupId** | **String** | Floodlight activity group ID of this floodlight activity. This is a required field. |  [optional] |
|**floodlightActivityGroupName** | **String** | Name of the associated floodlight activity group. This is a read-only field. |  [optional] |
|**floodlightActivityGroupTagString** | **String** | Tag string of the associated floodlight activity group. This is a read-only field. |  [optional] |
|**floodlightActivityGroupType** | [**FloodlightActivityGroupTypeEnum**](#FloodlightActivityGroupTypeEnum) | Type of the associated floodlight activity group. This is a read-only field. |  [optional] |
|**floodlightConfigurationId** | **String** | Floodlight configuration ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group&#39;s floodlight configuration or from the existing activity&#39;s floodlight configuration. |  [optional] |
|**floodlightConfigurationIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**floodlightTagType** | [**FloodlightTagTypeEnum**](#FloodlightTagTypeEnum) | The type of Floodlight tag this activity will generate. This is a required field. |  [optional] |
|**id** | **String** | ID of this floodlight activity. This is a read-only, auto-generated field. |  [optional] |
|**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#floodlightActivity\&quot;. |  [optional] |
|**name** | **String** | Name of this floodlight activity. This is a required field. Must be less than 129 characters long and cannot contain quotes. |  [optional] |
|**notes** | **String** | General notes or implementation instructions for the tag. |  [optional] |
|**publisherTags** | [**List&lt;FloodlightActivityPublisherDynamicTag&gt;**](FloodlightActivityPublisherDynamicTag.md) | Publisher dynamic floodlight tags. |  [optional] |
|**secure** | **Boolean** | Whether this tag should use SSL. |  [optional] |
|**sslCompliant** | **Boolean** | Whether the floodlight activity is SSL-compliant. This is a read-only field, its value detected by the system from the floodlight tags. |  [optional] |
|**sslRequired** | **Boolean** | Whether this floodlight activity must be SSL-compliant. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the activity. This can only be set to ACTIVE or ARCHIVED_AND_DISABLED. The ARCHIVED status is no longer supported and cannot be set for Floodlight activities. The DISABLED_POLICY status indicates that a Floodlight activity is violating Google policy. Contact your account manager for more information. |  [optional] |
|**subaccountId** | **String** | Subaccount ID of this floodlight activity. This is a read-only field that can be left blank. |  [optional] |
|**tagFormat** | [**TagFormatEnum**](#TagFormatEnum) | Tag format type for the floodlight activity. If left blank, the tag format will default to HTML. |  [optional] |
|**tagString** | **String** | Value of the cat&#x3D; parameter in the floodlight tag, which the ad servers use to identify the activity. This is optional: if empty, a new tag string will be generated for you. This string must be 1 to 8 characters long, with valid characters being a-z0-9[ _ ]. This tag string must also be unique among activities of the same activity group. This field is read-only after insertion. |  [optional] |
|**userDefinedVariableTypes** | [**List&lt;UserDefinedVariableTypesEnum&gt;**](#List&lt;UserDefinedVariableTypesEnum&gt;) | List of the user-defined variables used by this conversion tag. These map to the \&quot;u[1-100]&#x3D;\&quot; in the tags. Each of these can have a user defined type. Acceptable values are U1 to U100, inclusive.  |  [optional] |



## Enum: CacheBustingTypeEnum

| Name | Value |
|---- | -----|
| JAVASCRIPT | &quot;JAVASCRIPT&quot; |
| ACTIVE_SERVER_PAGE | &quot;ACTIVE_SERVER_PAGE&quot; |
| JSP | &quot;JSP&quot; |
| PHP | &quot;PHP&quot; |
| COLD_FUSION | &quot;COLD_FUSION&quot; |



## Enum: CountingMethodEnum

| Name | Value |
|---- | -----|
| STANDARD_COUNTING | &quot;STANDARD_COUNTING&quot; |
| UNIQUE_COUNTING | &quot;UNIQUE_COUNTING&quot; |
| SESSION_COUNTING | &quot;SESSION_COUNTING&quot; |
| TRANSACTIONS_COUNTING | &quot;TRANSACTIONS_COUNTING&quot; |
| ITEMS_SOLD_COUNTING | &quot;ITEMS_SOLD_COUNTING&quot; |



## Enum: FloodlightActivityGroupTypeEnum

| Name | Value |
|---- | -----|
| COUNTER | &quot;COUNTER&quot; |
| SALE | &quot;SALE&quot; |



## Enum: FloodlightTagTypeEnum

| Name | Value |
|---- | -----|
| IFRAME | &quot;IFRAME&quot; |
| IMAGE | &quot;IMAGE&quot; |
| GLOBAL_SITE_TAG | &quot;GLOBAL_SITE_TAG&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;ACTIVE&quot; |
| ARCHIVED_AND_DISABLED | &quot;ARCHIVED_AND_DISABLED&quot; |
| ARCHIVED | &quot;ARCHIVED&quot; |
| DISABLED_POLICY | &quot;DISABLED_POLICY&quot; |



## Enum: TagFormatEnum

| Name | Value |
|---- | -----|
| HTML | &quot;HTML&quot; |
| XHTML | &quot;XHTML&quot; |



## Enum: List&lt;UserDefinedVariableTypesEnum&gt;

| Name | Value |
|---- | -----|
| U1 | &quot;U1&quot; |
| U2 | &quot;U2&quot; |
| U3 | &quot;U3&quot; |
| U4 | &quot;U4&quot; |
| U5 | &quot;U5&quot; |
| U6 | &quot;U6&quot; |
| U7 | &quot;U7&quot; |
| U8 | &quot;U8&quot; |
| U9 | &quot;U9&quot; |
| U10 | &quot;U10&quot; |
| U11 | &quot;U11&quot; |
| U12 | &quot;U12&quot; |
| U13 | &quot;U13&quot; |
| U14 | &quot;U14&quot; |
| U15 | &quot;U15&quot; |
| U16 | &quot;U16&quot; |
| U17 | &quot;U17&quot; |
| U18 | &quot;U18&quot; |
| U19 | &quot;U19&quot; |
| U20 | &quot;U20&quot; |
| U21 | &quot;U21&quot; |
| U22 | &quot;U22&quot; |
| U23 | &quot;U23&quot; |
| U24 | &quot;U24&quot; |
| U25 | &quot;U25&quot; |
| U26 | &quot;U26&quot; |
| U27 | &quot;U27&quot; |
| U28 | &quot;U28&quot; |
| U29 | &quot;U29&quot; |
| U30 | &quot;U30&quot; |
| U31 | &quot;U31&quot; |
| U32 | &quot;U32&quot; |
| U33 | &quot;U33&quot; |
| U34 | &quot;U34&quot; |
| U35 | &quot;U35&quot; |
| U36 | &quot;U36&quot; |
| U37 | &quot;U37&quot; |
| U38 | &quot;U38&quot; |
| U39 | &quot;U39&quot; |
| U40 | &quot;U40&quot; |
| U41 | &quot;U41&quot; |
| U42 | &quot;U42&quot; |
| U43 | &quot;U43&quot; |
| U44 | &quot;U44&quot; |
| U45 | &quot;U45&quot; |
| U46 | &quot;U46&quot; |
| U47 | &quot;U47&quot; |
| U48 | &quot;U48&quot; |
| U49 | &quot;U49&quot; |
| U50 | &quot;U50&quot; |
| U51 | &quot;U51&quot; |
| U52 | &quot;U52&quot; |
| U53 | &quot;U53&quot; |
| U54 | &quot;U54&quot; |
| U55 | &quot;U55&quot; |
| U56 | &quot;U56&quot; |
| U57 | &quot;U57&quot; |
| U58 | &quot;U58&quot; |
| U59 | &quot;U59&quot; |
| U60 | &quot;U60&quot; |
| U61 | &quot;U61&quot; |
| U62 | &quot;U62&quot; |
| U63 | &quot;U63&quot; |
| U64 | &quot;U64&quot; |
| U65 | &quot;U65&quot; |
| U66 | &quot;U66&quot; |
| U67 | &quot;U67&quot; |
| U68 | &quot;U68&quot; |
| U69 | &quot;U69&quot; |
| U70 | &quot;U70&quot; |
| U71 | &quot;U71&quot; |
| U72 | &quot;U72&quot; |
| U73 | &quot;U73&quot; |
| U74 | &quot;U74&quot; |
| U75 | &quot;U75&quot; |
| U76 | &quot;U76&quot; |
| U77 | &quot;U77&quot; |
| U78 | &quot;U78&quot; |
| U79 | &quot;U79&quot; |
| U80 | &quot;U80&quot; |
| U81 | &quot;U81&quot; |
| U82 | &quot;U82&quot; |
| U83 | &quot;U83&quot; |
| U84 | &quot;U84&quot; |
| U85 | &quot;U85&quot; |
| U86 | &quot;U86&quot; |
| U87 | &quot;U87&quot; |
| U88 | &quot;U88&quot; |
| U89 | &quot;U89&quot; |
| U90 | &quot;U90&quot; |
| U91 | &quot;U91&quot; |
| U92 | &quot;U92&quot; |
| U93 | &quot;U93&quot; |
| U94 | &quot;U94&quot; |
| U95 | &quot;U95&quot; |
| U96 | &quot;U96&quot; |
| U97 | &quot;U97&quot; |
| U98 | &quot;U98&quot; |
| U99 | &quot;U99&quot; |
| U100 | &quot;U100&quot; |




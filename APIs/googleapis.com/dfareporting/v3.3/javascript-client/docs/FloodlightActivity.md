# CampaignManager360Api.FloodlightActivity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this floodlight activity. This is a read-only field that can be left blank. | [optional] 
**advertiserId** | **String** | Advertiser ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group&#39;s advertiser or the existing activity&#39;s advertiser. | [optional] 
**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**cacheBustingType** | **String** | Code type used for cache busting in the generated tag. Applicable only when floodlightActivityGroupType is COUNTER and countingMethod is STANDARD_COUNTING or UNIQUE_COUNTING. | [optional] 
**countingMethod** | **String** | Counting method for conversions for this floodlight activity. This is a required field. | [optional] 
**defaultTags** | [**[FloodlightActivityDynamicTag]**](FloodlightActivityDynamicTag.md) | Dynamic floodlight tags. | [optional] 
**expectedUrl** | **String** | URL where this tag will be deployed. If specified, must be less than 256 characters long. | [optional] 
**floodlightActivityGroupId** | **String** | Floodlight activity group ID of this floodlight activity. This is a required field. | [optional] 
**floodlightActivityGroupName** | **String** | Name of the associated floodlight activity group. This is a read-only field. | [optional] 
**floodlightActivityGroupTagString** | **String** | Tag string of the associated floodlight activity group. This is a read-only field. | [optional] 
**floodlightActivityGroupType** | **String** | Type of the associated floodlight activity group. This is a read-only field. | [optional] 
**floodlightConfigurationId** | **String** | Floodlight configuration ID of this floodlight activity. If this field is left blank, the value will be copied over either from the activity group&#39;s floodlight configuration or from the existing activity&#39;s floodlight configuration. | [optional] 
**floodlightConfigurationIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**floodlightTagType** | **String** | The type of Floodlight tag this activity will generate. This is a required field. | [optional] 
**hidden** | **Boolean** | Whether this activity is archived. | [optional] 
**id** | **String** | ID of this floodlight activity. This is a read-only, auto-generated field. | [optional] 
**idDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#floodlightActivity\&quot;. | [optional] 
**name** | **String** | Name of this floodlight activity. This is a required field. Must be less than 129 characters long and cannot contain quotes. | [optional] 
**notes** | **String** | General notes or implementation instructions for the tag. | [optional] 
**publisherTags** | [**[FloodlightActivityPublisherDynamicTag]**](FloodlightActivityPublisherDynamicTag.md) | Publisher dynamic floodlight tags. | [optional] 
**secure** | **Boolean** | Whether this tag should use SSL. | [optional] 
**sslCompliant** | **Boolean** | Whether the floodlight activity is SSL-compliant. This is a read-only field, its value detected by the system from the floodlight tags. | [optional] 
**sslRequired** | **Boolean** | Whether this floodlight activity must be SSL-compliant. | [optional] 
**subaccountId** | **String** | Subaccount ID of this floodlight activity. This is a read-only field that can be left blank. | [optional] 
**tagFormat** | **String** | Tag format type for the floodlight activity. If left blank, the tag format will default to HTML. | [optional] 
**tagString** | **String** | Value of the cat&#x3D; parameter in the floodlight tag, which the ad servers use to identify the activity. This is optional: if empty, a new tag string will be generated for you. This string must be 1 to 8 characters long, with valid characters being a-z0-9[ _ ]. This tag string must also be unique among activities of the same activity group. This field is read-only after insertion. | [optional] 
**userDefinedVariableTypes** | **[String]** | List of the user-defined variables used by this conversion tag. These map to the \&quot;u[1-100]&#x3D;\&quot; in the tags. Each of these can have a user defined type. Acceptable values are U1 to U100, inclusive.  | [optional] 



## Enum: CacheBustingTypeEnum


* `JAVASCRIPT` (value: `"JAVASCRIPT"`)

* `ACTIVE_SERVER_PAGE` (value: `"ACTIVE_SERVER_PAGE"`)

* `JSP` (value: `"JSP"`)

* `PHP` (value: `"PHP"`)

* `COLD_FUSION` (value: `"COLD_FUSION"`)





## Enum: CountingMethodEnum


* `STANDARD_COUNTING` (value: `"STANDARD_COUNTING"`)

* `UNIQUE_COUNTING` (value: `"UNIQUE_COUNTING"`)

* `SESSION_COUNTING` (value: `"SESSION_COUNTING"`)

* `TRANSACTIONS_COUNTING` (value: `"TRANSACTIONS_COUNTING"`)

* `ITEMS_SOLD_COUNTING` (value: `"ITEMS_SOLD_COUNTING"`)





## Enum: FloodlightActivityGroupTypeEnum


* `COUNTER` (value: `"COUNTER"`)

* `SALE` (value: `"SALE"`)





## Enum: FloodlightTagTypeEnum


* `IFRAME` (value: `"IFRAME"`)

* `IMAGE` (value: `"IMAGE"`)

* `GLOBAL_SITE_TAG` (value: `"GLOBAL_SITE_TAG"`)





## Enum: TagFormatEnum


* `HTML` (value: `"HTML"`)

* `XHTML` (value: `"XHTML"`)





## Enum: [UserDefinedVariableTypesEnum]


* `U1` (value: `"U1"`)

* `U2` (value: `"U2"`)

* `U3` (value: `"U3"`)

* `U4` (value: `"U4"`)

* `U5` (value: `"U5"`)

* `U6` (value: `"U6"`)

* `U7` (value: `"U7"`)

* `U8` (value: `"U8"`)

* `U9` (value: `"U9"`)

* `U10` (value: `"U10"`)

* `U11` (value: `"U11"`)

* `U12` (value: `"U12"`)

* `U13` (value: `"U13"`)

* `U14` (value: `"U14"`)

* `U15` (value: `"U15"`)

* `U16` (value: `"U16"`)

* `U17` (value: `"U17"`)

* `U18` (value: `"U18"`)

* `U19` (value: `"U19"`)

* `U20` (value: `"U20"`)

* `U21` (value: `"U21"`)

* `U22` (value: `"U22"`)

* `U23` (value: `"U23"`)

* `U24` (value: `"U24"`)

* `U25` (value: `"U25"`)

* `U26` (value: `"U26"`)

* `U27` (value: `"U27"`)

* `U28` (value: `"U28"`)

* `U29` (value: `"U29"`)

* `U30` (value: `"U30"`)

* `U31` (value: `"U31"`)

* `U32` (value: `"U32"`)

* `U33` (value: `"U33"`)

* `U34` (value: `"U34"`)

* `U35` (value: `"U35"`)

* `U36` (value: `"U36"`)

* `U37` (value: `"U37"`)

* `U38` (value: `"U38"`)

* `U39` (value: `"U39"`)

* `U40` (value: `"U40"`)

* `U41` (value: `"U41"`)

* `U42` (value: `"U42"`)

* `U43` (value: `"U43"`)

* `U44` (value: `"U44"`)

* `U45` (value: `"U45"`)

* `U46` (value: `"U46"`)

* `U47` (value: `"U47"`)

* `U48` (value: `"U48"`)

* `U49` (value: `"U49"`)

* `U50` (value: `"U50"`)

* `U51` (value: `"U51"`)

* `U52` (value: `"U52"`)

* `U53` (value: `"U53"`)

* `U54` (value: `"U54"`)

* `U55` (value: `"U55"`)

* `U56` (value: `"U56"`)

* `U57` (value: `"U57"`)

* `U58` (value: `"U58"`)

* `U59` (value: `"U59"`)

* `U60` (value: `"U60"`)

* `U61` (value: `"U61"`)

* `U62` (value: `"U62"`)

* `U63` (value: `"U63"`)

* `U64` (value: `"U64"`)

* `U65` (value: `"U65"`)

* `U66` (value: `"U66"`)

* `U67` (value: `"U67"`)

* `U68` (value: `"U68"`)

* `U69` (value: `"U69"`)

* `U70` (value: `"U70"`)

* `U71` (value: `"U71"`)

* `U72` (value: `"U72"`)

* `U73` (value: `"U73"`)

* `U74` (value: `"U74"`)

* `U75` (value: `"U75"`)

* `U76` (value: `"U76"`)

* `U77` (value: `"U77"`)

* `U78` (value: `"U78"`)

* `U79` (value: `"U79"`)

* `U80` (value: `"U80"`)

* `U81` (value: `"U81"`)

* `U82` (value: `"U82"`)

* `U83` (value: `"U83"`)

* `U84` (value: `"U84"`)

* `U85` (value: `"U85"`)

* `U86` (value: `"U86"`)

* `U87` (value: `"U87"`)

* `U88` (value: `"U88"`)

* `U89` (value: `"U89"`)

* `U90` (value: `"U90"`)

* `U91` (value: `"U91"`)

* `U92` (value: `"U92"`)

* `U93` (value: `"U93"`)

* `U94` (value: `"U94"`)

* `U95` (value: `"U95"`)

* `U96` (value: `"U96"`)

* `U97` (value: `"U97"`)

* `U98` (value: `"U98"`)

* `U99` (value: `"U99"`)

* `U100` (value: `"U100"`)





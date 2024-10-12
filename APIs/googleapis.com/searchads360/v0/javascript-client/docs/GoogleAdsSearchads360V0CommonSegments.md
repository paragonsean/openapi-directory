# SearchAds360ReportingApi.GoogleAdsSearchads360V0CommonSegments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adNetworkType** | **String** | Ad network type. | [optional] 
**assetInteractionTarget** | [**GoogleAdsSearchads360V0CommonAssetInteractionTarget**](GoogleAdsSearchads360V0CommonAssetInteractionTarget.md) |  | [optional] 
**conversionAction** | **String** | Resource name of the conversion action. | [optional] 
**conversionActionCategory** | **String** | Conversion action category. | [optional] 
**conversionActionName** | **String** | Conversion action name. | [optional] 
**conversionCustomDimensions** | [**[GoogleAdsSearchads360V0CommonValue]**](GoogleAdsSearchads360V0CommonValue.md) | The conversion custom dimensions. | [optional] 
**date** | **String** | Date to which metrics apply. yyyy-MM-dd format, for example, 2018-04-17. | [optional] 
**dayOfWeek** | **String** | Day of the week, for example, MONDAY. | [optional] 
**device** | **String** | Device to which metrics apply. | [optional] 
**keyword** | [**GoogleAdsSearchads360V0CommonKeyword**](GoogleAdsSearchads360V0CommonKeyword.md) |  | [optional] 
**month** | **String** | Month as represented by the date of the first day of a month. Formatted as yyyy-MM-dd. | [optional] 
**productBiddingCategoryLevel1** | **String** | Bidding category (level 1) of the product. | [optional] 
**productBiddingCategoryLevel2** | **String** | Bidding category (level 2) of the product. | [optional] 
**productBiddingCategoryLevel3** | **String** | Bidding category (level 3) of the product. | [optional] 
**productBiddingCategoryLevel4** | **String** | Bidding category (level 4) of the product. | [optional] 
**productBiddingCategoryLevel5** | **String** | Bidding category (level 5) of the product. | [optional] 
**productBrand** | **String** | Brand of the product. | [optional] 
**productChannel** | **String** | Channel of the product. | [optional] 
**productChannelExclusivity** | **String** | Channel exclusivity of the product. | [optional] 
**productCondition** | **String** | Condition of the product. | [optional] 
**productCountry** | **String** | Resource name of the geo target constant for the country of sale of the product. | [optional] 
**productCustomAttribute0** | **String** | Custom attribute 0 of the product. | [optional] 
**productCustomAttribute1** | **String** | Custom attribute 1 of the product. | [optional] 
**productCustomAttribute2** | **String** | Custom attribute 2 of the product. | [optional] 
**productCustomAttribute3** | **String** | Custom attribute 3 of the product. | [optional] 
**productCustomAttribute4** | **String** | Custom attribute 4 of the product. | [optional] 
**productItemId** | **String** | Item ID of the product. | [optional] 
**productLanguage** | **String** | Resource name of the language constant for the language of the product. | [optional] 
**productSoldBiddingCategoryLevel1** | **String** | Bidding category (level 1) of the product sold. | [optional] 
**productSoldBiddingCategoryLevel2** | **String** | Bidding category (level 2) of the product sold. | [optional] 
**productSoldBiddingCategoryLevel3** | **String** | Bidding category (level 3) of the product sold. | [optional] 
**productSoldBiddingCategoryLevel4** | **String** | Bidding category (level 4) of the product sold. | [optional] 
**productSoldBiddingCategoryLevel5** | **String** | Bidding category (level 5) of the product sold. | [optional] 
**productSoldBrand** | **String** | Brand of the product sold. | [optional] 
**productSoldCondition** | **String** | Condition of the product sold. | [optional] 
**productSoldCustomAttribute0** | **String** | Custom attribute 0 of the product sold. | [optional] 
**productSoldCustomAttribute1** | **String** | Custom attribute 1 of the product sold. | [optional] 
**productSoldCustomAttribute2** | **String** | Custom attribute 2 of the product sold. | [optional] 
**productSoldCustomAttribute3** | **String** | Custom attribute 3 of the product sold. | [optional] 
**productSoldCustomAttribute4** | **String** | Custom attribute 4 of the product sold. | [optional] 
**productSoldItemId** | **String** | Item ID of the product sold. | [optional] 
**productSoldTitle** | **String** | Title of the product sold. | [optional] 
**productSoldTypeL1** | **String** | Type (level 1) of the product sold. | [optional] 
**productSoldTypeL2** | **String** | Type (level 2) of the product sold. | [optional] 
**productSoldTypeL3** | **String** | Type (level 3) of the product sold. | [optional] 
**productSoldTypeL4** | **String** | Type (level 4) of the product sold. | [optional] 
**productSoldTypeL5** | **String** | Type (level 5) of the product sold. | [optional] 
**productStoreId** | **String** | Store ID of the product. | [optional] 
**productTitle** | **String** | Title of the product. | [optional] 
**productTypeL1** | **String** | Type (level 1) of the product. | [optional] 
**productTypeL2** | **String** | Type (level 2) of the product. | [optional] 
**productTypeL3** | **String** | Type (level 3) of the product. | [optional] 
**productTypeL4** | **String** | Type (level 4) of the product. | [optional] 
**productTypeL5** | **String** | Type (level 5) of the product. | [optional] 
**quarter** | **String** | Quarter as represented by the date of the first day of a quarter. Uses the calendar year for quarters, for example, the second quarter of 2018 starts on 2018-04-01. Formatted as yyyy-MM-dd. | [optional] 
**rawEventConversionDimensions** | [**[GoogleAdsSearchads360V0CommonValue]**](GoogleAdsSearchads360V0CommonValue.md) | The raw event conversion dimensions. | [optional] 
**week** | **String** | Week as defined as Monday through Sunday, and represented by the date of Monday. Formatted as yyyy-MM-dd. | [optional] 
**year** | **Number** | Year, formatted as yyyy. | [optional] 



## Enum: AdNetworkTypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `SEARCH` (value: `"SEARCH"`)

* `SEARCH_PARTNERS` (value: `"SEARCH_PARTNERS"`)

* `CONTENT` (value: `"CONTENT"`)

* `YOUTUBE_SEARCH` (value: `"YOUTUBE_SEARCH"`)

* `YOUTUBE_WATCH` (value: `"YOUTUBE_WATCH"`)

* `MIXED` (value: `"MIXED"`)





## Enum: ConversionActionCategoryEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `DEFAULT` (value: `"DEFAULT"`)

* `PAGE_VIEW` (value: `"PAGE_VIEW"`)

* `PURCHASE` (value: `"PURCHASE"`)

* `SIGNUP` (value: `"SIGNUP"`)

* `LEAD` (value: `"LEAD"`)

* `DOWNLOAD` (value: `"DOWNLOAD"`)

* `ADD_TO_CART` (value: `"ADD_TO_CART"`)

* `BEGIN_CHECKOUT` (value: `"BEGIN_CHECKOUT"`)

* `SUBSCRIBE_PAID` (value: `"SUBSCRIBE_PAID"`)

* `PHONE_CALL_LEAD` (value: `"PHONE_CALL_LEAD"`)

* `IMPORTED_LEAD` (value: `"IMPORTED_LEAD"`)

* `SUBMIT_LEAD_FORM` (value: `"SUBMIT_LEAD_FORM"`)

* `BOOK_APPOINTMENT` (value: `"BOOK_APPOINTMENT"`)

* `REQUEST_QUOTE` (value: `"REQUEST_QUOTE"`)

* `GET_DIRECTIONS` (value: `"GET_DIRECTIONS"`)

* `OUTBOUND_CLICK` (value: `"OUTBOUND_CLICK"`)

* `CONTACT` (value: `"CONTACT"`)

* `ENGAGEMENT` (value: `"ENGAGEMENT"`)

* `STORE_VISIT` (value: `"STORE_VISIT"`)

* `STORE_SALE` (value: `"STORE_SALE"`)

* `QUALIFIED_LEAD` (value: `"QUALIFIED_LEAD"`)

* `CONVERTED_LEAD` (value: `"CONVERTED_LEAD"`)





## Enum: DayOfWeekEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `MONDAY` (value: `"MONDAY"`)

* `TUESDAY` (value: `"TUESDAY"`)

* `WEDNESDAY` (value: `"WEDNESDAY"`)

* `THURSDAY` (value: `"THURSDAY"`)

* `FRIDAY` (value: `"FRIDAY"`)

* `SATURDAY` (value: `"SATURDAY"`)

* `SUNDAY` (value: `"SUNDAY"`)





## Enum: DeviceEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `MOBILE` (value: `"MOBILE"`)

* `TABLET` (value: `"TABLET"`)

* `DESKTOP` (value: `"DESKTOP"`)

* `CONNECTED_TV` (value: `"CONNECTED_TV"`)

* `OTHER` (value: `"OTHER"`)





## Enum: ProductChannelEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ONLINE` (value: `"ONLINE"`)

* `LOCAL` (value: `"LOCAL"`)





## Enum: ProductChannelExclusivityEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `SINGLE_CHANNEL` (value: `"SINGLE_CHANNEL"`)

* `MULTI_CHANNEL` (value: `"MULTI_CHANNEL"`)





## Enum: ProductConditionEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `OLD` (value: `"OLD"`)

* `NEW` (value: `"NEW"`)

* `REFURBISHED` (value: `"REFURBISHED"`)

* `USED` (value: `"USED"`)





## Enum: ProductSoldConditionEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `OLD` (value: `"OLD"`)

* `NEW` (value: `"NEW"`)

* `REFURBISHED` (value: `"REFURBISHED"`)

* `USED` (value: `"USED"`)





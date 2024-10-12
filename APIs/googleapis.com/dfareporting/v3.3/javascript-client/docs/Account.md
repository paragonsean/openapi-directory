# CampaignManager360Api.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountPermissionIds** | **[String]** | Account permissions assigned to this account. | [optional] 
**accountProfile** | **String** | Profile for this account. This is a read-only field that can be left blank. | [optional] 
**active** | **Boolean** | Whether this account is active. | [optional] 
**activeAdsLimitTier** | **String** | Maximum number of active ads allowed for this account. | [optional] 
**activeViewOptOut** | **Boolean** | Whether to serve creatives with Active View tags. If disabled, viewability data will not be available for any impressions. | [optional] 
**availablePermissionIds** | **[String]** | User role permissions available to the user roles of this account. | [optional] 
**countryId** | **String** | ID of the country associated with this account. | [optional] 
**currencyId** | **String** | ID of currency associated with this account. This is a required field. Acceptable values are: - \&quot;1\&quot; for USD - \&quot;2\&quot; for GBP - \&quot;3\&quot; for ESP - \&quot;4\&quot; for SEK - \&quot;5\&quot; for CAD - \&quot;6\&quot; for JPY - \&quot;7\&quot; for DEM - \&quot;8\&quot; for AUD - \&quot;9\&quot; for FRF - \&quot;10\&quot; for ITL - \&quot;11\&quot; for DKK - \&quot;12\&quot; for NOK - \&quot;13\&quot; for FIM - \&quot;14\&quot; for ZAR - \&quot;15\&quot; for IEP - \&quot;16\&quot; for NLG - \&quot;17\&quot; for EUR - \&quot;18\&quot; for KRW - \&quot;19\&quot; for TWD - \&quot;20\&quot; for SGD - \&quot;21\&quot; for CNY - \&quot;22\&quot; for HKD - \&quot;23\&quot; for NZD - \&quot;24\&quot; for MYR - \&quot;25\&quot; for BRL - \&quot;26\&quot; for PTE - \&quot;28\&quot; for CLP - \&quot;29\&quot; for TRY - \&quot;30\&quot; for ARS - \&quot;31\&quot; for PEN - \&quot;32\&quot; for ILS - \&quot;33\&quot; for CHF - \&quot;34\&quot; for VEF - \&quot;35\&quot; for COP - \&quot;36\&quot; for GTQ - \&quot;37\&quot; for PLN - \&quot;39\&quot; for INR - \&quot;40\&quot; for THB - \&quot;41\&quot; for IDR - \&quot;42\&quot; for CZK - \&quot;43\&quot; for RON - \&quot;44\&quot; for HUF - \&quot;45\&quot; for RUB - \&quot;46\&quot; for AED - \&quot;47\&quot; for BGN - \&quot;48\&quot; for HRK - \&quot;49\&quot; for MXN - \&quot;50\&quot; for NGN - \&quot;51\&quot; for EGP  | [optional] 
**defaultCreativeSizeId** | **String** | Default placement dimensions for this account. | [optional] 
**description** | **String** | Description of this account. | [optional] 
**id** | **String** | ID of this account. This is a read-only, auto-generated field. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#account\&quot;. | [optional] 
**locale** | **String** | Locale of this account. Acceptable values are: - \&quot;cs\&quot; (Czech) - \&quot;de\&quot; (German) - \&quot;en\&quot; (English) - \&quot;en-GB\&quot; (English United Kingdom) - \&quot;es\&quot; (Spanish) - \&quot;fr\&quot; (French) - \&quot;it\&quot; (Italian) - \&quot;ja\&quot; (Japanese) - \&quot;ko\&quot; (Korean) - \&quot;pl\&quot; (Polish) - \&quot;pt-BR\&quot; (Portuguese Brazil) - \&quot;ru\&quot; (Russian) - \&quot;sv\&quot; (Swedish) - \&quot;tr\&quot; (Turkish) - \&quot;zh-CN\&quot; (Chinese Simplified) - \&quot;zh-TW\&quot; (Chinese Traditional)  | [optional] 
**maximumImageSize** | **String** | Maximum image size allowed for this account, in kilobytes. Value must be greater than or equal to 1. | [optional] 
**name** | **String** | Name of this account. This is a required field, and must be less than 128 characters long and be globally unique. | [optional] 
**nielsenOcrEnabled** | **Boolean** | Whether campaigns created in this account will be enabled for Nielsen OCR reach ratings by default. | [optional] 
**reportsConfiguration** | [**ReportsConfiguration**](ReportsConfiguration.md) |  | [optional] 
**shareReportsWithTwitter** | **Boolean** | Share Path to Conversion reports with Twitter. | [optional] 
**teaserSizeLimit** | **String** | File size limit in kilobytes of Rich Media teaser creatives. Acceptable values are 1 to 10240, inclusive. | [optional] 



## Enum: AccountProfileEnum


* `BASIC` (value: `"ACCOUNT_PROFILE_BASIC"`)

* `STANDARD` (value: `"ACCOUNT_PROFILE_STANDARD"`)





## Enum: ActiveAdsLimitTierEnum


* `40K` (value: `"ACTIVE_ADS_TIER_40K"`)

* `75K` (value: `"ACTIVE_ADS_TIER_75K"`)

* `100K` (value: `"ACTIVE_ADS_TIER_100K"`)

* `200K` (value: `"ACTIVE_ADS_TIER_200K"`)

* `300K` (value: `"ACTIVE_ADS_TIER_300K"`)

* `500K` (value: `"ACTIVE_ADS_TIER_500K"`)

* `750K` (value: `"ACTIVE_ADS_TIER_750K"`)

* `1M` (value: `"ACTIVE_ADS_TIER_1M"`)





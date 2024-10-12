# CampaignManager360Api.TargetingTemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Account ID of this targeting template. This field, if left unset, will be auto-generated on insert and is read-only after insert. | [optional] 
**advertiserId** | **String** | Advertiser ID of this targeting template. This is a required field on insert and is read-only after insert. | [optional] 
**advertiserIdDimensionValue** | [**DimensionValue**](DimensionValue.md) |  | [optional] 
**dayPartTargeting** | [**DayPartTargeting**](DayPartTargeting.md) |  | [optional] 
**geoTargeting** | [**GeoTargeting**](GeoTargeting.md) |  | [optional] 
**id** | **String** | ID of this targeting template. This is a read-only, auto-generated field. | [optional] 
**keyValueTargetingExpression** | [**KeyValueTargetingExpression**](KeyValueTargetingExpression.md) |  | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;dfareporting#targetingTemplate\&quot;. | [optional] 
**languageTargeting** | [**LanguageTargeting**](LanguageTargeting.md) |  | [optional] 
**listTargetingExpression** | [**ListTargetingExpression**](ListTargetingExpression.md) |  | [optional] 
**name** | **String** | Name of this targeting template. This field is required. It must be less than 256 characters long and unique within an advertiser. | [optional] 
**subaccountId** | **String** | Subaccount ID of this targeting template. This field, if left unset, will be auto-generated on insert and is read-only after insert. | [optional] 
**technologyTargeting** | [**TechnologyTargeting**](TechnologyTargeting.md) |  | [optional] 



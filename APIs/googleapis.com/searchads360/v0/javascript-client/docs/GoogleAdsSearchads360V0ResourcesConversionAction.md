# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesConversionAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | App ID for an app conversion action. | [optional] 
**attributionModelSettings** | [**GoogleAdsSearchads360V0ResourcesConversionActionAttributionModelSettings**](GoogleAdsSearchads360V0ResourcesConversionActionAttributionModelSettings.md) |  | [optional] 
**category** | **String** | The category of conversions reported for this conversion action. | [optional] 
**clickThroughLookbackWindowDays** | **String** | The maximum number of days that may elapse between an interaction (for example, a click) and a conversion event. | [optional] 
**creationTime** | **String** | Output only. Timestamp of the Floodlight activity&#39;s creation, formatted in ISO 8601. | [optional] [readonly] 
**floodlightSettings** | [**GoogleAdsSearchads360V0ResourcesConversionActionFloodlightSettings**](GoogleAdsSearchads360V0ResourcesConversionActionFloodlightSettings.md) |  | [optional] 
**id** | **String** | Output only. The ID of the conversion action. | [optional] [readonly] 
**includeInClientAccountConversionsMetric** | **Boolean** | Whether this conversion action should be included in the \&quot;client_account_conversions\&quot; metric. | [optional] 
**includeInConversionsMetric** | **Boolean** | Output only. Whether this conversion action should be included in the \&quot;conversions\&quot; metric. | [optional] [readonly] 
**name** | **String** | The name of the conversion action. This field is required and should not be empty when creating new conversion actions. | [optional] 
**ownerCustomer** | **String** | Output only. The resource name of the conversion action owner customer, or null if this is a system-defined conversion action. | [optional] [readonly] 
**primaryForGoal** | **Boolean** | If a conversion action&#39;s primary_for_goal bit is false, the conversion action is non-biddable for all campaigns regardless of their customer conversion goal or campaign conversion goal. However, custom conversion goals do not respect primary_for_goal, so if a campaign has a custom conversion goal configured with a primary_for_goal &#x3D; false conversion action, that conversion action is still biddable. By default, primary_for_goal will be true if not set. In V9, primary_for_goal can only be set to false after creation through an &#39;update&#39; operation because it&#39;s not declared as optional. | [optional] 
**resourceName** | **String** | Immutable. The resource name of the conversion action. Conversion action resource names have the form: &#x60;customers/{customer_id}/conversionActions/{conversion_action_id}&#x60; | [optional] 
**status** | **String** | The status of this conversion action for conversion event accrual. | [optional] 
**type** | **String** | Immutable. The type of this conversion action. | [optional] 
**valueSettings** | [**GoogleAdsSearchads360V0ResourcesConversionActionValueSettings**](GoogleAdsSearchads360V0ResourcesConversionActionValueSettings.md) |  | [optional] 



## Enum: CategoryEnum


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





## Enum: StatusEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `ENABLED` (value: `"ENABLED"`)

* `REMOVED` (value: `"REMOVED"`)

* `HIDDEN` (value: `"HIDDEN"`)





## Enum: TypeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `AD_CALL` (value: `"AD_CALL"`)

* `CLICK_TO_CALL` (value: `"CLICK_TO_CALL"`)

* `GOOGLE_PLAY_DOWNLOAD` (value: `"GOOGLE_PLAY_DOWNLOAD"`)

* `GOOGLE_PLAY_IN_APP_PURCHASE` (value: `"GOOGLE_PLAY_IN_APP_PURCHASE"`)

* `UPLOAD_CALLS` (value: `"UPLOAD_CALLS"`)

* `UPLOAD_CLICKS` (value: `"UPLOAD_CLICKS"`)

* `WEBPAGE` (value: `"WEBPAGE"`)

* `WEBSITE_CALL` (value: `"WEBSITE_CALL"`)

* `STORE_SALES_DIRECT_UPLOAD` (value: `"STORE_SALES_DIRECT_UPLOAD"`)

* `STORE_SALES` (value: `"STORE_SALES"`)

* `FIREBASE_ANDROID_FIRST_OPEN` (value: `"FIREBASE_ANDROID_FIRST_OPEN"`)

* `FIREBASE_ANDROID_IN_APP_PURCHASE` (value: `"FIREBASE_ANDROID_IN_APP_PURCHASE"`)

* `FIREBASE_ANDROID_CUSTOM` (value: `"FIREBASE_ANDROID_CUSTOM"`)

* `FIREBASE_IOS_FIRST_OPEN` (value: `"FIREBASE_IOS_FIRST_OPEN"`)

* `FIREBASE_IOS_IN_APP_PURCHASE` (value: `"FIREBASE_IOS_IN_APP_PURCHASE"`)

* `FIREBASE_IOS_CUSTOM` (value: `"FIREBASE_IOS_CUSTOM"`)

* `THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN` (value: `"THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN"`)

* `THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE` (value: `"THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE"`)

* `THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM` (value: `"THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM"`)

* `THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN` (value: `"THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN"`)

* `THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE` (value: `"THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE"`)

* `THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM` (value: `"THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM"`)

* `ANDROID_APP_PRE_REGISTRATION` (value: `"ANDROID_APP_PRE_REGISTRATION"`)

* `ANDROID_INSTALLS_ALL_OTHER_APPS` (value: `"ANDROID_INSTALLS_ALL_OTHER_APPS"`)

* `FLOODLIGHT_ACTION` (value: `"FLOODLIGHT_ACTION"`)

* `FLOODLIGHT_TRANSACTION` (value: `"FLOODLIGHT_TRANSACTION"`)

* `GOOGLE_HOSTED` (value: `"GOOGLE_HOSTED"`)

* `LEAD_FORM_SUBMIT` (value: `"LEAD_FORM_SUBMIT"`)

* `SALESFORCE` (value: `"SALESFORCE"`)

* `SEARCH_ADS_360` (value: `"SEARCH_ADS_360"`)

* `SMART_CAMPAIGN_AD_CLICKS_TO_CALL` (value: `"SMART_CAMPAIGN_AD_CLICKS_TO_CALL"`)

* `SMART_CAMPAIGN_MAP_CLICKS_TO_CALL` (value: `"SMART_CAMPAIGN_MAP_CLICKS_TO_CALL"`)

* `SMART_CAMPAIGN_MAP_DIRECTIONS` (value: `"SMART_CAMPAIGN_MAP_DIRECTIONS"`)

* `SMART_CAMPAIGN_TRACKED_CALLS` (value: `"SMART_CAMPAIGN_TRACKED_CALLS"`)

* `STORE_VISITS` (value: `"STORE_VISITS"`)

* `WEBPAGE_CODELESS` (value: `"WEBPAGE_CODELESS"`)

* `UNIVERSAL_ANALYTICS_GOAL` (value: `"UNIVERSAL_ANALYTICS_GOAL"`)

* `UNIVERSAL_ANALYTICS_TRANSACTION` (value: `"UNIVERSAL_ANALYTICS_TRANSACTION"`)

* `GOOGLE_ANALYTICS_4_CUSTOM` (value: `"GOOGLE_ANALYTICS_4_CUSTOM"`)

* `GOOGLE_ANALYTICS_4_PURCHASE` (value: `"GOOGLE_ANALYTICS_4_PURCHASE"`)







# GoogleAdsSearchads360V0ResourcesConversionAction

A conversion action.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appId** | **String** | App ID for an app conversion action. |  [optional] |
|**attributionModelSettings** | [**GoogleAdsSearchads360V0ResourcesConversionActionAttributionModelSettings**](GoogleAdsSearchads360V0ResourcesConversionActionAttributionModelSettings.md) |  |  [optional] |
|**category** | [**CategoryEnum**](#CategoryEnum) | The category of conversions reported for this conversion action. |  [optional] |
|**clickThroughLookbackWindowDays** | **String** | The maximum number of days that may elapse between an interaction (for example, a click) and a conversion event. |  [optional] |
|**creationTime** | **String** | Output only. Timestamp of the Floodlight activity&#39;s creation, formatted in ISO 8601. |  [optional] [readonly] |
|**floodlightSettings** | [**GoogleAdsSearchads360V0ResourcesConversionActionFloodlightSettings**](GoogleAdsSearchads360V0ResourcesConversionActionFloodlightSettings.md) |  |  [optional] |
|**id** | **String** | Output only. The ID of the conversion action. |  [optional] [readonly] |
|**includeInClientAccountConversionsMetric** | **Boolean** | Whether this conversion action should be included in the \&quot;client_account_conversions\&quot; metric. |  [optional] |
|**includeInConversionsMetric** | **Boolean** | Output only. Whether this conversion action should be included in the \&quot;conversions\&quot; metric. |  [optional] [readonly] |
|**name** | **String** | The name of the conversion action. This field is required and should not be empty when creating new conversion actions. |  [optional] |
|**ownerCustomer** | **String** | Output only. The resource name of the conversion action owner customer, or null if this is a system-defined conversion action. |  [optional] [readonly] |
|**primaryForGoal** | **Boolean** | If a conversion action&#39;s primary_for_goal bit is false, the conversion action is non-biddable for all campaigns regardless of their customer conversion goal or campaign conversion goal. However, custom conversion goals do not respect primary_for_goal, so if a campaign has a custom conversion goal configured with a primary_for_goal &#x3D; false conversion action, that conversion action is still biddable. By default, primary_for_goal will be true if not set. In V9, primary_for_goal can only be set to false after creation through an &#39;update&#39; operation because it&#39;s not declared as optional. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the conversion action. Conversion action resource names have the form: &#x60;customers/{customer_id}/conversionActions/{conversion_action_id}&#x60; |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of this conversion action for conversion event accrual. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Immutable. The type of this conversion action. |  [optional] |
|**valueSettings** | [**GoogleAdsSearchads360V0ResourcesConversionActionValueSettings**](GoogleAdsSearchads360V0ResourcesConversionActionValueSettings.md) |  |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| DEFAULT | &quot;DEFAULT&quot; |
| PAGE_VIEW | &quot;PAGE_VIEW&quot; |
| PURCHASE | &quot;PURCHASE&quot; |
| SIGNUP | &quot;SIGNUP&quot; |
| LEAD | &quot;LEAD&quot; |
| DOWNLOAD | &quot;DOWNLOAD&quot; |
| ADD_TO_CART | &quot;ADD_TO_CART&quot; |
| BEGIN_CHECKOUT | &quot;BEGIN_CHECKOUT&quot; |
| SUBSCRIBE_PAID | &quot;SUBSCRIBE_PAID&quot; |
| PHONE_CALL_LEAD | &quot;PHONE_CALL_LEAD&quot; |
| IMPORTED_LEAD | &quot;IMPORTED_LEAD&quot; |
| SUBMIT_LEAD_FORM | &quot;SUBMIT_LEAD_FORM&quot; |
| BOOK_APPOINTMENT | &quot;BOOK_APPOINTMENT&quot; |
| REQUEST_QUOTE | &quot;REQUEST_QUOTE&quot; |
| GET_DIRECTIONS | &quot;GET_DIRECTIONS&quot; |
| OUTBOUND_CLICK | &quot;OUTBOUND_CLICK&quot; |
| CONTACT | &quot;CONTACT&quot; |
| ENGAGEMENT | &quot;ENGAGEMENT&quot; |
| STORE_VISIT | &quot;STORE_VISIT&quot; |
| STORE_SALE | &quot;STORE_SALE&quot; |
| QUALIFIED_LEAD | &quot;QUALIFIED_LEAD&quot; |
| CONVERTED_LEAD | &quot;CONVERTED_LEAD&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| ENABLED | &quot;ENABLED&quot; |
| REMOVED | &quot;REMOVED&quot; |
| HIDDEN | &quot;HIDDEN&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| AD_CALL | &quot;AD_CALL&quot; |
| CLICK_TO_CALL | &quot;CLICK_TO_CALL&quot; |
| GOOGLE_PLAY_DOWNLOAD | &quot;GOOGLE_PLAY_DOWNLOAD&quot; |
| GOOGLE_PLAY_IN_APP_PURCHASE | &quot;GOOGLE_PLAY_IN_APP_PURCHASE&quot; |
| UPLOAD_CALLS | &quot;UPLOAD_CALLS&quot; |
| UPLOAD_CLICKS | &quot;UPLOAD_CLICKS&quot; |
| WEBPAGE | &quot;WEBPAGE&quot; |
| WEBSITE_CALL | &quot;WEBSITE_CALL&quot; |
| STORE_SALES_DIRECT_UPLOAD | &quot;STORE_SALES_DIRECT_UPLOAD&quot; |
| STORE_SALES | &quot;STORE_SALES&quot; |
| FIREBASE_ANDROID_FIRST_OPEN | &quot;FIREBASE_ANDROID_FIRST_OPEN&quot; |
| FIREBASE_ANDROID_IN_APP_PURCHASE | &quot;FIREBASE_ANDROID_IN_APP_PURCHASE&quot; |
| FIREBASE_ANDROID_CUSTOM | &quot;FIREBASE_ANDROID_CUSTOM&quot; |
| FIREBASE_IOS_FIRST_OPEN | &quot;FIREBASE_IOS_FIRST_OPEN&quot; |
| FIREBASE_IOS_IN_APP_PURCHASE | &quot;FIREBASE_IOS_IN_APP_PURCHASE&quot; |
| FIREBASE_IOS_CUSTOM | &quot;FIREBASE_IOS_CUSTOM&quot; |
| THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN | &quot;THIRD_PARTY_APP_ANALYTICS_ANDROID_FIRST_OPEN&quot; |
| THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE | &quot;THIRD_PARTY_APP_ANALYTICS_ANDROID_IN_APP_PURCHASE&quot; |
| THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM | &quot;THIRD_PARTY_APP_ANALYTICS_ANDROID_CUSTOM&quot; |
| THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN | &quot;THIRD_PARTY_APP_ANALYTICS_IOS_FIRST_OPEN&quot; |
| THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE | &quot;THIRD_PARTY_APP_ANALYTICS_IOS_IN_APP_PURCHASE&quot; |
| THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM | &quot;THIRD_PARTY_APP_ANALYTICS_IOS_CUSTOM&quot; |
| ANDROID_APP_PRE_REGISTRATION | &quot;ANDROID_APP_PRE_REGISTRATION&quot; |
| ANDROID_INSTALLS_ALL_OTHER_APPS | &quot;ANDROID_INSTALLS_ALL_OTHER_APPS&quot; |
| FLOODLIGHT_ACTION | &quot;FLOODLIGHT_ACTION&quot; |
| FLOODLIGHT_TRANSACTION | &quot;FLOODLIGHT_TRANSACTION&quot; |
| GOOGLE_HOSTED | &quot;GOOGLE_HOSTED&quot; |
| LEAD_FORM_SUBMIT | &quot;LEAD_FORM_SUBMIT&quot; |
| SALESFORCE | &quot;SALESFORCE&quot; |
| SEARCH_ADS_360 | &quot;SEARCH_ADS_360&quot; |
| SMART_CAMPAIGN_AD_CLICKS_TO_CALL | &quot;SMART_CAMPAIGN_AD_CLICKS_TO_CALL&quot; |
| SMART_CAMPAIGN_MAP_CLICKS_TO_CALL | &quot;SMART_CAMPAIGN_MAP_CLICKS_TO_CALL&quot; |
| SMART_CAMPAIGN_MAP_DIRECTIONS | &quot;SMART_CAMPAIGN_MAP_DIRECTIONS&quot; |
| SMART_CAMPAIGN_TRACKED_CALLS | &quot;SMART_CAMPAIGN_TRACKED_CALLS&quot; |
| STORE_VISITS | &quot;STORE_VISITS&quot; |
| WEBPAGE_CODELESS | &quot;WEBPAGE_CODELESS&quot; |
| UNIVERSAL_ANALYTICS_GOAL | &quot;UNIVERSAL_ANALYTICS_GOAL&quot; |
| UNIVERSAL_ANALYTICS_TRANSACTION | &quot;UNIVERSAL_ANALYTICS_TRANSACTION&quot; |
| GOOGLE_ANALYTICS_4_CUSTOM | &quot;GOOGLE_ANALYTICS_4_CUSTOM&quot; |
| GOOGLE_ANALYTICS_4_PURCHASE | &quot;GOOGLE_ANALYTICS_4_PURCHASE&quot; |




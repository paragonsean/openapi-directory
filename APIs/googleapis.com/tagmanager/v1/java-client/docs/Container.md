

# Container

Represents a Google Tag Manager Container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**containerId** | **String** | The Container ID uniquely identifies the GTM Container. |  [optional] |
|**domainName** | **List&lt;String&gt;** | Optional list of domain names associated with the Container. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**enabledBuiltInVariable** | [**List&lt;EnabledBuiltInVariableEnum&gt;**](#List&lt;EnabledBuiltInVariableEnum&gt;) | List of enabled built-in variables. Valid values include: pageUrl, pageHostname, pagePath, referrer, event, clickElement, clickClasses, clickId, clickTarget, clickUrl, clickText, formElement, formClasses, formId, formTarget, formUrl, formText, errorMessage, errorUrl, errorLine, newHistoryFragment, oldHistoryFragment, newHistoryState, oldHistoryState, historySource, containerVersion, debugMode, randomNumber, containerId. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Container as computed at storage time. This value is recomputed whenever the account is modified. |  [optional] |
|**name** | **String** | Container display name. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**notes** | **String** | Container Notes. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**publicId** | **String** | Container Public ID. |  [optional] |
|**timeZoneCountryId** | **String** | Container Country ID. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**timeZoneId** | **String** | Container Time Zone ID. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**usageContext** | [**List&lt;UsageContextEnum&gt;**](#List&lt;UsageContextEnum&gt;) | List of Usage Contexts for the Container. Valid values include: web, android, ios. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |



## Enum: List&lt;EnabledBuiltInVariableEnum&gt;

| Name | Value |
|---- | -----|
| PAGE_URL | &quot;pageUrl&quot; |
| PAGE_HOSTNAME | &quot;pageHostname&quot; |
| PAGE_PATH | &quot;pagePath&quot; |
| REFERRER | &quot;referrer&quot; |
| EVENT | &quot;event&quot; |
| CLICK_ELEMENT | &quot;clickElement&quot; |
| CLICK_CLASSES | &quot;clickClasses&quot; |
| CLICK_ID | &quot;clickId&quot; |
| CLICK_TARGET | &quot;clickTarget&quot; |
| CLICK_URL | &quot;clickUrl&quot; |
| CLICK_TEXT | &quot;clickText&quot; |
| FIRST_PARTY_SERVING_URL | &quot;firstPartyServingUrl&quot; |
| FORM_ELEMENT | &quot;formElement&quot; |
| FORM_CLASSES | &quot;formClasses&quot; |
| FORM_ID | &quot;formId&quot; |
| FORM_TARGET | &quot;formTarget&quot; |
| FORM_URL | &quot;formUrl&quot; |
| FORM_TEXT | &quot;formText&quot; |
| ENVIRONMENT_NAME | &quot;environmentName&quot; |
| ERROR_MESSAGE | &quot;errorMessage&quot; |
| ERROR_URL | &quot;errorUrl&quot; |
| ERROR_LINE | &quot;errorLine&quot; |
| NEW_HISTORY_URL | &quot;newHistoryUrl&quot; |
| OLD_HISTORY_URL | &quot;oldHistoryUrl&quot; |
| NEW_HISTORY_FRAGMENT | &quot;newHistoryFragment&quot; |
| OLD_HISTORY_FRAGMENT | &quot;oldHistoryFragment&quot; |
| NEW_HISTORY_STATE | &quot;newHistoryState&quot; |
| OLD_HISTORY_STATE | &quot;oldHistoryState&quot; |
| HISTORY_SOURCE | &quot;historySource&quot; |
| CONTAINER_VERSION | &quot;containerVersion&quot; |
| DEBUG_MODE | &quot;debugMode&quot; |
| RANDOM_NUMBER | &quot;randomNumber&quot; |
| CONTAINER_ID | &quot;containerId&quot; |
| APP_ID | &quot;appId&quot; |
| APP_NAME | &quot;appName&quot; |
| APP_VERSION_CODE | &quot;appVersionCode&quot; |
| APP_VERSION_NAME | &quot;appVersionName&quot; |
| LANGUAGE | &quot;language&quot; |
| OS_VERSION | &quot;osVersion&quot; |
| PLATFORM | &quot;platform&quot; |
| SDK_VERSION | &quot;sdkVersion&quot; |
| DEVICE_NAME | &quot;deviceName&quot; |
| RESOLUTION | &quot;resolution&quot; |
| ADVERTISER_ID | &quot;advertiserId&quot; |
| ADVERTISING_TRACKING_ENABLED | &quot;advertisingTrackingEnabled&quot; |
| HTML_ID | &quot;htmlId&quot; |
| AMP_BROWSER_LANGUAGE | &quot;ampBrowserLanguage&quot; |
| AMP_CANONICAL_PATH | &quot;ampCanonicalPath&quot; |
| AMP_CANONICAL_URL | &quot;ampCanonicalUrl&quot; |
| AMP_CANONICAL_HOST | &quot;ampCanonicalHost&quot; |
| AMP_REFERRER | &quot;ampReferrer&quot; |
| AMP_TITLE | &quot;ampTitle&quot; |
| AMP_CLIENT_ID | &quot;ampClientId&quot; |
| AMP_CLIENT_TIMEZONE | &quot;ampClientTimezone&quot; |
| AMP_CLIENT_TIMESTAMP | &quot;ampClientTimestamp&quot; |
| AMP_CLIENT_SCREEN_WIDTH | &quot;ampClientScreenWidth&quot; |
| AMP_CLIENT_SCREEN_HEIGHT | &quot;ampClientScreenHeight&quot; |
| AMP_CLIENT_SCROLL_X | &quot;ampClientScrollX&quot; |
| AMP_CLIENT_SCROLL_Y | &quot;ampClientScrollY&quot; |
| AMP_CLIENT_MAX_SCROLL_X | &quot;ampClientMaxScrollX&quot; |
| AMP_CLIENT_MAX_SCROLL_Y | &quot;ampClientMaxScrollY&quot; |
| AMP_TOTAL_ENGAGED_TIME | &quot;ampTotalEngagedTime&quot; |
| AMP_PAGE_VIEW_ID | &quot;ampPageViewId&quot; |
| AMP_PAGE_LOAD_TIME | &quot;ampPageLoadTime&quot; |
| AMP_PAGE_DOWNLOAD_TIME | &quot;ampPageDownloadTime&quot; |
| AMP_GTM_EVENT | &quot;ampGtmEvent&quot; |
| EVENT_NAME | &quot;eventName&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN | &quot;firebaseEventParameterCampaign&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_ACLID | &quot;firebaseEventParameterCampaignAclid&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_ANID | &quot;firebaseEventParameterCampaignAnid&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_CLICK_TIMESTAMP | &quot;firebaseEventParameterCampaignClickTimestamp&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_CONTENT | &quot;firebaseEventParameterCampaignContent&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_CP1 | &quot;firebaseEventParameterCampaignCp1&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_GCLID | &quot;firebaseEventParameterCampaignGclid&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_SOURCE | &quot;firebaseEventParameterCampaignSource&quot; |
| FIREBASE_EVENT_PARAMETER_CAMPAIGN_TERM | &quot;firebaseEventParameterCampaignTerm&quot; |
| FIREBASE_EVENT_PARAMETER_CURRENCY | &quot;firebaseEventParameterCurrency&quot; |
| FIREBASE_EVENT_PARAMETER_DYNAMIC_LINK_ACCEPT_TIME | &quot;firebaseEventParameterDynamicLinkAcceptTime&quot; |
| FIREBASE_EVENT_PARAMETER_DYNAMIC_LINK_LINKID | &quot;firebaseEventParameterDynamicLinkLinkid&quot; |
| FIREBASE_EVENT_PARAMETER_NOTIFICATION_MESSAGE_DEVICE_TIME | &quot;firebaseEventParameterNotificationMessageDeviceTime&quot; |
| FIREBASE_EVENT_PARAMETER_NOTIFICATION_MESSAGE_ID | &quot;firebaseEventParameterNotificationMessageId&quot; |
| FIREBASE_EVENT_PARAMETER_NOTIFICATION_MESSAGE_NAME | &quot;firebaseEventParameterNotificationMessageName&quot; |
| FIREBASE_EVENT_PARAMETER_NOTIFICATION_MESSAGE_TIME | &quot;firebaseEventParameterNotificationMessageTime&quot; |
| FIREBASE_EVENT_PARAMETER_NOTIFICATION_TOPIC | &quot;firebaseEventParameterNotificationTopic&quot; |
| FIREBASE_EVENT_PARAMETER_PREVIOUS_APP_VERSION | &quot;firebaseEventParameterPreviousAppVersion&quot; |
| FIREBASE_EVENT_PARAMETER_PREVIOUS_OS_VERSION | &quot;firebaseEventParameterPreviousOsVersion&quot; |
| FIREBASE_EVENT_PARAMETER_PRICE | &quot;firebaseEventParameterPrice&quot; |
| FIREBASE_EVENT_PARAMETER_PRODUCT_ID | &quot;firebaseEventParameterProductId&quot; |
| FIREBASE_EVENT_PARAMETER_QUANTITY | &quot;firebaseEventParameterQuantity&quot; |
| FIREBASE_EVENT_PARAMETER_VALUE | &quot;firebaseEventParameterValue&quot; |
| VIDEO_PROVIDER | &quot;videoProvider&quot; |
| VIDEO_URL | &quot;videoUrl&quot; |
| VIDEO_TITLE | &quot;videoTitle&quot; |
| VIDEO_DURATION | &quot;videoDuration&quot; |
| VIDEO_PERCENT | &quot;videoPercent&quot; |
| VIDEO_VISIBLE | &quot;videoVisible&quot; |
| VIDEO_STATUS | &quot;videoStatus&quot; |
| VIDEO_CURRENT_TIME | &quot;videoCurrentTime&quot; |
| SCROLL_DEPTH_THRESHOLD | &quot;scrollDepthThreshold&quot; |
| SCROLL_DEPTH_UNITS | &quot;scrollDepthUnits&quot; |
| SCROLL_DEPTH_DIRECTION | &quot;scrollDepthDirection&quot; |
| ELEMENT_VISIBILITY_RATIO | &quot;elementVisibilityRatio&quot; |
| ELEMENT_VISIBILITY_TIME | &quot;elementVisibilityTime&quot; |
| ELEMENT_VISIBILITY_FIRST_TIME | &quot;elementVisibilityFirstTime&quot; |
| ELEMENT_VISIBILITY_RECENT_TIME | &quot;elementVisibilityRecentTime&quot; |



## Enum: List&lt;UsageContextEnum&gt;

| Name | Value |
|---- | -----|
| WEB | &quot;web&quot; |
| ANDROID | &quot;android&quot; |
| IOS | &quot;ios&quot; |
| ANDROID_SDK5 | &quot;androidSdk5&quot; |
| IOS_SDK5 | &quot;iosSdk5&quot; |
| AMP | &quot;amp&quot; |




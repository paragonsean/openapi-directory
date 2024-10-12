# TagManagerApi.Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | GTM Account ID. | [optional] 
**containerId** | **String** | The Container ID uniquely identifies the GTM Container. | [optional] 
**domainName** | **[String]** | Optional list of domain names associated with the Container. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**enabledBuiltInVariable** | **[String]** | List of enabled built-in variables. Valid values include: pageUrl, pageHostname, pagePath, referrer, event, clickElement, clickClasses, clickId, clickTarget, clickUrl, clickText, formElement, formClasses, formId, formTarget, formUrl, formText, errorMessage, errorUrl, errorLine, newHistoryFragment, oldHistoryFragment, newHistoryState, oldHistoryState, historySource, containerVersion, debugMode, randomNumber, containerId. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**fingerprint** | **String** | The fingerprint of the GTM Container as computed at storage time. This value is recomputed whenever the account is modified. | [optional] 
**name** | **String** | Container display name. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**notes** | **String** | Container Notes. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**publicId** | **String** | Container Public ID. | [optional] 
**timeZoneCountryId** | **String** | Container Country ID. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**timeZoneId** | **String** | Container Time Zone ID. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**usageContext** | **[String]** | List of Usage Contexts for the Container. Valid values include: web, android, ios. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 



## Enum: [EnabledBuiltInVariableEnum]


* `pageUrl` (value: `"pageUrl"`)

* `pageHostname` (value: `"pageHostname"`)

* `pagePath` (value: `"pagePath"`)

* `referrer` (value: `"referrer"`)

* `event` (value: `"event"`)

* `clickElement` (value: `"clickElement"`)

* `clickClasses` (value: `"clickClasses"`)

* `clickId` (value: `"clickId"`)

* `clickTarget` (value: `"clickTarget"`)

* `clickUrl` (value: `"clickUrl"`)

* `clickText` (value: `"clickText"`)

* `firstPartyServingUrl` (value: `"firstPartyServingUrl"`)

* `formElement` (value: `"formElement"`)

* `formClasses` (value: `"formClasses"`)

* `formId` (value: `"formId"`)

* `formTarget` (value: `"formTarget"`)

* `formUrl` (value: `"formUrl"`)

* `formText` (value: `"formText"`)

* `environmentName` (value: `"environmentName"`)

* `errorMessage` (value: `"errorMessage"`)

* `errorUrl` (value: `"errorUrl"`)

* `errorLine` (value: `"errorLine"`)

* `newHistoryUrl` (value: `"newHistoryUrl"`)

* `oldHistoryUrl` (value: `"oldHistoryUrl"`)

* `newHistoryFragment` (value: `"newHistoryFragment"`)

* `oldHistoryFragment` (value: `"oldHistoryFragment"`)

* `newHistoryState` (value: `"newHistoryState"`)

* `oldHistoryState` (value: `"oldHistoryState"`)

* `historySource` (value: `"historySource"`)

* `containerVersion` (value: `"containerVersion"`)

* `debugMode` (value: `"debugMode"`)

* `randomNumber` (value: `"randomNumber"`)

* `containerId` (value: `"containerId"`)

* `appId` (value: `"appId"`)

* `appName` (value: `"appName"`)

* `appVersionCode` (value: `"appVersionCode"`)

* `appVersionName` (value: `"appVersionName"`)

* `language` (value: `"language"`)

* `osVersion` (value: `"osVersion"`)

* `platform` (value: `"platform"`)

* `sdkVersion` (value: `"sdkVersion"`)

* `deviceName` (value: `"deviceName"`)

* `resolution` (value: `"resolution"`)

* `advertiserId` (value: `"advertiserId"`)

* `advertisingTrackingEnabled` (value: `"advertisingTrackingEnabled"`)

* `htmlId` (value: `"htmlId"`)

* `ampBrowserLanguage` (value: `"ampBrowserLanguage"`)

* `ampCanonicalPath` (value: `"ampCanonicalPath"`)

* `ampCanonicalUrl` (value: `"ampCanonicalUrl"`)

* `ampCanonicalHost` (value: `"ampCanonicalHost"`)

* `ampReferrer` (value: `"ampReferrer"`)

* `ampTitle` (value: `"ampTitle"`)

* `ampClientId` (value: `"ampClientId"`)

* `ampClientTimezone` (value: `"ampClientTimezone"`)

* `ampClientTimestamp` (value: `"ampClientTimestamp"`)

* `ampClientScreenWidth` (value: `"ampClientScreenWidth"`)

* `ampClientScreenHeight` (value: `"ampClientScreenHeight"`)

* `ampClientScrollX` (value: `"ampClientScrollX"`)

* `ampClientScrollY` (value: `"ampClientScrollY"`)

* `ampClientMaxScrollX` (value: `"ampClientMaxScrollX"`)

* `ampClientMaxScrollY` (value: `"ampClientMaxScrollY"`)

* `ampTotalEngagedTime` (value: `"ampTotalEngagedTime"`)

* `ampPageViewId` (value: `"ampPageViewId"`)

* `ampPageLoadTime` (value: `"ampPageLoadTime"`)

* `ampPageDownloadTime` (value: `"ampPageDownloadTime"`)

* `ampGtmEvent` (value: `"ampGtmEvent"`)

* `eventName` (value: `"eventName"`)

* `firebaseEventParameterCampaign` (value: `"firebaseEventParameterCampaign"`)

* `firebaseEventParameterCampaignAclid` (value: `"firebaseEventParameterCampaignAclid"`)

* `firebaseEventParameterCampaignAnid` (value: `"firebaseEventParameterCampaignAnid"`)

* `firebaseEventParameterCampaignClickTimestamp` (value: `"firebaseEventParameterCampaignClickTimestamp"`)

* `firebaseEventParameterCampaignContent` (value: `"firebaseEventParameterCampaignContent"`)

* `firebaseEventParameterCampaignCp1` (value: `"firebaseEventParameterCampaignCp1"`)

* `firebaseEventParameterCampaignGclid` (value: `"firebaseEventParameterCampaignGclid"`)

* `firebaseEventParameterCampaignSource` (value: `"firebaseEventParameterCampaignSource"`)

* `firebaseEventParameterCampaignTerm` (value: `"firebaseEventParameterCampaignTerm"`)

* `firebaseEventParameterCurrency` (value: `"firebaseEventParameterCurrency"`)

* `firebaseEventParameterDynamicLinkAcceptTime` (value: `"firebaseEventParameterDynamicLinkAcceptTime"`)

* `firebaseEventParameterDynamicLinkLinkid` (value: `"firebaseEventParameterDynamicLinkLinkid"`)

* `firebaseEventParameterNotificationMessageDeviceTime` (value: `"firebaseEventParameterNotificationMessageDeviceTime"`)

* `firebaseEventParameterNotificationMessageId` (value: `"firebaseEventParameterNotificationMessageId"`)

* `firebaseEventParameterNotificationMessageName` (value: `"firebaseEventParameterNotificationMessageName"`)

* `firebaseEventParameterNotificationMessageTime` (value: `"firebaseEventParameterNotificationMessageTime"`)

* `firebaseEventParameterNotificationTopic` (value: `"firebaseEventParameterNotificationTopic"`)

* `firebaseEventParameterPreviousAppVersion` (value: `"firebaseEventParameterPreviousAppVersion"`)

* `firebaseEventParameterPreviousOsVersion` (value: `"firebaseEventParameterPreviousOsVersion"`)

* `firebaseEventParameterPrice` (value: `"firebaseEventParameterPrice"`)

* `firebaseEventParameterProductId` (value: `"firebaseEventParameterProductId"`)

* `firebaseEventParameterQuantity` (value: `"firebaseEventParameterQuantity"`)

* `firebaseEventParameterValue` (value: `"firebaseEventParameterValue"`)

* `videoProvider` (value: `"videoProvider"`)

* `videoUrl` (value: `"videoUrl"`)

* `videoTitle` (value: `"videoTitle"`)

* `videoDuration` (value: `"videoDuration"`)

* `videoPercent` (value: `"videoPercent"`)

* `videoVisible` (value: `"videoVisible"`)

* `videoStatus` (value: `"videoStatus"`)

* `videoCurrentTime` (value: `"videoCurrentTime"`)

* `scrollDepthThreshold` (value: `"scrollDepthThreshold"`)

* `scrollDepthUnits` (value: `"scrollDepthUnits"`)

* `scrollDepthDirection` (value: `"scrollDepthDirection"`)

* `elementVisibilityRatio` (value: `"elementVisibilityRatio"`)

* `elementVisibilityTime` (value: `"elementVisibilityTime"`)

* `elementVisibilityFirstTime` (value: `"elementVisibilityFirstTime"`)

* `elementVisibilityRecentTime` (value: `"elementVisibilityRecentTime"`)





## Enum: [UsageContextEnum]


* `web` (value: `"web"`)

* `android` (value: `"android"`)

* `ios` (value: `"ios"`)

* `androidSdk5` (value: `"androidSdk5"`)

* `iosSdk5` (value: `"iosSdk5"`)

* `amp` (value: `"amp"`)





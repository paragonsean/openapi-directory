# TagManagerApi.BuiltInVariable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | GTM Account ID. | [optional] 
**containerId** | **String** | GTM Container ID. | [optional] 
**name** | **String** | Name of the built-in variable to be used to refer to the built-in variable. | [optional] 
**path** | **String** | GTM BuiltInVariable&#39;s API relative path. | [optional] 
**type** | **String** | Type of built-in variable. @required.tagmanager.accounts.containers.workspaces.built_in_variable.update @mutable tagmanager.accounts.containers.workspaces.built_in_variable.update | [optional] 
**workspaceId** | **String** | GTM Workspace ID. | [optional] 



## Enum: TypeEnum


* `builtInVariableTypeUnspecified` (value: `"builtInVariableTypeUnspecified"`)

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

* `environmentName` (value: `"environmentName"`)

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

* `requestPath` (value: `"requestPath"`)

* `requestMethod` (value: `"requestMethod"`)

* `clientName` (value: `"clientName"`)

* `queryString` (value: `"queryString"`)

* `serverPageLocationUrl` (value: `"serverPageLocationUrl"`)

* `serverPageLocationPath` (value: `"serverPageLocationPath"`)

* `serverPageLocationHostname` (value: `"serverPageLocationHostname"`)

* `visitorRegion` (value: `"visitorRegion"`)





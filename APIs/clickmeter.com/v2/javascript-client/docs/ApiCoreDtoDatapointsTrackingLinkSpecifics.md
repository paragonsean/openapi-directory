# ClickMeterApi.ApiCoreDtoDatapointsTrackingLinkSpecifics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appendQuery** | **Boolean** |  | [optional] 
**browserDestinationItem** | [**ApiCoreDtoDatapointsBrowserBaseDestinationItem**](ApiCoreDtoDatapointsBrowserBaseDestinationItem.md) |  | [optional] 
**destinationMode** | **String** |  | [optional] 
**domainId** | **Number** |  | [optional] 
**encodeUrl** | **Boolean** |  | [optional] 
**expirationClicks** | **Number** |  | [optional] 
**expirationDate** | **String** |  (A date in \&quot;YmdHis\&quot; format) | [optional] 
**firstUrl** | **String** |  | [optional] 
**goDomainId** | **Number** |  | [optional] 
**hideUrl** | **Boolean** |  | [optional] 
**hideUrlTitle** | **String** |  | [optional] 
**isABTest** | **Boolean** |  | [optional] 
**password** | **String** |  | [optional] 
**pauseAfterClicksExpiration** | **Boolean** |  | [optional] 
**pauseAfterDateExpiration** | **Boolean** |  | [optional] 
**randomDestinationItems** | [**[ApiCoreDtoDatapointsMultipleDestinationItem]**](ApiCoreDtoDatapointsMultipleDestinationItem.md) |  | [optional] 
**redirectType** | **String** |  | [optional] 
**referrerClean** | **String** |  | [optional] 
**scripts** | [**[ApiCoreDtoDatapointsDatapointRetargetingInfo]**](ApiCoreDtoDatapointsDatapointRetargetingInfo.md) |  | [optional] 
**sequentialDestinationItems** | [**[ApiCoreDtoDatapointsMultipleDestinationItem]**](ApiCoreDtoDatapointsMultipleDestinationItem.md) |  | [optional] 
**spilloverDestinationItems** | [**[ApiCoreDtoDatapointsMultipleDestinationItem]**](ApiCoreDtoDatapointsMultipleDestinationItem.md) |  | [optional] 
**uniqueDestinationItem** | [**ApiCoreDtoDatapointsUniqueDestinationItem**](ApiCoreDtoDatapointsUniqueDestinationItem.md) |  | [optional] 
**url** | **String** |  | [optional] 
**urlAfterClicksExpiration** | **String** |  | [optional] 
**urlAfterDateExpiration** | **String** |  | [optional] 
**urlsByLanguage** | [**[ApiCoreDtoDatapointsUrlByLanguageItem]**](ApiCoreDtoDatapointsUrlByLanguageItem.md) |  | [optional] 
**urlsByNation** | [**[ApiCoreDtoDatapointsUrlByNationItem]**](ApiCoreDtoDatapointsUrlByNationItem.md) |  | [optional] 
**weightedDestinationItems** | [**[ApiCoreDtoDatapointsWeightedDestinationItem]**](ApiCoreDtoDatapointsWeightedDestinationItem.md) |  | [optional] 



## Enum: DestinationModeEnum


* `Simple` (value: `"Simple"`)

* `RandomDestination` (value: `"RandomDestination"`)

* `DestinationByLanguage` (value: `"DestinationByLanguage"`)

* `SpilloverDestination` (value: `"SpilloverDestination"`)

* `DynamicUrl` (value: `"DynamicUrl"`)

* `BrowserDestination` (value: `"BrowserDestination"`)

* `DestinationByNation` (value: `"DestinationByNation"`)

* `UniqueDestination` (value: `"UniqueDestination"`)

* `SequentialDestination` (value: `"SequentialDestination"`)

* `WeightedDestination` (value: `"WeightedDestination"`)





## Enum: RedirectTypeEnum


* `PermanentRedirect` (value: `"PermanentRedirect"`)

* `TemporaryRedirect` (value: `"TemporaryRedirect"`)





## Enum: ReferrerCleanEnum


* `None` (value: `"None"`)

* `Clean` (value: `"Clean"`)

* `Myself` (value: `"Myself"`)





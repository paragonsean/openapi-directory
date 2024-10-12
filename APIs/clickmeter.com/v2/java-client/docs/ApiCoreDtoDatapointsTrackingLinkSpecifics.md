

# ApiCoreDtoDatapointsTrackingLinkSpecifics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appendQuery** | **Boolean** |  |  [optional] |
|**browserDestinationItem** | [**ApiCoreDtoDatapointsBrowserBaseDestinationItem**](ApiCoreDtoDatapointsBrowserBaseDestinationItem.md) |  |  [optional] |
|**destinationMode** | [**DestinationModeEnum**](#DestinationModeEnum) |  |  [optional] |
|**domainId** | **Integer** |  |  [optional] |
|**encodeUrl** | **Boolean** |  |  [optional] |
|**expirationClicks** | **Long** |  |  [optional] |
|**expirationDate** | **String** |  (A date in \&quot;YmdHis\&quot; format) |  [optional] |
|**firstUrl** | **String** |  |  [optional] |
|**goDomainId** | **Integer** |  |  [optional] |
|**hideUrl** | **Boolean** |  |  [optional] |
|**hideUrlTitle** | **String** |  |  [optional] |
|**isABTest** | **Boolean** |  |  [optional] |
|**password** | **String** |  |  [optional] |
|**pauseAfterClicksExpiration** | **Boolean** |  |  [optional] |
|**pauseAfterDateExpiration** | **Boolean** |  |  [optional] |
|**randomDestinationItems** | [**List&lt;ApiCoreDtoDatapointsMultipleDestinationItem&gt;**](ApiCoreDtoDatapointsMultipleDestinationItem.md) |  |  [optional] |
|**redirectType** | [**RedirectTypeEnum**](#RedirectTypeEnum) |  |  [optional] |
|**referrerClean** | [**ReferrerCleanEnum**](#ReferrerCleanEnum) |  |  [optional] |
|**scripts** | [**List&lt;ApiCoreDtoDatapointsDatapointRetargetingInfo&gt;**](ApiCoreDtoDatapointsDatapointRetargetingInfo.md) |  |  [optional] |
|**sequentialDestinationItems** | [**List&lt;ApiCoreDtoDatapointsMultipleDestinationItem&gt;**](ApiCoreDtoDatapointsMultipleDestinationItem.md) |  |  [optional] |
|**spilloverDestinationItems** | [**List&lt;ApiCoreDtoDatapointsMultipleDestinationItem&gt;**](ApiCoreDtoDatapointsMultipleDestinationItem.md) |  |  [optional] |
|**uniqueDestinationItem** | [**ApiCoreDtoDatapointsUniqueDestinationItem**](ApiCoreDtoDatapointsUniqueDestinationItem.md) |  |  [optional] |
|**url** | **String** |  |  [optional] |
|**urlAfterClicksExpiration** | **String** |  |  [optional] |
|**urlAfterDateExpiration** | **String** |  |  [optional] |
|**urlsByLanguage** | [**List&lt;ApiCoreDtoDatapointsUrlByLanguageItem&gt;**](ApiCoreDtoDatapointsUrlByLanguageItem.md) |  |  [optional] |
|**urlsByNation** | [**List&lt;ApiCoreDtoDatapointsUrlByNationItem&gt;**](ApiCoreDtoDatapointsUrlByNationItem.md) |  |  [optional] |
|**weightedDestinationItems** | [**List&lt;ApiCoreDtoDatapointsWeightedDestinationItem&gt;**](ApiCoreDtoDatapointsWeightedDestinationItem.md) |  |  [optional] |



## Enum: DestinationModeEnum

| Name | Value |
|---- | -----|
| SIMPLE | &quot;Simple&quot; |
| RANDOM_DESTINATION | &quot;RandomDestination&quot; |
| DESTINATION_BY_LANGUAGE | &quot;DestinationByLanguage&quot; |
| SPILLOVER_DESTINATION | &quot;SpilloverDestination&quot; |
| DYNAMIC_URL | &quot;DynamicUrl&quot; |
| BROWSER_DESTINATION | &quot;BrowserDestination&quot; |
| DESTINATION_BY_NATION | &quot;DestinationByNation&quot; |
| UNIQUE_DESTINATION | &quot;UniqueDestination&quot; |
| SEQUENTIAL_DESTINATION | &quot;SequentialDestination&quot; |
| WEIGHTED_DESTINATION | &quot;WeightedDestination&quot; |



## Enum: RedirectTypeEnum

| Name | Value |
|---- | -----|
| PERMANENT_REDIRECT | &quot;PermanentRedirect&quot; |
| TEMPORARY_REDIRECT | &quot;TemporaryRedirect&quot; |



## Enum: ReferrerCleanEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| CLEAN | &quot;Clean&quot; |
| MYSELF | &quot;Myself&quot; |




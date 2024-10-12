

# ApiCoreDtoDatapointsDatapoint


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationDate** | **String** |  (A date in \&quot;YmdHis\&quot; format) |  [optional] |
|**encodeIp** | **Boolean** |  |  [optional] |
|**fifthConversionId** | **Long** |  |  [optional] |
|**fifthConversionName** | **String** |  |  [optional] |
|**firstConversionId** | **Long** |  |  [optional] |
|**firstConversionName** | **String** |  |  [optional] |
|**fourthConversionId** | **Long** |  |  [optional] |
|**fourthConversionName** | **String** |  |  [optional] |
|**groupId** | **Long** |  |  [optional] |
|**groupName** | **String** |  |  [optional] |
|**id** | **Long** |  |  [optional] |
|**isPublic** | **Boolean** |  |  [optional] |
|**isSecured** | **Boolean** |  |  [optional] |
|**lightTracking** | **Boolean** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**notes** | **String** |  |  [optional] |
|**preferred** | **Boolean** |  |  [optional] |
|**redirectOnly** | **Boolean** |  |  [optional] |
|**secondConversionId** | **Long** |  |  [optional] |
|**secondConversionName** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tags** | [**List&lt;ApiCoreDtoTagsTag&gt;**](ApiCoreDtoTagsTag.md) |  |  [optional] |
|**thirdConversionId** | **Long** |  |  [optional] |
|**thirdConversionName** | **String** |  |  [optional] |
|**title** | **String** |  |  [optional] |
|**trackingCode** | **String** |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |
|**typeTL** | [**ApiCoreDtoDatapointsTrackingLinkSpecifics**](ApiCoreDtoDatapointsTrackingLinkSpecifics.md) |  |  [optional] |
|**typeTP** | [**ApiCoreDtoDatapointsTrackingPixelSpecifics**](ApiCoreDtoDatapointsTrackingPixelSpecifics.md) |  |  [optional] |
|**writePermited** | **Boolean** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| PAUSED | &quot;Paused&quot; |
| ABUSE | &quot;Abuse&quot; |
| DELETED | &quot;Deleted&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TRACKING_LINK | &quot;TrackingLink&quot; |
| TRACKING_PIXEL | &quot;TrackingPixel&quot; |




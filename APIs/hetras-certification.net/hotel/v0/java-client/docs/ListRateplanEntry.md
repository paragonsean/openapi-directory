

# ListRateplanEntry


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**Map&lt;String, LinkObject&gt;**](LinkObject.md) | Collection of links to related resources |  [optional] |
|**accessControl** | [**List&lt;AccessControlInfo&gt;**](AccessControlInfo.md) | List of distribution channel groups and channels the rateplan is sold through |  [optional] |
|**active** | **Boolean** | Defines if the rateplan has been ended and is expired |  [optional] |
|**activePeriods** | [**List&lt;DatePeriod&gt;**](DatePeriod.md) | List of active periods. Arrival and departure day for reservations based on this rateplan need to              fit into one of these time periods |  [optional] |
|**baseRateplan** | **String** | Code of the base rateplan if this rateplan is derived |  [optional] |
|**bookingPeriods** | [**List&lt;DatePeriod&gt;**](DatePeriod.md) | List of booking periods. During these time periods the rateplan is sold |  [optional] |
|**code** | **String** | Code of the rateplan |  [optional] |
|**commissionable** | **Boolean** | Defines if this rateplan is setup with a commission |  [optional] |
|**created** | **OffsetDateTime** | Timestamp the rateplan was created |  [optional] |
|**dayUse** | **Boolean** | Defines if this rateplan is used for day use reservations |  [optional] |
|**derivedRateplans** | **List&lt;String&gt;** | List of codes for all derived rateplans if any |  [optional] |
|**description** | **String** | Description of the rateplan |  [optional] |
|**group** | **String** | Code of the rateplan group |  [optional] |
|**includedServices** | **List&lt;String&gt;** | List of codes for the included services sold with this rateplan |  [optional] |
|**isYieldable** | **Boolean** | Gives the information if this rateplan is Yieldable rateplan |  [optional] |
|**marketCode** | **String** | The code of the market segment the rate plan is linked to |  [optional] |
|**name** | **String** | Name of the rateplan |  [optional] |
|**roomTypes** | [**List&lt;EmbeddedRoomTypeSimple&gt;**](EmbeddedRoomTypeSimple.md) | List of all room types sold through this rateplan |  [optional] |
|**suspended** | **Boolean** | Defines if a rateplan is suspended and no new reservations can be created for this              rateplan at the moment |  [optional] |
|**updated** | **OffsetDateTime** | Timestamp of when the rateplan was changed the last time |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Defines if this rateplan is visible to the public or only for specific customers |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| PUBLIC | &quot;Public&quot; |
| NEGOTIATED | &quot;Negotiated&quot; |




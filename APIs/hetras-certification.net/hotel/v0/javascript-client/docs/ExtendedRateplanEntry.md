# HetrasHotelApiVersion0.ExtendedRateplanEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**{String: LinkObject}**](LinkObject.md) | Collection of links to related resources | [optional] 
**accessControl** | [**[AccessControlInfo]**](AccessControlInfo.md) | List of distribution channel groups and channels the rateplan is sold through | [optional] 
**active** | **Boolean** | Defines if the rateplan has been ended and is expired | [optional] 
**activePeriods** | [**[DatePeriod]**](DatePeriod.md) | List of active periods. Arrival and departure day for reservations based on this rateplan need to              fit into one of these time periods | [optional] 
**bookingPeriods** | [**[DatePeriod]**](DatePeriod.md) | List of booking periods. During these time periods the rateplan is sold | [optional] 
**code** | **String** | Code of the rateplan | [optional] 
**commissionable** | **Boolean** | Defines if this rateplan is setup with a commission | [optional] 
**created** | **Date** | Timestamp the rateplan was created | [optional] 
**dayUse** | **Boolean** | Defines if this rateplan is used for day use reservations | [optional] 
**derivation** | [**Derivation**](Derivation.md) |  | [optional] 
**derivedRateplans** | [**[RelatedRateplan]**](RelatedRateplan.md) | Details about all the derived rateplans if any | [optional] 
**description** | **String** | Description of the rateplan | [optional] 
**folioName** | **String** | Text defining how the room charges for this rateplan are shown on the folio and              invoice for the guest | [optional] 
**group** | [**RateplanGroup**](RateplanGroup.md) |  | [optional] 
**includedServices** | **[String]** | List of codes for the included services sold with this rateplan | [optional] 
**isYieldable** | **Boolean** | Gives the information if this rateplan is Yieldable rateplan | [optional] 
**marketCode** | **String** | The code of the market segment the rate plan is linked to | [optional] 
**name** | **String** | Name of the rateplan | [optional] 
**noshowPolicy** | **String** | The code of the noshow policy for this rateplan | [optional] 
**restrictions** | [**Restrictions**](Restrictions.md) |  | [optional] 
**roomTypes** | [**[EmbeddedRoomType]**](EmbeddedRoomType.md) | List of all room types sold through this rateplan | [optional] 
**suspended** | **Boolean** | Defines if a rateplan is suspended and no new reservations can be created for this              rateplan at the moment | [optional] 
**taxesIncluded** | **Boolean** | Defines if the daily rates include VAT or not | [optional] 
**updated** | **Date** | Timestamp of when the rateplan was changed the last time | [optional] 
**visibility** | **String** | Defines if this rateplan is visible to the public or only for specific customers | [optional] 



## Enum: VisibilityEnum


* `Public` (value: `"Public"`)

* `Negotiated` (value: `"Negotiated"`)





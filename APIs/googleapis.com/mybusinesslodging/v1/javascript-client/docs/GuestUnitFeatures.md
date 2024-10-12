# MyBusinessLodgingApi.GuestUnitFeatures

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bungalowOrVilla** | **Boolean** | Bungalow or villa. An independent structure that is part of a hotel or resort that is rented to one party for a vacation stay. The hotel or resort may be completely comprised of bungalows or villas, or they may be one of several guestroom options. Guests in the bungalows or villas most often have the same, if not more, amenities and services offered to guests in other guestroom types. | [optional] 
**bungalowOrVillaException** | **String** | Bungalow or villa exception. | [optional] 
**connectingUnitAvailable** | **Boolean** | Connecting unit available. A guestroom type that features access to an adjacent guestroom for the purpose of booking both rooms. Most often used by families who need more than one room to accommodate the number of people in their group. | [optional] 
**connectingUnitAvailableException** | **String** | Connecting unit available exception. | [optional] 
**executiveFloor** | **Boolean** | Executive floor. A floor of the hotel where the guestrooms are only bookable by members of the hotel&#39;s frequent guest membership program. Benefits of this room class include access to a designated lounge which may or may not feature free breakfast, cocktails or other perks specific to members of the program. | [optional] 
**executiveFloorException** | **String** | Executive floor exception. | [optional] 
**maxAdultOccupantsCount** | **Number** | Max adult occupants count. The total number of adult guests allowed to stay overnight in the guestroom. | [optional] 
**maxAdultOccupantsCountException** | **String** | Max adult occupants count exception. | [optional] 
**maxChildOccupantsCount** | **Number** | Max child occupants count. The total number of children allowed to stay overnight in the room. | [optional] 
**maxChildOccupantsCountException** | **String** | Max child occupants count exception. | [optional] 
**maxOccupantsCount** | **Number** | Max occupants count. The total number of guests allowed to stay overnight in the guestroom. | [optional] 
**maxOccupantsCountException** | **String** | Max occupants count exception. | [optional] 
**privateHome** | **Boolean** | Private home. A privately owned home (house, townhouse, apartment, cabin, bungalow etc) that may or not serve as the owner&#39;s residence, but is rented out in its entirety or by the room(s) to paying guest(s) for vacation stays. Not for lease-based, long-term residency. | [optional] 
**privateHomeException** | **String** | Private home exception. | [optional] 
**suite** | **Boolean** | Suite. A guestroom category that implies both a bedroom area and a separate living area. There may or may not be full walls and doors separating the two areas, but regardless, they are very distinct. Does not mean a couch or chair in a bedroom. | [optional] 
**suiteException** | **String** | Suite exception. | [optional] 
**tier** | **String** | Tier. Classification of the unit based on available features/amenities. A non-standard tier is only permitted if at least one other unit type falls under the standard tier. | [optional] 
**tierException** | **String** | Tier exception. | [optional] 
**totalLivingAreas** | [**LivingArea**](LivingArea.md) |  | [optional] 
**views** | [**ViewsFromUnit**](ViewsFromUnit.md) |  | [optional] 



## Enum: BungalowOrVillaExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: ConnectingUnitAvailableExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: ExecutiveFloorExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: MaxAdultOccupantsCountExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: MaxChildOccupantsCountExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: MaxOccupantsCountExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: PrivateHomeExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: SuiteExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: TierEnum


* `UNIT_TIER_UNSPECIFIED` (value: `"UNIT_TIER_UNSPECIFIED"`)

* `STANDARD_UNIT` (value: `"STANDARD_UNIT"`)

* `DELUXE_UNIT` (value: `"DELUXE_UNIT"`)





## Enum: TierExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





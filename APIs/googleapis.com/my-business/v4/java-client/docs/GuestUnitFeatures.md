

# GuestUnitFeatures

Features and available amenities in the guest unit.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bungalowOrVilla** | **Boolean** | Bungalow or villa. An independent structure that is part of a hotel or resort that is rented to one party for a vacation stay. The hotel or resort may be completely comprised of bungalows or villas, or they may be one of several guestroom options. Guests in the bungalows or villas most often have the same, if not more, amenities and services offered to guests in other guestroom types. |  [optional] |
|**bungalowOrVillaException** | [**BungalowOrVillaExceptionEnum**](#BungalowOrVillaExceptionEnum) | Bungalow or villa exception. |  [optional] |
|**connectingUnitAvailable** | **Boolean** | Connecting unit available. A guestroom type that features access to an adjacent guestroom for the purpose of booking both rooms. Most often used by families who need more than one room to accommodate the number of people in their group. |  [optional] |
|**connectingUnitAvailableException** | [**ConnectingUnitAvailableExceptionEnum**](#ConnectingUnitAvailableExceptionEnum) | Connecting unit available exception. |  [optional] |
|**executiveFloor** | **Boolean** | Executive floor. A floor of the hotel where the guestrooms are only bookable by members of the hotel&#39;s frequent guest membership program. Benefits of this room class include access to a designated lounge which may or may not feature free breakfast, cocktails or other perks specific to members of the program. |  [optional] |
|**executiveFloorException** | [**ExecutiveFloorExceptionEnum**](#ExecutiveFloorExceptionEnum) | Executive floor exception. |  [optional] |
|**maxAdultOccupantsCount** | **Integer** | Max adult occupants count. The total number of adult guests allowed to stay overnight in the guestroom. |  [optional] |
|**maxAdultOccupantsCountException** | [**MaxAdultOccupantsCountExceptionEnum**](#MaxAdultOccupantsCountExceptionEnum) | Max adult occupants count exception. |  [optional] |
|**maxChildOccupantsCount** | **Integer** | Max child occupants count. The total number of children allowed to stay overnight in the room. |  [optional] |
|**maxChildOccupantsCountException** | [**MaxChildOccupantsCountExceptionEnum**](#MaxChildOccupantsCountExceptionEnum) | Max child occupants count exception. |  [optional] |
|**maxOccupantsCount** | **Integer** | Max occupants count. The total number of guests allowed to stay overnight in the guestroom. |  [optional] |
|**maxOccupantsCountException** | [**MaxOccupantsCountExceptionEnum**](#MaxOccupantsCountExceptionEnum) | Max occupants count exception. |  [optional] |
|**privateHome** | **Boolean** | Private home. A privately owned home (house, townhouse, apartment, cabin, bungalow etc) that may or not serve as the owner&#39;s residence, but is rented out in its entirety or by the room(s) to paying guest(s) for vacation stays. Not for lease-based, long-term residency. |  [optional] |
|**privateHomeException** | [**PrivateHomeExceptionEnum**](#PrivateHomeExceptionEnum) | Private home exception. |  [optional] |
|**suite** | **Boolean** | Suite. A guestroom category that implies both a bedroom area and a separate living area. There may or may not be full walls and doors separating the two areas, but regardless, they are very distinct. Does not mean a couch or chair in a bedroom. |  [optional] |
|**suiteException** | [**SuiteExceptionEnum**](#SuiteExceptionEnum) | Suite exception. |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | Tier. Classification of the unit based on available features/amenities. A non-standard tier is only permitted if at least one other unit type falls under the standard tier. |  [optional] |
|**tierException** | [**TierExceptionEnum**](#TierExceptionEnum) | Tier exception. |  [optional] |
|**totalLivingAreas** | [**LivingArea**](LivingArea.md) |  |  [optional] |
|**views** | [**ViewsFromUnit**](ViewsFromUnit.md) |  |  [optional] |



## Enum: BungalowOrVillaExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: ConnectingUnitAvailableExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: ExecutiveFloorExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: MaxAdultOccupantsCountExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: MaxChildOccupantsCountExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: MaxOccupantsCountExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: PrivateHomeExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: SuiteExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| UNIT_TIER_UNSPECIFIED | &quot;UNIT_TIER_UNSPECIFIED&quot; |
| STANDARD_UNIT | &quot;STANDARD_UNIT&quot; |
| DELUXE_UNIT | &quot;DELUXE_UNIT&quot; |



## Enum: TierExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |




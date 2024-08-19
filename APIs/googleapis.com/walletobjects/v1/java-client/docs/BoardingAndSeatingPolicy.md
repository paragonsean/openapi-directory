

# BoardingAndSeatingPolicy


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**boardingPolicy** | [**BoardingPolicyEnum**](#BoardingPolicyEnum) | Indicates the policy the airline uses for boarding. If unset, Google will default to &#x60;zoneBased&#x60;. |  [optional] |
|**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#boardingAndSeatingPolicy\&quot;&#x60;. |  [optional] |
|**seatClassPolicy** | [**SeatClassPolicyEnum**](#SeatClassPolicyEnum) | Seating policy which dictates how we display the seat class. If unset, Google will default to &#x60;cabinBased&#x60;. |  [optional] |



## Enum: BoardingPolicyEnum

| Name | Value |
|---- | -----|
| BOARDING_POLICY_UNSPECIFIED | &quot;BOARDING_POLICY_UNSPECIFIED&quot; |
| ZONE_BASED | &quot;ZONE_BASED&quot; |
| ZONE_BASED2 | &quot;zoneBased&quot; |
| GROUP_BASED | &quot;GROUP_BASED&quot; |
| GROUP_BASED2 | &quot;groupBased&quot; |
| BOARDING_POLICY_OTHER | &quot;BOARDING_POLICY_OTHER&quot; |
| BOARDING_POLICY_OTHER2 | &quot;boardingPolicyOther&quot; |



## Enum: SeatClassPolicyEnum

| Name | Value |
|---- | -----|
| SEAT_CLASS_POLICY_UNSPECIFIED | &quot;SEAT_CLASS_POLICY_UNSPECIFIED&quot; |
| CABIN_BASED | &quot;CABIN_BASED&quot; |
| CABIN_BASED2 | &quot;cabinBased&quot; |
| CLASS_BASED | &quot;CLASS_BASED&quot; |
| CLASS_BASED2 | &quot;classBased&quot; |
| TIER_BASED | &quot;TIER_BASED&quot; |
| TIER_BASED2 | &quot;tierBased&quot; |
| SEAT_CLASS_POLICY_OTHER | &quot;SEAT_CLASS_POLICY_OTHER&quot; |
| SEAT_CLASS_POLICY_OTHER2 | &quot;seatClassPolicyOther&quot; |




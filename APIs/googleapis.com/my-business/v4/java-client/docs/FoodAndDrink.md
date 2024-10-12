

# FoodAndDrink

Meals, snacks, and beverages available at the property.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bar** | **Boolean** | Bar. A designated room, lounge or area of an on-site restaurant with seating at a counter behind which a hotel staffer takes the guest&#39;s order and provides the requested alcoholic drink. Can be indoors or outdoors. Also known as Pub. |  [optional] |
|**barException** | [**BarExceptionEnum**](#BarExceptionEnum) | Bar exception. |  [optional] |
|**breakfastAvailable** | **Boolean** | Breakfast available. The morning meal is offered to all guests. Can be free or for a fee. |  [optional] |
|**breakfastAvailableException** | [**BreakfastAvailableExceptionEnum**](#BreakfastAvailableExceptionEnum) | Breakfast available exception. |  [optional] |
|**breakfastBuffet** | **Boolean** | Breakfast buffet. Breakfast meal service where guests serve themselves from a variety of dishes/foods that are put out on a table. |  [optional] |
|**breakfastBuffetException** | [**BreakfastBuffetExceptionEnum**](#BreakfastBuffetExceptionEnum) | Breakfast buffet exception. |  [optional] |
|**buffet** | **Boolean** | Buffet. A type of meal where guests serve themselves from a variety of dishes/foods that are put out on a table. Includes lunch and/or dinner meals. A breakfast-only buffet is not sufficient. |  [optional] |
|**buffetException** | [**BuffetExceptionEnum**](#BuffetExceptionEnum) | Buffet exception. |  [optional] |
|**dinnerBuffet** | **Boolean** | Dinner buffet. Dinner meal service where guests serve themselves from a variety of dishes/foods that are put out on a table. |  [optional] |
|**dinnerBuffetException** | [**DinnerBuffetExceptionEnum**](#DinnerBuffetExceptionEnum) | Dinner buffet exception. |  [optional] |
|**freeBreakfast** | **Boolean** | Free breakfast. Breakfast is offered for free to all guests. Does not apply if limited to certain room packages. |  [optional] |
|**freeBreakfastException** | [**FreeBreakfastExceptionEnum**](#FreeBreakfastExceptionEnum) | Free breakfast exception. |  [optional] |
|**restaurant** | **Boolean** | Restaurant. A business onsite at the hotel that is open to the public as well as guests, and offers meals and beverages to consume at tables or counters. May or may not include table service. Also known as cafe, buffet, eatery. A \&quot;breakfast room\&quot; where the hotel serves breakfast only to guests (not the general public) does not count as a restaurant. |  [optional] |
|**restaurantException** | [**RestaurantExceptionEnum**](#RestaurantExceptionEnum) | Restaurant exception. |  [optional] |
|**restaurantsCount** | **Integer** | Restaurants count. The number of restaurants at the hotel. |  [optional] |
|**restaurantsCountException** | [**RestaurantsCountExceptionEnum**](#RestaurantsCountExceptionEnum) | Restaurants count exception. |  [optional] |
|**roomService** | **Boolean** | Room service. A hotel staffer delivers meals prepared onsite to a guest&#39;s room as per their request. May or may not be available during specific hours. Services should be available to all guests (not based on rate/room booked/reward program, etc). |  [optional] |
|**roomServiceException** | [**RoomServiceExceptionEnum**](#RoomServiceExceptionEnum) | Room service exception. |  [optional] |
|**tableService** | **Boolean** | Table service. A restaurant in which a staff member is assigned to a guest&#39;s table to take their order, deliver and clear away food, and deliver the bill, if applicable. Also known as sit-down restaurant. |  [optional] |
|**tableServiceException** | [**TableServiceExceptionEnum**](#TableServiceExceptionEnum) | Table service exception. |  [optional] |
|**twentyFourHourRoomService** | **Boolean** | 24hr room service. Room service is available 24 hours a day. |  [optional] |
|**twentyFourHourRoomServiceException** | [**TwentyFourHourRoomServiceExceptionEnum**](#TwentyFourHourRoomServiceExceptionEnum) | 24hr room service exception. |  [optional] |
|**vendingMachine** | **Boolean** | Vending machine. A glass-fronted mechanized cabinet displaying and dispensing snacks and beverages for purchase by coins, paper money and/or credit cards. |  [optional] |
|**vendingMachineException** | [**VendingMachineExceptionEnum**](#VendingMachineExceptionEnum) | Vending machine exception. |  [optional] |



## Enum: BarExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: BreakfastAvailableExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: BreakfastBuffetExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: BuffetExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: DinnerBuffetExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: FreeBreakfastExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: RestaurantExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: RestaurantsCountExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: RoomServiceExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: TableServiceExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: TwentyFourHourRoomServiceExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: VendingMachineExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |




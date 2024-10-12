# MyBusinessLodgingApi.Policies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allInclusiveAvailable** | **Boolean** | All inclusive available. The hotel offers a rate option that includes the cost of the room, meals, activities, and other amenities that might otherwise be charged separately. | [optional] 
**allInclusiveAvailableException** | **String** | All inclusive available exception. | [optional] 
**allInclusiveOnly** | **Boolean** | All inclusive only. The only rate option offered by the hotel is a rate that includes the cost of the room, meals, activities and other amenities that might otherwise be charged separately. | [optional] 
**allInclusiveOnlyException** | **String** | All inclusive only exception. | [optional] 
**checkinTime** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**checkinTimeException** | **String** | Check-in time exception. | [optional] 
**checkoutTime** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**checkoutTimeException** | **String** | Check-out time exception. | [optional] 
**kidsStayFree** | **Boolean** | Kids stay free. The children of guests are allowed to stay in the room/suite of a parent or adult without an additional fee. The policy may or may not stipulate a limit of the child&#39;s age or the overall number of children allowed. | [optional] 
**kidsStayFreeException** | **String** | Kids stay free exception. | [optional] 
**maxChildAge** | **Number** | Max child age. The hotel allows children up to a certain age to stay in the room/suite of a parent or adult without an additional fee. | [optional] 
**maxChildAgeException** | **String** | Max child age exception. | [optional] 
**maxKidsStayFreeCount** | **Number** | Max kids stay free count. The hotel allows a specific, defined number of children to stay in the room/suite of a parent or adult without an additional fee. | [optional] 
**maxKidsStayFreeCountException** | **String** | Max kids stay free count exception. | [optional] 
**paymentOptions** | [**PaymentOptions**](PaymentOptions.md) |  | [optional] 
**smokeFreeProperty** | **Boolean** | Smoke free property. Smoking is not allowed inside the building, on balconies, or in outside spaces. Hotels that offer a designated area for guests to smoke are not considered smoke-free properties. | [optional] 
**smokeFreePropertyException** | **String** | Smoke free property exception. | [optional] 



## Enum: AllInclusiveAvailableExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: AllInclusiveOnlyExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: CheckinTimeExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: CheckoutTimeExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: KidsStayFreeExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: MaxChildAgeExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: MaxKidsStayFreeCountExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





## Enum: SmokeFreePropertyExceptionEnum


* `EXCEPTION_UNSPECIFIED` (value: `"EXCEPTION_UNSPECIFIED"`)

* `UNDER_CONSTRUCTION` (value: `"UNDER_CONSTRUCTION"`)

* `DEPENDENT_ON_SEASON` (value: `"DEPENDENT_ON_SEASON"`)

* `DEPENDENT_ON_DAY_OF_WEEK` (value: `"DEPENDENT_ON_DAY_OF_WEEK"`)





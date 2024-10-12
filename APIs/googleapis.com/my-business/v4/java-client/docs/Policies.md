

# Policies

Property rules that impact guests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allInclusiveAvailable** | **Boolean** | All inclusive available. The hotel offers a rate option that includes the cost of the room, meals, activities, and other amenities that might otherwise be charged separately. |  [optional] |
|**allInclusiveAvailableException** | [**AllInclusiveAvailableExceptionEnum**](#AllInclusiveAvailableExceptionEnum) | All inclusive available exception. |  [optional] |
|**allInclusiveOnly** | **Boolean** | All inclusive only. The only rate option offered by the hotel is a rate that includes the cost of the room, meals, activities and other amenities that might otherwise be charged separately. |  [optional] |
|**allInclusiveOnlyException** | [**AllInclusiveOnlyExceptionEnum**](#AllInclusiveOnlyExceptionEnum) | All inclusive only exception. |  [optional] |
|**checkinTime** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |
|**checkinTimeException** | [**CheckinTimeExceptionEnum**](#CheckinTimeExceptionEnum) | Check-in time exception. |  [optional] |
|**checkoutTime** | [**TimeOfDay**](TimeOfDay.md) |  |  [optional] |
|**checkoutTimeException** | [**CheckoutTimeExceptionEnum**](#CheckoutTimeExceptionEnum) | Check-out time exception. |  [optional] |
|**kidsStayFree** | **Boolean** | Kids stay free. The children of guests are allowed to stay in the room/suite of a parent or adult without an additional fee. The policy may or may not stipulate a limit of the child&#39;s age or the overall number of children allowed. |  [optional] |
|**kidsStayFreeException** | [**KidsStayFreeExceptionEnum**](#KidsStayFreeExceptionEnum) | Kids stay free exception. |  [optional] |
|**maxChildAge** | **Integer** | Max child age. The hotel allows children up to a certain age to stay in the room/suite of a parent or adult without an additional fee. |  [optional] |
|**maxChildAgeException** | [**MaxChildAgeExceptionEnum**](#MaxChildAgeExceptionEnum) | Max child age exception. |  [optional] |
|**maxKidsStayFreeCount** | **Integer** | Max kids stay free count. The hotel allows a specific, defined number of children to stay in the room/suite of a parent or adult without an additional fee. |  [optional] |
|**maxKidsStayFreeCountException** | [**MaxKidsStayFreeCountExceptionEnum**](#MaxKidsStayFreeCountExceptionEnum) | Max kids stay free count exception. |  [optional] |
|**paymentOptions** | [**PaymentOptions**](PaymentOptions.md) |  |  [optional] |
|**smokeFreeProperty** | **Boolean** | Smoke free property. Smoking is not allowed inside the building, on balconies, or in outside spaces. Hotels that offer a designated area for guests to smoke are not considered smoke-free properties. |  [optional] |
|**smokeFreePropertyException** | [**SmokeFreePropertyExceptionEnum**](#SmokeFreePropertyExceptionEnum) | Smoke free property exception. |  [optional] |



## Enum: AllInclusiveAvailableExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: AllInclusiveOnlyExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: CheckinTimeExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: CheckoutTimeExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: KidsStayFreeExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: MaxChildAgeExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: MaxKidsStayFreeCountExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |



## Enum: SmokeFreePropertyExceptionEnum

| Name | Value |
|---- | -----|
| EXCEPTION_UNSPECIFIED | &quot;EXCEPTION_UNSPECIFIED&quot; |
| UNDER_CONSTRUCTION | &quot;UNDER_CONSTRUCTION&quot; |
| DEPENDENT_ON_SEASON | &quot;DEPENDENT_ON_SEASON&quot; |
| DEPENDENT_ON_DAY_OF_WEEK | &quot;DEPENDENT_ON_DAY_OF_WEEK&quot; |




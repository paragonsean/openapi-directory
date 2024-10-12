# ViatorApiDocumentationAmpSpecificationMerchantPartners.BookingStatusItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amended** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking has been amended | [optional] 
**cancelled** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking has been cancelled | [optional] 
**confirmed** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking is confirmed | [optional] 
**failed** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking has failed | [optional] 
**level** | **String** | **level** of *this* item&#39;s booking status | [optional] 
**pending** | **Boolean** | **indicator**: &#x60;true&#x60; if *this* item&#39;s booking is pending | [optional] 
**status** | **Number** | **numeric identifier** of *this* item&#39;s booking status | [optional] 
**text** | **String** | **natural-language description** of *this* item&#39;s booking status; e.g., &#39;Waiting to be booked&#39; | [optional] 
**type** | **String** | **specifier** of *this* item&#39;s booking status * See: [bookingStatus fields and meanings](#section/Appendices/bookingStatus-field-values-and-meanings)  | [optional] 



## Enum: LevelEnum


* `ITEM` (value: `"ITEM"`)

* `ITINERARY` (value: `"ITINERARY"`)





## Enum: TypeEnum


* `WAITING` (value: `"WAITING"`)

* `CONFIRMED` (value: `"CONFIRMED"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `PENDING` (value: `"PENDING"`)

* `FAILED` (value: `"FAILED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `AMENDED` (value: `"AMENDED"`)

* `PENDING_AMEND` (value: `"PENDING_AMEND"`)

* `REJECTED` (value: `"REJECTED"`)

* `ON_HOLD` (value: `"ON_HOLD"`)





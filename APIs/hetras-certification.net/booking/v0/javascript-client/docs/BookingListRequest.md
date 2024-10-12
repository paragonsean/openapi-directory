# HetrasBookingApiVersion0.BookingListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockCode** | **String** | Return all bookings where the block code matches the specified value. | [optional] 
**cancellationId** | **String** | Return bookings for this cancellation id. | [optional] 
**channelCodes** | **[String]** | Return all bookings where the channel code is one of the specified values. | [optional] 
**companyEmail** | **String** | Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
**companyId** | **String** | Return all bookings the id of the company or travel agent profile matches the specified value. | [optional] 
**companyName** | **String** | Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
**customerEmail** | **String** | Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
**customerId** | **String** | Return all bookings the id of one of the guests or the contact matches the specified value. | [optional] 
**customerName** | **String** | Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. | [optional] 
**dateFilter** | **String** | Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range. | [optional] 
**exclude** | **String** | To be able to request reservations without personal data based on GDPR. | [optional] 
**externalId** | **String** | Return all bookings exactly matching the specified external id. This filter is case sensitive. | [optional] 
**from** | **Date** | Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later. | [optional] 
**hotelId** | **Number** | Only return bookings for this specific hotel. | [optional] 
**labels** | **[String]** | Return all reservations with at least one of the specified labels. | [optional] 
**marketCodes** | **[String]** | Return all bookings where the market code is one of the specified values. | [optional] 
**ratePlanCodes** | **[String]** | Return all bookings where the rate plan code is one of the specified values. | [optional] 
**reservationNumber** | **Number** | Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels. | [optional] 
**reservationStatuses** | **[String]** | Return all bookings where the reservation status is one of the specified values. | [optional] 
**roomNumber** | **String** | Return all bookings having the specified room number assigned. | [optional] 
**roomTypes** | **[String]** | Return all bookings where the room type is one of the specified values. | [optional] 
**subChannelCodes** | **[String]** | Return all bookings where the subchannel code is one of the specified values. | [optional] 
**to** | **Date** | End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier. | [optional] 



## Enum: DateFilterEnum


* `ArrivalDate` (value: `"ArrivalDate"`)

* `DepartureDate` (value: `"DepartureDate"`)

* `StayDate` (value: `"StayDate"`)

* `CreationDate` (value: `"CreationDate"`)

* `ModificationDate` (value: `"ModificationDate"`)





## Enum: ExcludeEnum


* `Customers` (value: `"Customers"`)





## Enum: [ReservationStatusesEnum]


* `Tentative` (value: `"Tentative"`)

* `Waitlisted` (value: `"Waitlisted"`)

* `OnRequest` (value: `"OnRequest"`)

* `NonGuaranteed` (value: `"NonGuaranteed"`)

* `Guaranteed` (value: `"Guaranteed"`)

* `InHouse` (value: `"InHouse"`)

* `CheckedOut` (value: `"CheckedOut"`)

* `NoShow` (value: `"NoShow"`)

* `Denied` (value: `"Denied"`)

* `Cancelled` (value: `"Cancelled"`)

* `Released` (value: `"Released"`)

* `Walked` (value: `"Walked"`)

* `Expired` (value: `"Expired"`)

* `WalkIn` (value: `"WalkIn"`)

* `Registered` (value: `"Registered"`)







# BookingListRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blockCode** | **String** | Return all bookings where the block code matches the specified value. |  [optional] |
|**cancellationId** | **String** | Return bookings for this cancellation id. |  [optional] |
|**channelCodes** | **List&lt;String&gt;** | Return all bookings where the channel code is one of the specified values. |  [optional] |
|**companyEmail** | **String** | Return all bookings where the primary email address of the company or the travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. |  [optional] |
|**companyId** | **String** | Return all bookings the id of the company or travel agent profile matches the specified value. |  [optional] |
|**companyName** | **String** | Return all bookings where the name of the linked company or travel agent profile contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. |  [optional] |
|**customerEmail** | **String** | Return all bookings where the primary email address of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. |  [optional] |
|**customerId** | **String** | Return all bookings the id of one of the guests or the contact matches the specified value. |  [optional] |
|**customerName** | **String** | Return all bookings where the first or lastname of one of the guests or the contact contains the specified value. The search is executed case insensitive              and also stripping of any whitespaces. |  [optional] |
|**dateFilter** | [**DateFilterEnum**](#DateFilterEnum) | Select a date field you want to filter bookings by. Only one filter at a time can be applied. The to and from dates              will then define the time range. |  [optional] |
|**exclude** | [**ExcludeEnum**](#ExcludeEnum) | To be able to request reservations without personal data based on GDPR. |  [optional] |
|**externalId** | **String** | Return all bookings exactly matching the specified external id. This filter is case sensitive. |  [optional] |
|**from** | **OffsetDateTime** | Start date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or later. |  [optional] |
|**hotelId** | **Integer** | Only return bookings for this specific hotel. |  [optional] |
|**labels** | **List&lt;String&gt;** | Return all reservations with at least one of the specified labels. |  [optional] |
|**marketCodes** | **List&lt;String&gt;** | Return all bookings where the market code is one of the specified values. |  [optional] |
|**ratePlanCodes** | **List&lt;String&gt;** | Return all bookings where the rate plan code is one of the specified values. |  [optional] |
|**reservationNumber** | **Integer** | Return bookings matching this reservation number. Please note that reservation numbers are only unique within a hotel. If you              don´t specify a hotel filter at the same time you could get back multiple bookings from different hotels. |  [optional] |
|**reservationStatuses** | [**List&lt;ReservationStatusesEnum&gt;**](#List&lt;ReservationStatusesEnum&gt;) | Return all bookings where the reservation status is one of the specified values. |  [optional] |
|**roomNumber** | **String** | Return all bookings having the specified room number assigned. |  [optional] |
|**roomTypes** | **List&lt;String&gt;** | Return all bookings where the room type is one of the specified values. |  [optional] |
|**subChannelCodes** | **List&lt;String&gt;** | Return all bookings where the subchannel code is one of the specified values. |  [optional] |
|**to** | **OffsetDateTime** | End date for the selected date filter. If you select arrival date as date filter the bookings returned will have at least              one reservation arriving on the specified date or earlier. |  [optional] |



## Enum: DateFilterEnum

| Name | Value |
|---- | -----|
| ARRIVAL_DATE | &quot;ArrivalDate&quot; |
| DEPARTURE_DATE | &quot;DepartureDate&quot; |
| STAY_DATE | &quot;StayDate&quot; |
| CREATION_DATE | &quot;CreationDate&quot; |
| MODIFICATION_DATE | &quot;ModificationDate&quot; |



## Enum: ExcludeEnum

| Name | Value |
|---- | -----|
| CUSTOMERS | &quot;Customers&quot; |



## Enum: List&lt;ReservationStatusesEnum&gt;

| Name | Value |
|---- | -----|
| TENTATIVE | &quot;Tentative&quot; |
| WAITLISTED | &quot;Waitlisted&quot; |
| ON_REQUEST | &quot;OnRequest&quot; |
| NON_GUARANTEED | &quot;NonGuaranteed&quot; |
| GUARANTEED | &quot;Guaranteed&quot; |
| IN_HOUSE | &quot;InHouse&quot; |
| CHECKED_OUT | &quot;CheckedOut&quot; |
| NO_SHOW | &quot;NoShow&quot; |
| DENIED | &quot;Denied&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| RELEASED | &quot;Released&quot; |
| WALKED | &quot;Walked&quot; |
| EXPIRED | &quot;Expired&quot; |
| WALK_IN | &quot;WalkIn&quot; |
| REGISTERED | &quot;Registered&quot; |




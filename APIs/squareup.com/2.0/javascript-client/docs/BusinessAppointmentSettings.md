# SquareConnectApi.BusinessAppointmentSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alignmentTime** | **String** | The time unit of the service duration for bookings. | [optional] 
**anyTeamMemberBookingEnabled** | **Boolean** | Indicates whether a customer can choose from all available time slots and have a staff member assigned automatically (&#x60;true&#x60;) or not (&#x60;false&#x60;). | [optional] 
**cancellationFeeMoney** | [**Money**](Money.md) |  | [optional] 
**cancellationPolicy** | **String** | The cancellation policy adopted by the seller. | [optional] 
**cancellationPolicyText** | **String** | The free-form text of the seller&#39;s cancellation policy. | [optional] 
**cancellationWindowSeconds** | **Number** | The cut-off time in seconds for allowing clients to cancel or reschedule an appointment. | [optional] 
**locationTypes** | **[String]** | Types of the location allowed for bookings. | [optional] 
**maxAppointmentsPerDayLimit** | **Number** | The maximum number of daily appointments per team member or per location. | [optional] 
**maxAppointmentsPerDayLimitType** | **String** | Indicates whether the daily appointment limit applies to team members or to business locations. | [optional] 
**maxBookingLeadTimeSeconds** | **Number** | The maximum lead time in seconds before a service can be booked. Bookings must be created at most this far ahead of the booking&#39;s starting time. | [optional] 
**minBookingLeadTimeSeconds** | **Number** | The minimum lead time in seconds before a service can be booked. Bookings must be created at least this far ahead of the booking&#39;s starting time. | [optional] 
**multipleServiceBookingEnabled** | **Boolean** | Indicates whether a customer can book multiple services in a single online booking. | [optional] 
**skipBookingFlowStaffSelection** | **Boolean** | Indicates whether customers has an assigned staff member (&#x60;true&#x60;) or can select s staff member of their choice (&#x60;false&#x60;). | [optional] 



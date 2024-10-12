

# AppointmentTemplate

Appointment templates are blocks of time during which a doctor usually sees appointments with the same profile. These may have a longer duration then the corresponding profile, in which case they may allow multiple appointments to be booked during that period.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** | Indicats that the object has been soft-deleted and should not be used |  [optional] [readonly] |
|**dateEnd** | **String** |  |  [optional] |
|**dateStart** | **String** |  |  [optional] |
|**duration** | **Integer** | Length of an appointment in minutes |  [optional] |
|**examRoom** | **Integer** | **1-based** index for the exam room |  |
|**id** | **Integer** |  |  [optional] [readonly] |
|**office** | **Integer** |  |  |
|**openSlots** | [**List&lt;OpenSlot&gt;**](OpenSlot.md) | Array of time intervals during which the template is available. Only computed if the available and verbose query parameters are passed. Note that only slots long enough to fit an appointment with the corresponding profile are included. |  [optional] |
|**profile** | **Integer** | ID of the appointment profile to default to |  |
|**scheduledTime** | **String** |  |  |
|**weekDays** | **List&lt;Integer&gt;** | Array of integers that indicate week days (&#x60;0&#x60; &#x3D; Monday, ..., &#x60;6&#x60; &#x3D; Sunday) |  |




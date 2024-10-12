

# AppointmentProfile

Appointment profiles are for common kinds of appointments a doctor might have, such as \"physical exam\", which have a standard duration and should show up as the same color on the calendar.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**archived** | **Boolean** | Indicates that the object has been soft-deleted and should not be used |  [optional] [readonly] |
|**color** | **String** |  |  |
|**doctor** | **Integer** |  |  [optional] |
|**duration** | **Integer** | Length of an appointment in minutes |  [optional] |
|**id** | **Integer** |  |  [optional] [readonly] |
|**name** | **String** |  |  |
|**onlineScheduling** | **Boolean** | Whether this profile should be available for online scheduling |  |
|**reason** | **String** |  |  [optional] |
|**sortOrder** | **Integer** | Override the usual ordering ordering of appointments in the patient&#39;s appointments page. Lower values are shown at the top |  [optional] |




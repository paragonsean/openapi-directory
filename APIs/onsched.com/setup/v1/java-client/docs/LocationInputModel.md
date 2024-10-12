

# LocationInputModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**AddressInputModel**](AddressInputModel.md) |  |  [optional] |
|**adminEmail** | **String** | Field is required. |  [optional] |
|**adminName** | **String** | This field is no longer required and has been deprecated. |  [optional] |
|**appointmentReminders** | [**AppointmentRemindersInputModel**](AppointmentRemindersInputModel.md) |  |  [optional] |
|**businessHours** | [**BusinessHoursInputModel**](BusinessHoursInputModel.md) |  |  [optional] |
|**defaults** | [**BusinessDefaultsInputModel**](BusinessDefaultsInputModel.md) |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**fax** | **String** |  |  [optional] |
|**friendlyId** | **String** | Use the friendlyId as an alternative to the assigned locationId  Choose something easy and meaningful. Must be unique within your company.  FriendlyId&#39;s are limited to maximum of 64 characters. |  [optional] |
|**name** | **String** |  |  [optional] |
|**phone** | **String** | GroupSize Limits the number of people that can come  along on a single appointment |  [optional] |
|**regionId** | **String** |  |  [optional] |
|**settings** | [**OnlineSettingsInputModel**](OnlineSettingsInputModel.md) |  |  [optional] |
|**timezoneName** | **String** | Field is required. It is in Iana format. e.g. America/New_York. Use moment.js in your client for ease of timezone detection and selection |  [optional] |
|**website** | **String** |  |  [optional] |




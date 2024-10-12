# SmartMe.RegisterRealtimeApiData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apiUrl** | **String** | The URL of your endpoint. To this endpoint all the values are send to. | [optional] 
**basicAuthPassword** | **String** | The Password (basic auth) of your endpoint. Leave empty of none. | [optional] 
**basicAuthUsername** | **String** | The Username (basic auth) of your endpoint. Leave empty of none. | [optional] 
**id** | **String** | The ID of the registration | [optional] 
**meterId** | **String** | The ID of the Meter. Just used if the RegistrationType is \&quot;SingleMeterRegistration\&quot;. | [optional] 
**registrationType** | **String** | The Type of this registration (per meter, per user, ...) | [optional] 
**serialNumber** | **String** | The serial number of the Meter. Just used if the RegistrationType is \&quot;SingleMeterRegistration\&quot; and the MeterId is null.               Example: 1 SME 01 63000000 or 6300000 | [optional] 



## Enum: RegistrationTypeEnum


* `Disabled` (value: `"Disabled"`)

* `SingleMeterRegistration` (value: `"SingleMeterRegistration"`)

* `UserRegistration` (value: `"UserRegistration"`)





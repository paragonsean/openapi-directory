# SasPortalApiTesting.SasPortalUpdateSignedDeviceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encodedDevice** | **Blob** | Required. The JSON Web Token signed using a CPI private key. Payload must be the JSON encoding of the device. The user_id field must be set. | [optional] 
**installerId** | **String** | Required. Unique installer ID (CPI ID) from the Certified Professional Installers database. | [optional] 



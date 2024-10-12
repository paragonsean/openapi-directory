# SasPortalApiTesting.SasPortalValidateInstallerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encodedSecret** | **String** | Required. JSON Web Token signed using a CPI private key. Payload must include a \&quot;secret\&quot; claim whose value is the secret. | [optional] 
**installerId** | **String** | Required. Unique installer id (CPI ID) from the Certified Professional Installers database. | [optional] 
**secret** | **String** | Required. Secret returned by the GenerateSecret. | [optional] 



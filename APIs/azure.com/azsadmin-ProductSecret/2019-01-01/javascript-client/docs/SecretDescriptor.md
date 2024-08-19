# DeploymentAdminClient.SecretDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedCharacters** | **String** | The allowed characters in the password | [optional] 
**alternativeDnsNames** | **[String]** | Alternative DNS Names. | [optional] 
**alternativeIpAddresses** | **[String]** | The list of alternative IP addresses. | [optional] 
**keyLength** | **Number** | The key length. | [optional] 
**passwordLength** | **Number** | The minimum password length is 8 characters, and the maximum password length is 128 characters. | [optional] 
**passwordValidationRegex** | **String** | Password validation regular expression. | [optional] 
**rotationStatus** | **String** | The storage account key secret rotation status. | [optional] 
**secondaryKeyIsActive** | **Boolean** | A value indicating whether the secondary or primary storage account key is active as a secret. | [optional] 
**subject** | **String** | Certificate&#39;s subject | [optional] 



## Enum: RotationStatusEnum


* `None` (value: `"None"`)

* `PlantNewSak` (value: `"PlantNewSak"`)

* `RotateInactiveSak` (value: `"RotateInactiveSak"`)

* `Complete` (value: `"Complete"`)





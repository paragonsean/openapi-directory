

# SecretDescriptor

The secret type-specific descriptor.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedCharacters** | **String** | The allowed characters in the password |  [optional] |
|**alternativeDnsNames** | **List&lt;String&gt;** | Alternative DNS Names. |  [optional] |
|**alternativeIpAddresses** | **List&lt;String&gt;** | The list of alternative IP addresses. |  [optional] |
|**keyLength** | **Integer** | The key length. |  [optional] |
|**passwordLength** | **Integer** | The minimum password length is 8 characters, and the maximum password length is 128 characters. |  [optional] |
|**passwordValidationRegex** | **String** | Password validation regular expression. |  [optional] |
|**rotationStatus** | [**RotationStatusEnum**](#RotationStatusEnum) | The storage account key secret rotation status. |  [optional] |
|**secondaryKeyIsActive** | **Boolean** | A value indicating whether the secondary or primary storage account key is active as a secret. |  [optional] |
|**subject** | **String** | Certificate&#39;s subject |  [optional] |



## Enum: RotationStatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PLANT_NEW_SAK | &quot;PlantNewSak&quot; |
| ROTATE_INACTIVE_SAK | &quot;RotateInactiveSak&quot; |
| COMPLETE | &quot;Complete&quot; |






# SharedAccessSignatureAuthorizationRuleAccessRightsDescription

Description of the shared access key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyName** | **String** | Name of the key. |  |
|**primaryKey** | **String** | Primary SAS key value. |  [optional] |
|**rights** | [**RightsEnum**](#RightsEnum) | Rights that this key has. |  |
|**secondaryKey** | **String** | Secondary SAS key value. |  [optional] |



## Enum: RightsEnum

| Name | Value |
|---- | -----|
| SERVICE_CONFIG | &quot;ServiceConfig&quot; |
| ENROLLMENT_READ | &quot;EnrollmentRead&quot; |
| ENROLLMENT_WRITE | &quot;EnrollmentWrite&quot; |
| DEVICE_CONNECT | &quot;DeviceConnect&quot; |
| REGISTRATION_STATUS_READ | &quot;RegistrationStatusRead&quot; |
| REGISTRATION_STATUS_WRITE | &quot;RegistrationStatusWrite&quot; |




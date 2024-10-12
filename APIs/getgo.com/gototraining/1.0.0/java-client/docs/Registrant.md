

# Registrant

Describes a training registrant.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confirmationUrl** | **String** | The URL where the confirmation for the registration can be found |  |
|**email** | **String** | The registrant&#39;s email address |  |
|**givenName** | **String** | The registrant&#39;s first name |  |
|**joinUrl** | **String** | The URL the registrant will use to join the training |  |
|**registrantKey** | **String** | The registrant&#39;s key |  |
|**registrationDate** | **OffsetDateTime** | The date and time the registration took place |  |
|**status** | [**StatusEnum**](#StatusEnum) | The registrant&#39;s status |  |
|**surname** | **String** | The registrant&#39;s surname |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| WAITING | &quot;WAITING&quot; |
| APPROVED | &quot;APPROVED&quot; |
| DENIED | &quot;DENIED&quot; |




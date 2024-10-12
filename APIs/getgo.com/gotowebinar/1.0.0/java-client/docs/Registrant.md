

# Registrant

Describes a webinar registrant

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | **String** | The registrant&#39;s email address |  |
|**firstName** | **String** | The registrant&#39;s first name |  |
|**joinUrl** | **String** | The URL the registrant will use to join the webinar |  |
|**lastName** | **String** | The registrant&#39;s last name |  |
|**registrantKey** | **Long** | The registrant&#39;s key |  |
|**registrationDate** | **OffsetDateTime** | The registration date and time |  |
|**status** | [**StatusEnum**](#StatusEnum) | The registration status |  |
|**timeZone** | **String** | The time zone where the webinar will take place |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| APPROVED | &quot;APPROVED&quot; |
| DENIED | &quot;DENIED&quot; |
| WAITING | &quot;WAITING&quot; |




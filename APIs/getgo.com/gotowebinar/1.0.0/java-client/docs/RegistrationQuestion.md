

# RegistrationQuestion

Describes a custom field for a webinar registration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answers** | [**List&lt;RegistrationAnswer&gt;**](RegistrationAnswer.md) | The answers to a multiple choice custom registration field |  [optional] |
|**maxSize** | **Integer** | The character size of the custom registration field (max 1000) |  |
|**question** | **String** | The value (text) of the custom registration field |  |
|**questionKey** | **Long** | The unique key of the custom registration field |  |
|**required** | **Boolean** | Indicates whether the custom registration field is compulsory |  |
|**type** | [**TypeEnum**](#TypeEnum) | Indicates whether the custom registration field requires a single short answer or whether it is a multiple choice question |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MULTIPLE_CHOICE | &quot;multipleChoice&quot; |
| SHORT_ANSWER | &quot;shortAnswer&quot; |




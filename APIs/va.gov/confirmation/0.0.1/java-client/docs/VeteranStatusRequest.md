

# VeteranStatusRequest

Attributes required to retrieve a Veteran's status

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**birthDate** | **String** | Birth date for the person of interest in any valid ISO8601 format |  |
|**firstName** | **String** | First name for the person of interest |  |
|**gender** | [**GenderEnum**](#GenderEnum) | Optional gender of M or F for the person of interest |  [optional] |
|**lastName** | **String** | Last name for the person of interest |  |
|**middleName** | **String** | Optional middle name for the person of interest |  [optional] |
|**ssn** | **String** | Social Security Number for the person of interest with or without dashes |  |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| M | &quot;M&quot; |
| F | &quot;F&quot; |




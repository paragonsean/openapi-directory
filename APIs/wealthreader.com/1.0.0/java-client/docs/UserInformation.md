

# UserInformation

Información relativa a la persona que hace login

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ID** | **String** |  |  |
|**address** | **String** |  |  [optional] |
|**birthDate** | **LocalDate** |  |  [optional] |
|**birthPlace** | **String** |  |  [optional] |
|**cellPhone** | **String** | Número de teléfono con el prefijo internacional, sin espacios |  [optional] |
|**city** | **String** |  |  [optional] |
|**country** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**gender** | [**GenderEnum**](#GenderEnum) |  |  [optional] |
|**job** | **String** | El valor aquí es muy variable de una entidad a otra: de indicar solamente si es cuenta propia o cuenta ajena a indicar el tipo de profesión |  [optional] |
|**maritalStatus** | [**MaritalStatusEnum**](#MaritalStatusEnum) |  |  [optional] |
|**name** | **String** |  |  |
|**postalCode** | **String** |  |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| MALE | &quot;male&quot; |
| FEMALE | &quot;female&quot; |



## Enum: MaritalStatusEnum

| Name | Value |
|---- | -----|
| SINGLE | &quot;single&quot; |
| MARRIED | &quot;married&quot; |




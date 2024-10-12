

# Holiday

A Canadian holiday. Includes a name, the literal date of the holiday, the observed date of the holiday (ie, accommodating for weekends), and a list of regions that observe this holiday.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **LocalDate** | ISO date: the literal date of the holiday |  |
|**federal** | [**FederalEnum**](#FederalEnum) | Whether this holiday is observed by federally-regulated industries. |  |
|**id** | **Integer** | Primary key for a holiday |  |
|**nameEn** | **String** | English name |  |
|**nameFr** | **String** | French name |  |
|**observedDate** | **LocalDate** | ISO date: when this holiday is observed |  |
|**optional** | [**OptionalEnum**](#OptionalEnum) | Whether this is a province-wide statutory holiday, or one that is optional for employers. |  [optional] |
|**provinces** | [**List&lt;Province&gt;**](Province.md) |  |  [optional] |



## Enum: FederalEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |
| NUMBER_0 | 0 |



## Enum: OptionalEnum

| Name | Value |
|---- | -----|
| NUMBER_1 | 1 |




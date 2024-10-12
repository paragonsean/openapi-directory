

# Score

Represents dataset scores. A score is a number between 0 and 1 that indicates how trustworthy the person, vehicle, or company is accordig to the result of the background check. Severity represents the risk associated with each dataset according to the background check. Keep in mind that you should use either the score or the severity but not both

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**byId** | [**ScoreDetail**](ScoreDetail.md) |  |  |
|**byName** | [**ScoreDetail**](ScoreDetail.md) |  |  |
|**dataSet** | [**DataSetEnum**](#DataSetEnum) | Dataset summed up to create the score |  |
|**result** | [**ResultEnum**](#ResultEnum) | Overall result of the data collected. If at least one collected data status is found, the result will be found, otherwise, it will be the most frecuent status |  [optional] |
|**score** | **Float** | Dataset score. Number between 0 and 1 where 1 is the best score. |  |
|**severity** | [**SeverityEnum**](#SeverityEnum) | Risk asociated with each category for the search according to the information found. None is returned when the person, vehicle or company is in the clear. Unknown is returned when the score is none due to a problem with one of the searches |  |



## Enum: DataSetEnum

| Name | Value |
|---- | -----|
| AFFILIATIONS_AND_INSURANCES | &quot;affiliations_and_insurances&quot; |
| ALERT_IN_MEDIA | &quot;alert_in_media&quot; |
| BEHAVIOR | &quot;behavior&quot; |
| BUSINESS_BACKGROUND | &quot;business_background&quot; |
| CRIMINAL_RECORD | &quot;criminal_record&quot; |
| DRIVING_LICENSES | &quot;driving_licenses&quot; |
| INTERNATIONAL_BACKGROUND | &quot;international_background&quot; |
| LEGAL_BACKGROUND | &quot;legal_background&quot; |
| PERSONAL_IDENTITY | &quot;personal_identity&quot; |
| PROFESSIONAL_BACKGROUND | &quot;professional_background&quot; |
| TRAFFIC_FINES | &quot;traffic_fines&quot; |
| VEHICLE_INFORMATION | &quot;vehicle_information&quot; |
| VEHICLE_PERMITS | &quot;vehicle_permits&quot; |
| TAXES_AND_FINANCES | &quot;taxes_and_finances&quot; |



## Enum: ResultEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| FOUND | &quot;found&quot; |
| NOT_FOUND | &quot;not_found&quot; |
| ERROR | &quot;error&quot; |
| DELAYED | &quot;delayed&quot; |
| IGNORED | &quot;ignored&quot; |



## Enum: SeverityEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;unknown&quot; |
| NONE | &quot;none&quot; |
| VERY_LOW | &quot;very_low&quot; |
| LOW | &quot;low&quot; |
| MEDIUM | &quot;medium&quot; |
| HIGH | &quot;high&quot; |
| VERY_HIGH | &quot;very_high&quot; |




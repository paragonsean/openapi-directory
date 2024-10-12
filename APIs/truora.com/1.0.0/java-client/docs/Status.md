

# Status

Represents the status of databases used to generate background checks

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSet** | [**DataSetEnum**](#DataSetEnum) | Background check dataset |  [optional] |
|**databaseId** | **String** | Database ID. Can be used to verify the database status |  [optional] |
|**databaseName** | **String** | Background check database name. Do not use this field to identify the database as it may change during the check execution. Use database_id instead |  [optional] |
|**invalidInputs** | **List&lt;String&gt;** | List of missing or invalid inputs |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the search finished successfully, **error** means the search failed, **expired** means the search took too long to finish and therefore failed, **skipped** means the search failed because a wrong number or type of parameters was provided, **delayed** means the search is waiting for an additional requirement to be met and can last up to 3 days |  [optional] |



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



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;not_started&quot; |
| COMPLETED | &quot;completed&quot; |
| EXPIRED | &quot;expired&quot; |
| ERROR | &quot;error&quot; |
| DELAYED | &quot;delayed&quot; |
| SKIPPED | &quot;skipped&quot; |




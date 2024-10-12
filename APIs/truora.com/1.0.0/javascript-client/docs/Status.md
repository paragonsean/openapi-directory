# ChecksApi.Status

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSet** | **String** | Background check dataset | [optional] 
**databaseId** | **String** | Database ID. Can be used to verify the database status | [optional] 
**databaseName** | **String** | Background check database name. Do not use this field to identify the database as it may change during the check execution. Use database_id instead | [optional] 
**invalidInputs** | **[String]** | List of missing or invalid inputs | [optional] 
**status** | **String** | Result status of the background check. **Not_started** means the background check is still in queue, since there is a limit of background checks that can be processed simultaneously, **completed** means the search finished successfully, **error** means the search failed, **expired** means the search took too long to finish and therefore failed, **skipped** means the search failed because a wrong number or type of parameters was provided, **delayed** means the search is waiting for an additional requirement to be met and can last up to 3 days | [optional] 



## Enum: DataSetEnum


* `affiliations_and_insurances` (value: `"affiliations_and_insurances"`)

* `alert_in_media` (value: `"alert_in_media"`)

* `behavior` (value: `"behavior"`)

* `business_background` (value: `"business_background"`)

* `criminal_record` (value: `"criminal_record"`)

* `driving_licenses` (value: `"driving_licenses"`)

* `international_background` (value: `"international_background"`)

* `legal_background` (value: `"legal_background"`)

* `personal_identity` (value: `"personal_identity"`)

* `professional_background` (value: `"professional_background"`)

* `traffic_fines` (value: `"traffic_fines"`)

* `vehicle_information` (value: `"vehicle_information"`)

* `vehicle_permits` (value: `"vehicle_permits"`)

* `taxes_and_finances` (value: `"taxes_and_finances"`)





## Enum: StatusEnum


* `not_started` (value: `"not_started"`)

* `completed` (value: `"completed"`)

* `expired` (value: `"expired"`)

* `error` (value: `"error"`)

* `delayed` (value: `"delayed"`)

* `skipped` (value: `"skipped"`)





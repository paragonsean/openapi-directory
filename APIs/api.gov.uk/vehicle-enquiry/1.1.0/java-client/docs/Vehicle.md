

# Vehicle


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artEndDate** | **LocalDate** | Additional Rate of Tax End Date, format: YYYY-MM-DD |  [optional] |
|**co2Emissions** | **Integer** | Carbon Dioxide emissions in grams per kilometre |  [optional] |
|**colour** | **String** | Vehicle colour |  [optional] |
|**dateOfLastV5CIssued** | **LocalDate** | Date of last V5C issued |  [optional] |
|**engineCapacity** | **Integer** | Engine capacity in cubic centimetres |  [optional] |
|**euroStatus** | **String** | Euro Status (Dealer / Customer Provided (new vehicles)) |  [optional] |
|**fuelType** | **String** | Fuel type (Method of Propulsion) |  [optional] |
|**make** | **String** | Vehicle make |  [optional] |
|**markedForExport** | **Boolean** | True only if vehicle has been export marked |  [optional] |
|**monthOfFirstDvlaRegistration** | **LocalDate** | Month of First DVLA Registration |  [optional] |
|**monthOfFirstRegistration** | **LocalDate** | Month of First Registration |  [optional] |
|**motExpiryDate** | **LocalDate** | Mot Expiry Date |  [optional] |
|**motStatus** | [**MotStatusEnum**](#MotStatusEnum) | MOT Status of the vehicle |  [optional] |
|**realDrivingEmissions** | **String** | Real Driving Emissions value |  [optional] |
|**registrationNumber** | **String** | Registration number of the vehicle |  |
|**revenueWeight** | **Integer** | Revenue weight in kilograms |  [optional] |
|**taxDueDate** | **LocalDate** | Date of tax liablity, Used in calculating licence information presented to user |  [optional] |
|**taxStatus** | [**TaxStatusEnum**](#TaxStatusEnum) | Tax status of the vehicle |  [optional] |
|**typeApproval** | **String** | Vehicle Type Approval Category |  [optional] |
|**wheelplan** | **String** | Vehicle wheel plan |  [optional] |
|**yearOfManufacture** | **Integer** | Year of Manufacture |  [optional] |



## Enum: MotStatusEnum

| Name | Value |
|---- | -----|
| NO_DETAILS_HELD_BY_DVLA | &quot;No details held by DVLA&quot; |
| NO_RESULTS_RETURNED | &quot;No results returned&quot; |
| NOT_VALID | &quot;Not valid&quot; |
| VALID | &quot;Valid&quot; |



## Enum: TaxStatusEnum

| Name | Value |
|---- | -----|
| NOT_TAXED_FOR_ON_ROAD_USE | &quot;Not Taxed for on Road Use&quot; |
| SORN | &quot;SORN&quot; |
| TAXED | &quot;Taxed&quot; |
| UNTAXED | &quot;Untaxed&quot; |




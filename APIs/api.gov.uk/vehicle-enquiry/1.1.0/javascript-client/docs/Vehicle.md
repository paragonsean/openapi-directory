# VehicleEnquiryApi.Vehicle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artEndDate** | **Date** | Additional Rate of Tax End Date, format: YYYY-MM-DD | [optional] 
**co2Emissions** | **Number** | Carbon Dioxide emissions in grams per kilometre | [optional] 
**colour** | **String** | Vehicle colour | [optional] 
**dateOfLastV5CIssued** | **Date** | Date of last V5C issued | [optional] 
**engineCapacity** | **Number** | Engine capacity in cubic centimetres | [optional] 
**euroStatus** | **String** | Euro Status (Dealer / Customer Provided (new vehicles)) | [optional] 
**fuelType** | **String** | Fuel type (Method of Propulsion) | [optional] 
**make** | **String** | Vehicle make | [optional] 
**markedForExport** | **Boolean** | True only if vehicle has been export marked | [optional] 
**monthOfFirstDvlaRegistration** | **Date** | Month of First DVLA Registration | [optional] 
**monthOfFirstRegistration** | **Date** | Month of First Registration | [optional] 
**motExpiryDate** | **Date** | Mot Expiry Date | [optional] 
**motStatus** | **String** | MOT Status of the vehicle | [optional] 
**realDrivingEmissions** | **String** | Real Driving Emissions value | [optional] 
**registrationNumber** | **String** | Registration number of the vehicle | 
**revenueWeight** | **Number** | Revenue weight in kilograms | [optional] 
**taxDueDate** | **Date** | Date of tax liablity, Used in calculating licence information presented to user | [optional] 
**taxStatus** | **String** | Tax status of the vehicle | [optional] 
**typeApproval** | **String** | Vehicle Type Approval Category | [optional] 
**wheelplan** | **String** | Vehicle wheel plan | [optional] 
**yearOfManufacture** | **Number** | Year of Manufacture | [optional] 



## Enum: MotStatusEnum


* `No details held by DVLA` (value: `"No details held by DVLA"`)

* `No results returned` (value: `"No results returned"`)

* `Not valid` (value: `"Not valid"`)

* `Valid` (value: `"Valid"`)





## Enum: TaxStatusEnum


* `Not Taxed for on Road Use` (value: `"Not Taxed for on Road Use"`)

* `SORN` (value: `"SORN"`)

* `Taxed` (value: `"Taxed"`)

* `Untaxed` (value: `"Untaxed"`)





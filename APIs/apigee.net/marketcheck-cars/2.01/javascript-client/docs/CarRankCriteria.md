# MarketcheckApis.CarRankCriteria

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carfax1Owner** | **Number** | Flag to indicate whether listing is carfax_1_owner.Weight for this is ranking process between 0-1. | [optional] [default to 0.9]
**carfaxCleanTitle** | **Number** | Flag to indicate whether listing is carfax_clean_title.Weight for this is ranking process between 0-1 | [optional] [default to 0.9]
**dom** | **Number** | Days on Market value for the car based on current and historical listings found in the Marketcheck database for this car.Weight for this is ranking process between 0-1 | [optional] [default to 0.9]
**dom180** | **Number** | Days on Market value for the car based on current and last 6 month listings found in the Marketcheck database for this car.Weight for this is ranking process between 0-1 | [optional] [default to 0.9]
**domActive** | **Number** | Days on Market value for the car based on current and last 30 days listings found in the Marketcheck database for this car.Weight for this is ranking process between 0-1 | [optional] [default to 0.9]
**isCertified** | **Number** | Certified car.Weight for this is ranking process between 0-1 | [optional] [default to 1]
**miles** | **Number** | Odometer reading / reported miles usage for the car.Weight for this is ranking process between 0-1 | [optional] [default to 0.9]
**price** | **Number** | Asking price for the vehicle. Weight for this is ranking process between 0-1. | [optional] [default to 0.9]



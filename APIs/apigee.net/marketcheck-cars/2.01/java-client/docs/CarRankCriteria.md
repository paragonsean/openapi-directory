

# CarRankCriteria

Ranking query request

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**carfax1Owner** | **BigDecimal** | Flag to indicate whether listing is carfax_1_owner.Weight for this is ranking process between 0-1. |  [optional] |
|**carfaxCleanTitle** | **BigDecimal** | Flag to indicate whether listing is carfax_clean_title.Weight for this is ranking process between 0-1 |  [optional] |
|**dom** | **BigDecimal** | Days on Market value for the car based on current and historical listings found in the Marketcheck database for this car.Weight for this is ranking process between 0-1 |  [optional] |
|**dom180** | **BigDecimal** | Days on Market value for the car based on current and last 6 month listings found in the Marketcheck database for this car.Weight for this is ranking process between 0-1 |  [optional] |
|**domActive** | **BigDecimal** | Days on Market value for the car based on current and last 30 days listings found in the Marketcheck database for this car.Weight for this is ranking process between 0-1 |  [optional] |
|**isCertified** | **BigDecimal** | Certified car.Weight for this is ranking process between 0-1 |  [optional] |
|**miles** | **BigDecimal** | Odometer reading / reported miles usage for the car.Weight for this is ranking process between 0-1 |  [optional] |
|**price** | **BigDecimal** | Asking price for the vehicle. Weight for this is ranking process between 0-1. |  [optional] |




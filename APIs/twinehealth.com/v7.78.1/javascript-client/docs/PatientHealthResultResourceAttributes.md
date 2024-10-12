# FitbitPlusApi.PatientHealthResultResourceAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread** | **String** | Links together results. This should be the same as the thread of _action, if it is defined | [optional] 
**aggregation** | **String** |  | [optional] 
**annotations** | [**[PatientHealthResultResourceAttributesAnnotationsInner]**](PatientHealthResultResourceAttributesAnnotationsInner.md) |  | [optional] 
**channel** | **String** |  | [optional] 
**data** | [**PatientHealthResultResourceAttributesData**](PatientHealthResultResourceAttributesData.md) |  | [optional] 
**externalId** | **String** |  | [optional] 
**metricType** | **String** |  | [optional] 
**occurredAt** | **String** |  | [optional] 
**occurredAtTimeZone** | **String** |  | [optional] 
**skipped** | **Boolean** |  | [optional] 
**source** | [**PatientHealthResultResourceAttributesSource**](PatientHealthResultResourceAttributesSource.md) |  | [optional] 
**type** | **String** | Type of result. Usually the same as metric_type except for lifestyle actions | [optional] 
**window** | **String** |  | [optional] 



## Enum: MetricTypeEnum


* `blood_pressure_systolic` (value: `"blood_pressure_systolic"`)

* `blood_pressure_diastolic` (value: `"blood_pressure_diastolic"`)

* `hemoglobin_a1c` (value: `"hemoglobin_a1c"`)

* `hdl_cholesterol` (value: `"hdl_cholesterol"`)

* `ldl_cholesterol` (value: `"ldl_cholesterol"`)

* `total_cholesterol` (value: `"total_cholesterol"`)

* `triglycerides` (value: `"triglycerides"`)

* `blood_urea_nitrogen` (value: `"blood_urea_nitrogen"`)

* `creatinine` (value: `"creatinine"`)

* `hemoglobin` (value: `"hemoglobin"`)

* `hematocrit` (value: `"hematocrit"`)

* `total_serum_iron` (value: `"total_serum_iron"`)

* `thyroid_stimulating_hormone` (value: `"thyroid_stimulating_hormone"`)

* `free_thyroxine` (value: `"free_thyroxine"`)

* `free_triiodothyronine` (value: `"free_triiodothyronine"`)

* `total_triiodothyronine` (value: `"total_triiodothyronine"`)

* `cd4_cell_count` (value: `"cd4_cell_count"`)

* `hiv_viral_load` (value: `"hiv_viral_load"`)

* `inr` (value: `"inr"`)

* `free_testosterone` (value: `"free_testosterone"`)

* `total_testosterone` (value: `"total_testosterone"`)

* `c_reactive_protein` (value: `"c_reactive_protein"`)

* `prostate_specific_antigen` (value: `"prostate_specific_antigen"`)

* `cotinine` (value: `"cotinine"`)

* `c_peptide` (value: `"c_peptide"`)

* `blood_pressure` (value: `"blood_pressure"`)

* `blood_glucose` (value: `"blood_glucose"`)

* `weight` (value: `"weight"`)

* `heart_rate` (value: `"heart_rate"`)

* `body_fat_percentage` (value: `"body_fat_percentage"`)

* `body_mass_index` (value: `"body_mass_index"`)

* `body_temperature` (value: `"body_temperature"`)

* `forced_expiratory_volume1` (value: `"forced_expiratory_volume1"`)

* `forced_vital_capacity` (value: `"forced_vital_capacity"`)

* `lean_body_mass` (value: `"lean_body_mass"`)

* `nausea_level` (value: `"nausea_level"`)

* `oxygen_saturation` (value: `"oxygen_saturation"`)

* `pain_level` (value: `"pain_level"`)

* `peak_expiratory_flow_rate` (value: `"peak_expiratory_flow_rate"`)

* `peripheral_perfusion_index` (value: `"peripheral_perfusion_index"`)

* `respiratory_rate` (value: `"respiratory_rate"`)

* `inhaler_usage` (value: `"inhaler_usage"`)





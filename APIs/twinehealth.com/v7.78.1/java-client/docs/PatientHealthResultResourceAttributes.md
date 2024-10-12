

# PatientHealthResultResourceAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**thread** | **String** | Links together results. This should be the same as the thread of _action, if it is defined |  [optional] |
|**aggregation** | **String** |  |  [optional] |
|**annotations** | [**List&lt;PatientHealthResultResourceAttributesAnnotationsInner&gt;**](PatientHealthResultResourceAttributesAnnotationsInner.md) |  |  [optional] |
|**channel** | **String** |  |  [optional] |
|**data** | [**PatientHealthResultResourceAttributesData**](PatientHealthResultResourceAttributesData.md) |  |  [optional] |
|**externalId** | **String** |  |  [optional] |
|**metricType** | [**MetricTypeEnum**](#MetricTypeEnum) |  |  [optional] |
|**occurredAt** | **String** |  |  [optional] |
|**occurredAtTimeZone** | **String** |  |  [optional] |
|**skipped** | **Boolean** |  |  [optional] |
|**source** | [**PatientHealthResultResourceAttributesSource**](PatientHealthResultResourceAttributesSource.md) |  |  [optional] |
|**type** | **String** | Type of result. Usually the same as metric_type except for lifestyle actions |  [optional] |
|**window** | **String** |  |  [optional] |



## Enum: MetricTypeEnum

| Name | Value |
|---- | -----|
| BLOOD_PRESSURE_SYSTOLIC | &quot;blood_pressure_systolic&quot; |
| BLOOD_PRESSURE_DIASTOLIC | &quot;blood_pressure_diastolic&quot; |
| HEMOGLOBIN_A1C | &quot;hemoglobin_a1c&quot; |
| HDL_CHOLESTEROL | &quot;hdl_cholesterol&quot; |
| LDL_CHOLESTEROL | &quot;ldl_cholesterol&quot; |
| TOTAL_CHOLESTEROL | &quot;total_cholesterol&quot; |
| TRIGLYCERIDES | &quot;triglycerides&quot; |
| BLOOD_UREA_NITROGEN | &quot;blood_urea_nitrogen&quot; |
| CREATININE | &quot;creatinine&quot; |
| HEMOGLOBIN | &quot;hemoglobin&quot; |
| HEMATOCRIT | &quot;hematocrit&quot; |
| TOTAL_SERUM_IRON | &quot;total_serum_iron&quot; |
| THYROID_STIMULATING_HORMONE | &quot;thyroid_stimulating_hormone&quot; |
| FREE_THYROXINE | &quot;free_thyroxine&quot; |
| FREE_TRIIODOTHYRONINE | &quot;free_triiodothyronine&quot; |
| TOTAL_TRIIODOTHYRONINE | &quot;total_triiodothyronine&quot; |
| CD4_CELL_COUNT | &quot;cd4_cell_count&quot; |
| HIV_VIRAL_LOAD | &quot;hiv_viral_load&quot; |
| INR | &quot;inr&quot; |
| FREE_TESTOSTERONE | &quot;free_testosterone&quot; |
| TOTAL_TESTOSTERONE | &quot;total_testosterone&quot; |
| C_REACTIVE_PROTEIN | &quot;c_reactive_protein&quot; |
| PROSTATE_SPECIFIC_ANTIGEN | &quot;prostate_specific_antigen&quot; |
| COTININE | &quot;cotinine&quot; |
| C_PEPTIDE | &quot;c_peptide&quot; |
| BLOOD_PRESSURE | &quot;blood_pressure&quot; |
| BLOOD_GLUCOSE | &quot;blood_glucose&quot; |
| WEIGHT | &quot;weight&quot; |
| HEART_RATE | &quot;heart_rate&quot; |
| BODY_FAT_PERCENTAGE | &quot;body_fat_percentage&quot; |
| BODY_MASS_INDEX | &quot;body_mass_index&quot; |
| BODY_TEMPERATURE | &quot;body_temperature&quot; |
| FORCED_EXPIRATORY_VOLUME1 | &quot;forced_expiratory_volume1&quot; |
| FORCED_VITAL_CAPACITY | &quot;forced_vital_capacity&quot; |
| LEAN_BODY_MASS | &quot;lean_body_mass&quot; |
| NAUSEA_LEVEL | &quot;nausea_level&quot; |
| OXYGEN_SATURATION | &quot;oxygen_saturation&quot; |
| PAIN_LEVEL | &quot;pain_level&quot; |
| PEAK_EXPIRATORY_FLOW_RATE | &quot;peak_expiratory_flow_rate&quot; |
| PERIPHERAL_PERFUSION_INDEX | &quot;peripheral_perfusion_index&quot; |
| RESPIRATORY_RATE | &quot;respiratory_rate&quot; |
| INHALER_USAGE | &quot;inhaler_usage&quot; |




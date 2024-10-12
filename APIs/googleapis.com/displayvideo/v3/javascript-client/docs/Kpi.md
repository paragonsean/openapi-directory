# DisplayVideo360Api.Kpi

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kpiAmountMicros** | **String** | The goal amount, in micros of the advertiser&#39;s currency. Applicable when kpi_type is one of: * &#x60;KPI_TYPE_CPM&#x60; * &#x60;KPI_TYPE_CPC&#x60; * &#x60;KPI_TYPE_CPA&#x60; * &#x60;KPI_TYPE_CPIAVC&#x60; * &#x60;KPI_TYPE_VCPM&#x60; For example: 1500000 represents 1.5 standard units of the currency. | [optional] 
**kpiPercentageMicros** | **String** | The decimal representation of the goal percentage in micros. Applicable when kpi_type is one of: * &#x60;KPI_TYPE_CTR&#x60; * &#x60;KPI_TYPE_VIEWABILITY&#x60; * &#x60;KPI_TYPE_CLICK_CVR&#x60; * &#x60;KPI_TYPE_IMPRESSION_CVR&#x60; * &#x60;KPI_TYPE_VTR&#x60; * &#x60;KPI_TYPE_AUDIO_COMPLETION_RATE&#x60; * &#x60;KPI_TYPE_VIDEO_COMPLETION_RATE&#x60; For example: 70000 represents 7% (decimal 0.07). | [optional] 
**kpiString** | **String** | A KPI string, which can be empty. Must be UTF-8 encoded with a length of no more than 100 characters. Applicable when kpi_type is &#x60;KPI_TYPE_OTHER&#x60;. | [optional] 
**kpiType** | **String** | Required. The type of KPI. | [optional] 



## Enum: KpiTypeEnum


* `UNSPECIFIED` (value: `"KPI_TYPE_UNSPECIFIED"`)

* `CPM` (value: `"KPI_TYPE_CPM"`)

* `CPC` (value: `"KPI_TYPE_CPC"`)

* `CPA` (value: `"KPI_TYPE_CPA"`)

* `CTR` (value: `"KPI_TYPE_CTR"`)

* `VIEWABILITY` (value: `"KPI_TYPE_VIEWABILITY"`)

* `CPIAVC` (value: `"KPI_TYPE_CPIAVC"`)

* `CPE` (value: `"KPI_TYPE_CPE"`)

* `CLICK_CVR` (value: `"KPI_TYPE_CLICK_CVR"`)

* `IMPRESSION_CVR` (value: `"KPI_TYPE_IMPRESSION_CVR"`)

* `VCPM` (value: `"KPI_TYPE_VCPM"`)

* `VTR` (value: `"KPI_TYPE_VTR"`)

* `AUDIO_COMPLETION_RATE` (value: `"KPI_TYPE_AUDIO_COMPLETION_RATE"`)

* `VIDEO_COMPLETION_RATE` (value: `"KPI_TYPE_VIDEO_COMPLETION_RATE"`)

* `OTHER` (value: `"KPI_TYPE_OTHER"`)





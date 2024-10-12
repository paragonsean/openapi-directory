

# Kpi

Settings that control the key performance indicator, or KPI, of an insertion order.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kpiAmountMicros** | **String** | The goal amount, in micros of the advertiser&#39;s currency. Applicable when kpi_type is one of: * &#x60;KPI_TYPE_CPM&#x60; * &#x60;KPI_TYPE_CPC&#x60; * &#x60;KPI_TYPE_CPA&#x60; * &#x60;KPI_TYPE_CPIAVC&#x60; * &#x60;KPI_TYPE_VCPM&#x60; For example: 1500000 represents 1.5 standard units of the currency. |  [optional] |
|**kpiPercentageMicros** | **String** | The decimal representation of the goal percentage in micros. Applicable when kpi_type is one of: * &#x60;KPI_TYPE_CTR&#x60; * &#x60;KPI_TYPE_VIEWABILITY&#x60; * &#x60;KPI_TYPE_CLICK_CVR&#x60; * &#x60;KPI_TYPE_IMPRESSION_CVR&#x60; * &#x60;KPI_TYPE_VTR&#x60; * &#x60;KPI_TYPE_AUDIO_COMPLETION_RATE&#x60; * &#x60;KPI_TYPE_VIDEO_COMPLETION_RATE&#x60; For example: 70000 represents 7% (decimal 0.07). |  [optional] |
|**kpiString** | **String** | A KPI string, which can be empty. Must be UTF-8 encoded with a length of no more than 100 characters. Applicable when kpi_type is &#x60;KPI_TYPE_OTHER&#x60;. |  [optional] |
|**kpiType** | [**KpiTypeEnum**](#KpiTypeEnum) | Required. The type of KPI. |  [optional] |



## Enum: KpiTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;KPI_TYPE_UNSPECIFIED&quot; |
| CPM | &quot;KPI_TYPE_CPM&quot; |
| CPC | &quot;KPI_TYPE_CPC&quot; |
| CPA | &quot;KPI_TYPE_CPA&quot; |
| CTR | &quot;KPI_TYPE_CTR&quot; |
| VIEWABILITY | &quot;KPI_TYPE_VIEWABILITY&quot; |
| CPIAVC | &quot;KPI_TYPE_CPIAVC&quot; |
| CPE | &quot;KPI_TYPE_CPE&quot; |
| CLICK_CVR | &quot;KPI_TYPE_CLICK_CVR&quot; |
| IMPRESSION_CVR | &quot;KPI_TYPE_IMPRESSION_CVR&quot; |
| VCPM | &quot;KPI_TYPE_VCPM&quot; |
| VTR | &quot;KPI_TYPE_VTR&quot; |
| AUDIO_COMPLETION_RATE | &quot;KPI_TYPE_AUDIO_COMPLETION_RATE&quot; |
| VIDEO_COMPLETION_RATE | &quot;KPI_TYPE_VIDEO_COMPLETION_RATE&quot; |
| OTHER | &quot;KPI_TYPE_OTHER&quot; |




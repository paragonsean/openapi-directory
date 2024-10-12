

# Cohort

Defines a cohort selection criteria. A cohort is a group of users who share a common characteristic. For example, users with the same `firstSessionDate` belong to the same cohort.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateRange** | [**DateRange**](DateRange.md) |  |  [optional] |
|**dimension** | **String** | Dimension used by the cohort. Required and only supports &#x60;firstSessionDate&#x60;. |  [optional] |
|**name** | **String** | Assigns a name to this cohort. The dimension &#x60;cohort&#x60; is valued to this name in a report response. If set, cannot begin with &#x60;cohort_&#x60; or &#x60;RESERVED_&#x60;. If not set, cohorts are named by their zero based index &#x60;cohort_0&#x60;, &#x60;cohort_1&#x60;, etc. |  [optional] |




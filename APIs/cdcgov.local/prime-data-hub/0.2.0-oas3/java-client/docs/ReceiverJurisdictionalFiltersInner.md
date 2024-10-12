

# ReceiverJurisdictionalFiltersInner

A single filter

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**doesNotMatch** | **Boolean** | Ensure that the result does not match |  [optional] |
|**matchFields** | [**MatchFieldsEnum**](#MatchFieldsEnum) | What fields to match in the filter |  [optional] |
|**matchValues** | **List&lt;String&gt;** | What is the value to match against |  [optional] |



## Enum: MatchFieldsEnum

| Name | Value |
|---- | -----|
| FACILITY_OR_PATIENT_ADDRESS | &quot;FACILITY_OR_PATIENT_ADDRESS&quot; |
| FACILITY_ADDRESS | &quot;FACILITY_ADDRESS&quot; |
| FACILITY_NAME | &quot;FACILITY_NAME&quot; |
| ABNORMAL_VALUE | &quot;ABNORMAL_VALUE&quot; |




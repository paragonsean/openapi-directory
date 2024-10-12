# AirflowApiStable.ListTaskInstanceForm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dagIds** | **[String]** | Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**durationGte** | **Number** | Returns objects greater than or equal to the specified values.  This can be combined with duration_lte parameter to receive only the selected period.  | [optional] 
**durationLte** | **Number** | Returns objects less than or equal to the specified values.  This can be combined with duration_gte parameter to receive only the selected range.  | [optional] 
**endDateGte** | **Date** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
**endDateLte** | **Date** | Returns objects less than or equal to the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
**executionDateGte** | **Date** | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte parameter to receive only the selected period.  | [optional] 
**executionDateLte** | **Date** | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte parameter to receive only the selected period.  | [optional] 
**pool** | **[String]** | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**queue** | **[String]** | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**startDateGte** | **Date** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte parameter to receive only the selected period.  | [optional] 
**startDateLte** | **Date** | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period.  | [optional] 
**state** | [**[TaskState]**](TaskState.md) | The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 



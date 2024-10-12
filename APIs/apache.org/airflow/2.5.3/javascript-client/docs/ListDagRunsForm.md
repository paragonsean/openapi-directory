# AirflowApiStable.ListDagRunsForm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dagIds** | **[String]** | Return objects with specific DAG IDs. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 
**endDateGte** | **Date** | Returns objects greater or equal the specified date.  This can be combined with end_date_lte parameter to receive only the selected period.  | [optional] 
**endDateLte** | **Date** | Returns objects less than or equal to the specified date.  This can be combined with end_date_gte parameter to receive only the selected period.  | [optional] 
**executionDateGte** | **Date** | Returns objects greater or equal to the specified date.  This can be combined with execution_date_lte key to receive only the selected period.  | [optional] 
**executionDateLte** | **Date** | Returns objects less than or equal to the specified date.  This can be combined with execution_date_gte key to receive only the selected period.  | [optional] 
**orderBy** | **String** | The name of the field to order the results by. Prefix a field name with &#x60;-&#x60; to reverse the sort order.  *New in version 2.1.0*  | [optional] 
**pageLimit** | **Number** | The numbers of items to return. | [optional] [default to 100]
**pageOffset** | **Number** | The number of items to skip before starting to collect the result set. | [optional] 
**startDateGte** | **Date** | Returns objects greater or equal the specified date.  This can be combined with start_date_lte key to receive only the selected period.  | [optional] 
**startDateLte** | **Date** | Returns objects less or equal the specified date.  This can be combined with start_date_gte parameter to receive only the selected period  | [optional] 
**states** | **[String]** | Return objects with specific states. The value can be repeated to retrieve multiple matching values (OR condition). | [optional] 



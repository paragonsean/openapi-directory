# GoogleWorkspaceAlertCenterApi.ReportingRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alertDetails** | **Blob** | Any other associated alert details, for example, AlertConfiguration. | [optional] 
**name** | **String** | Rule name | [optional] 
**query** | **Blob** | Alert Rule query Sample Query query { condition { filter { expected_application_id: 777491262838 expected_event_name: \&quot;indexable_content_change\&quot; filter_op: IN } } conjunction_operator: OR } | [optional] 



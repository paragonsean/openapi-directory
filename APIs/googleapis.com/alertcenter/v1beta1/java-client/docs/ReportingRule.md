

# ReportingRule

Alerts from Reporting Rules configured by Admin.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertDetails** | **byte[]** | Any other associated alert details, for example, AlertConfiguration. |  [optional] |
|**name** | **String** | Rule name |  [optional] |
|**query** | **byte[]** | Alert Rule query Sample Query query { condition { filter { expected_application_id: 777491262838 expected_event_name: \&quot;indexable_content_change\&quot; filter_op: IN } } conjunction_operator: OR } |  [optional] |




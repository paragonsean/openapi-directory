

# Resource


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | If ID is set that is a permission for a specific resource. if it is not set it is a permission for all resources of that resource type. |  [optional] |
|**name** | **String** | Optional name of the resource if the resource has a name field. |  [optional] |
|**org** | **String** | Optional name of the organization of the organization with orgID. |  [optional] |
|**orgID** | **String** | If orgID is set that is a permission for all resources owned my that org. if it is not set it is a permission for all resources of that resource type. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| AUTHORIZATIONS | &quot;authorizations&quot; |
| BUCKETS | &quot;buckets&quot; |
| DASHBOARDS | &quot;dashboards&quot; |
| ORGS | &quot;orgs&quot; |
| SOURCES | &quot;sources&quot; |
| TASKS | &quot;tasks&quot; |
| TELEGRAFS | &quot;telegrafs&quot; |
| USERS | &quot;users&quot; |
| VARIABLES | &quot;variables&quot; |
| SCRAPERS | &quot;scrapers&quot; |
| SECRETS | &quot;secrets&quot; |
| LABELS | &quot;labels&quot; |
| VIEWS | &quot;views&quot; |
| DOCUMENTS | &quot;documents&quot; |
| NOTIFICATION_RULES | &quot;notificationRules&quot; |
| NOTIFICATION_ENDPOINTS | &quot;notificationEndpoints&quot; |
| CHECKS | &quot;checks&quot; |
| DBRP | &quot;dbrp&quot; |
| NOTEBOOKS | &quot;notebooks&quot; |




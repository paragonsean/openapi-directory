

# NewIssuesNotificationSettingRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | Whether notifications should be sent |  |
|**issueSeverity** | [**IssueSeverityEnum**](#IssueSeverityEnum) | The severity levels of issues to send notifications for (only applicable for &#x60;new-remediations-vulnerabilities&#x60; notificationType) |  |
|**issueType** | [**IssueTypeEnum**](#IssueTypeEnum) | Filter the types of issue to include in notifications (only applicable for &#x60;new-remediations-vulnerabilities&#x60; notificationType) |  |



## Enum: IssueSeverityEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| HIGH | &quot;high&quot; |



## Enum: IssueTypeEnum

| Name | Value |
|---- | -----|
| ALL | &quot;all&quot; |
| VULN | &quot;vuln&quot; |
| LICENSE | &quot;license&quot; |
| NONE | &quot;none&quot; |




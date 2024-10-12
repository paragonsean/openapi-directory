# SnykApi.SetNotificationSettingsRequestNewIssuesRemediations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | Whether notifications should be sent | 
**issueSeverity** | **String** | The severity levels of issues to send notifications for (only applicable for &#x60;new-remediations-vulnerabilities&#x60; notificationType) | 
**issueType** | **String** | Filter the types of issue to include in notifications (only applicable for &#x60;new-remediations-vulnerabilities&#x60; notificationType) | 



## Enum: IssueSeverityEnum


* `all` (value: `"all"`)

* `high` (value: `"high"`)





## Enum: IssueTypeEnum


* `all` (value: `"all"`)

* `vuln` (value: `"vuln"`)

* `license` (value: `"license"`)

* `none` (value: `"none"`)





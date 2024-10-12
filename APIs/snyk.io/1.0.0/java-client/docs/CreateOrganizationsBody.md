

# CreateOrganizationsBody


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupId** | **String** | The group ID. The &#x60;API_KEY&#x60; must have access to this group. |  [optional] |
|**name** | **String** | The name of the new organization |  |
|**sourceOrgId** | **String** | The id of an organization to copy settings from.  If provided, this organization must be associated with the same group.  The items that will be copied are:  Source control integrations (GitHub, GitLab, BitBucket) \\+ Container registries integrations (ACR, Docker Hub, ECR, GCR) \\+ Container orchestrators integrations (Kubernetes) \\+ PaaS and Serverless Integrations (Heroku, AWS Lambda) \\+ Notification integrations (Slack, Jira) \\+ Policies \\+ Ignore settings \\+ Language settings \\+ Infrastructure as Code settings \\+ Snyk Code settings  The following will not be copied across: Service accounts \\+ Members \\+ Projects \\+ Notification preferences |  [optional] |




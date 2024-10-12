

# CreateBackupPlanRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupPlan** | [**CreateBackupPlanRequestBackupPlan**](CreateBackupPlanRequestBackupPlan.md) |  |  |
|**backupPlanTags** | **Map&lt;String, String&gt;** | To help organize your resources, you can assign your own metadata to the resources that you create. Each tag is a key-value pair. The specified tags are assigned to all backups created with this plan. |  [optional] |
|**creatorRequestId** | **String** | &lt;p&gt;Identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a &lt;code&gt;CreatorRequestId&lt;/code&gt; that matches an existing backup plan, that plan is returned. This parameter is optional.&lt;/p&gt; &lt;p&gt;If used, this parameter must contain 1 to 50 alphanumeric or &#39;-_.&#39; characters.&lt;/p&gt; |  [optional] |




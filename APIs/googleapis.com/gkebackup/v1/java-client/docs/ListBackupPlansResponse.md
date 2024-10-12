

# ListBackupPlansResponse

Response message for ListBackupPlans.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupPlans** | [**List&lt;BackupPlan&gt;**](BackupPlan.md) | The list of BackupPlans matching the given criteria. |  [optional] |
|**nextPageToken** | **String** | A token which may be sent as page_token in a subsequent &#x60;ListBackupPlans&#x60; call to retrieve the next page of results. If this field is omitted or empty, then there are no more results to return. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |




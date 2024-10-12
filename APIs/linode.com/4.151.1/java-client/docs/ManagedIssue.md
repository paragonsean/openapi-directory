

# ManagedIssue

An Issue that was detected with a service Linode is managing. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**created** | **OffsetDateTime** | When this Issue was created. Issues are created in response to issues detected with Managed Services, so this is also when the Issue was detected.  |  [optional] [readonly] |
|**entity** | [**ManagedIssueEntity**](ManagedIssueEntity.md) |  |  [optional] |
|**id** | **Integer** | This Issue&#39;s unique ID.  |  [optional] [readonly] |
|**services** | **List&lt;Integer&gt;** | An array of Managed Service IDs that were affected by this Issue.  |  [optional] [readonly] |




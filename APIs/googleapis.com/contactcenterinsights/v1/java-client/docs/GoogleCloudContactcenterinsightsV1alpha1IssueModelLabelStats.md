

# GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStats

Aggregated statistics about an issue model.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**analyzedConversationsCount** | **String** | Number of conversations the issue model has analyzed at this point in time. |  [optional] |
|**issueStats** | [**Map&lt;String, GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStatsIssueStats&gt;**](GoogleCloudContactcenterinsightsV1alpha1IssueModelLabelStatsIssueStats.md) | Statistics on each issue. Key is the issue&#39;s resource name. |  [optional] |
|**unclassifiedConversationsCount** | **String** | Number of analyzed conversations for which no issue was applicable at this point in time. |  [optional] |




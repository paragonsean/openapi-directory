

# GoogleCloudDataplexV1GovernanceEvent

Payload associated with Governance related log events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entity** | [**GoogleCloudDataplexV1GovernanceEventEntity**](GoogleCloudDataplexV1GovernanceEventEntity.md) |  |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | The type of the event. |  [optional] |
|**message** | **String** | The log message. |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| RESOURCE_IAM_POLICY_UPDATE | &quot;RESOURCE_IAM_POLICY_UPDATE&quot; |
| BIGQUERY_TABLE_CREATE | &quot;BIGQUERY_TABLE_CREATE&quot; |
| BIGQUERY_TABLE_UPDATE | &quot;BIGQUERY_TABLE_UPDATE&quot; |
| BIGQUERY_TABLE_DELETE | &quot;BIGQUERY_TABLE_DELETE&quot; |
| BIGQUERY_CONNECTION_CREATE | &quot;BIGQUERY_CONNECTION_CREATE&quot; |
| BIGQUERY_CONNECTION_UPDATE | &quot;BIGQUERY_CONNECTION_UPDATE&quot; |
| BIGQUERY_CONNECTION_DELETE | &quot;BIGQUERY_CONNECTION_DELETE&quot; |
| BIGQUERY_TAXONOMY_CREATE | &quot;BIGQUERY_TAXONOMY_CREATE&quot; |
| BIGQUERY_POLICY_TAG_CREATE | &quot;BIGQUERY_POLICY_TAG_CREATE&quot; |
| BIGQUERY_POLICY_TAG_DELETE | &quot;BIGQUERY_POLICY_TAG_DELETE&quot; |
| BIGQUERY_POLICY_TAG_SET_IAM_POLICY | &quot;BIGQUERY_POLICY_TAG_SET_IAM_POLICY&quot; |
| ACCESS_POLICY_UPDATE | &quot;ACCESS_POLICY_UPDATE&quot; |
| GOVERNANCE_RULE_MATCHED_RESOURCES | &quot;GOVERNANCE_RULE_MATCHED_RESOURCES&quot; |
| GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS | &quot;GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS&quot; |
| GOVERNANCE_RULE_ERRORS | &quot;GOVERNANCE_RULE_ERRORS&quot; |
| GOVERNANCE_RULE_PROCESSING | &quot;GOVERNANCE_RULE_PROCESSING&quot; |




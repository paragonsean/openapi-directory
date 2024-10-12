# CloudDataplexApi.GoogleCloudDataplexV1GovernanceEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**GoogleCloudDataplexV1GovernanceEventEntity**](GoogleCloudDataplexV1GovernanceEventEntity.md) |  | [optional] 
**eventType** | **String** | The type of the event. | [optional] 
**message** | **String** | The log message. | [optional] 



## Enum: EventTypeEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `RESOURCE_IAM_POLICY_UPDATE` (value: `"RESOURCE_IAM_POLICY_UPDATE"`)

* `BIGQUERY_TABLE_CREATE` (value: `"BIGQUERY_TABLE_CREATE"`)

* `BIGQUERY_TABLE_UPDATE` (value: `"BIGQUERY_TABLE_UPDATE"`)

* `BIGQUERY_TABLE_DELETE` (value: `"BIGQUERY_TABLE_DELETE"`)

* `BIGQUERY_CONNECTION_CREATE` (value: `"BIGQUERY_CONNECTION_CREATE"`)

* `BIGQUERY_CONNECTION_UPDATE` (value: `"BIGQUERY_CONNECTION_UPDATE"`)

* `BIGQUERY_CONNECTION_DELETE` (value: `"BIGQUERY_CONNECTION_DELETE"`)

* `BIGQUERY_TAXONOMY_CREATE` (value: `"BIGQUERY_TAXONOMY_CREATE"`)

* `BIGQUERY_POLICY_TAG_CREATE` (value: `"BIGQUERY_POLICY_TAG_CREATE"`)

* `BIGQUERY_POLICY_TAG_DELETE` (value: `"BIGQUERY_POLICY_TAG_DELETE"`)

* `BIGQUERY_POLICY_TAG_SET_IAM_POLICY` (value: `"BIGQUERY_POLICY_TAG_SET_IAM_POLICY"`)

* `ACCESS_POLICY_UPDATE` (value: `"ACCESS_POLICY_UPDATE"`)

* `GOVERNANCE_RULE_MATCHED_RESOURCES` (value: `"GOVERNANCE_RULE_MATCHED_RESOURCES"`)

* `GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS` (value: `"GOVERNANCE_RULE_SEARCH_LIMIT_EXCEEDS"`)

* `GOVERNANCE_RULE_ERRORS` (value: `"GOVERNANCE_RULE_ERRORS"`)

* `GOVERNANCE_RULE_PROCESSING` (value: `"GOVERNANCE_RULE_PROCESSING"`)







# GooglePrivacyDlpV2DiscoveryBigQueryFilter

Determines what tables will have profiles generated within an organization or project. Includes the ability to filter by regular expression patterns on project ID, dataset ID, and table ID.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**otherTables** | **Object** | Catch-all for all other tables not specified by other filters. Should always be last, except for single-table configurations, which will only have a TableReference target. |  [optional] |
|**tables** | [**GooglePrivacyDlpV2BigQueryTableCollection**](GooglePrivacyDlpV2BigQueryTableCollection.md) |  |  [optional] |




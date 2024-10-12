

# ViewDefinition

Describes the definition of a logical view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privacyPolicy** | [**PrivacyPolicy**](PrivacyPolicy.md) |  |  [optional] |
|**query** | **String** | Required. A query that BigQuery executes when the view is referenced. |  [optional] |
|**useExplicitColumnNames** | **Boolean** | True if the column names are explicitly specified. For example by using the &#39;CREATE VIEW v(c1, c2) AS ...&#39; syntax. Can only be set for GoogleSQL views. |  [optional] |
|**useLegacySql** | **Boolean** | Specifies whether to use BigQuery&#39;s legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery&#39;s GoogleSQL: https://cloud.google.com/bigquery/sql-reference/ Queries and views that reference this view must use the same flag value. A wrapper is used here because the default value is True. |  [optional] |
|**userDefinedFunctionResources** | [**List&lt;UserDefinedFunctionResource&gt;**](UserDefinedFunctionResource.md) | Describes user-defined function resources used in the query. |  [optional] |




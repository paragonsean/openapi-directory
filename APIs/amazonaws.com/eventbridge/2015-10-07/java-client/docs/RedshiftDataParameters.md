

# RedshiftDataParameters

These are custom parameters to be used when the target is a Amazon Redshift cluster or Redshift Serverless workgroup to invoke the Amazon Redshift Data API ExecuteStatement based on EventBridge events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**secretManagerArn** | [**String**](String.md) |  |  [optional] |
|**database** | [**String**](String.md) |  |  |
|**dbUser** | [**String**](String.md) |  |  [optional] |
|**sql** | [**String**](String.md) |  |  [optional] |
|**statementName** | [**String**](String.md) |  |  [optional] |
|**withEvent** | [**Boolean**](Boolean.md) |  |  [optional] |
|**sqls** | **List&lt;String&gt;** | A list of SQLs. |  [optional] |




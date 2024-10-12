

# DescribeAnalysisSchemesRequest

Container for the parameters to the <code><a>DescribeAnalysisSchemes</a></code> operation. Specifies the name of the domain you want to describe. To limit the response to particular analysis schemes, specify the names of the analysis schemes you want to describe. To show the active configuration and exclude any pending changes, set the <code>Deployed</code> option to <code>true</code>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | [**String**](String.md) |  |  |
|**analysisSchemeNames** | [**List**](List.md) |  |  [optional] |
|**deployed** | [**Boolean**](Boolean.md) |  |  [optional] |




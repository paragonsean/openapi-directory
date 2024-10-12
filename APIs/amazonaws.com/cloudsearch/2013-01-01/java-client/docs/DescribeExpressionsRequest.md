

# DescribeExpressionsRequest

Container for the parameters to the <code><a>DescribeDomains</a></code> operation. Specifies the name of the domain you want to describe. To restrict the response to particular expressions, specify the names of the expressions you want to describe. To show the active configuration and exclude any pending changes, set the <code>Deployed</code> option to <code>true</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | [**String**](String.md) |  |  |
|**expressionNames** | [**List**](List.md) |  |  [optional] |
|**deployed** | [**Boolean**](Boolean.md) |  |  [optional] |




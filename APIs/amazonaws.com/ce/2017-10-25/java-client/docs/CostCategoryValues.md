

# CostCategoryValues

<p>The Cost Categories values used for filtering the costs.</p> <p>If <code>Values</code> and <code>Key</code> are not specified, the <code>ABSENT</code> <code>MatchOption</code> is applied to all Cost Categories. That is, it filters on resources that aren't mapped to any Cost Categories.</p> <p>If <code>Values</code> is provided and <code>Key</code> isn't specified, the <code>ABSENT</code> <code>MatchOption</code> is applied to the Cost Categories <code>Key</code> only. That is, it filters on resources without the given Cost Categories key.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | The unique name of the Cost Category. |  [optional] |
|**values** | [**List**](List.md) |  |  [optional] |
|**matchOptions** | [**List**](List.md) |  |  [optional] |




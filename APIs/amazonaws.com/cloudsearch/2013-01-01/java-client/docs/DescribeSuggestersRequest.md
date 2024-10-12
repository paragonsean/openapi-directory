

# DescribeSuggestersRequest

Container for the parameters to the <code><a>DescribeSuggester</a></code> operation. Specifies the name of the domain you want to describe. To restrict the response to particular suggesters, specify the names of the suggesters you want to describe. To show the active configuration and exclude any pending changes, set the <code>Deployed</code> option to <code>true</code>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | [**String**](String.md) |  |  |
|**suggesterNames** | [**List**](List.md) |  |  [optional] |
|**deployed** | [**Boolean**](Boolean.md) |  |  [optional] |




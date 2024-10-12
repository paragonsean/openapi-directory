

# Filters

May be used to filter budgets by resource group, resource, or meter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**meters** | **List&lt;UUID&gt;** | The list of filters on meters (GUID), mandatory for budgets of usage category.  |  [optional] |
|**resourceGroups** | **List&lt;String&gt;** | The list of filters on resource groups, allowed at subscription level only. |  [optional] |
|**resources** | **List&lt;String&gt;** | The list of filters on resources. |  [optional] |
|**tags** | **Map&lt;String, List&lt;String&gt;&gt;** | The dictionary of filters on tags. |  [optional] |






# PolicyFilter

<p>Contains information about a filter to refine policies returned in a query.</p> <p>This data type is used as a response parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html\">ListPolicies</a> operation.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principal** | [**PolicyFilterPrincipal**](PolicyFilterPrincipal.md) |  |  [optional] |
|**resource** | [**PolicyFilterResource**](PolicyFilterResource.md) |  |  [optional] |
|**policyType** | [**PolicyType**](PolicyType.md) |  |  [optional] |
|**policyTemplateId** | [**String**](String.md) |  |  [optional] |




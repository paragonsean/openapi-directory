

# PolicyItem

<p>Contains information about a policy.</p> <p>This data type is used as a response parameter for the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_ListPolicies.html\">ListPolicies</a> operation.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policyStoreId** | [**String**](String.md) |  |  |
|**policyId** | [**String**](String.md) |  |  |
|**policyType** | [**PolicyType**](PolicyType.md) |  |  |
|**principal** | [**PolicyItemPrincipal**](PolicyItemPrincipal.md) |  |  [optional] |
|**resource** | [**PolicyItemResource**](PolicyItemResource.md) |  |  [optional] |
|**definition** | [**PolicyItemDefinition**](PolicyItemDefinition.md) |  |  |
|**createdDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**lastUpdatedDate** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |




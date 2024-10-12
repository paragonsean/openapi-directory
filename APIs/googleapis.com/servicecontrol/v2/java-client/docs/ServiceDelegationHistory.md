

# ServiceDelegationHistory

The history of delegation across multiple services as the result of the original user's action. Such as \"service A uses its own account to do something for user B\". This differs from ServiceAccountDelegationInfo, which only tracks the history of direct token exchanges (impersonation).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**originalPrincipal** | **String** | The original end user who initiated the request to GCP. |  [optional] |
|**serviceMetadata** | [**List&lt;ServiceMetadata&gt;**](ServiceMetadata.md) | Data identifying the service specific jobs or units of work that were involved in a chain of service calls. |  [optional] |






# AlternativePaymentToken


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**ContactObject**](ContactObject.md) | The billing address object. |  |
|**method** | **AlternativePaymentMethods** | The token payment method. |  |
|**links** | [**List&lt;SelfLink&gt;**](SelfLink.md) | The links related to resource. |  [optional] [readonly] |
|**createdTime** | **OffsetDateTime** | Token created time. |  [optional] [readonly] |
|**expirationTime** | **OffsetDateTime** | Token expiration time. |  [optional] [readonly] |
|**id** | **String** | The token identifier string. |  [optional] [readonly] |
|**isUsed** | **Boolean** | Whether the token was already used. |  [optional] [readonly] |
|**leadSource** | [**LeadSource**](LeadSource.md) |  |  [optional] |
|**riskMetadata** | [**RiskMetadata**](RiskMetadata.md) |  |  [optional] |
|**updatedTime** | **OffsetDateTime** | Token updated time. |  [optional] [readonly] |
|**usageTime** | **OffsetDateTime** | Token usage time. |  [optional] [readonly] |




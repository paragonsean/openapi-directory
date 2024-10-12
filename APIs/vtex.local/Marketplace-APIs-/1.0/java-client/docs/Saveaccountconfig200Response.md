

# Saveaccountconfig200Response


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchFlux** | **String** | Type of approval configuration that apply to received SKUs sent by sellers. The possible values are:   &#x60;default&#x60;: the matcher approves the SKU.   &#x60;manual&#x60;: manual SKU&#39;s approvals.   &#x60;AutoApprove&#x60;: automatic SKU&#39;s approvals. |  [optional] |
|**matchers** |  | [Matchers](https://help.vtex.com/en/tutorial/understanding-vtex-matcher-scoring) configurations for approving and rejecting [received SKUs](https://help.vtex.com/en/tutorial/cataloging-received-skus--tutorials_396) sent by sellers. |  [optional] |
|**rules** | [**Saveaccountconfig200ResponseRules**](Saveaccountconfig200ResponseRules.md) |  |  [optional] |
|**score** | [**Saveaccountconfig200ResponseScore**](Saveaccountconfig200ResponseScore.md) |  |  [optional] |
|**specificationsMapping** |  | This attribute maps product and SKU&#39;s specifications between the marketplace and the seller. |  [optional] |




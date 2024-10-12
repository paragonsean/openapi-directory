# Suggestions.SaveaccountconfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matchFlux** | **String** | This field determines the type of approval configuration applied to SKUs received  from a seller. The possible values include:   - &#x60;default&#x60; where the Matcher reviews the SKU, and approves it based on its score   - &#x60;manual&#x60; for manual approvals through the Received SKU UI or Match API   - &#x60;autoApprove&#x60; for every SKU received from a given seller to be approved automatically, regardless of the Matcher Score. | [default to &#39;autoApprove&#39;]
**matchers** | [**[Matcher]**](Matcher.md) | Matchers for approving and rejecting SKUs received from sellers. | 
**score** | [**Score**](Score.md) |  | 
**specificationsMapping** | **[String]** | This attribute maps product and SKU specifications. | 



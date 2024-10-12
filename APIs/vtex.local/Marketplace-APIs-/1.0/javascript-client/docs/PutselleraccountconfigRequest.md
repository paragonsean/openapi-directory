# Suggestions.PutselleraccountconfigRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mapping** | **Object** | Mapping of SKU and product Specifications. This object should be sent in the following format for all fields you wish to map:  {specificationName}:{specificationValue},  Example:  Choose voltage: Voltage,  Choose size: Size | 
**matchFlux** | **String** | This field determines the type of approval configuration applied to SKUs received  from a seller. The possible values include:   - &#x60;default&#x60; where the Matcher reviews the SKU, and approves it based on its score   - &#x60;manual&#x60; for manual approvals through the Received SKU UI or Match API   - &#x60;autoApprove&#x60; for every SKU received from a given seller to be approved automatically, regardless of the Matcher Score. | [default to &#39;autoApprove&#39;]
**sellerId** | **String** | A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to &#39;seller123&#39;]



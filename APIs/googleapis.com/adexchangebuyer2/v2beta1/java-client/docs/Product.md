

# Product

A product is a segment of inventory that a seller wants to sell. It is associated with certain terms and targeting information which helps the buyer know more about the inventory.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableEndTime** | **String** | The proposed end time for the deal. The field will be truncated to the order of seconds during serving. |  [optional] |
|**availableStartTime** | **String** | Inventory availability dates. The start time will be truncated to seconds during serving. Thus, a field specified as 3:23:34.456 (HH:mm:ss.SSS) will be truncated to 3:23:34 when serving. |  [optional] |
|**createTime** | **String** | Creation time. |  [optional] |
|**creatorContacts** | [**List&lt;ContactInformation&gt;**](ContactInformation.md) | Optional contact information for the creator of this product. |  [optional] |
|**displayName** | **String** | The display name for this product as set by the seller. |  [optional] |
|**hasCreatorSignedOff** | **Boolean** | If the creator has already signed off on the product, then the buyer can finalize the deal by accepting the product as is. When copying to a proposal, if any of the terms are changed, then auto_finalize is automatically set to false. |  [optional] |
|**productId** | **String** | The unique ID for the product. |  [optional] |
|**productRevision** | **String** | The revision number of the product (auto-assigned by Marketplace). |  [optional] |
|**publisherProfileId** | **String** | An ID which can be used by the Publisher Profile API to get more information about the seller that created this product. |  [optional] |
|**seller** | [**Seller**](Seller.md) |  |  [optional] |
|**syndicationProduct** | [**SyndicationProductEnum**](#SyndicationProductEnum) | The syndication product associated with the deal. |  [optional] |
|**targetingCriterion** | [**List&lt;TargetingCriteria&gt;**](TargetingCriteria.md) | Targeting that is shared between the buyer and the seller. Each targeting criterion has a specified key and for each key there is a list of inclusion value or exclusion values. |  [optional] |
|**terms** | [**DealTerms**](DealTerms.md) |  |  [optional] |
|**updateTime** | **String** | Time of last update. |  [optional] |
|**webPropertyCode** | **String** | The web-property code for the seller. This needs to be copied as is when adding a new deal to a proposal. |  [optional] |



## Enum: SyndicationProductEnum

| Name | Value |
|---- | -----|
| SYNDICATION_PRODUCT_UNSPECIFIED | &quot;SYNDICATION_PRODUCT_UNSPECIFIED&quot; |
| CONTENT | &quot;CONTENT&quot; |
| MOBILE | &quot;MOBILE&quot; |
| VIDEO | &quot;VIDEO&quot; |
| GAMES | &quot;GAMES&quot; |




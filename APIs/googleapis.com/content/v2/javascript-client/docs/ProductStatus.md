# ContentApiForShopping.ProductStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationDate** | **String** | Date on which the item has been created, in ISO 8601 format. | [optional] 
**dataQualityIssues** | [**[ProductStatusDataQualityIssue]**](ProductStatusDataQualityIssue.md) | DEPRECATED - never populated | [optional] 
**destinationStatuses** | [**[ProductStatusDestinationStatus]**](ProductStatusDestinationStatus.md) | The intended destinations for the product. | [optional] 
**googleExpirationDate** | **String** | Date on which the item expires in Google Shopping, in ISO 8601 format. | [optional] 
**itemLevelIssues** | [**[ProductStatusItemLevelIssue]**](ProductStatusItemLevelIssue.md) | A list of all issues associated with the product. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string \&quot;&#x60;content#productStatus&#x60;\&quot; | [optional] 
**lastUpdateDate** | **String** | Date on which the item has been last updated, in ISO 8601 format. | [optional] 
**link** | **String** | The link to the product. | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**productId** | **String** | The ID of the product for which status is reported. | [optional] 
**title** | **String** | The title of the product. | [optional] 



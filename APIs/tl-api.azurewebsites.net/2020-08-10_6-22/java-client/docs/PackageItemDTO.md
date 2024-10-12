

# PackageItemDTO

The PackageItemDTO Class. Contains relevant fields of PackageItem DTO by masking actual Package entity's fields in application.             

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**articleId** | **Integer** | Refer to ArticleId in Article table in DB.              |  |
|**articleName** | **String** | Name of the article(Addon) in a particular package.              read only              |  [optional] |
|**articleNumber** | **Integer** | Number assigned the article(Addon) in a particular package.              read only              |  [optional] |
|**articlePrice** | **BigDecimal** | Price of the article determined from that package. Price of a same article can be varied from package to package.              |  [optional] |
|**endOrder** | **Integer** | Number of the installment this article is available to.              |  [optional] |
|**isIncludeServiceInCharge** | **Boolean** | Is Included in service charge  |  [optional] |
|**measureUnit** | **String** |  |  [optional] |
|**numberOfItems** | **BigDecimal** | How many article(Addon) is available for that package from that type.              |  [optional] |
|**startOrder** | **Integer** | Number of the installment this article is available from.              |  [optional] |




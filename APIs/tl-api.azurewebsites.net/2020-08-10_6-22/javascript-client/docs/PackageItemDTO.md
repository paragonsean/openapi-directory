# Api.PackageItemDTO

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**articleId** | **Number** | Refer to ArticleId in Article table in DB.              | 
**articleName** | **String** | Name of the article(Addon) in a particular package.              read only              | [optional] 
**articleNumber** | **Number** | Number assigned the article(Addon) in a particular package.              read only              | [optional] 
**articlePrice** | **Number** | Price of the article determined from that package. Price of a same article can be varied from package to package.              | [optional] 
**endOrder** | **Number** | Number of the installment this article is available to.              | [optional] 
**isIncludeServiceInCharge** | **Boolean** | Is Included in service charge  | [optional] 
**measureUnit** | **String** |  | [optional] 
**numberOfItems** | **Number** | How many article(Addon) is available for that package from that type.              | [optional] 
**startOrder** | **Number** | Number of the installment this article is available from.              | [optional] 



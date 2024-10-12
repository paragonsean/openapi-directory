

# ArticleDTO

The ArticleDTO Class. Contains relevant fields of Article DTO by masking actual Article entity's fields in application.             

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeStatus** | **Boolean** | Active Status  |  [optional] |
|**applyForAllGyms** | **Boolean** |  |  [optional] |
|**articleId** | **Integer** |  |  [optional] |
|**availableGyms** | [**List&lt;GymDTO&gt;**](GymDTO.md) |  |  |
|**availableQty** | **BigDecimal** | Default AvailableQty |  [optional] |
|**barcode** | **String** |  |  [optional] |
|**createdDate** | **OffsetDateTime** |  |  [optional] |
|**createdUser** | **String** |  |  [optional] |
|**cronExpression** | **String** | Access Schedule CRON Expression  |  [optional] |
|**description** | **String** |  |  [optional] |
|**discount** | **BigDecimal** |  |  [optional] |
|**employeeDiscount** | **BigDecimal** | Default EmployeeDiscount |  [optional] |
|**employeePrice** | **BigDecimal** | Default EmployeePrice |  [optional] |
|**gymArticles** | [**List&lt;GymArticleDetailsDTO&gt;**](GymArticleDetailsDTO.md) | Gym Customizations  |  [optional] |
|**isAddOn** | **Boolean** |  |  [optional] |
|**isInventoryItem** | **Boolean** | Default IsInventoryItem of the Article  |  [optional] |
|**isObsolete** | **Boolean** | Default IsObsolete of the Article  |  [optional] |
|**measureUnit** | **String** |  |  |
|**modifiedDate** | **OffsetDateTime** |  |  [optional] |
|**modifiedUser** | **String** |  |  [optional] |
|**name** | **String** |  |  |
|**number** | **Integer** |  |  [optional] |
|**price** | **BigDecimal** |  |  |
|**reorderLevel** | **BigDecimal** | Deafault ReorderLevel |  [optional] |
|**revenueAccountId** | **Integer** | Default Revenue account |  [optional] |
|**sellingPrice** | **BigDecimal** | Default SellingPrice |  [optional] |
|**tags** | **String** |  |  [optional] |
|**type** | **String** |  |  |
|**vat** | **BigDecimal** |  |  [optional] |
|**vatApplicable** | **Boolean** | VAT Applicable  |  [optional] |




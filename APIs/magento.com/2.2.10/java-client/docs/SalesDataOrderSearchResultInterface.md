

# SalesDataOrderSearchResultInterface

Order search result interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**items** | [**List&lt;SalesDataOrderInterface&gt;**](SalesDataOrderInterface.md) | Array of collection items. |  |
|**searchCriteria** | [**FrameworkSearchCriteriaInterface**](FrameworkSearchCriteriaInterface.md) |  |  |
|**totalCount** | **Integer** | Total count. |  |




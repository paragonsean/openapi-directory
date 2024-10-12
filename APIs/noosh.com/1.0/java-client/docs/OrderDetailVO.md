

# OrderDetailVO

Java type: com.noosh.nooshapi.vo.OrderDetailVO

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceptedDate** | **LocalDate** |  |  [optional] |
|**annulledDate** | **LocalDate** |  |  [optional] |
|**approvedDate** | **LocalDate** |  |  [optional] |
|**awardedDate** | **LocalDate** |  |  [optional] |
|**budgetType** | **String** |  |  [optional] |
|**buyer** | [**UserVO**](UserVO.md) |  |  [optional] |
|**buyerWorkgroup** | [**WorkgroupBaseVO**](WorkgroupBaseVO.md) |  |  [optional] |
|**changeOrders** | [**List&lt;OrderDetailBaseVO&gt;**](OrderDetailBaseVO.md) |  |  [optional] |
|**classification** | **String** |  |  [optional] |
|**closedDate** | **LocalDate** |  |  [optional] |
|**closingChangeOrders** | [**List&lt;OrderDetailBaseVO&gt;**](OrderDetailBaseVO.md) |  |  [optional] |
|**comments** | **String** |  |  [optional] |
|**completionDate** | **LocalDate** |  |  [optional] |
|**creatorUserId** | **Long** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**customFields** | [**List&lt;PropertyPaAndAttVO&gt;**](PropertyPaAndAttVO.md) |  |  [optional] |
|**grandTotal** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**grandTotalWithChanges** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**itemCount** | **Integer** |  |  [optional] |
|**lastActivityDate** | **LocalDate** |  |  [optional] |
|**lastChanged** | **LocalDate** |  |  [optional] |
|**lastStatusChange** | **LocalDate** |  |  [optional] |
|**miscCost** | **Double** |  |  [optional] |
|**orderId** | **Long** |  |  [optional] |
|**orderItems** | [**List&lt;OrderItemSimpleVO&gt;**](OrderItemSimpleVO.md) |  |  [optional] |
|**orderNumber** | **String** |  |  [optional] |
|**orderTitle** | **String** |  |  [optional] |
|**orderTotal** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**oversPercent** | **Double** |  |  [optional] |
|**parentOrderId** | **Long** |  |  [optional] |
|**paymentReference** | **String** |  |  [optional] |
|**printOrderIds** | **List&lt;Long&gt;** |  |  [optional] |
|**quoteId** | **Long** |  |  [optional] |
|**shipping** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**status** | **String** |  |  [optional] |
|**statusComments** | **String** |  |  [optional] |
|**supplier** | [**UserVO**](UserVO.md) |  |  [optional] |
|**supplierReference** | **String** |  |  [optional] |
|**supplierSelectionReason** | **String** |  |  [optional] |
|**supplierWorkgroup** | [**WorkgroupBaseVO**](WorkgroupBaseVO.md) |  |  [optional] |
|**tax** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**transactionalCurrency** | **String** |  |  [optional] |
|**transactionalGrandTotal** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**transactionalGrandTotalWithChanges** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**transactionalOrderTotal** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**transactionalShipping** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**transactionalTax** | **Object** | Java type: java.math.BigDecimal |  [optional] |
|**undersPercent** | **Double** |  |  [optional] |




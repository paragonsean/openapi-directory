

# SalesOrderFinancialInfoDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cashDiscountDate** | **OffsetDateTime** | The date for the cash discount  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**dueDate** | **OffsetDateTime** | The due date for the invoice  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**invoiceDate** | **OffsetDateTime** | The invoice date  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**invoiceId** | **String** | The id of the invoice issued for the order |  [optional] |
|**invoiceSeparately** | **Boolean** | Whether the order should be invoiced separately |  [optional] |
|**postPeriod** | **String** | The post period for the invoice |  [optional] |
|**terms** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |




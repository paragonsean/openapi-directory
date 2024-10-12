

# RtiTransactionBase1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**employerCore** | [**EmployerCore1**](EmployerCore1.md) |  |  [optional] |
|**requestData** | **String** | The rti transaction bases&#39; request data |  [optional] |
|**responseData** | **String** | The rti transaction bases&#39; response data |  [optional] |
|**rtiType** | **String** | The rti transaction bases&#39; rti type |  [optional] |
|**taxYear** | **Integer** | The rti transaction bases&#39; tax year |  [optional] |
|**timestamp** | **OffsetDateTime** | The rti transaction bases&#39; timestamp |  [optional] |
|**transactionStatus** | [**TransactionStatusEnum**](#TransactionStatusEnum) | The rti transaction bases&#39; transaction status |  [optional] |
|**transmissionDate** | **OffsetDateTime** | The rti transaction bases&#39; transmission date |  [optional] |



## Enum: TransactionStatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| REQUEST_GENERATED | &quot;RequestGenerated&quot; |
| COMPLETED_WITH_ERROR | &quot;CompletedWithError&quot; |
| COMPLETED_WITH_SUCCESS | &quot;CompletedWithSuccess&quot; |
| TIME_OUT | &quot;TimeOut&quot; |




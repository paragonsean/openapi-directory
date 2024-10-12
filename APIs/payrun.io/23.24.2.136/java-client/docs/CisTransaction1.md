

# CisTransaction1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cisMessageType** | [**CisMessageTypeEnum**](#CisMessageTypeEnum) | The cis transactions&#39; cis message type |  [optional] |
|**employerCore** | [**EmployerCore**](EmployerCore.md) |  |  [optional] |
|**requestData** | **String** | The cis transactions&#39; request data |  [optional] |
|**responseData** | **String** | The cis transactions&#39; response data |  [optional] |
|**taxYear** | **Integer** | The cis transactions&#39; tax year |  [optional] |
|**timestamp** | **OffsetDateTime** | The cis transactions&#39; timestamp |  [optional] |
|**transactionStatus** | [**TransactionStatusEnum**](#TransactionStatusEnum) | The cis transactions&#39; transaction status |  [optional] |
|**transmissionDate** | **OffsetDateTime** | The cis transactions&#39; transmission date |  [optional] |



## Enum: CisMessageTypeEnum

| Name | Value |
|---- | -----|
| VERIFICATION | &quot;Verification&quot; |
| RETURN | &quot;Return&quot; |



## Enum: TransactionStatusEnum

| Name | Value |
|---- | -----|
| NEW | &quot;New&quot; |
| REQUEST_GENERATED | &quot;RequestGenerated&quot; |
| COMPLETED_WITH_ERROR | &quot;CompletedWithError&quot; |
| COMPLETED_WITH_SUCCESS | &quot;CompletedWithSuccess&quot; |
| TIME_OUT | &quot;TimeOut&quot; |




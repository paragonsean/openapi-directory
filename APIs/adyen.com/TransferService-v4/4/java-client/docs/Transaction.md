

# Transaction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolder** | [**ResourceReference**](ResourceReference.md) | Contains information about the account holder associated with the &#x60;balanceAccount&#x60;. |  |
|**amount** | [**Amount**](Amount.md) | Contains information about the amount of the transaction. |  |
|**balanceAccount** | [**ResourceReference**](ResourceReference.md) | Contains information about the balance account involved in the transaction. |  |
|**balancePlatform** | **String** | The unique identifier of the balance platform. |  |
|**bookingDate** | **OffsetDateTime** | The date the transaction was booked into the balance account. |  |
|**creationDate** | **OffsetDateTime** | The date and time when the event was triggered, in ISO 8601 extended format. For example, **2020-12-18T10:15:30+01:00**. |  [optional] |
|**id** | **String** | The unique identifier of the transaction. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the transaction.   Possible values:  * **pending**: The transaction is still pending.  * **booked**: The transaction has been booked to the balance account.   |  |
|**transfer** | [**TransferData**](TransferData.md) | Contains information about the transfer related to the transaction. |  [optional] |
|**valueDate** | **OffsetDateTime** | The date the transfer amount becomes available in the balance account. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| BOOKED | &quot;booked&quot; |
| PENDING | &quot;pending&quot; |




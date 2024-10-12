

# AirTravelDocumentCommon


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentNumber** | **String** | Identifier of the travel document prefixed by its owner code [NALC - 3 digits]. Can either be a primary or a conjunctive document number. Necessary for TicketingReference definition. |  [optional] |
|**documentStatus** | [**DocumentStatusEnum**](#DocumentStatusEnum) | Status of the travel document contained in the fare element |  [optional] |
|**documentType** | [**DocumentTypeEnum**](#DocumentTypeEnum) | Type of the travel document |  [optional] |



## Enum: DocumentStatusEnum

| Name | Value |
|---- | -----|
| ISSUED | &quot;ISSUED&quot; |
| REFUNDED | &quot;REFUNDED&quot; |
| VOID | &quot;VOID&quot; |
| ORIGINAL | &quot;ORIGINAL&quot; |
| EXCHANGED | &quot;EXCHANGED&quot; |



## Enum: DocumentTypeEnum

| Name | Value |
|---- | -----|
| ETICKET | &quot;ETICKET&quot; |
| PTICKET | &quot;PTICKET&quot; |
| EMD | &quot;EMD&quot; |
| MCO | &quot;MCO&quot; |




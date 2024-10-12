

# TicketCountsEntity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approved** | **Boolean** | Defines whether this ticket count is approved or not. |  |
|**comment** | **String** | Comment for the ticket count. |  |
|**currency** | **String** | Currency of the gross (&lt;a href&#x3D;&#39;https://en.wikipedia.org/wiki/ISO_4217#Active_codes&#39;&gt;ISO 4212 alphabetic code&lt;/a&gt;). |  [optional] |
|**date** | **LocalDate** | Date of the ticket count. |  |
|**_final** | **Boolean** | Whether this ticket count is the last and final one of its event or not. If it is, it means that no further ticket counts will be added for the event it belongs to. |  |
|**gross** | **Float** | Gross (&#x3D; income for the sold tickets, including VAT but excluding all commissions). |  [optional] |
|**id** | **Integer** | Unique ID of the ticket count. |  |
|**reservations** | **Integer** | Ticket reservations (&#x3D; number of reserved tickets). *This field may be omitted according to the customer configuration.* |  [optional] |
|**sales** | **Integer** | Ticket sales (&#x3D; number of sold tickets). |  |




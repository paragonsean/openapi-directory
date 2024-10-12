

# PartyIdentification


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address**](Address.md) | Address of the bank account owner. |  [optional] |
|**dateOfBirth** | **LocalDate** | The date of birth of the individual in [ISO-8601](https://www.w3.org/TR/NOTE-datetime) format. For example, **YYYY-MM-DD**. Should not be before January 1, 1900.  Allowed only when &#x60;type&#x60; is **individual**. |  [optional] |
|**firstName** | **String** | First name of the individual.  Allowed only when &#x60;type&#x60; is **individual**. |  [optional] |
|**fullName** | **String** | The name of the entity. |  |
|**lastName** | **String** | Last name of the individual.  Allowed only when &#x60;type&#x60; is **individual**. |  [optional] |
|**reference** | **String** | A unique reference to identify the party or counterparty involved in transfers. This identifier ensures consistency and uniqueness throughout all transactions initiated to and from the same party. For example, your client&#39;s unique wallet or payee ID. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of entity that owns the bank account.   Possible values: **individual**, **organization**, or **unknown**. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| INDIVIDUAL | &quot;individual&quot; |
| ORGANIZATION | &quot;organization&quot; |
| UNKNOWN | &quot;unknown&quot; |




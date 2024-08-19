

# CapabilityProblemEntityRecursive


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documents** | **List&lt;String&gt;** | List of document IDs to which the verification errors related to the capabilities correspond to. |  [optional] |
|**id** | **String** | The ID of the entity. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of entity.   Possible values: **LegalEntity**, **BankAccount**, **Document**. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_ACCOUNT | &quot;BankAccount&quot; |
| DOCUMENT | &quot;Document&quot; |
| LEGAL_ENTITY | &quot;LegalEntity&quot; |






# CustomerSecret

The pair of customer secret.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | The encryption algorithm used to encrypt data. |  |
|**keyIdentifier** | **String** | The identifier to the data service input object which this secret corresponds to. |  |
|**keyValue** | **String** | It contains the encrypted customer secret. |  |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| RSA1_5 | &quot;RSA1_5&quot; |
| RSA_OAEP | &quot;RSA_OAEP&quot; |
| PLAIN_TEXT | &quot;PlainText&quot; |






# DebitAccountHolderResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHolderCode** | **String** | The code of the account holder. |  [optional] |
|**bankAccountUUID** | **String** | The Adyen-generated unique alphanumeric identifier (UUID) of the account holder&#39;s bank account. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. |  [optional] |
|**merchantReferences** | **List&lt;String&gt;** | List of the &#x60;reference&#x60; values from the &#x60;split&#x60; array in the request. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |




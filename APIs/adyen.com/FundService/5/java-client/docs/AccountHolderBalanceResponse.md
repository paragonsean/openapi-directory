

# AccountHolderBalanceResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balancePerAccount** | [**List&lt;AccountDetailBalance&gt;**](AccountDetailBalance.md) | A list of each account and their balances. |  [optional] |
|**invalidFields** | [**List&lt;ErrorFieldType&gt;**](ErrorFieldType.md) | Contains field validation errors that would prevent requests from being processed. |  [optional] |
|**pspReference** | **String** | The reference of a request. Can be used to uniquely identify the request. |  [optional] |
|**resultCode** | **String** | The result code. |  [optional] |
|**totalBalance** | [**DetailBalance**](DetailBalance.md) | The total balance of the account holder. |  [optional] |




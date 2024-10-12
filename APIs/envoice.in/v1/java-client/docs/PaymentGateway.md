

# PaymentGateway


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canDisconnect** | **Boolean** |  |  [optional] |
|**clientImportUri** | **String** |  |  [optional] |
|**connectionType** | [**ConnectionTypeEnum**](#ConnectionTypeEnum) |  |  [optional] |
|**externalConnectionId** | **Integer** |  |  [optional] |
|**fields** | [**List&lt;PaymentGatewayInputField&gt;**](PaymentGatewayInputField.md) |  |  [optional] |
|**isConnected** | **Boolean** |  |  [optional] |
|**isEnabled** | **Boolean** |  |  [optional] |
|**maximumAmount** | **Double** |  |  [optional] |
|**minimumAmount** | **Double** |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**oauthUri** | **String** |  |  [optional] |
|**refundUri** | **String** |  |  [optional] |
|**supportedCurrencies** | [**List&lt;Currency&gt;**](Currency.md) |  |  [optional] |
|**supportsClientsImport** | **Boolean** |  |  [optional] |
|**supportsInstantCheckout** | **Boolean** |  |  [optional] |
|**supportsRefund** | **Boolean** |  |  [optional] |



## Enum: ConnectionTypeEnum

| Name | Value |
|---- | -----|
| O_AUTH | &quot;OAuth&quot; |
| INPUT_FIELDS | &quot;InputFields&quot; |
| DROPDOWN | &quot;Dropdown&quot; |




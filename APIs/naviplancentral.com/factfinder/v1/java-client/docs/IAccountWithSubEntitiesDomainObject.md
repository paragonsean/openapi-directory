

# IAccountWithSubEntitiesDomainObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountHoldings** | [**List&lt;IAccountHoldingDomainObject&gt;**](IAccountHoldingDomainObject.md) |  |  [optional] |
|**accountId** | **Integer** |  |  [optional] |
|**accountType** | **Integer** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**externalDestinationId** | **String** |  |  [optional] |
|**externalSourceId** | **String** |  |  [optional] |
|**externalSourceName** | **String** |  |  [optional] |
|**factFinderId** | **Integer** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**marketValue** | **Double** |  |  [optional] |
|**owner** | [**OwnerEnum**](#OwnerEnum) |  |  [optional] |
|**ownerDependentId** | **Integer** |  |  [optional] |
|**savingsStrategies** | [**List&lt;IAccountSavingsStrategyDomainObject&gt;**](IAccountSavingsStrategyDomainObject.md) |  |  [optional] |



## Enum: OwnerEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| JOINT | &quot;Joint&quot; |
| DEPENDENT | &quot;Dependent&quot; |
| OTHER | &quot;Other&quot; |




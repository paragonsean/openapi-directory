

# AccountModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountType** | **Integer** |  |  [optional] |
|**description** | **String** |  |  |
|**externalDestinationId** | **String** |  |  [optional] |
|**externalSourceId** | **String** |  |  [optional] |
|**externalSourceName** | **String** |  |  [optional] |
|**factFinderId** | **Integer** |  |  |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**marketValue** | **Double** |  |  [optional] |
|**owner** | [**OwnerEnum**](#OwnerEnum) |  |  [optional] |
|**ownerDependentId** | **Integer** |  |  [optional] |



## Enum: OwnerEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| JOINT | &quot;Joint&quot; |
| DEPENDENT | &quot;Dependent&quot; |
| OTHER | &quot;Other&quot; |






# SubaccountRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyid** | **String** | Clé API |  |
|**subAccountAddCredit** | **String** | montant du crédit à ajouter |  [optional] |
|**subAccountCountryCode** | **String** |  |  [optional] |
|**subAccountEdit** | [**SubAccountEditEnum**](#SubAccountEditEnum) | action à réaliser soit setPrice pour définir un prix ou addCredit pour ajouter du credit ou setRestriction modifier la restriction stop / |  |
|**subAccountKeyId** | **String** | keyid du sous-compte |  [optional] |
|**subAccountPrice** | **String** |  |  [optional] |
|**subAccountRestrictionStop** | [**SubAccountRestrictionStopEnum**](#SubAccountRestrictionStopEnum) |  |  [optional] |
|**subAccountRestrictionTime** | [**SubAccountRestrictionTimeEnum**](#SubAccountRestrictionTimeEnum) |  |  [optional] |



## Enum: SubAccountEditEnum

| Name | Value |
|---- | -----|
| SET_PRICE | &quot;setPrice&quot; |
| ADD_CREDIT | &quot;addCredit&quot; |
| SET_RESTRICTION | &quot;setRestriction&quot; |



## Enum: SubAccountRestrictionStopEnum

| Name | Value |
|---- | -----|
| _0 | &quot;0&quot; |
| _1 | &quot;1&quot; |



## Enum: SubAccountRestrictionTimeEnum

| Name | Value |
|---- | -----|
| _0 | &quot;0&quot; |
| _1 | &quot;1&quot; |




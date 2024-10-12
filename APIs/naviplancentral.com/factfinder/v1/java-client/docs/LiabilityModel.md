

# LiabilityModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balance** | **Double** |  |  [optional] |
|**balanceAsOfDate** | **OffsetDateTime** |  |  [optional] |
|**description** | **String** |  |  |
|**externalDestinationId** | **String** |  |  [optional] |
|**externalSourceId** | **String** |  |  [optional] |
|**externalSourceName** | **String** |  |  [optional] |
|**factFinderId** | **Integer** |  |  |
|**frequency** | **Integer** |  |  [optional] |
|**interestRate** | **Double** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**liabilityType** | **Integer** |  |  [optional] |
|**loanDate** | **OffsetDateTime** |  |  [optional] |
|**originalPrincipal** | **Double** |  |  [optional] |
|**owner** | [**OwnerEnum**](#OwnerEnum) |  |  [optional] |
|**payment** | **Double** |  |  [optional] |
|**paymentType** | [**PaymentTypeEnum**](#PaymentTypeEnum) |  |  [optional] |



## Enum: OwnerEnum

| Name | Value |
|---- | -----|
| CLIENT | &quot;Client&quot; |
| CO_CLIENT | &quot;CoClient&quot; |
| JOINT | &quot;Joint&quot; |



## Enum: PaymentTypeEnum

| Name | Value |
|---- | -----|
| INTEREST_ONLY | &quot;InterestOnly&quot; |
| PRINCIPAL_AND_INTEREST | &quot;PrincipalAndInterest&quot; |
| SET_PRINCIPAL | &quot;SetPrincipal&quot; |
| LAST_PERIOD | &quot;LastPeriod&quot; |




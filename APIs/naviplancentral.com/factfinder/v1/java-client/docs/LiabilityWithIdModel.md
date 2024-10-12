

# LiabilityWithIdModel


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**balance** | **Double** |  |  [optional] |
|**balanceAsOfDate** | **OffsetDateTime** |  |  [optional] |
|**description** | **String** |  |  [optional] |
|**externalDestinationId** | **String** |  |  [optional] |
|**externalSourceId** | **String** |  |  [optional] |
|**externalSourceName** | **String** |  |  [optional] |
|**factFinderId** | **Integer** |  |  [optional] |
|**frequency** | **Integer** |  |  [optional] |
|**interestRate** | **Double** |  |  [optional] |
|**lastUpdated** | **OffsetDateTime** |  |  [optional] |
|**liabilityId** | **Integer** |  |  [optional] |
|**liabilityType** | **Integer** |  |  [optional] |
|**links** | [**List&lt;ObjectLink&gt;**](ObjectLink.md) |  |  [optional] |
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




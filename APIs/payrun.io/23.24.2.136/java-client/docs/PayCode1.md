

# PayCode1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**benefit** | **Boolean** | The pay codes&#39; benefit |  [optional] |
|**code** | **String** | The pay codes&#39; code |  [optional] |
|**description** | **String** | The pay codes&#39; description |  [optional] |
|**effectiveDate** | **LocalDate** | The pay codes&#39; effective date |  [optional] |
|**metaData** | **Object** | The pay codes&#39; meta data |  [optional] |
|**nextRevisionDate** | **LocalDate** | The pay codes&#39; next revision date |  [optional] |
|**niable** | **Boolean** | The pay codes&#39; niable |  [optional] |
|**nominalCode** | [**NominalCode3**](NominalCode3.md) |  |  [optional] |
|**nonArrestable** | **Boolean** | The pay codes&#39; non arrestable |  [optional] |
|**notional** | **Boolean** | The pay codes&#39; notional |  [optional] |
|**readonly** | **Boolean** | The pay codes&#39; readonly |  [optional] |
|**region** | [**RegionEnum**](#RegionEnum) | The pay codes&#39; region |  [optional] |
|**revision** | **Integer** | The pay codes&#39; revision |  [optional] |
|**taxable** | **Boolean** | The pay codes&#39; taxable |  [optional] |
|**territory** | [**TerritoryEnum**](#TerritoryEnum) | The pay codes&#39; territory |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The pay codes&#39; type |  [optional] |



## Enum: RegionEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| ENGLAND | &quot;England&quot; |
| SCOTLAND | &quot;Scotland&quot; |
| WALES | &quot;Wales&quot; |



## Enum: TerritoryEnum

| Name | Value |
|---- | -----|
| UNITED_KINGDOM | &quot;UnitedKingdom&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NOT_SET | &quot;NotSet&quot; |
| PAYMENT | &quot;Payment&quot; |
| DEDUCTION | &quot;Deduction&quot; |




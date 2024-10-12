

# CredasApiModelsPropertyRegisterPropertyRegisterCheckResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkStatus** | [**CheckStatusEnum**](#CheckStatusEnum) | Unknown &#x3D; 0, Pass &#x3D; 1, Refer &#x3D; 2, Fail &#x3D; 3 |  [optional] |
|**hasBeenOverridden** | **Boolean** |  |  [optional] |
|**matchResult** | [**MatchResultEnum**](#MatchResultEnum) | Unknown &#x3D; 0, FullNameMatch &#x3D; 1, SurnameMatch &#x3D; 2, NoNameMatch &#x3D; 3, NoAddressMatch &#x3D; 4, TitleNotRegistered &#x3D; 5, Unavailable &#x3D; 6, OutOfHours &#x3D; 7 |  [optional] |
|**matchResultText** | **String** |  |  [optional] |
|**propertyOwnership** | [**PropertyOwnershipEnum**](#PropertyOwnershipEnum) | Unknown &#x3D; 0, SoleOwnership &#x3D; 1, JointOwnership &#x3D; 2 |  [optional] |
|**propertyOwnershipText** | **String** |  |  [optional] |
|**titleNumber** | **String** |  |  [optional] |



## Enum: CheckStatusEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |



## Enum: MatchResultEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |
| NUMBER_3 | 3 |
| NUMBER_4 | 4 |
| NUMBER_5 | 5 |
| NUMBER_6 | 6 |
| NUMBER_7 | 7 |



## Enum: PropertyOwnershipEnum

| Name | Value |
|---- | -----|
| NUMBER_0 | 0 |
| NUMBER_1 | 1 |
| NUMBER_2 | 2 |




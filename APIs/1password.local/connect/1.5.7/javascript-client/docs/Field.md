# 1PasswordConnect.Field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entropy** | **Number** | For fields with a purpose of &#x60;PASSWORD&#x60; this is the entropy of the value | [optional] [readonly] 
**generate** | **Boolean** | If value is not present then a new value should be generated for this field | [optional] [default to false]
**id** | **String** |  | 
**label** | **String** |  | [optional] 
**purpose** | **String** | Some item types, Login and Password, have fields used for autofill. This property indicates that purpose and is required for some item types. | [optional] 
**recipe** | [**GeneratorRecipe**](GeneratorRecipe.md) |  | [optional] 
**section** | [**FieldSection**](FieldSection.md) |  | [optional] 
**type** | **String** |  | [default to &#39;STRING&#39;]
**value** | **String** |  | [optional] 



## Enum: PurposeEnum


* `empty` (value: `""`)

* `USERNAME` (value: `"USERNAME"`)

* `PASSWORD` (value: `"PASSWORD"`)

* `NOTES` (value: `"NOTES"`)





## Enum: TypeEnum


* `STRING` (value: `"STRING"`)

* `EMAIL` (value: `"EMAIL"`)

* `CONCEALED` (value: `"CONCEALED"`)

* `URL` (value: `"URL"`)

* `TOTP` (value: `"TOTP"`)

* `DATE` (value: `"DATE"`)

* `MONTH_YEAR` (value: `"MONTH_YEAR"`)

* `MENU` (value: `"MENU"`)





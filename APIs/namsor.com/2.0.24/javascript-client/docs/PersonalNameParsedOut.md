# NamSorApiV2.PersonalNameParsedOut

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstLastName** | [**FirstLastNameOut**](FirstLastNameOut.md) |  | [optional] 
**id** | **String** |  | [optional] 
**name** | **String** | The input name | [optional] 
**nameParserType** | **String** | Name parsing is addressed as a classification problem, for example FN1LN1 means a first then last name order. | [optional] 
**nameParserTypeAlt** | **String** | Second best alternative parsing. Name parsing is addressed as a classification problem, for example FN1LN1 means a first then last name order. | [optional] 
**score** | **Number** | Higher score is better, but score is not normalized. Use calibratedProbability if available.  | [optional] 
**script** | **String** |  | [optional] 



## Enum: NameParserTypeEnum


* `FN1LN1` (value: `"FN1LN1"`)

* `LN1FN1` (value: `"LN1FN1"`)

* `FN1LN2` (value: `"FN1LN2"`)

* `LN2FN1` (value: `"LN2FN1"`)

* `FN1LNx` (value: `"FN1LNx"`)

* `LNxFN1` (value: `"LNxFN1"`)

* `FN2LN1` (value: `"FN2LN1"`)

* `LN1FN2` (value: `"LN1FN2"`)

* `FN2LN2` (value: `"FN2LN2"`)

* `LN2FN2` (value: `"LN2FN2"`)

* `FN2LNx` (value: `"FN2LNx"`)

* `LNxFN2` (value: `"LNxFN2"`)

* `FNxLN1` (value: `"FNxLN1"`)

* `LN1FNx` (value: `"LN1FNx"`)

* `FNxLN2` (value: `"FNxLN2"`)

* `LN2FNx` (value: `"LN2FNx"`)

* `FNxLNx` (value: `"FNxLNx"`)

* `LNxFNx` (value: `"LNxFNx"`)





## Enum: NameParserTypeAltEnum


* `FN1LN1` (value: `"FN1LN1"`)

* `LN1FN1` (value: `"LN1FN1"`)

* `FN1LN2` (value: `"FN1LN2"`)

* `LN2FN1` (value: `"LN2FN1"`)

* `FN1LNx` (value: `"FN1LNx"`)

* `LNxFN1` (value: `"LNxFN1"`)

* `FN2LN1` (value: `"FN2LN1"`)

* `LN1FN2` (value: `"LN1FN2"`)

* `FN2LN2` (value: `"FN2LN2"`)

* `LN2FN2` (value: `"LN2FN2"`)

* `FN2LNx` (value: `"FN2LNx"`)

* `LNxFN2` (value: `"LNxFN2"`)

* `FNxLN1` (value: `"FNxLN1"`)

* `LN1FNx` (value: `"LN1FNx"`)

* `FNxLN2` (value: `"FNxLN2"`)

* `LN2FNx` (value: `"LN2FNx"`)

* `FNxLNx` (value: `"FNxLNx"`)

* `LNxFNx` (value: `"LNxFNx"`)





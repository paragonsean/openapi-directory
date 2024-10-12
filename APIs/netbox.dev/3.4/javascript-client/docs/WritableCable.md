# NetBoxApi.WritableCable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aTerminations** | [**[GenericObject]**](GenericObject.md) |  | [optional] 
**bTerminations** | [**[GenericObject]**](GenericObject.md) |  | [optional] 
**color** | **String** |  | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**description** | **String** |  | [optional] 
**display** | **String** |  | [optional] [readonly] 
**id** | **Number** |  | [optional] [readonly] 
**label** | **String** |  | [optional] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**length** | **Number** |  | [optional] 
**lengthUnit** | **String** |  | [optional] 
**status** | **String** |  | [optional] 
**tags** | [**[NestedTag]**](NestedTag.md) |  | [optional] 
**tenant** | **Number** |  | [optional] 
**type** | **String** |  | [optional] 
**url** | **String** |  | [optional] [readonly] 



## Enum: LengthUnitEnum


* `km` (value: `"km"`)

* `m` (value: `"m"`)

* `cm` (value: `"cm"`)

* `mi` (value: `"mi"`)

* `ft` (value: `"ft"`)

* `in` (value: `"in"`)





## Enum: StatusEnum


* `connected` (value: `"connected"`)

* `planned` (value: `"planned"`)

* `decommissioning` (value: `"decommissioning"`)





## Enum: TypeEnum


* `cat3` (value: `"cat3"`)

* `cat5` (value: `"cat5"`)

* `cat5e` (value: `"cat5e"`)

* `cat6` (value: `"cat6"`)

* `cat6a` (value: `"cat6a"`)

* `cat7` (value: `"cat7"`)

* `cat7a` (value: `"cat7a"`)

* `cat8` (value: `"cat8"`)

* `dac-active` (value: `"dac-active"`)

* `dac-passive` (value: `"dac-passive"`)

* `mrj21-trunk` (value: `"mrj21-trunk"`)

* `coaxial` (value: `"coaxial"`)

* `mmf` (value: `"mmf"`)

* `mmf-om1` (value: `"mmf-om1"`)

* `mmf-om2` (value: `"mmf-om2"`)

* `mmf-om3` (value: `"mmf-om3"`)

* `mmf-om4` (value: `"mmf-om4"`)

* `mmf-om5` (value: `"mmf-om5"`)

* `smf` (value: `"smf"`)

* `smf-os1` (value: `"smf-os1"`)

* `smf-os2` (value: `"smf-os2"`)

* `aoc` (value: `"aoc"`)

* `power` (value: `"power"`)





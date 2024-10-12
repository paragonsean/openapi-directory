# NetBoxApi.WritablePowerFeed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amperage** | **Number** |  | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**maxUtilization** | **Number** | Maximum permissible draw (percentage) | [optional] 
**name** | **String** |  | 
**phase** | **String** |  | [optional] 
**powerPanel** | **Number** |  | 
**rack** | **Number** |  | [optional] 
**status** | **String** |  | [optional] 
**supply** | **String** |  | [optional] 
**tags** | **[String]** |  | [optional] 
**type** | **String** |  | [optional] 
**voltage** | **Number** |  | [optional] 



## Enum: PhaseEnum


* `single-phase` (value: `"single-phase"`)

* `three-phase` (value: `"three-phase"`)





## Enum: StatusEnum


* `offline` (value: `"offline"`)

* `active` (value: `"active"`)

* `planned` (value: `"planned"`)

* `failed` (value: `"failed"`)





## Enum: SupplyEnum


* `ac` (value: `"ac"`)

* `dc` (value: `"dc"`)





## Enum: TypeEnum


* `primary` (value: `"primary"`)

* `redundant` (value: `"redundant"`)





# NetBoxApi.WritableRack

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assetTag** | **String** | A unique tag used to identify this rack | [optional] 
**comments** | **String** |  | [optional] 
**created** | **Date** |  | [optional] [readonly] 
**customFields** | **Object** |  | [optional] 
**descUnits** | **Boolean** | Units are numbered top-to-bottom | [optional] 
**deviceCount** | **Number** |  | [optional] [readonly] 
**displayName** | **String** |  | [optional] [readonly] 
**facilityId** | **String** | Locally-assigned identifier | [optional] 
**group** | **Number** | Assigned group | [optional] 
**id** | **Number** |  | [optional] [readonly] 
**lastUpdated** | **Date** |  | [optional] [readonly] 
**name** | **String** |  | 
**outerDepth** | **Number** | Outer dimension of rack (depth) | [optional] 
**outerUnit** | **String** |  | [optional] 
**outerWidth** | **Number** | Outer dimension of rack (width) | [optional] 
**powerfeedCount** | **Number** |  | [optional] [readonly] 
**role** | **Number** | Functional role | [optional] 
**serial** | **String** |  | [optional] 
**site** | **Number** |  | 
**status** | **String** |  | [optional] 
**tags** | **[String]** |  | [optional] 
**tenant** | **Number** |  | [optional] 
**type** | **String** |  | [optional] 
**uHeight** | **Number** | Height in rack units | [optional] 
**width** | **Number** | Rail-to-rail width | [optional] 



## Enum: OuterUnitEnum


* `mm` (value: `"mm"`)

* `in` (value: `"in"`)





## Enum: StatusEnum


* `reserved` (value: `"reserved"`)

* `available` (value: `"available"`)

* `planned` (value: `"planned"`)

* `active` (value: `"active"`)

* `deprecated` (value: `"deprecated"`)





## Enum: TypeEnum


* `2-post-frame` (value: `"2-post-frame"`)

* `4-post-frame` (value: `"4-post-frame"`)

* `4-post-cabinet` (value: `"4-post-cabinet"`)

* `wall-frame` (value: `"wall-frame"`)

* `wall-cabinet` (value: `"wall-cabinet"`)





## Enum: WidthEnum


* `10` (value: `10`)

* `19` (value: `19`)

* `21` (value: `21`)

* `23` (value: `23`)





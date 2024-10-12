# BigQueryApi.DatasetAccessEntry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | [**DatasetReference**](DatasetReference.md) |  | [optional] 
**targetTypes** | **[String]** | Which resources in the dataset this entry applies to. Currently, only views are supported, but additional target types may be added in the future. | [optional] 



## Enum: [TargetTypesEnum]


* `TARGET_TYPE_UNSPECIFIED` (value: `"TARGET_TYPE_UNSPECIFIED"`)

* `VIEWS` (value: `"VIEWS"`)

* `ROUTINES` (value: `"ROUTINES"`)





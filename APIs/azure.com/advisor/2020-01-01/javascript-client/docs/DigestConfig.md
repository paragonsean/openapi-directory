# AdvisorManagementClient.DigestConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actionGroupResourceId** | **String** | Action group resource id used by digest. | [optional] 
**categories** | **[String]** | Categories to send digest for. If categories are not provided, then digest will be sent for all categories. | [optional] 
**frequency** | **Number** | Frequency that digest will be triggered, in days. Value must be between 7 and 30 days inclusive. | [optional] 
**language** | **String** | Language for digest content body. Value must be ISO 639-1 code for one of Azure portal supported languages. Otherwise, it will be converted into one. Default value is English (en). | [optional] 
**name** | **String** | Name of digest configuration. Value is case-insensitive and must be unique within a subscription. | [optional] 
**state** | **String** | State of digest configuration. | [optional] 



## Enum: [CategoriesEnum]


* `HighAvailability` (value: `"HighAvailability"`)

* `Security` (value: `"Security"`)

* `Performance` (value: `"Performance"`)

* `Cost` (value: `"Cost"`)

* `OperationalExcellence` (value: `"OperationalExcellence"`)





## Enum: StateEnum


* `Active` (value: `"Active"`)

* `Disabled` (value: `"Disabled"`)





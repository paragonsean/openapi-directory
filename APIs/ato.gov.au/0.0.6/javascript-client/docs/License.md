# BusinessRegistries.License

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**id** | **String** | The resource&#39;s unique identifier. | [optional] [readonly] 
**licenseType** | **String** | The license type. | [optional] [default to &#39;Australian Financial Services License&#39;]
**lifecycleState** | **String** | The business name&#39;s lifecycle state. | [optional] [default to &#39;Pending Approval&#39;]
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 



## Enum: LicenseTypeEnum


* `Australian Financial Services License` (value: `"Australian Financial Services License"`)

* `License 2B` (value: `"License 2B"`)





## Enum: LifecycleStateEnum


* `Approved` (value: `"Approved"`)

* `Expired` (value: `"Expired"`)

* `Issued` (value: `"Issued"`)

* `Pending Approval` (value: `"Pending Approval"`)

* `Suspended` (value: `"Suspended"`)





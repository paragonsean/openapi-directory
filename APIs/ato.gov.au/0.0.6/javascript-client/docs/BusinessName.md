# BusinessRegistries.BusinessName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**id** | **String** | The resource&#39;s unique identifier. | [optional] [readonly] 
**lifecycleState** | **String** | The business name&#39;s lifecycle state. | [optional] [default to &#39;Pending Approval&#39;]
**name** | **String** | The business name. | [optional] 
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 



## Enum: LifecycleStateEnum


* `Approved` (value: `"Approved"`)

* `Expired` (value: `"Expired"`)

* `Issued` (value: `"Issued"`)

* `Pending Approval` (value: `"Pending Approval"`)

* `Suspended` (value: `"Suspended"`)





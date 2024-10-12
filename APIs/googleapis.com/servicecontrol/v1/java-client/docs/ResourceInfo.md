

# ResourceInfo

Describes a resource associated with this operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**permission** | **String** | The resource permission required for this request. |  [optional] |
|**resourceContainer** | **String** | The identifier of the parent of this resource instance. Must be in one of the following formats: - &#x60;projects/&#x60; - &#x60;folders/&#x60; - &#x60;organizations/&#x60; |  [optional] |
|**resourceLocation** | **String** | The location of the resource. If not empty, the resource will be checked against location policy. The value must be a valid zone, region or multiregion. For example: \&quot;europe-west4\&quot; or \&quot;northamerica-northeast1-a\&quot; |  [optional] |
|**resourceName** | **String** | Name of the resource. This is used for auditing purposes. |  [optional] |




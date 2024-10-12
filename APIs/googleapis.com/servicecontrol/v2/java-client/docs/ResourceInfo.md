

# ResourceInfo

Describes a resource referenced in the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**container** | **String** | Optional. The identifier of the container of this resource. For Google Cloud APIs, the resource container must be one of the following formats: - &#x60;projects/&#x60; - &#x60;folders/&#x60; - &#x60;organizations/&#x60; Required for the policy enforcement on the container level (e.g. VPCSC, Location Policy check, Org Policy check). |  [optional] |
|**location** | **String** | Optional. The location of the resource, it must be a valid zone, region or multiregion, for example: \&quot;europe-west4\&quot;, \&quot;northamerica-northeast1-a\&quot;. Required for location policy check. |  [optional] |
|**name** | **String** | The name of the resource referenced in the request. |  [optional] |
|**permission** | **String** | The resource permission needed for this request. The format must be \&quot;{service}/{plural}.{verb}\&quot;. |  [optional] |
|**type** | **String** | The resource type in the format of \&quot;{service}/{kind}\&quot;. |  [optional] |




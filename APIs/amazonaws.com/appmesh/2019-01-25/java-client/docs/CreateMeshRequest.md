

# CreateMeshRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Up to 36 letters, numbers, hyphens, and underscores are allowed. |  [optional] |
|**meshName** | **String** | The name to use for the service mesh. |  |
|**spec** | [**CreateMeshRequestSpec**](CreateMeshRequestSpec.md) |  |  [optional] |
|**tags** | [**List&lt;TagRef&gt;**](TagRef.md) | Optional metadata that you can apply to the service mesh to assist with categorization and organization. Each tag consists of a key and an optional value, both of which you define. Tag keys can have a maximum character length of 128 characters, and tag values can have a maximum length of 256 characters. |  [optional] |




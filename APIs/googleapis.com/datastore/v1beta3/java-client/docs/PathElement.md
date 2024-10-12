

# PathElement

A (kind, ID/name) pair used to construct a key path. If either name or ID is set, the element is complete. If neither is set, the element is incomplete.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The auto-allocated ID of the entity. Never equal to zero. Values less than zero are discouraged and may not be supported in the future. |  [optional] |
|**kind** | **String** | The kind of the entity. A kind matching regex &#x60;__.*__&#x60; is reserved/read-only. A kind must not contain more than 1500 bytes when UTF-8 encoded. Cannot be &#x60;\&quot;\&quot;&#x60;. Must be valid UTF-8 bytes. Legacy values that are not valid UTF-8 are encoded as &#x60;__bytes__&#x60; where &#x60;&#x60; is the base-64 encoding of the bytes. |  [optional] |
|**name** | **String** | The name of the entity. A name matching regex &#x60;__.*__&#x60; is reserved/read-only. A name must not be more than 1500 bytes when UTF-8 encoded. Cannot be &#x60;\&quot;\&quot;&#x60;. Must be valid UTF-8 bytes. Legacy values that are not valid UTF-8 are encoded as &#x60;__bytes__&#x60; where &#x60;&#x60; is the base-64 encoding of the bytes. |  [optional] |




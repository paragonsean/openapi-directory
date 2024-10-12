

# GoogleFirestoreAdminV1beta2IndexConfig

The index configuration for this field.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ancestorField** | **String** | Output only. Specifies the resource name of the &#x60;Field&#x60; from which this field&#39;s index configuration is set (when &#x60;uses_ancestor_config&#x60; is true), or from which it *would* be set if this field had no index configuration (when &#x60;uses_ancestor_config&#x60; is false). |  [optional] |
|**indexes** | [**List&lt;GoogleFirestoreAdminV1beta2Index&gt;**](GoogleFirestoreAdminV1beta2Index.md) | The indexes supported for this field. |  [optional] |
|**reverting** | **Boolean** | Output only When true, the &#x60;Field&#x60;&#39;s index configuration is in the process of being reverted. Once complete, the index config will transition to the same state as the field specified by &#x60;ancestor_field&#x60;, at which point &#x60;uses_ancestor_config&#x60; will be &#x60;true&#x60; and &#x60;reverting&#x60; will be &#x60;false&#x60;. |  [optional] |
|**usesAncestorConfig** | **Boolean** | Output only. When true, the &#x60;Field&#x60;&#39;s index configuration is set from the configuration specified by the &#x60;ancestor_field&#x60;. When false, the &#x60;Field&#x60;&#39;s index configuration is defined explicitly. |  [optional] |




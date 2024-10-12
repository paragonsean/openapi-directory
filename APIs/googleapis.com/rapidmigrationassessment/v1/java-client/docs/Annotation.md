

# Annotation

Message describing an Annotation

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Create time stamp. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Labels as key value pairs. |  [optional] |
|**name** | **String** | name of resource. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of an annotation. |  [optional] |
|**updateTime** | **String** | Output only. Update time stamp. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| LEGACY_EXPORT_CONSENT | &quot;TYPE_LEGACY_EXPORT_CONSENT&quot; |
| QWIKLAB | &quot;TYPE_QWIKLAB&quot; |




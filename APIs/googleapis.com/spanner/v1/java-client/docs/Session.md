

# Session

A session in the Cloud Spanner API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approximateLastUseTime** | **String** | Output only. The approximate timestamp when the session is last used. It is typically earlier than the actual last use time. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The timestamp when the session is created. |  [optional] [readonly] |
|**creatorRole** | **String** | The database role which created this session. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels for the session. * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: &#x60;[a-z]([-a-z0-9]*[a-z0-9])?&#x60;. * Label values must be between 0 and 63 characters long and must conform to the regular expression &#x60;([a-z]([-a-z0-9]*[a-z0-9])?)?&#x60;. * No more than 64 labels can be associated with a given session. See https://goo.gl/xmQnxf for more information on and examples of labels. |  [optional] |
|**name** | **String** | Output only. The name of the session. This is always system-assigned. |  [optional] [readonly] |






# HotKeyInfo

Information about a hot key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hotKeyAge** | **String** | The age of the hot key measured from when it was first detected. |  [optional] |
|**key** | **String** | A detected hot key that is causing limited parallelism. This field will be populated only if the following flag is set to true: \&quot;--enable_hot_key_logging\&quot;. |  [optional] |
|**keyTruncated** | **Boolean** | If true, then the above key is truncated and cannot be deserialized. This occurs if the key above is populated and the key size is &gt;5MB. |  [optional] |




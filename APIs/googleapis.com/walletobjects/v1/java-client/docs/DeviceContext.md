

# DeviceContext

Device context associated with the object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceToken** | **String** | If set, redemption information will only be returned to the given device upon activation of the object. This should not be used as a stable identifier to trace a user&#39;s device. It can change across different passes for the same device or even across different activations for the same device. When setting this, callers must also set has_linked_device on the object being activated. |  [optional] |




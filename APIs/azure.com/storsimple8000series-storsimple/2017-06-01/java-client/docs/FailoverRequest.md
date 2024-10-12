

# FailoverRequest

The request object for triggering a failover of volume containers, from a source device to a target device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetDeviceId** | **String** | The ARM path ID of the device which will act as the failover target. |  [optional] |
|**volumeContainers** | **List&lt;String&gt;** | The list of path IDs of the volume containers which needs to be failed-over to the target device. |  [optional] |




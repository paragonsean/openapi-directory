

# Tunnelv1ProtoTunnelerInfo

TunnelerInfo contains metadata about tunneler launched by connection manager.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backoffRetryCount** | **Integer** | backoff_retry_count stores the number of times the tunneler has been retried by tunManager for current backoff sequence. Gets reset to 0 if time difference between 2 consecutive retries exceeds backoffRetryResetTime. |  [optional] |
|**id** | **String** | id is the unique id of a tunneler. |  [optional] |
|**latestErr** | [**Tunnelv1ProtoTunnelerError**](Tunnelv1ProtoTunnelerError.md) |  |  [optional] |
|**latestRetryTime** | **String** | latest_retry_time stores the time when the tunneler was last restarted. |  [optional] |
|**totalRetryCount** | **Integer** | total_retry_count stores the total number of times the tunneler has been retried by tunManager. |  [optional] |




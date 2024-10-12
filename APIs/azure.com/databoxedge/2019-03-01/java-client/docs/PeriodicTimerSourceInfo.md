

# PeriodicTimerSourceInfo

Periodic timer event source.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**schedule** | **String** | Periodic frequency at which timer event needs to be raised. Supports daily, hourly, minutes, and seconds. |  |
|**startTime** | **OffsetDateTime** | The time of the day that results in a valid trigger. Schedule is computed with reference to the time specified up to seconds. If timezone is not specified the time will considered to be in device timezone. The value will always be returned as UTC time. |  |
|**topic** | **String** | Topic where periodic events are published to IoT device. |  [optional] |




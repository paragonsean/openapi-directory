

# BatchVmwareVmRecoverableRangesRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**afterTime** | **OffsetDateTime** | Query filter - only ranges after this time will be included. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. |  [optional] |
|**beforeTime** | **OffsetDateTime** | Query filter - only ranges before this time will be included. The date-time string should be in ISO8601 format, such as &#x60;2018-01-01T01:23:45.678Z&#x60;. |  [optional] |
|**vmIds** | **List&lt;String&gt;** | The ID of each CDP-enabled virtual machine for which recoverable ranges are being retrieved. |  |




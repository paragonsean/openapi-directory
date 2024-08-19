

# GoogleChromeManagementV1DiskInfo

Status of the single storage device.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesReadThisSession** | **String** | Output only. Number of bytes read since last boot. |  [optional] [readonly] |
|**bytesWrittenThisSession** | **String** | Output only. Number of bytes written since last boot. |  [optional] [readonly] |
|**discardTimeThisSession** | **String** | Output only. Time spent discarding since last boot. Discarding is writing to clear blocks which are no longer in use. Supported on kernels 4.18+. |  [optional] [readonly] |
|**health** | **String** | Output only. Disk health. |  [optional] [readonly] |
|**ioTimeThisSession** | **String** | Output only. Counts the time the disk and queue were busy, so unlike the fields above, parallel requests are not counted multiple times. |  [optional] [readonly] |
|**manufacturer** | **String** | Output only. Disk manufacturer. |  [optional] [readonly] |
|**model** | **String** | Output only. Disk model. |  [optional] [readonly] |
|**readTimeThisSession** | **String** | Output only. Time spent reading from disk since last boot. |  [optional] [readonly] |
|**serialNumber** | **String** | Output only. Disk serial number. |  [optional] [readonly] |
|**sizeBytes** | **String** | Output only. Disk size. |  [optional] [readonly] |
|**type** | **String** | Output only. Disk type: eMMC / NVMe / ATA / SCSI. |  [optional] [readonly] |
|**volumeIds** | **List&lt;String&gt;** | Output only. Disk volumes. |  [optional] [readonly] |
|**writeTimeThisSession** | **String** | Output only. Time spent writing to disk since last boot. |  [optional] [readonly] |




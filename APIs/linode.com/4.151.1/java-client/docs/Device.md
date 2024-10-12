

# Device

Device can be either a Disk or Volume identified by `disk_id` or `volume_id`. Only one type per slot allowed. Can be null. Devices mapped from _sde_ through _sdh_ are unavailable in `fullvirt` virt_mode. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskId** | **Integer** | The Disk ID, or &#x60;null&#x60; if a Volume is assigned to this slot. |  [optional] |
|**volumeId** | **Integer** | The Volume ID, or &#x60;null&#x60; if a Disk is assigned to this slot. |  [optional] |




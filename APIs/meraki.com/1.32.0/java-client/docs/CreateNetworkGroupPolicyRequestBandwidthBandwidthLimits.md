

# CreateNetworkGroupPolicyRequestBandwidthBandwidthLimits

The bandwidth limits object, specifying upload and download speed for clients bound to the group policy. These are only enforced if 'settings' is set to 'custom'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**limitDown** | **Integer** | The maximum download limit (integer, in Kbps). null indicates no limit |  [optional] |
|**limitUp** | **Integer** | The maximum upload limit (integer, in Kbps). null indicates no limit |  [optional] |




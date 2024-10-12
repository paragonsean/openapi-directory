

# GoogleCloudOrgpolicyV2AlternatePolicySpec

Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run/darklaunch.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**launch** | **String** | Reference to the launch that will be used while audit logging and to control the launch. Should be set only in the alternate policy. |  [optional] |
|**spec** | [**GoogleCloudOrgpolicyV2PolicySpec**](GoogleCloudOrgpolicyV2PolicySpec.md) |  |  [optional] |






# DiskIopsConfiguration

The SSD IOPS (input/output operations per second) configuration for an Amazon FSx for NetApp ONTAP or FSx for OpenZFS file system. By default, Amazon FSx automatically provisions 3 IOPS per GB of storage capacity. You can provision additional IOPS per GB of storage. The configuration consists of the total number of provisioned SSD IOPS and how it is was provisioned, or the mode (by the customer or by Amazon FSx).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**DiskIopsConfigurationMode**](DiskIopsConfigurationMode.md) |  |  [optional] |
|**iops** | [**Integer**](Integer.md) |  |  [optional] |




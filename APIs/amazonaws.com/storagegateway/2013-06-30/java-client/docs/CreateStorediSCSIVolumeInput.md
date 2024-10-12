

# CreateStorediSCSIVolumeInput

<p>A JSON object containing one or more of the following fields:</p> <ul> <li> <p> <a>CreateStorediSCSIVolumeInput$DiskId</a> </p> </li> <li> <p> <a>CreateStorediSCSIVolumeInput$NetworkInterfaceId</a> </p> </li> <li> <p> <a>CreateStorediSCSIVolumeInput$PreserveExistingData</a> </p> </li> <li> <p> <a>CreateStorediSCSIVolumeInput$SnapshotId</a> </p> </li> <li> <p> <a>CreateStorediSCSIVolumeInput$TargetName</a> </p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**gatewayARN** | **String** | The Amazon Resource Name (ARN) of the gateway. Use the &lt;a&gt;ListGateways&lt;/a&gt; operation to return a list of gateways for your account and Amazon Web Services Region. |  |
|**diskId** | [**String**](String.md) |  |  |
|**snapshotId** | [**String**](String.md) |  |  [optional] |
|**preserveExistingData** | [**Boolean**](Boolean.md) |  |  |
|**targetName** | [**String**](String.md) |  |  |
|**networkInterfaceId** | [**String**](String.md) |  |  |
|**kmSEncrypted** | [**Boolean**](Boolean.md) |  |  [optional] |
|**kmSKey** | [**String**](String.md) |  |  [optional] |
|**tags** | [**List**](List.md) |  |  [optional] |




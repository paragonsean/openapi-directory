

# UpdateNetworkBluetoothSettingsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**advertisingEnabled** | **Boolean** | Whether APs will advertise beacons. |  [optional] |
|**major** | **Integer** | The major number to be used in the beacon identifier. Only valid in &#39;Non-unique&#39; mode. |  [optional] |
|**majorMinorAssignmentMode** | [**MajorMinorAssignmentModeEnum**](#MajorMinorAssignmentModeEnum) | The way major and minor number should be assigned to nodes in the network. (&#39;Unique&#39;, &#39;Non-unique&#39;) |  [optional] |
|**minor** | **Integer** | The minor number to be used in the beacon identifier. Only valid in &#39;Non-unique&#39; mode. |  [optional] |
|**scanningEnabled** | **Boolean** | Whether APs will scan for Bluetooth enabled clients. |  [optional] |
|**uuid** | **String** | The UUID to be used in the beacon identifier. |  [optional] |



## Enum: MajorMinorAssignmentModeEnum

| Name | Value |
|---- | -----|
| NON_UNIQUE | &quot;Non-unique&quot; |
| UNIQUE | &quot;Unique&quot; |




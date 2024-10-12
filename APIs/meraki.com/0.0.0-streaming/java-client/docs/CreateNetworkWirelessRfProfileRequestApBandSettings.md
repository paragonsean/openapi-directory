

# CreateNetworkWirelessRfProfileRequestApBandSettings

Settings that will be enabled if selectionType is set to 'ap'.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bandOperationMode** | [**BandOperationModeEnum**](#BandOperationModeEnum) | Choice between &#39;dual&#39;, &#39;2.4ghz&#39; or &#39;5ghz&#39;. Defaults to dual. |  [optional] |
|**bandSteeringEnabled** | **Boolean** | Steers client to most open band. Can be either true or false. Defaults to true. |  [optional] |



## Enum: BandOperationModeEnum

| Name | Value |
|---- | -----|
| _2_4GHZ | &quot;2.4ghz&quot; |
| _5GHZ | &quot;5ghz&quot; |
| DUAL | &quot;dual&quot; |






# CreateNetworkCameraWirelessProfileRequestSsid

The details of the SSID config.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authMode** | [**AuthModeEnum**](#AuthModeEnum) | The auth mode of the SSID. It can be set to (&#39;psk&#39;, &#39;8021x-radius&#39;). |  [optional] |
|**encryptionMode** | **String** | The encryption mode of the SSID. It can be set to (&#39;wpa&#39;, &#39;wpa-eap&#39;). With &#39;wpa&#39; mode, the authMode should be &#39;psk&#39; and with &#39;wpa-eap&#39; the authMode should be &#39;8021x-radius&#39; |  [optional] |
|**name** | **String** | The name of the SSID. |  [optional] |
|**psk** | **String** | The pre-shared key of the SSID. |  [optional] |



## Enum: AuthModeEnum

| Name | Value |
|---- | -----|
| _8021X_RADIUS | &quot;8021x-radius&quot; |
| PSK | &quot;psk&quot; |




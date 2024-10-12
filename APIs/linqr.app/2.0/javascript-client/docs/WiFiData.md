# LinQr.WiFiData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **Boolean** | Hidden network. Set to &#x60;true&#x60; if the SSID broadcasting is disabled (network is hidden). | [optional] [default to false]
**password** | **String** | Network password. The value is not required for the public network. | [optional] 
**security** | [**WiFiSecurity**](WiFiSecurity.md) | Network authentication type. Value &#x60;nopass&#x60; is used to set explicitly no access password (public network) and is an equivalent for left the password unset. In that case, the value may be also omitted. | [optional] 
**ssid** | **String** | Network SSID (name). | 



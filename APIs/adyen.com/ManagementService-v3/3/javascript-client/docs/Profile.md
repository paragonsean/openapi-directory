# ManagementApi.Profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authType** | **String** | The type of Wi-Fi network. Possible values: **wpa-psk**, **wpa2-psk**, **wpa-eap**, **wpa2-eap**. | 
**autoWifi** | **Boolean** | Indicates whether to automatically select the best authentication method available. Does not work on older terminal models. | [optional] 
**bssType** | **String** | Use **infra** for infrastructure-based networks. This applies to most networks. Use **adhoc** only if the communication is p2p-based between base stations. | 
**channel** | **Number** | The channel number of the Wi-Fi network. The recommended setting is **0** for automatic channel selection. | [optional] 
**defaultProfile** | **Boolean** | Indicates whether this is your preferred wireless network. If **true**, the terminal will try connecting to this network first. | [optional] 
**eap** | **String** | For &#x60;authType&#x60; **wpa-eap** or **wpa2-eap**. Possible values: **tls**, **peap**, **leap**, **fast** | [optional] 
**eapCaCert** | **File** | For &#x60;authType&#x60; **wpa-eap** or **wpa2-eap**. The root certificate from the CA that signed the certificate of the RADIUS server that is part of your wireless network. | [optional] 
**eapClientCert** | **File** | For &#x60;eap&#x60; **tls**. The certificate chain for the terminals. All terminals in the same network will use the same EAP client certificate. | [optional] 
**eapClientKey** | **File** | For &#x60;eap&#x60; **tls**. The RSA private key for the client. Include the lines BEGIN RSA PRIVATE KEY and END RSA PRIVATE KEY. | [optional] 
**eapClientPwd** | **String** | For &#x60;eap&#x60; **tls**. The password of the RSA key file, if that file is password-protected. | [optional] 
**eapIdentity** | **String** | For &#x60;authType&#x60; **wpa-eap** or **wpa2-eap**. The EAP-PEAP username from your MS-CHAP account. Must match the configuration of your RADIUS server. | [optional] 
**eapIntermediateCert** | **File** | For &#x60;eap&#x60; **tls**. The EAP intermediate certificate. | [optional] 
**eapPwd** | **String** | For &#x60;eap&#x60; **peap**. The EAP-PEAP password from your MS-CHAP account. Must match the configuration of your RADIUS server. | [optional] 
**hiddenSsid** | **Boolean** | Indicates if the network doesn&#39;t broadcast its SSID. Mandatory for Android terminals, because these terminals rely on this setting to be able to connect to any network. | [optional] 
**name** | **String** | Your name for the Wi-Fi profile. | [optional] 
**psk** | **String** | For &#x60;authType&#x60; **wpa-psk or **wpa2-psk**. The password to the wireless network. | [optional] 
**ssid** | **String** | The name of the wireless network. | 
**wsec** | **String** | The type of encryption. Possible values: **auto**, **ccmp** (recommended), **tkip** | 



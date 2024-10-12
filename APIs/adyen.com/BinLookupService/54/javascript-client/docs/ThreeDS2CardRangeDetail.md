# AdyenBinLookupApi.ThreeDS2CardRangeDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acsInfoInd** | **[String]** | Provides additional information to the 3DS Server. Possible values: - 01 (Authentication is available at ACS) - 02 (Attempts supported by ACS or DS) - 03 (Decoupled authentication supported) - 04 (Whitelisting supported) | [optional] 
**brandCode** | **String** | Card brand. | [optional] 
**endRange** | **String** | BIN end range. | [optional] 
**startRange** | **String** | BIN start range. | [optional] 
**threeDS2Versions** | **[String]** | Supported 3D Secure protocol versions | [optional] 
**threeDSMethodURL** | **String** | In a 3D Secure 2 browser-based flow, this is the URL where you should send the device fingerprint to. | [optional] 



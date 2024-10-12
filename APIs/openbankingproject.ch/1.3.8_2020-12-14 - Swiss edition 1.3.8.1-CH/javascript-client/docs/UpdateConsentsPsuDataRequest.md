# SwissNextGenBankingApiFramework.UpdateConsentsPsuDataRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**psuData** | [**PsuData**](PsuData.md) |  | 
**authenticationMethodId** | **String** | An identification provided by the ASPSP for the later identification of the authentication method selection.  | 
**scaAuthenticationData** | **String** | SCA authentication data, depending on the chosen authentication method. If the data is binary, then it is base64 encoded.  | 
**confirmationCode** | **String** | Confirmation Code as retrieved by the TPP from the redirect based SCA process. | 



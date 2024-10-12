# AdyenCheckoutApi.ThreeDS2Result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticationValue** | **String** | The &#x60;authenticationValue&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**cavvAlgorithm** | **String** | The algorithm used by the ACS to calculate the authentication value, only for Cartes Bancaires integrations. | [optional] 
**dsTransID** | **String** | The &#x60;dsTransID&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**eci** | **String** | The &#x60;eci&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**messageVersion** | **String** | The &#x60;messageVersion&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**threeDSServerTransID** | **String** | The &#x60;threeDSServerTransID&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**timestamp** | **String** | The &#x60;timestamp&#x60; value of the 3D Secure 2 authentication. | [optional] 
**transStatus** | **String** | The &#x60;transStatus&#x60; value as defined in the 3D Secure 2 specification. | [optional] 
**transStatusReason** | **String** | Provides information on why the &#x60;transStatus&#x60; field has the specified value. For possible values, refer to [our docs](https://docs.adyen.com/online-payments/3d-secure/api-reference#possible-transstatusreason-values). | [optional] 
**whiteListStatus** | **String** | The &#x60;whiteListStatus&#x60; value as defined in the 3D Secure 2 specification. | [optional] 



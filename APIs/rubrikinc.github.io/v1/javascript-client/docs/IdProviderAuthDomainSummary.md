# RubrikRestApi.IdProviderAuthDomainSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityId** | **String** | Entity ID of the Id Provider (IdP). | 
**id** | **String** | ID of this authentication domain. | 
**name** | **String** | Domain name. | 
**organizationId** | **String** | ID of the organization that added the authentication domain. | [optional] 
**signCert** | **String** | The Identity Provider (IdP) X509 certificate, stored using the PEM format, used to sign the SAML assertion. | 
**signCertExpiryDate** | **String** | The expiry date of the Identity Provider (IdP) X509 certificate. The date is a string with the ISO-8601 format like 2017-01-23T20:12:45.000Z with milliseconds precision. | 
**skewnessInSec** | **Number** | The clock skewness tolerance, in seconds, between the Identity Provider (IdP) and the Rubrik cluster. | 
**ssoUrl** | **String** | The Identity Provider (IdP) endpoint that Rubrik sends authentication request to in order to initiate SSO login. | 



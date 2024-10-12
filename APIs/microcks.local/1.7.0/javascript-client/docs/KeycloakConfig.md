# MicrocksApiV17.KeycloakConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authServerUrl** | **String** | SSO Server authentication url | 
**enabled** | **Boolean** | Whether Keycloak authentification and usage is enabled | 
**publicClient** | **String** | Name of public-client that can be used for requesting OAuth token | 
**realm** | **String** | Authentication realm name | 
**resource** | **String** | Name of Keycloak resource/application used on client side | 
**sslRequired** | **String** | SSL certificates requirements | 



## Enum: SslRequiredEnum


* `none` (value: `"none"`)

* `external` (value: `"external"`)





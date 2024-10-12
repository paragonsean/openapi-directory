# CertificateManagerApi.TrustConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The creation timestamp of a TrustConfig. | [optional] [readonly] 
**description** | **String** | One or more paragraphs of text description of a TrustConfig. | [optional] 
**etag** | **String** | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. | [optional] 
**labels** | **{String: String}** | Set of labels associated with a TrustConfig. | [optional] 
**name** | **String** | A user-defined name of the trust config. TrustConfig names must be unique globally and match pattern &#x60;projects/_*_/locations/_*_/trustConfigs/_*&#x60;. | [optional] 
**trustStores** | [**[TrustStore]**](TrustStore.md) | Set of trust stores to perform validation against. This field is supported when TrustConfig is configured with Load Balancers, currently not supported for SPIFFE certificate validation. Only one TrustStore specified is currently allowed. | [optional] 
**updateTime** | **String** | Output only. The last update timestamp of a TrustConfig. | [optional] [readonly] 



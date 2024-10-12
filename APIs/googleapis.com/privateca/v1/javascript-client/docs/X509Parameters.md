# CertificateAuthorityApi.X509Parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalExtensions** | [**[X509Extension]**](X509Extension.md) | Optional. Describes custom X.509 extensions. | [optional] 
**aiaOcspServers** | **[String]** | Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the \&quot;Authority Information Access\&quot; extension in the certificate. | [optional] 
**caOptions** | [**CaOptions**](CaOptions.md) |  | [optional] 
**keyUsage** | [**KeyUsage**](KeyUsage.md) |  | [optional] 
**nameConstraints** | [**NameConstraints**](NameConstraints.md) |  | [optional] 
**policyIds** | [**[ObjectId]**](ObjectId.md) | Optional. Describes the X.509 certificate policy object identifiers, per https://tools.ietf.org/html/rfc5280#section-4.2.1.4. | [optional] 



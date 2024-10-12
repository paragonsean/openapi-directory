

# X509Parameters

An X509Parameters is used to describe certain fields of an X.509 certificate, such as the key usage fields, fields specific to CA certificates, certificate policy extensions and custom extensions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalExtensions** | [**List&lt;X509Extension&gt;**](X509Extension.md) | Optional. Describes custom X.509 extensions. |  [optional] |
|**aiaOcspServers** | **List&lt;String&gt;** | Optional. Describes Online Certificate Status Protocol (OCSP) endpoint addresses that appear in the \&quot;Authority Information Access\&quot; extension in the certificate. |  [optional] |
|**caOptions** | [**CaOptions**](CaOptions.md) |  |  [optional] |
|**keyUsage** | [**KeyUsage**](KeyUsage.md) |  |  [optional] |
|**nameConstraints** | [**NameConstraints**](NameConstraints.md) |  |  [optional] |
|**policyIds** | [**List&lt;ObjectId&gt;**](ObjectId.md) | Optional. Describes the X.509 certificate policy object identifiers, per https://tools.ietf.org/html/rfc5280#section-4.2.1.4. |  [optional] |




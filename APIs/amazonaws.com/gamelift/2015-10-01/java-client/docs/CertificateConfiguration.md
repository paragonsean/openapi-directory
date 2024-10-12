

# CertificateConfiguration

Determines whether a TLS/SSL certificate is generated for a fleet. This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate. The certificate can be retrieved by calling the <a href=\"https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html\">Amazon GameLift Server SDK</a> operation <code>GetInstanceCertificate</code>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateType** | [**CertificateType**](CertificateType.md) |  |  |




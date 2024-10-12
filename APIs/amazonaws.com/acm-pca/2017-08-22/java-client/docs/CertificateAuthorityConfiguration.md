

# CertificateAuthorityConfiguration

Contains configuration information for your private certificate authority (CA). This includes information about the class of public key algorithm and the key pair that your private CA creates when it issues a certificate. It also includes the signature algorithm that it uses when issuing certificates, and its X.500 distinguished name. You must specify this information when you call the <a href=\"https://docs.aws.amazon.com/privateca/latest/APIReference/API_CreateCertificateAuthority.html\">CreateCertificateAuthority</a> action. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keyAlgorithm** | [**KeyAlgorithm**](KeyAlgorithm.md) |  |  |
|**signingAlgorithm** | [**SigningAlgorithm**](SigningAlgorithm.md) |  |  |
|**subject** | [**CertificateAuthorityConfigurationSubject**](CertificateAuthorityConfigurationSubject.md) |  |  |
|**csrExtensions** | [**CertificateAuthorityConfigurationCsrExtensions**](CertificateAuthorityConfigurationCsrExtensions.md) |  |  [optional] |




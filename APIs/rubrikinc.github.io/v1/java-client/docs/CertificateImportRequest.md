

# CertificateImportRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**csrId** | **String** | ID of the certificate signing request (CSR) associated with the imported certificate. |  [optional] |
|**description** | **String** | User-friendly description for the certificate. |  [optional] |
|**name** | **String** | Display name for the certificate. |  |
|**pemFile** | **String** | The certificates, and optionally private key to be imported, in PEM format. |  |
|**privateKey** | **String** | The private key, in PEM format, to be imported. If a private key is provided using this field instead of the pemFile field, the import fails if the private key is not successfully parsed. |  [optional] |




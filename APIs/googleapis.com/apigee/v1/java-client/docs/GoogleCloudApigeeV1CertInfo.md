

# GoogleCloudApigeeV1CertInfo

X.509 certificate as defined in RFC 5280.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**basicConstraints** | **String** | X.509 basic constraints extension. |  [optional] |
|**expiryDate** | **String** | X.509 &#x60;notAfter&#x60; validity period in milliseconds since epoch. |  [optional] |
|**isValid** | **String** | Flag that specifies whether the certificate is valid. Flag is set to &#x60;Yes&#x60; if the certificate is valid, &#x60;No&#x60; if expired, or &#x60;Not yet&#x60; if not yet valid. |  [optional] |
|**issuer** | **String** | X.509 issuer. |  [optional] |
|**publicKey** | **String** | Public key component of the X.509 subject public key info. |  [optional] |
|**serialNumber** | **String** | X.509 serial number. |  [optional] |
|**sigAlgName** | **String** | X.509 signatureAlgorithm. |  [optional] |
|**subject** | **String** | X.509 subject. |  [optional] |
|**subjectAlternativeNames** | **List&lt;String&gt;** | X.509 subject alternative names (SANs) extension. |  [optional] |
|**validFrom** | **String** | X.509 &#x60;notBefore&#x60; validity period in milliseconds since epoch. |  [optional] |
|**version** | **Integer** | X.509 version. |  [optional] |




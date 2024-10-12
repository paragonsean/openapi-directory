

# CertificateChains

Certificate chains needed to verify the attestation. Certificates in chains are PEM-encoded and are ordered based on https://tools.ietf.org/html/rfc5246#section-7.4.2.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**caviumCerts** | **List&lt;String&gt;** | Cavium certificate chain corresponding to the attestation. |  [optional] |
|**googleCardCerts** | **List&lt;String&gt;** | Google card certificate chain corresponding to the attestation. |  [optional] |
|**googlePartitionCerts** | **List&lt;String&gt;** | Google partition certificate chain corresponding to the attestation. |  [optional] |




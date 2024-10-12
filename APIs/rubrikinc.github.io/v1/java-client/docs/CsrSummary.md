

# CsrSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**csr** | **String** | Base64 encoded PKCS#10 certificate signing request. The request should start with -----BEGIN CERTIFICATE REQUEST-----. |  |
|**csrId** | **String** | ID of the generated CSR. |  |
|**hostnames** | **List&lt;String&gt;** | A comma-separated list of host names that are associated with the certificate. This list accepts wildcard hostnames, such as &#39;*.rubrik.example.com&#39;, in addition to fully-qualified domain names. |  |
|**name** | **String** | Display name for the generated CSR. |  |
|**subject** | **String** | Subject line of the CSR. |  |




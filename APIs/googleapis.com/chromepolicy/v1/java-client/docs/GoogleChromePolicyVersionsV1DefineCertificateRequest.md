

# GoogleChromePolicyVersionsV1DefineCertificateRequest

Request object for creating a certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ceritificateName** | **String** | Optional. The optional name of the certificate. If not specified, the certificate issuer will be used as the name. |  [optional] |
|**certificate** | **String** | Required. The raw contents of the .PEM, .CRT, or .CER file. |  [optional] |
|**settings** | [**List&lt;GoogleChromePolicyVersionsV1NetworkSetting&gt;**](GoogleChromePolicyVersionsV1NetworkSetting.md) | Optional. Certificate settings within the chrome.networks.certificates namespace. |  [optional] |
|**targetResource** | **String** | Required. The target resource on which this certificate is applied. The following resources are supported: * Organizational Unit (\&quot;orgunits/{orgunit_id}\&quot;) |  [optional] |




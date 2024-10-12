

# GoogleChromePolicyVersionsV1RemoveCertificateErrorDetails

Details of the errors encountered during a remove certificate request. This message will be returned as part of the details of a google.rpc.Status returned to the user when there is an error in their request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**certificateReferences** | [**List&lt;GoogleChromePolicyVersionsV1CertificateReference&gt;**](GoogleChromePolicyVersionsV1CertificateReference.md) | Output only. If the certificate was not removed, a list of references to the certificate that prevented it from being removed. Only unreferenced certificates can be removed. |  [optional] [readonly] |




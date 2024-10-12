

# SelfManagedCertificate

Certificate data for a SelfManaged Certificate. SelfManaged Certificates are uploaded by the user. Updating such certificates before they expire remains the user's responsibility.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pemCertificate** | **String** | Input only. The PEM-encoded certificate chain. Leaf certificate comes first, followed by intermediate ones if any. |  [optional] |
|**pemPrivateKey** | **String** | Input only. The PEM-encoded private key of the leaf certificate. |  [optional] |




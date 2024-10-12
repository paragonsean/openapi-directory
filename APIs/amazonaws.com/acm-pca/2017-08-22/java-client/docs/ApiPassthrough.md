

# ApiPassthrough

<p>Contains X.509 certificate information to be placed in an issued certificate. An <code>APIPassthrough</code> or <code>APICSRPassthrough</code> template variant must be selected, or else this parameter is ignored. </p> <p>If conflicting or duplicate certificate information is supplied from other sources, Amazon Web Services Private CA applies <a href=\"https://docs.aws.amazon.com/privateca/latest/userguide/UsingTemplates.html#template-order-of-operations\">order of operation rules</a> to determine what information is used.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**extensions** | [**ApiPassthroughExtensions**](ApiPassthroughExtensions.md) |  |  [optional] |
|**subject** | [**ASN1Subject**](ASN1Subject.md) |  |  [optional] |




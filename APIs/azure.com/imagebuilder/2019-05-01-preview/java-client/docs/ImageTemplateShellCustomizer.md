

# ImageTemplateShellCustomizer

Runs a shell script during the customization phase (Linux). Corresponds to Packer shell provisioner. Exactly one of 'scriptUri' or 'inline' can be specified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inline** | **List&lt;String&gt;** | Array of shell commands to execute |  [optional] |
|**scriptUri** | **String** | URI of the shell script to be run for customizing. It can be a github link, SAS URI for Azure Storage, etc |  [optional] |
|**sha256Checksum** | **String** | SHA256 checksum of the shell script provided in the scriptUri field |  [optional] |




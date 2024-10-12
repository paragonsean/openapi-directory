

# PscConfig

Information for Private Service Connect (PSC) setup for a Looker instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedVpcs** | **List&lt;String&gt;** | Optional. List of VPCs that are allowed ingress into looker. Format: projects/{project}/global/networks/{network} |  [optional] |
|**lookerServiceAttachmentUri** | **String** | Output only. URI of the Looker service attachment. |  [optional] [readonly] |
|**serviceAttachments** | [**List&lt;ServiceAttachment&gt;**](ServiceAttachment.md) | Optional. List of egress service attachment configurations. |  [optional] |




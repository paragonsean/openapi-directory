

# EndpointAttachment

represents the Connector's Endpoint Attachment resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the resource. |  [optional] |
|**endpointIp** | **String** | Output only. The Private Service Connect connection endpoint ip |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] |
|**name** | **String** | Output only. Resource name of the Endpoint Attachment. Format: projects/{project}/locations/{location}/endpointAttachments/{endpoint_attachment} |  [optional] [readonly] |
|**serviceAttachment** | **String** | Required. The path of the service attachment |  [optional] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |




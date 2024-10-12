

# ManagedZone

represents the Connector's Managed Zone resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Created time. |  [optional] [readonly] |
|**description** | **String** | Optional. Description of the resource. |  [optional] |
|**dns** | **String** | Required. DNS Name of the resource |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. Resource labels to represent user-provided metadata. Refer to cloud documentation on labels for more details. https://cloud.google.com/compute/docs/labeling-resources |  [optional] |
|**name** | **String** | Output only. Resource name of the Managed Zone. Format: projects/{project}/locations/global/managedZones/{managed_zone} |  [optional] [readonly] |
|**targetProject** | **String** | Required. The name of the Target Project |  [optional] |
|**targetVpc** | **String** | Required. The name of the Target Project VPC Network |  [optional] |
|**updateTime** | **String** | Output only. Updated time. |  [optional] [readonly] |




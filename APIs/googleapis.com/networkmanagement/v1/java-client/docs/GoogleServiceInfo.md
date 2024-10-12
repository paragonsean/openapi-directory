

# GoogleServiceInfo

For display only. Details of a Google Service sending packets to a VPC network. Although the source IP might be a publicly routable address, some Google Services use special routes within Google production infrastructure to reach Compute Engine Instances. https://cloud.google.com/vpc/docs/routes#special_return_paths

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**googleServiceType** | [**GoogleServiceTypeEnum**](#GoogleServiceTypeEnum) | Recognized type of a Google Service. |  [optional] |
|**sourceIp** | **String** | Source IP address. |  [optional] |



## Enum: GoogleServiceTypeEnum

| Name | Value |
|---- | -----|
| GOOGLE_SERVICE_TYPE_UNSPECIFIED | &quot;GOOGLE_SERVICE_TYPE_UNSPECIFIED&quot; |
| IAP | &quot;IAP&quot; |
| GFE_PROXY_OR_HEALTH_CHECK_PROBER | &quot;GFE_PROXY_OR_HEALTH_CHECK_PROBER&quot; |
| CLOUD_DNS | &quot;CLOUD_DNS&quot; |
| GOOGLE_API | &quot;GOOGLE_API&quot; |
| GOOGLE_API_PSC | &quot;GOOGLE_API_PSC&quot; |
| GOOGLE_API_VPC_SC | &quot;GOOGLE_API_VPC_SC&quot; |




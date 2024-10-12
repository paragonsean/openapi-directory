

# NodeGroup

Dataproc Node Group. The Dataproc NodeGroup resource is not related to the Dataproc NodeGroupAffinity resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**labels** | **Map&lt;String, String&gt;** | Optional. Node group labels. Label keys must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty. If specified, they must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). The node group must have no more than 32 labelsn. |  [optional] |
|**name** | **String** | The Node group resource name (https://aip.dev/122). |  [optional] |
|**nodeGroupConfig** | [**InstanceGroupConfig**](InstanceGroupConfig.md) |  |  [optional] |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) | Required. Node group roles. |  [optional] |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| DRIVER | &quot;DRIVER&quot; |




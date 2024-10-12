# CloudDataprocApi.NodeGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | Optional. Node group labels. Label keys must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). Label values can be empty. If specified, they must consist of from 1 to 63 characters and conform to RFC 1035 (https://www.ietf.org/rfc/rfc1035.txt). The node group must have no more than 32 labelsn. | [optional] 
**name** | **String** | The Node group resource name (https://aip.dev/122). | [optional] 
**nodeGroupConfig** | [**InstanceGroupConfig**](InstanceGroupConfig.md) |  | [optional] 
**roles** | **[String]** | Required. Node group roles. | [optional] 



## Enum: [RolesEnum]


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `DRIVER` (value: `"DRIVER"`)





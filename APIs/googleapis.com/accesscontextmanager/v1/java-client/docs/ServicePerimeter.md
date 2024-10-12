

# ServicePerimeter

`ServicePerimeter` describes a set of Google Cloud resources which can freely import and export data amongst themselves, but not export outside of the `ServicePerimeter`. If a request with a source within this `ServicePerimeter` has a target outside of the `ServicePerimeter`, the request will be blocked. Otherwise the request is allowed. There are two types of Service Perimeter - Regular and Bridge. Regular Service Perimeters cannot overlap, a single Google Cloud project or VPC network can only belong to a single regular Service Perimeter. Service Perimeter Bridges can contain only Google Cloud projects as members, a single Google Cloud project may belong to multiple Service Perimeter Bridges.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the &#x60;ServicePerimeter&#x60; and its use. Does not affect behavior. |  [optional] |
|**name** | **String** | Resource name for the &#x60;ServicePerimeter&#x60;. Format: &#x60;accessPolicies/{access_policy}/servicePerimeters/{service_perimeter}&#x60;. The &#x60;service_perimeter&#x60; component must begin with a letter, followed by alphanumeric characters or &#x60;_&#x60;. After you create a &#x60;ServicePerimeter&#x60;, you cannot change its &#x60;name&#x60;. |  [optional] |
|**perimeterType** | [**PerimeterTypeEnum**](#PerimeterTypeEnum) | Perimeter type indicator. A single project or VPC network is allowed to be a member of single regular perimeter, but multiple service perimeter bridges. A project cannot be a included in a perimeter bridge without being included in regular perimeter. For perimeter bridges, the restricted service list as well as access level lists must be empty. |  [optional] |
|**spec** | [**ServicePerimeterConfig**](ServicePerimeterConfig.md) |  |  [optional] |
|**status** | [**ServicePerimeterConfig**](ServicePerimeterConfig.md) |  |  [optional] |
|**title** | **String** | Human readable title. Must be unique within the Policy. |  [optional] |
|**useExplicitDryRunSpec** | **Boolean** | Use explicit dry run spec flag. Ordinarily, a dry-run spec implicitly exists for all Service Perimeters, and that spec is identical to the status for those Service Perimeters. When this flag is set, it inhibits the generation of the implicit spec, thereby allowing the user to explicitly provide a configuration (\&quot;spec\&quot;) to use in a dry-run version of the Service Perimeter. This allows the user to test changes to the enforced config (\&quot;status\&quot;) without actually enforcing them. This testing is done through analyzing the differences between currently enforced and suggested restrictions. use_explicit_dry_run_spec must bet set to True if any of the fields in the spec are set to non-default values. |  [optional] |



## Enum: PerimeterTypeEnum

| Name | Value |
|---- | -----|
| REGULAR | &quot;PERIMETER_TYPE_REGULAR&quot; |
| BRIDGE | &quot;PERIMETER_TYPE_BRIDGE&quot; |




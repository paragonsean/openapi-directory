

# PolicyBasedRoute

Policy-based routes route L4 network traffic based on not just destination IP address, but also source IP address, protocol, and more. If a policy-based route conflicts with other types of routes, the policy-based route always take precedence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Time when the policy-based route was created. |  [optional] [readonly] |
|**description** | **String** | Optional. An optional description of this resource. Provide this field when you create the resource. |  [optional] |
|**filter** | [**Filter**](Filter.md) |  |  [optional] |
|**interconnectAttachment** | [**InterconnectAttachment**](InterconnectAttachment.md) |  |  [optional] |
|**kind** | **String** | Output only. Type of this resource. Always networkconnectivity#policyBasedRoute for policy-based Route resources. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | User-defined labels. |  [optional] |
|**name** | **String** | Immutable. A unique name of the resource in the form of &#x60;projects/{project_number}/locations/global/PolicyBasedRoutes/{policy_based_route_id}&#x60; |  [optional] |
|**network** | **String** | Required. Fully-qualified URL of the network that this route applies to, for example: projects/my-project/global/networks/my-network. |  [optional] |
|**nextHopIlbIp** | **String** | Optional. The IP address of a global-access-enabled L4 ILB that is the next hop for matching packets. For this version, only nextHopIlbIp is supported. |  [optional] |
|**nextHopOtherRoutes** | [**NextHopOtherRoutesEnum**](#NextHopOtherRoutesEnum) | Optional. Other routes that will be referenced to determine the next hop of the packet. |  [optional] |
|**priority** | **Integer** | Optional. The priority of this policy-based route. Priority is used to break ties in cases where there are more than one matching policy-based routes found. In cases where multiple policy-based routes are matched, the one with the lowest-numbered priority value wins. The default value is 1000. The priority value must be from 1 to 65535, inclusive. |  [optional] |
|**selfLink** | **String** | Output only. Server-defined fully-qualified URL for this resource. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when the policy-based route was updated. |  [optional] [readonly] |
|**virtualMachine** | [**VirtualMachine**](VirtualMachine.md) |  |  [optional] |
|**warnings** | [**List&lt;Warnings&gt;**](Warnings.md) | Output only. If potential misconfigurations are detected for this route, this field will be populated with warning messages. |  [optional] [readonly] |



## Enum: NextHopOtherRoutesEnum

| Name | Value |
|---- | -----|
| OTHER_ROUTES_UNSPECIFIED | &quot;OTHER_ROUTES_UNSPECIFIED&quot; |
| DEFAULT_ROUTING | &quot;DEFAULT_ROUTING&quot; |




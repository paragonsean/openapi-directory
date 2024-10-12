# NetworkServicesApi.LbRouteExtension

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp when the resource was created. | [optional] [readonly] 
**description** | **String** | Optional. A human-readable description of the resource. | [optional] 
**extensionChains** | [**[ExtensionChain]**](ExtensionChain.md) | Required. A set of ordered extension chains that contain the match conditions and extensions to execute. Match conditions for each extension chain are evaluated in sequence for a given request. The first extension chain that has a condition that matches the request is executed. Any subsequent extension chains do not execute. Limited to 5 extension chains per resource. | [optional] 
**forwardingRules** | **[String]** | Required. A list of references to the forwarding rules to which this service extension is attached to. At least one forwarding rule is required. There can be only one &#x60;LbRouteExtension&#x60; resource per forwarding rule. | [optional] 
**labels** | **{String: String}** | Optional. Set of labels associated with the &#x60;LbRouteExtension&#x60; resource. The format must comply with [the requirements for labels](/compute/docs/labeling-resources#requirements) for Google Cloud resources. | [optional] 
**loadBalancingScheme** | **String** | Required. All backend services and forwarding rules referenced by this extension must share the same load balancing scheme. Supported values: &#x60;INTERNAL_MANAGED&#x60;, &#x60;EXTERNAL_MANAGED&#x60;. For more information, refer to [Choosing a load balancer](https://cloud.google.com/load-balancing/docs/backend-service). | [optional] 
**name** | **String** | Required. Identifier. Name of the &#x60;LbRouteExtension&#x60; resource in the following format: &#x60;projects/{project}/locations/{location}/lbRouteExtensions/{lb_route_extension}&#x60;. | [optional] 
**updateTime** | **String** | Output only. The timestamp when the resource was updated. | [optional] [readonly] 



## Enum: LoadBalancingSchemeEnum


* `LOAD_BALANCING_SCHEME_UNSPECIFIED` (value: `"LOAD_BALANCING_SCHEME_UNSPECIFIED"`)

* `INTERNAL_MANAGED` (value: `"INTERNAL_MANAGED"`)

* `EXTERNAL_MANAGED` (value: `"EXTERNAL_MANAGED"`)





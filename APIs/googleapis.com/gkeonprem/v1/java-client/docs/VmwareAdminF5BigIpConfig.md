

# VmwareAdminF5BigIpConfig

VmwareAdminF5BigIpConfig represents configuration parameters for an F5 BIG-IP load balancer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | The load balancer&#39;s IP address. |  [optional] |
|**partition** | **String** | The preexisting partition to be used by the load balancer. This partition is usually created for the admin cluster for example: &#39;my-f5-admin-partition&#39;. |  [optional] |
|**snatPool** | **String** | The pool name. Only necessary, if using SNAT. |  [optional] |




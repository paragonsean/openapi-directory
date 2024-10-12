

# VmwareAdminLoadBalancerConfig

VmwareAdminLoadBalancerConfig contains load balancer configuration for VMware admin cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**f5Config** | [**VmwareAdminF5BigIpConfig**](VmwareAdminF5BigIpConfig.md) |  |  [optional] |
|**manualLbConfig** | [**VmwareAdminManualLbConfig**](VmwareAdminManualLbConfig.md) |  |  [optional] |
|**metalLbConfig** | **Object** | VmwareAdminMetalLbConfig represents configuration parameters for a MetalLB load balancer. For admin clusters, currently no configurations is needed. |  [optional] |
|**seesawConfig** | [**VmwareAdminSeesawConfig**](VmwareAdminSeesawConfig.md) |  |  [optional] |
|**vipConfig** | [**VmwareAdminVipConfig**](VmwareAdminVipConfig.md) |  |  [optional] |




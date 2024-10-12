

# LinuxNodeConfig

Parameters that can be configured on Linux nodes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cgroupMode** | [**CgroupModeEnum**](#CgroupModeEnum) | cgroup_mode specifies the cgroup mode to be used on the node. |  [optional] |
|**sysctls** | **Map&lt;String, String&gt;** | The Linux kernel parameters to be applied to the nodes and all pods running on the nodes. The following parameters are supported. net.core.busy_poll net.core.busy_read net.core.netdev_max_backlog net.core.rmem_max net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse |  [optional] |



## Enum: CgroupModeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;CGROUP_MODE_UNSPECIFIED&quot; |
| V1 | &quot;CGROUP_MODE_V1&quot; |
| V2 | &quot;CGROUP_MODE_V2&quot; |




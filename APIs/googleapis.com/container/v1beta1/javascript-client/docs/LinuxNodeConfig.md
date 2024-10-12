# KubernetesEngineApi.LinuxNodeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cgroupMode** | **String** | cgroup_mode specifies the cgroup mode to be used on the node. | [optional] 
**sysctls** | **{String: String}** | The Linux kernel parameters to be applied to the nodes and all pods running on the nodes. The following parameters are supported. net.core.busy_poll net.core.busy_read net.core.netdev_max_backlog net.core.rmem_max net.core.wmem_default net.core.wmem_max net.core.optmem_max net.core.somaxconn net.ipv4.tcp_rmem net.ipv4.tcp_wmem net.ipv4.tcp_tw_reuse | [optional] 



## Enum: CgroupModeEnum


* `UNSPECIFIED` (value: `"CGROUP_MODE_UNSPECIFIED"`)

* `V1` (value: `"CGROUP_MODE_V1"`)

* `V2` (value: `"CGROUP_MODE_V2"`)





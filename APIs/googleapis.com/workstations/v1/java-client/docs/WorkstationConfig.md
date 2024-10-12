

# WorkstationConfig

A workstation configuration resource in the Cloud Workstations API. Workstation configurations act as templates for workstations. The workstation configuration defines details such as the workstation virtual machine (VM) instance type, persistent storage, container image defining environment, which IDE or Code Editor to use, and more. Administrators and platform teams can also use [Identity and Access Management (IAM)](https://cloud.google.com/iam/docs/overview) rules to grant access to teams or to individual developers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**annotations** | **Map&lt;String, String&gt;** | Optional. Client-specified annotations. |  [optional] |
|**conditions** | [**List&lt;Status&gt;**](Status.md) | Output only. Status conditions describing the current resource state. |  [optional] [readonly] |
|**container** | [**Container**](Container.md) |  |  [optional] |
|**createTime** | **String** | Output only. Time when this workstation configuration was created. |  [optional] [readonly] |
|**degraded** | **Boolean** | Output only. Whether this resource is degraded, in which case it may require user action to restore full functionality. See also the conditions field. |  [optional] [readonly] |
|**deleteTime** | **String** | Output only. Time when this workstation configuration was soft-deleted. |  [optional] [readonly] |
|**disableTcpConnections** | **Boolean** | Optional. Disables support for plain TCP connections in the workstation. By default the service supports TCP connections via a websocket relay. Setting this option to true disables that relay, which prevents the usage of services that require plain tcp connections, such as ssh. When enabled, all communication must occur over https or wss. |  [optional] |
|**displayName** | **String** | Optional. Human-readable name for this workstation configuration. |  [optional] |
|**enableAuditAgent** | **Boolean** | Optional. Whether to enable Linux &#x60;auditd&#x60; logging on the workstation. When enabled, a service account must also be specified that has &#x60;logging.buckets.write&#x60; permission on the project. Operating system audit logging is distinct from [Cloud Audit Logs](https://cloud.google.com/workstations/docs/audit-logging). |  [optional] |
|**encryptionKey** | [**CustomerEncryptionKey**](CustomerEncryptionKey.md) |  |  [optional] |
|**etag** | **String** | Optional. Checksum computed by the server. May be sent on update and delete requests to make sure that the client has an up-to-date value before proceeding. |  [optional] |
|**host** | [**Host**](Host.md) |  |  [optional] |
|**idleTimeout** | **String** | Optional. Number of seconds to wait before automatically stopping a workstation after it last received user traffic. A value of &#x60;\&quot;0s\&quot;&#x60; indicates that Cloud Workstations VMs created with this configuration should never time out due to idleness. Provide [duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#duration) terminated by &#x60;s&#x60; for seconds—for example, &#x60;\&quot;7200s\&quot;&#x60; (2 hours). The default is &#x60;\&quot;1200s\&quot;&#x60; (20 minutes). |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Optional. [Labels](https://cloud.google.com/workstations/docs/label-resources) that are applied to the workstation configuration and that are also propagated to the underlying Compute Engine resources. |  [optional] |
|**name** | **String** | Identifier. Full name of this workstation configuration. |  [optional] |
|**persistentDirectories** | [**List&lt;PersistentDirectory&gt;**](PersistentDirectory.md) | Optional. Directories to persist across workstation sessions. |  [optional] |
|**readinessChecks** | [**List&lt;ReadinessCheck&gt;**](ReadinessCheck.md) | Optional. Readiness checks to perform when starting a workstation using this workstation configuration. Mark a workstation as running only after all specified readiness checks return 200 status codes. |  [optional] |
|**reconciling** | **Boolean** | Output only. Indicates whether this workstation configuration is currently being updated to match its intended state. |  [optional] [readonly] |
|**replicaZones** | **List&lt;String&gt;** | Optional. Immutable. Specifies the zones used to replicate the VM and disk resources within the region. If set, exactly two zones within the workstation cluster&#39;s region must be specified—for example, &#x60;[&#39;us-central1-a&#39;, &#39;us-central1-f&#39;]&#x60;. If this field is empty, two default zones within the region are used. Immutable after the workstation configuration is created. |  [optional] |
|**runningTimeout** | **String** | Optional. Number of seconds that a workstation can run until it is automatically shut down. We recommend that workstations be shut down daily to reduce costs and so that security updates can be applied upon restart. The idle_timeout and running_timeout fields are independent of each other. Note that the running_timeout field shuts down VMs after the specified time, regardless of whether or not the VMs are idle. Provide duration terminated by &#x60;s&#x60; for seconds—for example, &#x60;\&quot;54000s\&quot;&#x60; (15 hours). Defaults to &#x60;\&quot;43200s\&quot;&#x60; (12 hours). A value of &#x60;\&quot;0s\&quot;&#x60; indicates that workstations using this configuration should never time out. If encryption_key is set, it must be greater than &#x60;\&quot;0s\&quot;&#x60; and less than &#x60;\&quot;86400s\&quot;&#x60; (24 hours). Warning: A value of &#x60;\&quot;0s\&quot;&#x60; indicates that Cloud Workstations VMs created with this configuration have no maximum running time. This is strongly discouraged because you incur costs and will not pick up security updates. |  [optional] |
|**uid** | **String** | Output only. A system-assigned unique identifier for this workstation configuration. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. Time when this workstation configuration was most recently updated. |  [optional] [readonly] |






# GuestOSNICCustomization

Guest OS nic customization

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocation** | [**AllocationEnum**](#AllocationEnum) | IP address allocation method |  [optional] |
|**dnsServers** | **List&lt;String&gt;** | List of dns servers to use |  [optional] |
|**gateway** | **List&lt;String&gt;** | Gateway addresses assigned to nic |  [optional] |
|**ipAddress** | **String** |  |  [optional] |
|**mask** | **String** |  |  [optional] |
|**primaryWinsServer** | **String** |  |  [optional] |
|**secondaryWinsServer** | **String** |  |  [optional] |



## Enum: AllocationEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;static&quot; |
| DYNAMIC | &quot;dynamic&quot; |




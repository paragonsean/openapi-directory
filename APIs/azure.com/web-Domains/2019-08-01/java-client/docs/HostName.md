

# HostName

Details of a hostname derived from a domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureResourceName** | **String** | Name of the Azure resource the hostname is assigned to. If it is assigned to a Traffic Manager then it will be the Traffic Manager name otherwise it will be the app name. |  [optional] |
|**azureResourceType** | [**AzureResourceTypeEnum**](#AzureResourceTypeEnum) | Type of the Azure resource the hostname is assigned to. |  [optional] |
|**customHostNameDnsRecordType** | [**CustomHostNameDnsRecordTypeEnum**](#CustomHostNameDnsRecordTypeEnum) | Type of the DNS record. |  [optional] |
|**hostNameType** | [**HostNameTypeEnum**](#HostNameTypeEnum) | Type of the hostname. |  [optional] |
|**name** | **String** | Name of the hostname. |  [optional] |
|**siteNames** | **List&lt;String&gt;** | List of apps the hostname is assigned to. This list will have more than one app only if the hostname is pointing to a Traffic Manager. |  [optional] |



## Enum: AzureResourceTypeEnum

| Name | Value |
|---- | -----|
| WEBSITE | &quot;Website&quot; |
| TRAFFIC_MANAGER | &quot;TrafficManager&quot; |



## Enum: CustomHostNameDnsRecordTypeEnum

| Name | Value |
|---- | -----|
| C_NAME | &quot;CName&quot; |
| A | &quot;A&quot; |



## Enum: HostNameTypeEnum

| Name | Value |
|---- | -----|
| VERIFIED | &quot;Verified&quot; |
| MANAGED | &quot;Managed&quot; |




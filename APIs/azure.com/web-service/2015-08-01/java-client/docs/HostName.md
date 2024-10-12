

# HostName

Details of a hostname derived from a domain

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureResourceName** | **String** | Name of the Azure resource the hostname is assigned to. If it is assigned to a traffic manager then it will be the traffic manager name otherwise it will be the website name |  [optional] |
|**azureResourceType** | [**AzureResourceTypeEnum**](#AzureResourceTypeEnum) | Type of the Azure resource the hostname is assigned to |  [optional] |
|**customHostNameDnsRecordType** | [**CustomHostNameDnsRecordTypeEnum**](#CustomHostNameDnsRecordTypeEnum) | Type of the Dns record |  [optional] |
|**hostNameType** | [**HostNameTypeEnum**](#HostNameTypeEnum) | Type of the hostname |  [optional] |
|**name** | **String** | Name of the hostname |  [optional] |
|**siteNames** | **List&lt;String&gt;** | List of sites the hostname is assigned to. This list will have more than one site only if the hostname is pointing to a Traffic Manager |  [optional] |



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




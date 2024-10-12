# WebSiteManagementClient.HostName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureResourceName** | **String** | Name of the Azure resource the hostname is assigned to. If it is assigned to a traffic manager then it will be the traffic manager name otherwise it will be the website name | [optional] 
**azureResourceType** | **String** | Type of the Azure resource the hostname is assigned to | [optional] 
**customHostNameDnsRecordType** | **String** | Type of the Dns record | [optional] 
**hostNameType** | **String** | Type of the hostname | [optional] 
**name** | **String** | Name of the hostname | [optional] 
**siteNames** | **[String]** | List of sites the hostname is assigned to. This list will have more than one site only if the hostname is pointing to a Traffic Manager | [optional] 



## Enum: AzureResourceTypeEnum


* `Website` (value: `"Website"`)

* `TrafficManager` (value: `"TrafficManager"`)





## Enum: CustomHostNameDnsRecordTypeEnum


* `CName` (value: `"CName"`)

* `A` (value: `"A"`)





## Enum: HostNameTypeEnum


* `Verified` (value: `"Verified"`)

* `Managed` (value: `"Managed"`)





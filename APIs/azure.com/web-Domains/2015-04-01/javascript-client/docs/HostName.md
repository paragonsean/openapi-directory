# DomainsApiClient.HostName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azureResourceName** | **String** | Name of the Azure resource the hostname is assigned to. If it is assigned to a Traffic Manager then it will be the Traffic Manager name otherwise it will be the app name. | [optional] 
**azureResourceType** | **String** | Type of the Azure resource the hostname is assigned to. | [optional] 
**customHostNameDnsRecordType** | **String** | Type of the DNS record. | [optional] 
**hostNameType** | **String** | Type of the hostname. | [optional] 
**name** | **String** | Name of the hostname. | [optional] 
**siteNames** | **[String]** | List of apps the hostname is assigned to. This list will have more than one app only if the hostname is pointing to a Traffic Manager. | [optional] 



## Enum: AzureResourceTypeEnum


* `Website` (value: `"Website"`)

* `TrafficManager` (value: `"TrafficManager"`)





## Enum: CustomHostNameDnsRecordTypeEnum


* `CName` (value: `"CName"`)

* `A` (value: `"A"`)





## Enum: HostNameTypeEnum


* `Verified` (value: `"Verified"`)

* `Managed` (value: `"Managed"`)





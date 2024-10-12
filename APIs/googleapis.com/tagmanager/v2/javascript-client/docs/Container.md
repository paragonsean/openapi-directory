# TagManagerApi.Container

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | GTM Account ID. | [optional] 
**containerId** | **String** | The Container ID uniquely identifies the GTM Container. | [optional] 
**domainName** | **[String]** | List of domain names associated with the Container. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**features** | [**ContainerFeatures**](ContainerFeatures.md) |  | [optional] 
**fingerprint** | **String** | The fingerprint of the GTM Container as computed at storage time. This value is recomputed whenever the account is modified. | [optional] 
**name** | **String** | Container display name. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**notes** | **String** | Container Notes. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**path** | **String** | GTM Container&#39;s API relative path. | [optional] 
**publicId** | **String** | Container Public ID. | [optional] 
**tagIds** | **[String]** | All Tag IDs that refer to this Container. | [optional] 
**tagManagerUrl** | **String** | Auto generated link to the tag manager UI | [optional] 
**taggingServerUrls** | **[String]** | List of server-side container URLs for the Container. If multiple URLs are provided, all URL paths must match. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 
**usageContext** | **[String]** | List of Usage Contexts for the Container. Valid values include: web, android, or ios. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update | [optional] 



## Enum: [UsageContextEnum]


* `usageContextUnspecified` (value: `"usageContextUnspecified"`)

* `web` (value: `"web"`)

* `android` (value: `"android"`)

* `ios` (value: `"ios"`)

* `androidSdk5` (value: `"androidSdk5"`)

* `iosSdk5` (value: `"iosSdk5"`)

* `amp` (value: `"amp"`)

* `server` (value: `"server"`)







# Container

Represents a Google Tag Manager Container, which specifies the platform tags will run on, manages workspaces, and retains container versions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**containerId** | **String** | The Container ID uniquely identifies the GTM Container. |  [optional] |
|**domainName** | **List&lt;String&gt;** | List of domain names associated with the Container. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**features** | [**ContainerFeatures**](ContainerFeatures.md) |  |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Container as computed at storage time. This value is recomputed whenever the account is modified. |  [optional] |
|**name** | **String** | Container display name. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**notes** | **String** | Container Notes. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**path** | **String** | GTM Container&#39;s API relative path. |  [optional] |
|**publicId** | **String** | Container Public ID. |  [optional] |
|**tagIds** | **List&lt;String&gt;** | All Tag IDs that refer to this Container. |  [optional] |
|**tagManagerUrl** | **String** | Auto generated link to the tag manager UI |  [optional] |
|**taggingServerUrls** | **List&lt;String&gt;** | List of server-side container URLs for the Container. If multiple URLs are provided, all URL paths must match. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |
|**usageContext** | [**List&lt;UsageContextEnum&gt;**](#List&lt;UsageContextEnum&gt;) | List of Usage Contexts for the Container. Valid values include: web, android, or ios. @mutable tagmanager.accounts.containers.create @mutable tagmanager.accounts.containers.update |  [optional] |



## Enum: List&lt;UsageContextEnum&gt;

| Name | Value |
|---- | -----|
| USAGE_CONTEXT_UNSPECIFIED | &quot;usageContextUnspecified&quot; |
| WEB | &quot;web&quot; |
| ANDROID | &quot;android&quot; |
| IOS | &quot;ios&quot; |
| ANDROID_SDK5 | &quot;androidSdk5&quot; |
| IOS_SDK5 | &quot;iosSdk5&quot; |
| AMP | &quot;amp&quot; |
| SERVER | &quot;server&quot; |




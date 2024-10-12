

# ResourceNameAvailabilityRequest

Resource name availability request content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**isFqdn** | **Boolean** | Is fully qualified domain name. |  [optional] |
|**name** | **String** | Resource name to verify. |  |
|**type** | [**TypeEnum**](#TypeEnum) | Resource type used for verification. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SITE | &quot;Site&quot; |
| SLOT | &quot;Slot&quot; |
| HOSTING_ENVIRONMENT | &quot;HostingEnvironment&quot; |
| PUBLISHING_USER | &quot;PublishingUser&quot; |
| MICROSOFT_WEB_SITES | &quot;Microsoft.Web/sites&quot; |
| MICROSOFT_WEB_SITES_SLOTS | &quot;Microsoft.Web/sites/slots&quot; |
| MICROSOFT_WEB_HOSTING_ENVIRONMENTS | &quot;Microsoft.Web/hostingEnvironments&quot; |
| MICROSOFT_WEB_PUBLISHING_USERS | &quot;Microsoft.Web/publishingUsers&quot; |




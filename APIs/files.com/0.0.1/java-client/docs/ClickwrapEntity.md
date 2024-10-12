

# ClickwrapEntity

Create Clickwrap

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | Body text of Clickwrap (supports Markdown formatting). |  [optional] |
|**id** | **Integer** | Clickwrap ID |  [optional] |
|**name** | **String** | Name of the Clickwrap agreement (used when selecting from multiple Clickwrap agreements.) |  [optional] |
|**useWithBundles** | [**UseWithBundlesEnum**](#UseWithBundlesEnum) | Use this Clickwrap for Bundles? |  [optional] |
|**useWithInboxes** | [**UseWithInboxesEnum**](#UseWithInboxesEnum) | Use this Clickwrap for Inboxes? |  [optional] |
|**useWithUsers** | [**UseWithUsersEnum**](#UseWithUsersEnum) | Use this Clickwrap for User Registrations?  Note: This only applies to User Registrations where the User is invited to your Files.com site using an E-Mail invitation process where they then set their own password. |  [optional] |



## Enum: UseWithBundlesEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| AVAILABLE | &quot;available&quot; |
| REQUIRE | &quot;require&quot; |



## Enum: UseWithInboxesEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| AVAILABLE | &quot;available&quot; |
| REQUIRE | &quot;require&quot; |



## Enum: UseWithUsersEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| REQUIRE | &quot;require&quot; |




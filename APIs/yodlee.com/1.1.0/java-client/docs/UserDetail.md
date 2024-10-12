

# UserDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**UserAddress**](UserAddress.md) |  |  [optional] |
|**email** | **String** | The email address of the user.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**id** | **Long** | The unique identifier of a consumer/user in Yodlee system for whom the API services would be accessed for.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/samlLogin&lt;/li&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**loginName** | **String** | The login name of the user used for authentication.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;POST user/register&lt;/li&gt;&lt;li&gt;GET user&lt;/li&gt;&lt;/ul&gt; |  [optional] [readonly] |
|**name** | [**Name**](Name.md) |  |  [optional] |
|**preferences** | [**UserResponsePreferences**](UserResponsePreferences.md) |  |  [optional] |
|**roleType** | [**RoleTypeEnum**](#RoleTypeEnum) |  |  [optional] |
|**segmentName** | **String** |  |  [optional] |



## Enum: RoleTypeEnum

| Name | Value |
|---- | -----|
| INDIVIDUAL | &quot;INDIVIDUAL&quot; |




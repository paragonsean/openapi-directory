

# PayorCreateApiKeyRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Description of the key. |  [optional] |
|**name** | **String** | A name for the key. |  |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) | &lt;p&gt;A role to assign to the key.&lt;/p&gt; &lt;p&gt;If you want your API key to have write access then assign the role velo.payor.admin&lt;/p&gt; &lt;p&gt;A later version will change this property from a list to string&lt;/p&gt;  |  |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| ADMIN | &quot;velo.payor.admin&quot; |
| SUPPORT | &quot;velo.payor.support&quot; |




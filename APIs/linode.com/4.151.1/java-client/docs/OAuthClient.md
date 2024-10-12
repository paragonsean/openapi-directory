

# OAuthClient

A third-party application registered to Linode that users may log into with their Linode account through our authentication server at <a target=\"_top\" href=\"https://login.linode.com\">https://login.linode.com</a>.  Using an OAuth Client, a third-party developer may be given access to some, or all, of a User's account for the purposes of their application. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The OAuth Client ID.  This is used to identify the client, and is a publicly-known value (it is not a secret).  |  [optional] [readonly] |
|**label** | **String** | The name of this application.  This will be presented to users when they are asked to grant it access to their Account.  |  [optional] |
|**_public** | **Boolean** | If this is a public or private OAuth Client.  Public clients have a slightly different authentication workflow than private clients.  See the &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://oauth.net/2/\&quot;&gt;OAuth spec&lt;/a&gt; for more details.  |  [optional] |
|**redirectUri** | **String** | The location a successful log in from &lt;a target&#x3D;\&quot;_top\&quot; href&#x3D;\&quot;https://login.linode.com\&quot;&gt;https://login.linode.com&lt;/a&gt; should be redirected to for this client.  The receiver of this redirect should be ready to accept an OAuth exchange code and finish the OAuth exchange.  |  [optional] |
|**secret** | **String** | The OAuth Client secret, used in the OAuth exchange.  This is returned as &#x60;&lt;REDACTED&gt;&#x60; except when an OAuth Client is created or its secret is reset.  This is a secret, and should not be shared or disclosed publicly.  |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of this application.  &#x60;active&#x60; by default.  |  [optional] [readonly] |
|**thumbnailUrl** | **String** | The URL where this client&#39;s thumbnail may be viewed, or &#x60;null&#x60; if this client does not have a thumbnail set.  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| DISABLED | &quot;disabled&quot; |
| SUSPENDED | &quot;suspended&quot; |




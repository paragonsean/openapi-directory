

# OAuthSettings

Configuration for OAuth login&consent flow behavior as well as for OAuth Credentials.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loginHint** | **String** | Domain hint to send as hd&#x3D;? parameter in OAuth request flow. Enables redirect to primary IDP by skipping Google&#39;s login screen. https://developers.google.com/identity/protocols/OpenIDConnect#hd-param Note: IAP does not verify that the id token&#39;s hd claim matches this value since access behavior is managed by IAM policies. |  [optional] |
|**programmaticClients** | **List&lt;String&gt;** | List of client ids allowed to use IAP programmatically. |  [optional] |




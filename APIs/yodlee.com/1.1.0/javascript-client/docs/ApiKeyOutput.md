# YodleeCoreApis.ApiKeyOutput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdDate** | **String** | The date on which the apiKey was created for the customer.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET /auth/apiKey&lt;/li&gt;&lt;li&gt;POST /auth/apiKey&lt;/li&gt;&lt;/ul&gt; | [optional] 
**expiresIn** | **Number** | Time in seconds after which the JWT token created for users expires.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET /auth/apiKey&lt;/li&gt;&lt;li&gt;POST /auth/apiKey&lt;/li&gt;&lt;/ul&gt; | [optional] 
**key** | **String** | ApiKey or the issuer key used to generate the JWT token for authentication.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET /auth/apiKey&lt;/li&gt;&lt;li&gt;POST /auth/apiKey&lt;/li&gt;&lt;/ul&gt; | [optional] 
**publicKey** | **String** | Public key uploaded by the customer while generating ApiKey.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET /auth/apiKey&lt;/li&gt;&lt;li&gt;POST /auth/apiKey&lt;/li&gt;&lt;/ul&gt; | [optional] 



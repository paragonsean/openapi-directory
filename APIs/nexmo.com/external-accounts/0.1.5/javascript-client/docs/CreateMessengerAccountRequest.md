# ExternalAccountsApi.CreateMessengerAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | This is the Facebook Business Page token. You can obtain the token using one of the following methods:  * Linking your Facebook Business Page to your account [with our Dashboard tool](https://dashboard.nexmo.com/messages/social-channels/facebook-connect) * Requesting a Page Access Token using the steps in the [Facebook token reference](https://developers.facebook.com/docs/pages/access-tokens/)  | 
**applications** | **[String]** | Contains a list of application IDs which are linked to the account. &lt;ul&gt; &lt;li&gt;There is just one application allowed per an account.&lt;/li&gt; &lt;li&gt;The application type must be type \&quot;messages\&quot;.&lt;/li&gt; &lt;/ul&gt; For more information see [Application API spec](https://developer.nexmo.com/api/application.v2) | [optional] 
**externalId** | **String** | This is the unique identifier within the provider&#39;s domain. In this case it is the Page ID for your Facebook Page. Go to your Facebook Page, click \&quot;Settings\&quot;, click \&quot;Messenger platform \&quot; scroll down to \&quot;Messenger link\&quot; to find your Page ID. | 
**name** | **String** | Custom account name | [optional] 



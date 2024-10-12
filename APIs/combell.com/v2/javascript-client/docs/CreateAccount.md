# PublicApi.CreateAccount

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ftpPassword** | **String** | Ftp password for the account.&lt;br /&gt;  Applies only if the servicepack contains hosting.&lt;br /&gt;  Passwords have to adhere to following rules:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Between 8-20 characters.&lt;/li&gt;&lt;li&gt;Must be a mix of letters and digits.&lt;/li&gt;&lt;li&gt;Must contain at least one digit (0-9).&lt;/li&gt;&lt;li&gt;Must contain at least one letter (a-z).&lt;/li&gt;&lt;li&gt;Cannot contain spaces.&lt;/li&gt;&lt;li&gt;Cannot contain characters: * € $ &amp; + } { &#39; \&quot; \\ &lt;/li&gt;&lt;/ul&gt; | [optional] 
**identifier** | **String** | An identifier for the account.&lt;br /&gt;  Should be a domain name for hosting accounts. | [optional] 
**servicepackId** | **Number** | The servicepack id that defines the account. | [optional] 



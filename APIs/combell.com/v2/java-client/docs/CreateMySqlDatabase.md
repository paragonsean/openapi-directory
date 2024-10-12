

# CreateMySqlDatabase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Integer** | The id of the account on which to create the database. |  [optional] |
|**databaseName** | **String** | The name for the database. This will be prefixed during provisioning.  The provided name during creation will be different from the provisioned database name. |  [optional] |
|**password** | **String** | The password for the database user.&lt;br /&gt;  Passwords have to adhere to following rules:&lt;br /&gt;&lt;ul&gt;&lt;li&gt;Between 8-20 characters.&lt;/li&gt;&lt;li&gt;Must be a mix of letters and digits.&lt;/li&gt;&lt;li&gt;Must contain at least one digit (0-9).&lt;/li&gt;&lt;li&gt;Must contain at least one letter (a-z).&lt;/li&gt;&lt;li&gt;Cannot contain spaces.&lt;/li&gt;&lt;li&gt;Cannot contain characters: * € $ &amp; + } { &#39; \&quot; \\ &lt;/li&gt;&lt;/ul&gt; |  [optional] |




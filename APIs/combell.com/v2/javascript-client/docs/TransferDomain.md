# PublicApi.TransferDomain

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authCode** | **String** | Authorization code which allows the transfer to execute. | [optional] 
**domainName** | **String** | The domain name to transfer.&lt;br /&gt;  Only pass the domain part and the tld.&lt;br /&gt;&lt;i&gt;For abc.com, abc is the domain part, com is the tld.&lt;/i&gt; | [optional] 
**nameServers** | **[String]** | List of name servers. When empty, the transfer will be done on default name servers. | [optional] 
**registrant** | [**RegistrantInput**](RegistrantInput.md) |  | [optional] 



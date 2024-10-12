

# UpdateDomainNameserversRequest

<p>Replaces the current set of name servers for the domain with the specified set of name servers. If you use Amazon Route 53 as your DNS service, specify the four name servers in the delegation set for the hosted zone for the domain.</p> <p>If successful, this operation returns an operation ID that you can use to track the progress and completion of the action. If the request is not completed successfully, the domain registrant will be notified by email. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainName** | [**String**](String.md) |  |  |
|**fiAuthKey** | [**String**](String.md) |  |  [optional] |
|**nameservers** | [**List**](List.md) |  |  |




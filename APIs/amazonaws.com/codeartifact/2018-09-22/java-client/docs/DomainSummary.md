

# DomainSummary

 Information about a domain, including its name, Amazon Resource Name (ARN), and status. The <a href=\"https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListDomains.html\">ListDomains</a> operation returns a list of <code>DomainSummary</code> objects. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  [optional] |
|**owner** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  [optional] |
|**status** | [**DomainStatus**](DomainStatus.md) |  |  [optional] |
|**createdTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**encryptionKey** | [**String**](String.md) |  |  [optional] |




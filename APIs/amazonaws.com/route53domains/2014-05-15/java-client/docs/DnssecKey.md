

# DnssecKey

<p>Information about the DNSSEC key.</p> <p>You get this from your DNS provider and then give it to Route 53 (by using <a href=\"https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_AssociateDelegationSignerToDomain.html\">AssociateDelegationSignerToDomain</a>) to pass it to the registry to establish the chain of trust.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**Integer**](Integer.md) |  |  [optional] |
|**flags** | [**Integer**](Integer.md) |  |  [optional] |
|**publicKey** | [**String**](String.md) |  |  [optional] |
|**digestType** | [**Integer**](Integer.md) |  |  [optional] |
|**digest** | [**String**](String.md) |  |  [optional] |
|**keyTag** | [**Integer**](Integer.md) |  |  [optional] |
|**id** | [**String**](String.md) |  |  [optional] |




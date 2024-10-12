

# CertVerification

A set of ACME challenges you can use to allow Hosting to create an SSL certificate for your domain name before directing traffic to Hosting servers. Use either the DNS or HTTP challenge; it's not necessary to provide both.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dns** | [**DnsUpdates**](DnsUpdates.md) |  |  [optional] |
|**http** | [**HttpUpdate**](HttpUpdate.md) |  |  [optional] |




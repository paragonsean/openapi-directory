

# DnsUpdates

A set of DNS record updates that you should make to allow Hosting to serve secure content in response to requests against your domain name. These updates present the current state of your domain name's DNS records when Hosting last queried them, and the desired set of records that Hosting needs to see before your custom domain can be fully active.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkTime** | **String** | The last time Hosting checked your custom domain&#39;s DNS records. |  [optional] |
|**desired** | [**List&lt;DnsRecordSet&gt;**](DnsRecordSet.md) | The set of DNS records Hosting needs to serve secure content on the domain. |  [optional] |
|**discovered** | [**List&lt;DnsRecordSet&gt;**](DnsRecordSet.md) | The set of DNS records Hosting discovered when inspecting a domain. |  [optional] |




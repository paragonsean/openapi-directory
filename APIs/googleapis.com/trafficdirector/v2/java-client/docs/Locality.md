

# Locality

Identifies location of where either Envoy runs or where upstream hosts run.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**region** | **String** | Region this :ref:&#x60;zone &#x60; belongs to. |  [optional] |
|**subZone** | **String** | When used for locality of upstream hosts, this field further splits zone into smaller chunks of sub-zones so they can be load balanced independently. |  [optional] |
|**zone** | **String** | Defines the local service zone where Envoy is running. Though optional, it should be set if discovery service routing is used and the discovery service exposes :ref:&#x60;zone data &#x60;, either in this message or via :option:&#x60;--service-zone&#x60;. The meaning of zone is context dependent, e.g. &#x60;Availability Zone (AZ) &#x60;_ on AWS, &#x60;Zone &#x60;_ on GCP, etc. |  [optional] |




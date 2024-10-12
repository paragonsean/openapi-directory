

# DnsPeering

DNS peering configuration. These configurations are used to create DNS peering with the customer Cloud DNS.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Optional. Optional description of the dns zone. |  [optional] |
|**domain** | **String** | Required. The dns name suffix of the zone. |  [optional] |
|**name** | **String** | Required. The resource name of the dns peering zone. Format: projects/{project}/locations/{location}/instances/{instance}/dnsPeerings/{dns_peering} |  [optional] |
|**targetNetwork** | **String** | Optional. Optional target network to which dns peering should happen. |  [optional] |
|**targetProject** | **String** | Optional. Optional target project to which dns peering should happen. |  [optional] |




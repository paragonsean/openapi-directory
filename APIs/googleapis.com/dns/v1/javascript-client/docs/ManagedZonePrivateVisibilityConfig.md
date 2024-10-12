# CloudDnsApi.ManagedZonePrivateVisibilityConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gkeClusters** | [**[ManagedZonePrivateVisibilityConfigGKECluster]**](ManagedZonePrivateVisibilityConfigGKECluster.md) | The list of Google Kubernetes Engine clusters that can see this zone. | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#managedZonePrivateVisibilityConfig&#39;]
**networks** | [**[ManagedZonePrivateVisibilityConfigNetwork]**](ManagedZonePrivateVisibilityConfigNetwork.md) | The list of VPC networks that can see this zone. | [optional] 



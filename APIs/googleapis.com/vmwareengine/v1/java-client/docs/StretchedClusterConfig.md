

# StretchedClusterConfig

Configuration of a stretched cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**preferredLocation** | **String** | Required. Zone that will remain operational when connection between the two zones is lost. Specify the resource name of a zone that belongs to the region of the private cloud. For example: &#x60;projects/{project}/locations/europe-west3-a&#x60; where &#x60;{project}&#x60; can either be a project number or a project ID. |  [optional] |
|**secondaryLocation** | **String** | Required. Additional zone for a higher level of availability and load balancing. Specify the resource name of a zone that belongs to the region of the private cloud. For example: &#x60;projects/{project}/locations/europe-west3-b&#x60; where &#x60;{project}&#x60; can either be a project number or a project ID. |  [optional] |




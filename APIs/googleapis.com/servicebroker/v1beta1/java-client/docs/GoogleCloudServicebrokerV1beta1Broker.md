

# GoogleCloudServicebrokerV1beta1Broker

Broker represents a consumable collection of Service Registry catalogs exposed as an OSB Broker.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp for when the broker was created. |  [optional] |
|**name** | **String** | Name of the broker in the format: &lt;projects&gt;/&lt;project-id&gt;/brokers/&lt;broker&gt;. This allows for multiple brokers per project which can be used to enable having custom brokers per GKE cluster, for example. |  [optional] |
|**title** | **String** | User friendly title of the broker. Limited to 1024 characters. Requests with longer titles will be rejected. |  [optional] |
|**url** | **String** | Output only. URL of the broker OSB-compliant endpoint, for example: https://servicebroker.googleapis.com/projects/&lt;project&gt;/brokers/&lt;broker&gt; |  [optional] |




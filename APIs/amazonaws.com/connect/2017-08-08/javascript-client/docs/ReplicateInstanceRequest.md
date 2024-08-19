# AmazonConnectService.ReplicateInstanceRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicaRegion** | **String** | The Amazon Web Services Region where to replicate the Amazon Connect instance. | 
**clientToken** | **String** | A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\&quot;&gt;Making retries safe with idempotent APIs&lt;/a&gt;. | [optional] 
**replicaAlias** | **String** | The alias for the replicated instance. The &lt;code&gt;ReplicaAlias&lt;/code&gt; must be unique. | 



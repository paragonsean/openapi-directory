# CloudPubSubApi.CreateSnapshotRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | Optional. See [Creating and managing labels](https://cloud.google.com/pubsub/docs/labels). | [optional] 
**subscription** | **String** | Required. The subscription whose backlog the snapshot retains. Specifically, the created snapshot is guaranteed to retain: (a) The existing backlog on the subscription. More precisely, this is defined as the messages in the subscription&#39;s backlog that are unacknowledged upon the successful completion of the &#x60;CreateSnapshot&#x60; request; as well as: (b) Any messages published to the subscription&#39;s topic following the successful completion of the CreateSnapshot request. Format is &#x60;projects/{project}/subscriptions/{sub}&#x60;. | [optional] 



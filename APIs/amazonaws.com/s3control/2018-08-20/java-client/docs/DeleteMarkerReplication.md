

# DeleteMarkerReplication

<p>Specifies whether S3 on Outposts replicates delete markers. If you specify a <code>Filter</code> element in your replication configuration, you must also include a <code>DeleteMarkerReplication</code> element. If your <code>Filter</code> includes a <code>Tag</code> element, the <code>DeleteMarkerReplication</code> element's <code>Status</code> child element must be set to <code>Disabled</code>, because S3 on Outposts does not support replicating delete markers for tag-based rules.</p> <p>For more information about delete marker replication, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html#outposts-replication-what-is-replicated\">How delete operations affect replication</a> in the <i>Amazon S3 User Guide</i>. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**DeleteMarkerReplicationStatus**](DeleteMarkerReplicationStatus.md) |  |  |




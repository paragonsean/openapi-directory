

# MultiRegionAccessPointRoute

<p>A structure for a Multi-Region Access Point that indicates where Amazon S3 traffic can be routed. Routes can be either active or passive. Active routes can process Amazon S3 requests through the Multi-Region Access Point, but passive routes are not eligible to process Amazon S3 requests. </p> <p>Each route contains the Amazon S3 bucket name and the Amazon Web Services Region that the bucket is located in. The route also includes the <code>TrafficDialPercentage</code> value, which shows whether the bucket and Region are active (indicated by a value of <code>100</code>) or passive (indicated by a value of <code>0</code>).</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bucket** | [**String**](String.md) |  |  [optional] |
|**region** | [**String**](String.md) |  |  [optional] |
|**trafficDialPercentage** | [**Integer**](Integer.md) |  |  |






# CloudFrontOriginAccessIdentityList

Lists the origin access identities for CloudFront.Send a <code>GET</code> request to the <code>/<i>CloudFront API version</i>/origin-access-identity/cloudfront</code> resource. The response includes a <code>CloudFrontOriginAccessIdentityList</code> element with zero or more <code>CloudFrontOriginAccessIdentitySummary</code> child elements. By default, your entire list of origin access identities is returned in one single page. If the list is long, you can paginate it using the <code>MaxItems</code> and <code>Marker</code> parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**marker** | [**String**](String.md) |  |  |
|**nextMarker** | [**String**](String.md) |  |  [optional] |
|**maxItems** | [**Integer**](Integer.md) |  |  |
|**isTruncated** | [**Boolean**](Boolean.md) |  |  |
|**quantity** | [**Integer**](Integer.md) |  |  |
|**items** | [**List**](List.md) |  |  [optional] |




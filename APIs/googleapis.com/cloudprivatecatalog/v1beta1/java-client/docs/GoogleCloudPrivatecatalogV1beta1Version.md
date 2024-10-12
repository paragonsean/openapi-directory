

# GoogleCloudPrivatecatalogV1beta1Version

The consumer representation of a version which is a child resource under a `Product` with asset data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**asset** | **Map&lt;String, Object&gt;** | Output only. The asset which has been validated and is ready to be provisioned. See google.cloud.privatecatalogproducer.v1beta.Version.asset for details. |  [optional] |
|**createTime** | **String** | Output only. The time when the version was created. |  [optional] |
|**description** | **String** | Output only. The user-supplied description of the version. Maximum of 256 characters. |  [optional] |
|**name** | **String** | Output only. The resource name of the version, in the format &#x60;catalogs/{catalog_id}/products/{product_id}/versions/a-z*[a-z0-9]&#39;.  A unique identifier for the version under a product. |  [optional] |
|**updateTime** | **String** | Output only. The time when the version was last updated. |  [optional] |




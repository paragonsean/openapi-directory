

# OfflineStoreConfig

<p>The configuration of an <code>OfflineStore</code>.</p> <p>Provide an <code>OfflineStoreConfig</code> in a request to <code>CreateFeatureGroup</code> to create an <code>OfflineStore</code>.</p> <p>To encrypt an <code>OfflineStore</code> using at rest data encryption, specify Amazon Web Services Key Management Service (KMS) key ID, or <code>KMSKeyId</code>, in <code>S3StorageConfig</code>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**s3StorageConfig** | [**OfflineStoreConfigS3StorageConfig**](OfflineStoreConfigS3StorageConfig.md) |  |  |
|**disableGlueTableCreation** | [**Boolean**](Boolean.md) |  |  [optional] |
|**dataCatalogConfig** | [**OfflineStoreConfigDataCatalogConfig**](OfflineStoreConfigDataCatalogConfig.md) |  |  [optional] |
|**tableFormat** | [**TableFormat**](TableFormat.md) |  |  [optional] |




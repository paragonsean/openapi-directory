

# KeyUsage

A KeyUsage describes key usage values that may appear in an X.509 certificate.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**baseKeyUsage** | [**KeyUsageOptions**](KeyUsageOptions.md) |  |  [optional] |
|**extendedKeyUsage** | [**ExtendedKeyUsageOptions**](ExtendedKeyUsageOptions.md) |  |  [optional] |
|**unknownExtendedKeyUsages** | [**List&lt;ObjectId&gt;**](ObjectId.md) | Used to describe extended key usages that are not listed in the KeyUsage.ExtendedKeyUsageOptions message. |  [optional] |




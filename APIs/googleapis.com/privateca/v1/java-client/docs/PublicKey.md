

# PublicKey

A PublicKey describes a public key.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**format** | [**FormatEnum**](#FormatEnum) | Required. The format of the public key. |  [optional] |
|**key** | **byte[]** | Required. A public key. The padding and encoding must match with the &#x60;KeyFormat&#x60; value specified for the &#x60;format&#x60; field. |  [optional] |



## Enum: FormatEnum

| Name | Value |
|---- | -----|
| KEY_FORMAT_UNSPECIFIED | &quot;KEY_FORMAT_UNSPECIFIED&quot; |
| PEM | &quot;PEM&quot; |




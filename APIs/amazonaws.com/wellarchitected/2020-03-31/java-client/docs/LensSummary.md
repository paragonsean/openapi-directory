

# LensSummary

A lens summary of a lens.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lensArn** | [**String**](String.md) |  |  [optional] |
|**lensAlias** | **String** | &lt;p&gt;The alias of the lens.&lt;/p&gt; &lt;p&gt;For Amazon Web Services official lenses, this is either the lens alias, such as &lt;code&gt;serverless&lt;/code&gt;, or the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-east-1::lens/serverless&lt;/code&gt;. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.&lt;/p&gt; &lt;p&gt;For custom lenses, this is the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Each lens is identified by its &lt;a&gt;LensSummary$LensAlias&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**lensName** | **String** | The full name of the lens. |  [optional] |
|**lensType** | [**LensType**](LensType.md) |  |  [optional] |
|**description** | **String** | The description of the lens. |  [optional] |
|**createdAt** | **OffsetDateTime** | The date and time recorded. |  [optional] |
|**updatedAt** | **OffsetDateTime** | The date and time recorded. |  [optional] |
|**lensVersion** | [**String**](String.md) |  |  [optional] |
|**owner** | **String** | An Amazon Web Services account ID. |  [optional] |
|**lensStatus** | [**LensStatus**](LensStatus.md) |  |  [optional] |




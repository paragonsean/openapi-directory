

# LensUpgradeSummary

Lens upgrade summary return object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**workloadId** | **String** | The ID assigned to the workload. This ID is unique within an Amazon Web Services Region. |  [optional] |
|**workloadName** | **String** | &lt;p&gt;The name of the workload.&lt;/p&gt; &lt;p&gt;The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.&lt;/p&gt; |  [optional] |
|**lensAlias** | **String** | &lt;p&gt;The alias of the lens.&lt;/p&gt; &lt;p&gt;For Amazon Web Services official lenses, this is either the lens alias, such as &lt;code&gt;serverless&lt;/code&gt;, or the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-east-1::lens/serverless&lt;/code&gt;. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.&lt;/p&gt; &lt;p&gt;For custom lenses, this is the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Each lens is identified by its &lt;a&gt;LensSummary$LensAlias&lt;/a&gt;.&lt;/p&gt; |  [optional] |
|**lensArn** | [**String**](String.md) |  |  [optional] |
|**currentLensVersion** | [**String**](String.md) |  |  [optional] |
|**latestLensVersion** | [**String**](String.md) |  |  [optional] |




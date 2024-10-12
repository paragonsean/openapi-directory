# AwsWellArchitectedTool.LensReviewReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lensAlias** | **String** | &lt;p&gt;The alias of the lens.&lt;/p&gt; &lt;p&gt;For Amazon Web Services official lenses, this is either the lens alias, such as &lt;code&gt;serverless&lt;/code&gt;, or the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-east-1::lens/serverless&lt;/code&gt;. Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.&lt;/p&gt; &lt;p&gt;For custom lenses, this is the lens ARN, such as &lt;code&gt;arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Each lens is identified by its &lt;a&gt;LensSummary$LensAlias&lt;/a&gt;.&lt;/p&gt; | [optional] 
**lensArn** | **String** |  | [optional] 
**base64String** | **String** | &lt;p&gt;The Base64-encoded string representation of a lens review report.&lt;/p&gt; &lt;p&gt;This data can be used to create a PDF file.&lt;/p&gt; &lt;p&gt;Only returned by &lt;a&gt;GetConsolidatedReport&lt;/a&gt; when &lt;code&gt;PDF&lt;/code&gt; format is requested.&lt;/p&gt; | [optional] 



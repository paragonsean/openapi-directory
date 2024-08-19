# AmazonCodeGuruSecurity.CreateScanRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysisType** | **String** | The type of analysis you want CodeGuru Security to perform in the scan, either &lt;code&gt;Security&lt;/code&gt; or &lt;code&gt;All&lt;/code&gt;. The &lt;code&gt;Security&lt;/code&gt; type only generates findings related to security. The &lt;code&gt;All&lt;/code&gt; type generates both security findings and quality findings. Defaults to &lt;code&gt;Security&lt;/code&gt; type if missing. | [optional] 
**clientToken** | **String** | The idempotency token for the request. Amazon CodeGuru Security uses this value to prevent the accidental creation of duplicate scans if there are failures and retries. | [optional] 
**resourceId** | [**CreateScanRequestResourceId**](CreateScanRequestResourceId.md) |  | 
**scanName** | **String** | The unique name that CodeGuru Security uses to track revisions across multiple scans of the same resource. Only allowed for a &lt;code&gt;STANDARD&lt;/code&gt; scan type. If not specified, it will be auto generated.  | 
**scanType** | **String** | &lt;p&gt;The type of scan, either &lt;code&gt;Standard&lt;/code&gt; or &lt;code&gt;Express&lt;/code&gt;. Defaults to &lt;code&gt;Standard&lt;/code&gt; type if missing.&lt;/p&gt; &lt;p&gt; &lt;code&gt;Express&lt;/code&gt; scans run on limited resources and use a limited set of detectors to analyze your code in near-real time. &lt;code&gt;Standard&lt;/code&gt; scans have standard resource limits and use the full set of detectors to analyze your code.&lt;/p&gt; | [optional] 
**tags** | **{String: String}** | &lt;p&gt;An array of key-value pairs used to tag a scan. A tag is a custom attribute label with two parts:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;A tag key. For example, &lt;code&gt;CostCenter&lt;/code&gt;, &lt;code&gt;Environment&lt;/code&gt;, or &lt;code&gt;Secret&lt;/code&gt;. Tag keys are case sensitive.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;An optional tag value field. For example, &lt;code&gt;111122223333&lt;/code&gt;, &lt;code&gt;Production&lt;/code&gt;, or a team name. Omitting the tag value is the same as using an empty string. Tag values are case sensitive.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 



## Enum: AnalysisTypeEnum


* `Security` (value: `"Security"`)

* `All` (value: `"All"`)





## Enum: ScanTypeEnum


* `Standard` (value: `"Standard"`)

* `Express` (value: `"Express"`)





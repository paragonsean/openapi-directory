

# HTTPRequest

<note> <p>This is <b>AWS WAF Classic</b> documentation. For more information, see <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html\">AWS WAF Classic</a> in the developer guide.</p> <p> <b>For the latest version of AWS WAF</b>, use the AWS WAFV2 API and see the <a href=\"https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html\">AWS WAF Developer Guide</a>. With the latest version, AWS WAF has a single set of endpoints for regional and global use. </p> </note> <p>The response from a <a>GetSampledRequests</a> request includes an <code>HTTPRequest</code> complex type that appears as <code>Request</code> in the response syntax. <code>HTTPRequest</code> contains information about one of the web requests that were returned by <code>GetSampledRequests</code>. </p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientIP** | [**String**](String.md) |  |  [optional] |
|**country** | [**String**](String.md) |  |  [optional] |
|**URI** | [**String**](String.md) |  |  [optional] |
|**method** | [**String**](String.md) |  |  [optional] |
|**htTPVersion** | [**String**](String.md) |  |  [optional] |
|**headers** | [**List**](List.md) |  |  [optional] |




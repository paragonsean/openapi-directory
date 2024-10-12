

# CreateCustomDataIdentifierRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientToken** | **String** | A unique, case-sensitive token that you provide to ensure the idempotency of the request. |  [optional] |
|**description** | **String** | &lt;p&gt;A custom description of the custom data identifier. The description can contain as many as 512 characters.&lt;/p&gt; &lt;p&gt;We strongly recommend that you avoid including any sensitive data in the description of a custom data identifier. Other users of your account might be able to see this description, depending on the actions that they&#39;re allowed to perform in Amazon Macie.&lt;/p&gt; |  [optional] |
|**ignoreWords** | **List&lt;String&gt;** | An array that lists specific character sequences (&lt;i&gt;ignore words&lt;/i&gt;) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive. |  [optional] |
|**keywords** | **List&lt;String&gt;** | An array that lists specific character sequences (&lt;i&gt;keywords&lt;/i&gt;), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren&#39;t case sensitive. |  [optional] |
|**maximumMatchDistance** | **Integer** | The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50. |  [optional] |
|**name** | **String** | &lt;p&gt;A custom name for the custom data identifier. The name can contain as many as 128 characters.&lt;/p&gt; &lt;p&gt;We strongly recommend that you avoid including any sensitive data in the name of a custom data identifier. Other users of your account might be able to see this name, depending on the actions that they&#39;re allowed to perform in Amazon Macie.&lt;/p&gt; |  |
|**regex** | **String** | The regular expression (&lt;i&gt;regex&lt;/i&gt;) that defines the pattern to match. The expression can contain as many as 512 characters. |  |
|**severityLevels** | [**List&lt;SeverityLevel&gt;**](SeverityLevel.md) | &lt;p&gt;The severity to assign to findings that the custom data identifier produces, based on the number of occurrences of text that matches the custom data identifier&#39;s detection criteria. You can specify as many as three SeverityLevel objects in this array, one for each severity: LOW, MEDIUM, or HIGH. If you specify more than one, the occurrences thresholds must be in ascending order by severity, moving from LOW to HIGH. For example, 1 for LOW, 50 for MEDIUM, and 100 for HIGH. If an S3 object contains fewer occurrences than the lowest specified threshold, Amazon Macie doesn&#39;t create a finding.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify any values for this array, Macie creates findings for S3 objects that contain at least one occurrence of text that matches the detection criteria, and Macie automatically assigns the MEDIUM severity to those findings.&lt;/p&gt; |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A string-to-string map of key-value pairs that specifies the tags (keys and values) for an Amazon Macie resource. |  [optional] |




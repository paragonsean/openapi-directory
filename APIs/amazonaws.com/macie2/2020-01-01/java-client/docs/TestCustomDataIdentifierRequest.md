

# TestCustomDataIdentifierRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ignoreWords** | **List&lt;String&gt;** | An array that lists specific character sequences (&lt;i&gt;ignore words&lt;/i&gt;) to exclude from the results. If the text matched by the regular expression contains any string in this array, Amazon Macie ignores it. The array can contain as many as 10 ignore words. Each ignore word can contain 4-90 UTF-8 characters. Ignore words are case sensitive. |  [optional] |
|**keywords** | **List&lt;String&gt;** | An array that lists specific character sequences (&lt;i&gt;keywords&lt;/i&gt;), one of which must precede and be within proximity (maximumMatchDistance) of the regular expression to match. The array can contain as many as 50 keywords. Each keyword can contain 3-90 UTF-8 characters. Keywords aren&#39;t case sensitive. |  [optional] |
|**maximumMatchDistance** | **Integer** | The maximum number of characters that can exist between the end of at least one complete character sequence specified by the keywords array and the end of the text that matches the regex pattern. If a complete keyword precedes all the text that matches the pattern and the keyword is within the specified distance, Amazon Macie includes the result. The distance can be 1-300 characters. The default value is 50. |  [optional] |
|**regex** | **String** | The regular expression (&lt;i&gt;regex&lt;/i&gt;) that defines the pattern to match. The expression can contain as many as 512 characters. |  |
|**sampleText** | **String** | The sample text to inspect by using the custom data identifier. The text can contain as many as 1,000 characters. |  |




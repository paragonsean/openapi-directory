

# TranscriptNormalization

Transcription normalization configuration. Use transcription normalization to automatically replace parts of the transcript with phrases of your choosing. For StreamingRecognize, this normalization only applies to stable partial transcripts (stability > 0.8) and final transcripts.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entries** | [**List&lt;Entry&gt;**](Entry.md) | A list of replacement entries. We will perform replacement with one entry at a time. For example, the second entry in [\&quot;cat\&quot; &#x3D;&gt; \&quot;dog\&quot;, \&quot;mountain cat\&quot; &#x3D;&gt; \&quot;mountain dog\&quot;] will never be applied because we will always process the first entry before it. At most 100 entries. |  [optional] |




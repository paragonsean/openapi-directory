

# ListTapesOutput

<p>A JSON object containing the following fields:</p> <ul> <li> <p> <a>ListTapesOutput$Marker</a> </p> </li> <li> <p> <a>ListTapesOutput$VolumeInfos</a> </p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tapeInfos** | [**List&lt;TapeInfo&gt;**](TapeInfo.md) | An array of &lt;a&gt;TapeInfo&lt;/a&gt; objects, where each object describes a single tape. If there are no tapes in the tape library or VTS, then the &lt;code&gt;TapeInfos&lt;/code&gt; is an empty array. |  [optional] |
|**marker** | [**String**](String.md) |  |  [optional] |




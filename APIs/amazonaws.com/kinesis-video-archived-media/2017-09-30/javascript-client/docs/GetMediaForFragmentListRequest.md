# AmazonKinesisVideoStreamsArchivedMedia.GetMediaForFragmentListRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streamName** | **String** | The name of the stream from which to retrieve fragment media. Specify either this parameter or the &lt;code&gt;StreamARN&lt;/code&gt; parameter. | [optional] 
**streamARN** | **String** | The Amazon Resource Name (ARN) of the stream from which to retrieve fragment media. Specify either this parameter or the &lt;code&gt;StreamName&lt;/code&gt; parameter. | [optional] 
**fragments** | **[String]** | A list of the numbers of fragments for which to retrieve media. You retrieve these values with &lt;a&gt;ListFragments&lt;/a&gt;. | 



# AmazonKinesisVideoStreamsArchivedMedia.GetImagesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**streamName** | **String** | The name of the stream from which to retrieve the images. You must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. | [optional] 
**streamARN** | **String** | The Amazon Resource Name (ARN) of the stream from which to retrieve the images. You must specify either the &lt;code&gt;StreamName&lt;/code&gt; or the &lt;code&gt;StreamARN&lt;/code&gt;. | [optional] 
**imageSelectorType** | **String** | The origin of the Server or Producer timestamps to use to generate the images. | 
**startTimestamp** | **Date** | The starting point from which the images should be generated. This &lt;code&gt;StartTimestamp&lt;/code&gt; must be within an inclusive range of timestamps for an image to be returned. | 
**endTimestamp** | **Date** | The end timestamp for the range of images to be generated. If the time range between &lt;code&gt;StartTimestamp&lt;/code&gt; and &lt;code&gt;EndTimestamp&lt;/code&gt; is more than 300 seconds above &lt;code&gt;StartTimestamp&lt;/code&gt;, you will receive an &lt;code&gt;IllegalArgumentException&lt;/code&gt;. | 
**samplingInterval** | **Number** | &lt;p&gt;The time interval in milliseconds (ms) at which the images need to be generated from the stream, with a default of 3000 ms. The minimum value that can be provided is 200 ms. If the timestamp range is less than the sampling interval, the Image from the &lt;code&gt;startTimestamp&lt;/code&gt; will be returned if available. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The minimum value of 200 ms is a hard limit.&lt;/p&gt; &lt;/note&gt; | [optional] 
**format** | **String** | The format that will be used to encode the image. | 
**formatConfig** | **{String: String}** | The list of a key-value pair structure that contains extra parameters that can be applied when the image is generated. The &lt;code&gt;FormatConfig&lt;/code&gt; key is the &lt;code&gt;JPEGQuality&lt;/code&gt;, which indicates the JPEG quality key to be used to generate the image. The &lt;code&gt;FormatConfig&lt;/code&gt; value accepts ints from 1 to 100. If the value is 1, the image will be generated with less quality and the best compression. If the value is 100, the image will be generated with the best quality and less compression. If no value is provided, the default value of the &lt;code&gt;JPEGQuality&lt;/code&gt; key will be set to 80. | [optional] 
**widthPixels** | **Number** | The width of the output image that is used in conjunction with the &lt;code&gt;HeightPixels&lt;/code&gt; parameter. When both &lt;code&gt;WidthPixels&lt;/code&gt; and &lt;code&gt;HeightPixels&lt;/code&gt; parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the &lt;code&gt;WidthPixels&lt;/code&gt; parameter is provided or if only the &lt;code&gt;HeightPixels&lt;/code&gt; is provided, a &lt;code&gt;ValidationException&lt;/code&gt; will be thrown. If neither parameter is provided, the original image size from the stream will be returned. | [optional] 
**heightPixels** | **Number** | The height of the output image that is used in conjunction with the &lt;code&gt;WidthPixels&lt;/code&gt; parameter. When both &lt;code&gt;HeightPixels&lt;/code&gt; and &lt;code&gt;WidthPixels&lt;/code&gt; parameters are provided, the image will be stretched to fit the specified aspect ratio. If only the &lt;code&gt;HeightPixels&lt;/code&gt; parameter is provided, its original aspect ratio will be used to calculate the &lt;code&gt;WidthPixels&lt;/code&gt; ratio. If neither parameter is provided, the original image size will be returned. | [optional] 
**maxResults** | **Number** | &lt;p&gt;The maximum number of images to be returned by the API. &lt;/p&gt; &lt;note&gt; &lt;p&gt;The default limit is 25 images per API response. Providing a &lt;code&gt;MaxResults&lt;/code&gt; greater than this value will result in a page size of 25. Any additional results will be paginated. &lt;/p&gt; &lt;/note&gt; | [optional] 
**nextToken** | **String** | A token that specifies where to start paginating the next set of Images. This is the &lt;code&gt;GetImages:NextToken&lt;/code&gt; from a previously truncated response. | [optional] 



## Enum: ImageSelectorTypeEnum


* `PRODUCER_TIMESTAMP` (value: `"PRODUCER_TIMESTAMP"`)

* `SERVER_TIMESTAMP` (value: `"SERVER_TIMESTAMP"`)





## Enum: FormatEnum


* `JPEG` (value: `"JPEG"`)

* `PNG` (value: `"PNG"`)





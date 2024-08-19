

# VideoTopicDetails

Freebase topic information related to the video.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**relevantTopicIds** | **List&lt;String&gt;** | Similar to topic_id, except that these topics are merely relevant to the video. These are topics that may be mentioned in, or appear in the video. You can retrieve information about each topic using Freebase Topic API. |  [optional] |
|**topicCategories** | **List&lt;String&gt;** | A list of Wikipedia URLs that provide a high-level description of the video&#39;s content. |  [optional] |
|**topicIds** | **List&lt;String&gt;** | A list of Freebase topic IDs that are centrally associated with the video. These are topics that are centrally featured in the video, and it can be said that the video is mainly about each of these. You can retrieve information about each topic using the &lt; a href&#x3D;\&quot;http://wiki.freebase.com/wiki/Topic_API\&quot;&gt;Freebase Topic API. |  [optional] |




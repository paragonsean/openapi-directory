

# GroupResult

An array of face groups based on face similarity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groups** | **List&lt;List&lt;UUID&gt;&gt;** | A partition of the original faces based on face similarity. Groups are ranked by number of faces |  |
|**messyGroup** | **List&lt;UUID&gt;** | Face ids array of faces that cannot find any similar faces from original faces. |  [optional] |




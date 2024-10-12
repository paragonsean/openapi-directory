

# PersonMatch

Information about a person whose face matches a face(s) in an Amazon Rekognition collection. Includes information about the faces in the Amazon Rekognition collection (<a>FaceMatch</a>), information about the person (<a>PersonDetail</a>), and the time stamp for when the person was detected in a video. An array of <code>PersonMatch</code> objects is returned by <a>GetFaceSearch</a>. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**timestamp** | [**Integer**](Integer.md) |  |  [optional] |
|**person** | [**PersonMatchPerson**](PersonMatchPerson.md) |  |  [optional] |
|**faceMatches** | [**List**](List.md) |  |  [optional] |




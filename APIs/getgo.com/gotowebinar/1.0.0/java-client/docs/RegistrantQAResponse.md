

# RegistrantQAResponse

Describes a completed registration question for a webinar registrant. If you use 'Multiple choice' questions the response contains the numeric answerKey, otherwise the answer text. Example:<br>{<br>  \"firstName\": \"First\",<br>  \"lastName\": \"Last\",<br>  \"email\": \"First.Last@example.com\",<br>  \"responses\": [{<br>      \"questionKey\": 17023549,<br>      \"responseText\": \"This is a short answer\"},{<br>      \"questionKey\": 17023550,<br>      \"answerKey\": 17023553}  ]<br>}

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerKey** | **Long** | The numeric key of the answer to a multiple-choice question. |  [optional] |
|**questionKey** | **Long** | The unique key of the question |  |
|**responseText** | **String** | Answer of the question. |  [optional] |




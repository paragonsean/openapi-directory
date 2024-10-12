# GoogleFormsApi.TextAnswer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **String** | Output only. The answer value. Formatting used for different kinds of question: * ChoiceQuestion * &#x60;RADIO&#x60; or &#x60;DROP_DOWN&#x60;: A single string corresponding to the option that was selected. * &#x60;CHECKBOX&#x60;: Multiple strings corresponding to each option that was selected. * TextQuestion: The text that the user entered. * ScaleQuestion: A string containing the number that was selected. * DateQuestion * Without time or year: MM-DD e.g. \&quot;05-19\&quot; * With year: YYYY-MM-DD e.g. \&quot;1986-05-19\&quot; * With time: MM-DD HH:MM e.g. \&quot;05-19 14:51\&quot; * With year and time: YYYY-MM-DD HH:MM e.g. \&quot;1986-05-19 14:51\&quot; * TimeQuestion: String with time or duration in HH:MM format e.g. \&quot;14:51\&quot; * RowQuestion within QuestionGroupItem: The answer for each row of a QuestionGroupItem is represented as a separate Answer. Each will contain one string for &#x60;RADIO&#x60;-type choices or multiple strings for &#x60;CHECKBOX&#x60; choices. | [optional] [readonly] 



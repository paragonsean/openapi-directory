# ThePlaidApi.NameMatchScore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**isBusinessNameDetected** | **Boolean** | Is &#x60;true&#x60; if the name on either of the names that was matched for the score contained strings indicative of a business name, such as \&quot;CORP\&quot;, \&quot;LLC\&quot;, \&quot;INC\&quot;, or \&quot;LTD\&quot;. A &#x60;true&#x60; result generally indicates the entity is a business. However, a &#x60;false&#x60; result does not mean the entity is not a business, as some businesses do not use these strings in the names used for their financial institution accounts. | [optional] 
**isFirstNameOrLastNameMatch** | **Boolean** | first or last name completely matched, likely a family member | [optional] 
**isNicknameMatch** | **Boolean** | nickname matched, example Jennifer and Jenn. | [optional] 
**score** | **Number** | Represents the match score for name. 100 is a perfect score, 85-99 means a strong match, 50-84 is a partial match, less than 50 is a weak match and 0 is a complete mismatch. If the name is missing from either the API or financial institution, this is empty. | [optional] 



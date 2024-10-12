# RubrikRestApi.OracleRecoveryApiValidationErrors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acoMap** | [**[OracleAcoParameterDetail]**](OracleAcoParameterDetail.md) | List of Advanced Cloning Options (ACO) parameter values that were parsed. | [optional] 
**acoParameterErrors** | **[String]** | Other generic errors with the Advanced Cloning Options (ACO) parameters. | [optional] 
**acoValueValidationErrors** | [**[OracleAcoValueErrorDetail]**](OracleAcoValueErrorDetail.md) | List of Advanced Cloning Options (ACO) errors pertaining to the specified values. | [optional] 
**otherErrors** | **[String]** | Other generic validation error messages in the API. | [optional] 
**postScriptError** | **String** | Error message when post-script path is invalid. | [optional] 
**preScriptError** | **String** | Error message when pre-script path is invalid. | [optional] 



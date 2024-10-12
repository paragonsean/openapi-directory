# TrafficDirectorApi.GoogleRE2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxProgramSize** | **Number** | This field controls the RE2 \&quot;program size\&quot; which is a rough estimate of how complex a compiled regex is to evaluate. A regex that has a program size greater than the configured value will fail to compile. In this case, the configured max program size can be increased or the regex can be simplified. If not specified, the default is 100. This field is deprecated; regexp validation should be performed on the management server instead of being done by each individual client. | [optional] 



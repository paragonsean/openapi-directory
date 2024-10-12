

# DiagnosticsStackFrame

a single frame of a stack trace

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | address of the frame |  [optional] |
|**appCode** | **Boolean** | this line isn&#39;t from any framework |  |
|**classMethod** | **Boolean** | is a class method |  [optional] |
|**className** | **String** | name of the class |  [optional] |
|**codeFormatted** | **String** | Formatted frame string |  |
|**codeRaw** | **String** | Raw frame string |  |
|**_file** | **String** | name of the file |  [optional] |
|**frameworkName** | **String** | Name of the framework |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) | programming language of the frame |  [optional] |
|**line** | **Integer** | line number |  [optional] |
|**method** | **String** | name of the method |  [optional] |
|**methodParams** | **String** | parameters of the frames method |  [optional] |
|**relevant** | **Boolean** | frame should be shown always |  [optional] |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| JAVA_SCRIPT | &quot;JavaScript&quot; |
| C_SHARP | &quot;CSharp&quot; |
| OBJECTIVE_C | &quot;Objective-C&quot; |
| OBJECTIVE_CPP | &quot;Objective-Cpp&quot; |
| CPP | &quot;Cpp&quot; |
| C | &quot;C&quot; |
| SWIFT | &quot;Swift&quot; |
| JAVA | &quot;Java&quot; |
| UNKNOWN | &quot;Unknown&quot; |




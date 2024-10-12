

# ReasonStackFrame

frame belonging to the reason of the crash

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appCode** | **Boolean** | this line isn&#39;t from any framework |  [optional] |
|**classMethod** | **Boolean** | is a class method |  [optional] |
|**className** | **String** | name of the class |  [optional] |
|**codeFormatted** | **String** | Formatted frame string |  [optional] |
|**codeRaw** | **String** | Unformatted Frame string |  [optional] |
|**exceptionType** | **String** | Exception type. |  [optional] |
|**_file** | **String** | name of the file |  [optional] |
|**frameworkName** | **String** | Name of the framework |  [optional] |
|**language** | [**LanguageEnum**](#LanguageEnum) | programming language of the frame |  [optional] |
|**line** | **Integer** | line number |  [optional] |
|**method** | **String** | name of the method |  [optional] |
|**methodParams** | **String** | parameters of the frames method |  [optional] |
|**osExceptionType** | **String** | OS exception type. (aka. SIGNAL) |  [optional] |



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




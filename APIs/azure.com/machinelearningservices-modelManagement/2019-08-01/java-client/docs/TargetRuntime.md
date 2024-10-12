

# TargetRuntime

The target runtime.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The target operating system. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | The properties dictionary. |  [optional] [readonly] |
|**runtimeType** | [**RuntimeTypeEnum**](#RuntimeTypeEnum) | The target runtime type. |  [optional] |
|**targetArchitecture** | [**TargetArchitectureEnum**](#TargetArchitectureEnum) | The target architecture. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| LINUX | &quot;Linux&quot; |
| WINDOWS | &quot;Windows&quot; |



## Enum: RuntimeTypeEnum

| Name | Value |
|---- | -----|
| SPARK_PYTHON | &quot;SparkPython&quot; |
| TLC37 | &quot;Tlc37&quot; |
| TLC38 | &quot;Tlc38&quot; |
| TLC310 | &quot;Tlc310&quot; |
| PYTHON | &quot;Python&quot; |
| PYTHON_SLIM | &quot;PythonSlim&quot; |
| PYTHON_CUSTOM | &quot;PythonCustom&quot; |



## Enum: TargetArchitectureEnum

| Name | Value |
|---- | -----|
| AMD64 | &quot;Amd64&quot; |
| ARM32V7 | &quot;Arm32v7&quot; |




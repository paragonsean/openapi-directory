# DataflowApi.DisplayData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**boolValue** | **Boolean** | Contains value if the data is of a boolean type. | [optional] 
**durationValue** | **String** | Contains value if the data is of duration type. | [optional] 
**floatValue** | **Number** | Contains value if the data is of float type. | [optional] 
**int64Value** | **String** | Contains value if the data is of int64 type. | [optional] 
**javaClassValue** | **String** | Contains value if the data is of java class type. | [optional] 
**key** | **String** | The key identifying the display data. This is intended to be used as a label for the display data when viewed in a dax monitoring system. | [optional] 
**label** | **String** | An optional label to display in a dax UI for the element. | [optional] 
**namespace** | **String** | The namespace for the key. This is usually a class name or programming language namespace (i.e. python module) which defines the display data. This allows a dax monitoring system to specially handle the data and perform custom rendering. | [optional] 
**shortStrValue** | **String** | A possible additional shorter value to display. For example a java_class_name_value of com.mypackage.MyDoFn will be stored with MyDoFn as the short_str_value and com.mypackage.MyDoFn as the java_class_name value. short_str_value can be displayed and java_class_name_value will be displayed as a tooltip. | [optional] 
**strValue** | **String** | Contains value if the data is of string type. | [optional] 
**timestampValue** | **String** | Contains value if the data is of timestamp type. | [optional] 
**url** | **String** | An optional full URL. | [optional] 



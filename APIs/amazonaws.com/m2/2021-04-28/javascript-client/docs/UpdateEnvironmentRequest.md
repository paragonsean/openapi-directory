# AwsMainframeModernization.UpdateEnvironmentRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyDuringMaintenanceWindow** | **Boolean** | Indicates whether to update the runtime environment during the maintenance window. The default is false. Currently, Amazon Web Services Mainframe Modernization accepts the &lt;code&gt;engineVersion&lt;/code&gt; parameter only if &lt;code&gt;applyDuringMaintenanceWindow&lt;/code&gt; is true. If any parameter other than &lt;code&gt;engineVersion&lt;/code&gt; is provided in &lt;code&gt;UpdateEnvironmentRequest&lt;/code&gt;, it will fail if &lt;code&gt;applyDuringMaintenanceWindow&lt;/code&gt; is set to true. | [optional] 
**desiredCapacity** | **Number** | The desired capacity for the runtime environment to update. The minimum possible value is 0 and the maximum is 100. | [optional] 
**engineVersion** | **String** | The version of the runtime engine for the runtime environment. | [optional] 
**instanceType** | **String** | The instance type for the runtime environment to update. | [optional] 
**preferredMaintenanceWindow** | **String** | Configures the maintenance window you want for the runtime environment. If you do not provide a value, a random system-generated value will be assigned. | [optional] 



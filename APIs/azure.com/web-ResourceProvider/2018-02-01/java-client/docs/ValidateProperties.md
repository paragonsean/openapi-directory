

# ValidateProperties

App properties used for validation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacity** | **Integer** | Target capacity of the App Service plan (number of VMs). |  [optional] |
|**hostingEnvironment** | **String** | Name of App Service Environment where app or App Service plan should be created. |  [optional] |
|**isSpot** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if App Service plan is for Spot instances; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**isXenon** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if App Service plan is running as a windows container |  [optional] |
|**needLinuxWorkers** | **Boolean** | &lt;code&gt;true&lt;/code&gt; if App Service plan is for Linux workers; otherwise, &lt;code&gt;false&lt;/code&gt;. |  [optional] |
|**serverFarmId** | **String** | ARM resource ID of an App Service plan that would host the app. |  [optional] |
|**skuName** | **String** | Name of the target SKU for the App Service plan. |  [optional] |




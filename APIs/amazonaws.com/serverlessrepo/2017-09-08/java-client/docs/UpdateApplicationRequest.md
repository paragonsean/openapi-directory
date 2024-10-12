

# UpdateApplicationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**author** | **String** | &lt;p&gt;The name of the author publishing the app.&lt;/p&gt;&lt;p&gt;Minimum length&#x3D;1. Maximum length&#x3D;127.&lt;/p&gt;&lt;p&gt;Pattern \&quot;^[a-z0-9](([a-z0-9]|-(?!-))*[a-z0-9])?$\&quot;;&lt;/p&gt; |  [optional] |
|**description** | **String** | &lt;p&gt;The description of the application.&lt;/p&gt;&lt;p&gt;Minimum length&#x3D;1. Maximum length&#x3D;256&lt;/p&gt; |  [optional] |
|**homePageUrl** | **String** | A URL with more information about the application, for example the location of your GitHub repository for the application. |  [optional] |
|**labels** | **List&lt;String&gt;** | &lt;p&gt;Labels to improve discovery of apps in search results.&lt;/p&gt;&lt;p&gt;Minimum length&#x3D;1. Maximum length&#x3D;127. Maximum number of labels: 10&lt;/p&gt;&lt;p&gt;Pattern: \&quot;^[a-zA-Z0-9+\\\\-_:\\/@]+$\&quot;;&lt;/p&gt; |  [optional] |
|**readmeBody** | **String** | &lt;p&gt;A text readme file in Markdown language that contains a more detailed description of the application and how it works.&lt;/p&gt;&lt;p&gt;Maximum size 5 MB&lt;/p&gt; |  [optional] |
|**readmeUrl** | **String** | &lt;p&gt;A link to the readme file in Markdown language that contains a more detailed description of the application and how it works.&lt;/p&gt;&lt;p&gt;Maximum size 5 MB&lt;/p&gt; |  [optional] |




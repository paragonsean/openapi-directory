# ServiceConsumerManagementApi.Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **String** | The Markdown content of the page. You can use (&#x3D;&#x3D; include {path} &#x3D;&#x3D;) to include content from a Markdown file. The content can be used to produce the documentation page such as HTML format page. | [optional] 
**name** | **String** | The name of the page. It will be used as an identity of the page to generate URI of the page, text of the link to this page in navigation, etc. The full page name (start from the root page name to this page concatenated with &#x60;.&#x60;) can be used as reference to the page in your documentation. For example: pages: - name: Tutorial content: (&#x3D;&#x3D; include tutorial.md &#x3D;&#x3D;) subpages: - name: Java content: (&#x3D;&#x3D; include tutorial_java.md &#x3D;&#x3D;) You can reference &#x60;Java&#x60; page using Markdown reference link syntax: &#x60;Java&#x60;. | [optional] 
**subpages** | [**[Page]**](Page.md) | Subpages of this page. The order of subpages specified here will be honored in the generated docset. | [optional] 



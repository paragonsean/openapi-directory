

# DatabaseCreateDocumentRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Object** | Document data as JSON object. |  |
|**parentDocument** | **String** | Parent document unique ID. Use when you want your new document to be a child of a parent document. |  [optional] |
|**parentProperty** | **String** | Parent document property name. Use when you want your new document to be a child of a parent document. |  [optional] |
|**parentPropertyType** | **String** | Parent document property connection type. You can set this value to **assign**, **append** or **prepend**, default value is assign. Use when you want your new document to be a child of a parent document. |  [optional] |
|**read** | **List&lt;String&gt;** | An array of strings with read permissions. By default only the current user is granted with read permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. |  [optional] |
|**write** | **List&lt;String&gt;** | An array of strings with write permissions. By default only the current user is granted with write permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions. |  [optional] |




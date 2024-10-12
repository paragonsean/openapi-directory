

# Sender30

Information about the sender of the transaction. If a PAN number is provided in the sender_account_uri, the sender information section is required. Details- Conditional

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | [**Address31**](Address31.md) |  |  [optional] |
|**dateOfBirth** | **String** | Date of birth of the sender as an ISO 8601 Full Date. Valid Values- Refer &#39;Date And Time Formats&#39; |  [optional] |
|**email** | **String** | Email address of the sender. Phone number or email address should be provided if the partner is set up to receive notifications. Details- Conditional, 5-254 |  [optional] |
|**firstName** | **String** | First name of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 |  |
|**lastName** | **String** | Last name of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 |  |
|**middleName** | **String** | Middle name of the sender.\\n\\nType: Alphanumeric Special [a-zA-Z0-9 !\&quot;#$%&amp;&#39;()*+,-./\\:;&lt;&#x3D;&gt;?@[]_&#x60;{|}~ÀÁÂÃÄÅÇÈÉÊËÌÍÎÏÑÒÓÔÕÖÙÚÚÚÝàáâãäåçèéêëìíîïñòóôõöùúûüýÿ], Length: 1-40 |  [optional] |
|**phone** | **String** | Phone number of the sender. Phone number or email address should be provided if the partner is set up to receive notifications. Details- Conditional, 1-15 |  [optional] |




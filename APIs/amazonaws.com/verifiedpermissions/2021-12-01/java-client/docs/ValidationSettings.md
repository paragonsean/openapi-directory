

# ValidationSettings

<p>A structure that contains Cedar policy validation settings for the policy store. The validation mode determines which validation failures that Cedar considers serious enough to block acceptance of a new or edited static policy or policy template. </p> <p>This data type is used as a request parameter in the <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicyStore.html\">CreatePolicyStore</a> and <a href=\"https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore.html\">UpdatePolicyStore</a> operations.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ValidationMode**](ValidationMode.md) |  |  |






# ReceiptAction

<p>An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.</p> <p>For information about setting up receipt rules, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-receipt-rules.html\">Amazon SES Developer Guide</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**s3Action** | [**ReceiptActionS3Action**](ReceiptActionS3Action.md) |  |  [optional] |
|**bounceAction** | [**ReceiptActionBounceAction**](ReceiptActionBounceAction.md) |  |  [optional] |
|**workmailAction** | [**ReceiptActionWorkmailAction**](ReceiptActionWorkmailAction.md) |  |  [optional] |
|**lambdaAction** | [**ReceiptActionLambdaAction**](ReceiptActionLambdaAction.md) |  |  [optional] |
|**stopAction** | [**ReceiptActionStopAction**](ReceiptActionStopAction.md) |  |  [optional] |
|**addHeaderAction** | [**ReceiptActionAddHeaderAction**](ReceiptActionAddHeaderAction.md) |  |  [optional] |
|**snSAction** | [**ReceiptActionSNSAction**](ReceiptActionSNSAction.md) |  |  [optional] |




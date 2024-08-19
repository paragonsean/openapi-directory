

# PhoneNumberStatus

<p>The status of the phone number.</p> <ul> <li> <p> <code>CLAIMED</code> means the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimedPhoneNumber.html\">ClaimedPhoneNumber</a> or <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html\">UpdatePhoneNumber</a> operation succeeded.</p> </li> <li> <p> <code>IN_PROGRESS</code> means a <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimedPhoneNumber.html\">ClaimedPhoneNumber</a> or <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html\">UpdatePhoneNumber</a> operation is still in progress and has not yet completed. You can call <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribePhoneNumber.html\">DescribePhoneNumber</a> at a later time to verify if the previous operation has completed.</p> </li> <li> <p> <code>FAILED</code> indicates that the previous <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_ClaimedPhoneNumber.html\">ClaimedPhoneNumber</a> or <a href=\"https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdatePhoneNumber.html\">UpdatePhoneNumber</a> operation has failed. It will include a message indicating the failure reason. A common reason for a failure may be that the <code>TargetArn</code> value you are claiming or updating a phone number to has reached its limit of total claimed numbers. If you received a <code>FAILED</code> status from a <code>ClaimPhoneNumber</code> API call, you have one day to retry claiming the phone number before the number is released back to the inventory for other customers to claim.</p> </li> </ul>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**PhoneNumberWorkflowStatus**](PhoneNumberWorkflowStatus.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |




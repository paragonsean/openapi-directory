

# AnomalySubscription

<p>An <code>AnomalySubscription</code> resource (also referred to as an alert subscription) sends notifications about specific anomalies that meet an alerting criteria defined by you.</p> <p>You can specify the frequency of the alerts and the subscribers to notify.</p> <p>Anomaly subscriptions can be associated with one or more <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_AnomalyMonitor.html\"> <code>AnomalyMonitor</code> </a> resources, and they only send notifications about anomalies detected by those associated monitors. You can also configure a threshold to further control which anomalies are included in the notifications.</p> <p>Anomalies that don’t exceed the chosen threshold and therefore don’t trigger notifications from an anomaly subscription will still be available on the console and from the <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_GetAnomalies.html\"> <code>GetAnomalies</code> </a> API.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**subscriptionArn** | [**String**](String.md) |  |  [optional] |
|**accountId** | [**String**](String.md) |  |  [optional] |
|**monitorArnList** | [**List**](List.md) |  |  |
|**subscribers** | [**List**](List.md) |  |  |
|**threshold** | [**Double**](Double.md) |  |  [optional] |
|**frequency** | [**AnomalySubscriptionFrequency**](AnomalySubscriptionFrequency.md) |  |  |
|**subscriptionName** | [**String**](String.md) |  |  |
|**thresholdExpression** | [**AnomalySubscriptionThresholdExpression**](AnomalySubscriptionThresholdExpression.md) |  |  [optional] |




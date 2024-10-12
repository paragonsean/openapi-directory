# AwsRoute53RecoveryReadiness.UpdateResourceSetRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resourceSetType** | **String** | &lt;p&gt;The resource type of the resources in the resource set. Enter one of the following values for resource type:&lt;/p&gt; &lt;p&gt;AWS::ApiGateway::Stage, AWS::ApiGatewayV2::Stage, AWS::AutoScaling::AutoScalingGroup, AWS::CloudWatch::Alarm, AWS::EC2::CustomerGateway, AWS::DynamoDB::Table, AWS::EC2::Volume, AWS::ElasticLoadBalancing::LoadBalancer, AWS::ElasticLoadBalancingV2::LoadBalancer, AWS::Lambda::Function, AWS::MSK::Cluster, AWS::RDS::DBCluster, AWS::Route53::HealthCheck, AWS::SQS::Queue, AWS::SNS::Topic, AWS::SNS::Subscription, AWS::EC2::VPC, AWS::EC2::VPNConnection, AWS::EC2::VPNGateway, AWS::Route53RecoveryReadiness::DNSTargetResource&lt;/p&gt; | 
**resources** | [**[Resource]**](Resource.md) | A list of resource objects. | 



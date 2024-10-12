# TurbineLabsApi.HealthCheck

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthChecker** | [**HealthCheckHealthChecker**](HealthCheckHealthChecker.md) |  | 
**healthyEdgeIntervalMsec** | **Number** | Interval used for the first health check right after a host is marked as healthy. For subsequent health checks, the proxy will shift back to using the standard health check interval(\\&#39;interval_msec\\&#39;) that is defined. Defaults to the same value as \\&#39;interval_msec\\&#39; if not specified.  | [optional] 
**healthyThreshold** | **Number** | The number of healthy health checks required before a host is marked healthy. Note that during startup, only a single successful health check is required to mark a host healthy.  | 
**intervalJitterMsec** | **Number** | An optional jitter amount that is added to each interval value calculated by the proxy. If not specified, defaults to 0.  | [optional] 
**intervalMsec** | **Number** | The interval between health checks. The first round of health checks will occur during startup before any traffic is routed to a cluster. This means that the \\&#39;no_traffic_interval_msec\\&#39; value will be used as the first interval of health checks.  | 
**noTrafficIntervalMsec** | **Number** | Interval used when a cluster has never had traffic routed to it. It allows cluster information to be kept up to date, without sending a potentially large amount of active health checking traffic for no reason. Once a cluster has been used for traffic routing, The proxy will shift back to using the standard health check interval that is defined. Note that this interval takes precedence over any other. Defaults to 60s.  | [optional] 
**reuseConnection** | **Boolean** | Whether or not to reuse health check connections between health checks. Default is true.  | [optional] 
**timeoutMsec** | **Number** | The time to wait for a health check response. If the timeout is reached without a response, the health check attempt will be considered a failure. This is a required field and must be greater than 0.  | 
**unhealthyEdgeIntervalMsec** | **Number** | Interval used for the first health check right after a host is marked as unhealthy. For subsequent health checks, the proxy will shift back to using either \\&#39;unhealthy_interval_msec\\&#39; if present or the standard health check interval, \\&#39;interval_msec\\&#39;.  | [optional] 
**unhealthyIntervalMsec** | **Number** | Interval used for hosts that are marked as unhealthy. As soon as the host is marked as healthy, The proxy will shift back to using the standard health check interval that is defined. This defaults to the same value as \\&#39;interval_msec\\&#39; if not specified.  | [optional] 
**unhealthyThreshold** | **Number** | The number of unhealthy health checks required before a host is marked unhealthy. Note that for *http* health checking, if a host responds with 503, this threshold is ignored and the host is considered unhealthy immediately.  | 



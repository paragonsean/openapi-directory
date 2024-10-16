/*
 * Microcks API v1.7
 * API offered by Microcks, the Kubernetes native tools for API and microservices mocking and testing (microcks.io)
 *
 * The version of the OpenAPI document: 1.7.0
 * Contact: laurent@microcks.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.math.BigDecimal;
import org.openapitools.client.model.DailyInvocationStatistic;
import org.openapitools.client.model.TestConformanceMetric;
import org.openapitools.client.model.TestResultSummary;
import org.openapitools.client.model.WeightedMetricValue;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MetricsApi
 */
@Disabled
public class MetricsApiTest {

    private final MetricsApi api = new MetricsApi();

    /**
     * Get aggregated invocation statistics for a day
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAggregatedInvocationsStatsTest() throws ApiException {
        String day = null;
        DailyInvocationStatistic response = api.getAggregatedInvocationsStats(day);
        // TODO: test validations
    }

    /**
     * Get aggregation of conformance metrics
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getConformanceMetricsAggregationTest() throws ApiException {
        List<WeightedMetricValue> response = api.getConformanceMetricsAggregation();
        // TODO: test validations
    }

    /**
     * Get invocation statistics for Service
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInvocationStatsByServiceTest() throws ApiException {
        String serviceName = null;
        String serviceVersion = null;
        String day = null;
        DailyInvocationStatistic response = api.getInvocationStatsByService(serviceName, serviceVersion, day);
        // TODO: test validations
    }

    /**
     * Get aggregated invocations statistics for latest days
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLatestAggregatedInvocationsStatsTest() throws ApiException {
        Integer limit = null;
        Map<String, BigDecimal> response = api.getLatestAggregatedInvocationsStats(limit);
        // TODO: test validations
    }

    /**
     * Get latest tests results
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getLatestTestResultsTest() throws ApiException {
        Integer limit = null;
        List<TestResultSummary> response = api.getLatestTestResults(limit);
        // TODO: test validations
    }

    /**
     * Get conformance metrics for a Service
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getServiceTestConformanceMetricTest() throws ApiException {
        String serviceId = null;
        TestConformanceMetric response = api.getServiceTestConformanceMetric(serviceId);
        // TODO: test validations
    }

    /**
     * Get top invocation statistics for a day
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTopIvnocationsStatsByDayTest() throws ApiException {
        String day = null;
        Integer limit = null;
        List<DailyInvocationStatistic> response = api.getTopIvnocationsStatsByDay(day, limit);
        // TODO: test validations
    }

}

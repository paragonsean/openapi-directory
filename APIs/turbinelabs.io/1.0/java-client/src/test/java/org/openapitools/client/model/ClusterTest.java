/*
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import org.openapitools.client.model.CircuitBreakers;
import org.openapitools.client.model.HealthCheck;
import org.openapitools.client.model.Instance;
import org.openapitools.client.model.OutlierDetection;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for Cluster
 */
public class ClusterTest {
    private final Cluster model = new Cluster();

    /**
     * Model tests for Cluster
     */
    @Test
    public void testCluster() {
        // TODO: test Cluster
    }

    /**
     * Test the property 'circuitBreakers'
     */
    @Test
    public void circuitBreakersTest() {
        // TODO: test circuitBreakers
    }

    /**
     * Test the property 'healthChecks'
     */
    @Test
    public void healthChecksTest() {
        // TODO: test healthChecks
    }

    /**
     * Test the property 'instances'
     */
    @Test
    public void instancesTest() {
        // TODO: test instances
    }

    /**
     * Test the property 'name'
     */
    @Test
    public void nameTest() {
        // TODO: test name
    }

    /**
     * Test the property 'outlierDetection'
     */
    @Test
    public void outlierDetectionTest() {
        // TODO: test outlierDetection
    }

    /**
     * Test the property 'requireTls'
     */
    @Test
    public void requireTlsTest() {
        // TODO: test requireTls
    }

    /**
     * Test the property 'zoneKey'
     */
    @Test
    public void zoneKeyTest() {
        // TODO: test zoneKey
    }

    /**
     * Test the property 'checksum'
     */
    @Test
    public void checksumTest() {
        // TODO: test checksum
    }

    /**
     * Test the property 'clusterKey'
     */
    @Test
    public void clusterKeyTest() {
        // TODO: test clusterKey
    }

}

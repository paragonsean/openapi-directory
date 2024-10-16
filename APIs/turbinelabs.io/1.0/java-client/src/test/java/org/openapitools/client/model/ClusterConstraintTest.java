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
import org.openapitools.client.model.Metadatum;
import org.openapitools.client.model.ResponseData;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for ClusterConstraint
 */
public class ClusterConstraintTest {
    private final ClusterConstraint model = new ClusterConstraint();

    /**
     * Model tests for ClusterConstraint
     */
    @Test
    public void testClusterConstraint() {
        // TODO: test ClusterConstraint
    }

    /**
     * Test the property 'clusterKey'
     */
    @Test
    public void clusterKeyTest() {
        // TODO: test clusterKey
    }

    /**
     * Test the property 'constraintKey'
     */
    @Test
    public void constraintKeyTest() {
        // TODO: test constraintKey
    }

    /**
     * Test the property 'metadata'
     */
    @Test
    public void metadataTest() {
        // TODO: test metadata
    }

    /**
     * Test the property 'properties'
     */
    @Test
    public void propertiesTest() {
        // TODO: test properties
    }

    /**
     * Test the property 'responseData'
     */
    @Test
    public void responseDataTest() {
        // TODO: test responseData
    }

    /**
     * Test the property 'weight'
     */
    @Test
    public void weightTest() {
        // TODO: test weight
    }

}

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
import org.openapitools.client.model.AllConstraints;
import org.openapitools.client.model.CohortSeed;
import org.openapitools.client.model.Match;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for Rule
 */
public class RuleTest {
    private final Rule model = new Rule();

    /**
     * Model tests for Rule
     */
    @Test
    public void testRule() {
        // TODO: test Rule
    }

    /**
     * Test the property 'cohortSeed'
     */
    @Test
    public void cohortSeedTest() {
        // TODO: test cohortSeed
    }

    /**
     * Test the property 'constraints'
     */
    @Test
    public void constraintsTest() {
        // TODO: test constraints
    }

    /**
     * Test the property 'matches'
     */
    @Test
    public void matchesTest() {
        // TODO: test matches
    }

    /**
     * Test the property 'methods'
     */
    @Test
    public void methodsTest() {
        // TODO: test methods
    }

    /**
     * Test the property 'ruleKey'
     */
    @Test
    public void ruleKeyTest() {
        // TODO: test ruleKey
    }

}

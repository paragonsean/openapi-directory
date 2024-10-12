/*
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
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
import org.openapitools.client.model.CareContextDefinition;
import org.openapitools.client.model.ConsentRequestConsentHip;
import org.openapitools.client.model.ConsentRequestConsentHiu;
import org.openapitools.client.model.ConsentRequestConsentPatient;
import org.openapitools.client.model.HITypeEnum;
import org.openapitools.client.model.Permission;
import org.openapitools.client.model.Requester;
import org.openapitools.client.model.UsePurpose;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Model tests for ConsentRequestConsent
 */
public class ConsentRequestConsentTest {
    private final ConsentRequestConsent model = new ConsentRequestConsent();

    /**
     * Model tests for ConsentRequestConsent
     */
    @Test
    public void testConsentRequestConsent() {
        // TODO: test ConsentRequestConsent
    }

    /**
     * Test the property 'careContexts'
     */
    @Test
    public void careContextsTest() {
        // TODO: test careContexts
    }

    /**
     * Test the property 'hiTypes'
     */
    @Test
    public void hiTypesTest() {
        // TODO: test hiTypes
    }

    /**
     * Test the property 'hip'
     */
    @Test
    public void hipTest() {
        // TODO: test hip
    }

    /**
     * Test the property 'hiu'
     */
    @Test
    public void hiuTest() {
        // TODO: test hiu
    }

    /**
     * Test the property 'patient'
     */
    @Test
    public void patientTest() {
        // TODO: test patient
    }

    /**
     * Test the property 'permission'
     */
    @Test
    public void permissionTest() {
        // TODO: test permission
    }

    /**
     * Test the property 'purpose'
     */
    @Test
    public void purposeTest() {
        // TODO: test purpose
    }

    /**
     * Test the property 'requester'
     */
    @Test
    public void requesterTest() {
        // TODO: test requester
    }

}

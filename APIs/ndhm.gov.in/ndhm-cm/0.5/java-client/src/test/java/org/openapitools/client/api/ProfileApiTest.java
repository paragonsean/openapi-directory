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


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorResponse;
import org.openapitools.client.model.ShareProfileResult;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProfileApi
 */
@Disabled
public class ProfileApiTest {

    private final ProfileApi api = new ProfileApi();

    /**
     * Response to patient&#39;s share profile request
     *
     * Result of patient share profile request at HIP end. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05PatientsProfileOnSharePostTest() throws ApiException {
        String authorization = null;
        ShareProfileResult shareProfileResult = null;
        api.v05PatientsProfileOnSharePost(authorization, shareProfileResult);
        // TODO: test validations
    }

}

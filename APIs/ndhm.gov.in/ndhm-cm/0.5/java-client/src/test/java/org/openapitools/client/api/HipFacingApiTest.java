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
import org.openapitools.client.model.PatientAuthModeQueryRequest;
import org.openapitools.client.model.PatientAuthNotificationAcknowledgement;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for HipFacingApi
 */
@Disabled
public class HipFacingApiTest {

    private final HipFacingApi api = new HipFacingApi();

    /**
     * Get a patient&#39;s authentication modes relevant to specified purpose
     *
     * This API is meant for identify supported authentication modes for a patient given a specific purpose 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthFetchModesPost_0Test() throws ApiException {
        String authorization = null;
        PatientAuthModeQueryRequest patientAuthModeQueryRequest = null;
        api.v05UsersAuthFetchModesPost_0(authorization, patientAuthModeQueryRequest);
        // TODO: test validations
    }

    /**
     * callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)
     *
     * This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void v05UsersAuthOnNotifyPost_0Test() throws ApiException {
        String authorization = null;
        PatientAuthNotificationAcknowledgement patientAuthNotificationAcknowledgement = null;
        api.v05UsersAuthOnNotifyPost_0(authorization, patientAuthNotificationAcknowledgement);
        // TODO: test validations
    }

}

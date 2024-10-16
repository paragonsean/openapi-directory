/*
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.APIModelsApiError;
import org.openapitools.client.model.DealerDBModelsEDTLiteRegistration;
import org.openapitools.client.model.DealerDBModelsLicenseActivation;
import org.openapitools.client.model.DealerDBModelsLicenseActivationConfirm;
import org.openapitools.client.model.DealerDBModelsLicenseActivationCreate;
import org.openapitools.client.model.DealerDBModelsLicenseActivationUpdate;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for LicenseActivationsApi
 */
@Disabled
public class LicenseActivationsApiTest {

    private final LicenseActivationsApi api = new LicenseActivationsApi();

    /**
     * Create a license activation.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void licenseActivationsPostTest() throws ApiException {
        DealerDBModelsLicenseActivationCreate dealerDBModelsLicenseActivationCreate = null;
        DealerDBModelsLicenseActivation response = api.licenseActivationsPost(dealerDBModelsLicenseActivationCreate);
        // TODO: test validations
    }

    /**
     * Register an EDT Lite with the Server
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void licenseActivationsPostRegisterEDTLiteTest() throws ApiException {
        DealerDBModelsEDTLiteRegistration dealerDBModelsEDTLiteRegistration = null;
        Boolean response = api.licenseActivationsPostRegisterEDTLite(dealerDBModelsEDTLiteRegistration);
        // TODO: test validations
    }

    /**
     * Update a license activiation.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void licenseActivationsPutTest() throws ApiException {
        String ID = null;
        DealerDBModelsLicenseActivationUpdate dealerDBModelsLicenseActivationUpdate = null;
        DealerDBModelsLicenseActivation response = api.licenseActivationsPut(ID, dealerDBModelsLicenseActivationUpdate);
        // TODO: test validations
    }

    /**
     * Confirm that the client has applied the updated license.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void licenseActivationsPutConfirmTest() throws ApiException {
        String ID = null;
        DealerDBModelsLicenseActivationConfirm dealerDBModelsLicenseActivationConfirm = null;
        api.licenseActivationsPutConfirm(ID, dealerDBModelsLicenseActivationConfirm);
        // TODO: test validations
    }

}

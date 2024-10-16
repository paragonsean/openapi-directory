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
import org.openapitools.client.model.APIPagedResponseUpdateSystemModelsPackage;
import org.openapitools.client.model.UpdateSystemModelsPackage;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for PackagesApi
 */
@Disabled
public class PackagesApiTest {

    private final PackagesApi api = new PackagesApi();

    /**
     * Delete a Package.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void packagesDeletePackageTest() throws ApiException {
        String ID = null;
        api.packagesDeletePackage(ID);
        // TODO: test validations
    }

    /**
     * Find a Package.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void packagesGetPackageTest() throws ApiException {
        String ID = null;
        UpdateSystemModelsPackage response = api.packagesGetPackage(ID);
        // TODO: test validations
    }

    /**
     * List Packages.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void packagesGetPackagesTest() throws ApiException {
        Integer limit = null;
        Integer offset = null;
        String packageTypeID = null;
        Integer version = null;
        Boolean released = null;
        APIPagedResponseUpdateSystemModelsPackage response = api.packagesGetPackages(limit, offset, packageTypeID, version, released);
        // TODO: test validations
    }

    /**
     * Add a Package to the Update System.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void packagesPostPackageTest() throws ApiException {
        UpdateSystemModelsPackage updateSystemModelsPackage = null;
        String response = api.packagesPostPackage(updateSystemModelsPackage);
        // TODO: test validations
    }

    /**
     * Modify a Packge to the Update System.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void packagesPutPackageTest() throws ApiException {
        String ID = null;
        UpdateSystemModelsPackage updateSystemModelsPackage = null;
        api.packagesPutPackage(ID, updateSystemModelsPackage);
        // TODO: test validations
    }

}

/*
 * Otoroshi Admin API
 * Admin API of the Otoroshi reverse proxy
 *
 * The version of the OpenAPI document: 1.5.0-dev
 * Contact: oss@maif.fr
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ApiKey;
import org.openapitools.client.model.Deleted;
import org.openapitools.client.model.ErrorTemplate;
import org.openapitools.client.model.PatchInner;
import org.openapitools.client.model.Service;
import org.openapitools.client.model.Target;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ServicesApi
 */
@Disabled
public class ServicesApiTest {

    private final ServicesApi api = new ServicesApi();

    /**
     * Get all services
     *
     * Get all services
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void allServicesTest() throws ApiException {
        List<Service> response = api.allServices();
        // TODO: test validations
    }

    /**
     * Create a new service descriptor
     *
     * Create a new service descriptor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceTest() throws ApiException {
        Service service = null;
        Service response = api.createService(service);
        // TODO: test validations
    }

    /**
     * Create a service descriptor error template
     *
     * Update a service descriptor targets
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createServiceTemplateTest() throws ApiException {
        String serviceId = null;
        ErrorTemplate errorTemplate = null;
        ErrorTemplate response = api.createServiceTemplate(serviceId, errorTemplate);
        // TODO: test validations
    }

    /**
     * Delete a service descriptor
     *
     * Delete a service descriptor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteServiceTest() throws ApiException {
        String serviceId = null;
        Deleted response = api.deleteService(serviceId);
        // TODO: test validations
    }

    /**
     * Delete a service descriptor error template
     *
     * Delete a service descriptor error template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteServiceTemplateTest() throws ApiException {
        String serviceId = null;
        Deleted response = api.deleteServiceTemplate(serviceId);
        // TODO: test validations
    }

    /**
     * Update a service descriptor with a diff
     *
     * Update a service descriptor with a diff
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void patchServiceTest() throws ApiException {
        String serviceId = null;
        List<PatchInner> patchInner = null;
        Service response = api.patchService(serviceId, patchInner);
        // TODO: test validations
    }

    /**
     * Get a service descriptor
     *
     * Get a service descriptor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serviceTest() throws ApiException {
        String serviceId = null;
        Service response = api.service(serviceId);
        // TODO: test validations
    }

    /**
     * Add a target to a service descriptor
     *
     * Add a target to a service descriptor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serviceAddTargetTest() throws ApiException {
        String serviceId = null;
        Target target = null;
        List<Target> response = api.serviceAddTarget(serviceId, target);
        // TODO: test validations
    }

    /**
     * Delete a service descriptor target
     *
     * Delete a service descriptor target
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serviceDeleteTargetTest() throws ApiException {
        String serviceId = null;
        List<Target> response = api.serviceDeleteTarget(serviceId);
        // TODO: test validations
    }

    /**
     * Get all services descriptor for a group
     *
     * Get all services descriptor for a group
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serviceGroupServicesTest() throws ApiException {
        String serviceGroupId = null;
        List<ApiKey> response = api.serviceGroupServices(serviceGroupId);
        // TODO: test validations
    }

    /**
     * Get a service descriptor targets
     *
     * Get a service descriptor targets
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serviceTargetsTest() throws ApiException {
        String serviceId = null;
        List<Target> response = api.serviceTargets(serviceId);
        // TODO: test validations
    }

    /**
     * Get a service descriptor error template
     *
     * Get a service descriptor error template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void serviceTemplateTest() throws ApiException {
        String serviceId = null;
        ErrorTemplate response = api.serviceTemplate(serviceId);
        // TODO: test validations
    }

    /**
     * Update a service descriptor
     *
     * Update a service descriptor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceTest() throws ApiException {
        String serviceId = null;
        Service service = null;
        Service response = api.updateService(serviceId, service);
        // TODO: test validations
    }

    /**
     * Update a service descriptor targets
     *
     * Update a service descriptor targets
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceTargetsTest() throws ApiException {
        String serviceId = null;
        List<PatchInner> patchInner = null;
        List<Target> response = api.updateServiceTargets(serviceId, patchInner);
        // TODO: test validations
    }

    /**
     * Update an error template to a service descriptor
     *
     * Update an error template to a service descriptor
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateServiceTemplateTest() throws ApiException {
        String serviceId = null;
        ErrorTemplate errorTemplate = null;
        ErrorTemplate response = api.updateServiceTemplate(serviceId, errorTemplate);
        // TODO: test validations
    }

}

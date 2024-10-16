/*
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CreateNetworkSwitchQosRuleRequest;
import org.openapitools.client.model.UpdateNetworkSwitchQosRuleRequest;
import org.openapitools.client.model.UpdateNetworkSwitchQosRulesOrderRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for QosRulesApi
 */
@Disabled
public class QosRulesApiTest {

    private final QosRulesApi api = new QosRulesApi();

    /**
     * Add a quality of service rule
     *
     * Add a quality of service rule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNetworkSwitchQosRule_1Test() throws ApiException {
        String networkId = null;
        CreateNetworkSwitchQosRuleRequest createNetworkSwitchQosRuleRequest = null;
        Object response = api.createNetworkSwitchQosRule_1(networkId, createNetworkSwitchQosRuleRequest);
        // TODO: test validations
    }

    /**
     * Delete a quality of service rule
     *
     * Delete a quality of service rule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNetworkSwitchQosRule_1Test() throws ApiException {
        String networkId = null;
        String qosRuleId = null;
        api.deleteNetworkSwitchQosRule_1(networkId, qosRuleId);
        // TODO: test validations
    }

    /**
     * Return a quality of service rule
     *
     * Return a quality of service rule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSwitchQosRule_1Test() throws ApiException {
        String networkId = null;
        String qosRuleId = null;
        Object response = api.getNetworkSwitchQosRule_1(networkId, qosRuleId);
        // TODO: test validations
    }

    /**
     * Return the quality of service rule IDs by order in which they will be processed by the switch
     *
     * Return the quality of service rule IDs by order in which they will be processed by the switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSwitchQosRulesOrder_1Test() throws ApiException {
        String networkId = null;
        Object response = api.getNetworkSwitchQosRulesOrder_1(networkId);
        // TODO: test validations
    }

    /**
     * List quality of service rules
     *
     * List quality of service rules
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSwitchQosRules_1Test() throws ApiException {
        String networkId = null;
        List<Object> response = api.getNetworkSwitchQosRules_1(networkId);
        // TODO: test validations
    }

    /**
     * Update a quality of service rule
     *
     * Update a quality of service rule
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkSwitchQosRule_1Test() throws ApiException {
        String networkId = null;
        String qosRuleId = null;
        UpdateNetworkSwitchQosRuleRequest updateNetworkSwitchQosRuleRequest = null;
        Object response = api.updateNetworkSwitchQosRule_1(networkId, qosRuleId, updateNetworkSwitchQosRuleRequest);
        // TODO: test validations
    }

    /**
     * Update the order in which the rules should be processed by the switch
     *
     * Update the order in which the rules should be processed by the switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkSwitchQosRulesOrder_1Test() throws ApiException {
        String networkId = null;
        UpdateNetworkSwitchQosRulesOrderRequest updateNetworkSwitchQosRulesOrderRequest = null;
        Object response = api.updateNetworkSwitchQosRulesOrder_1(networkId, updateNetworkSwitchQosRulesOrderRequest);
        // TODO: test validations
    }

}

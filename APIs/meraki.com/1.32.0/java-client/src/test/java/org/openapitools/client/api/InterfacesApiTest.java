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
import org.openapitools.client.model.CreateDeviceSwitchRoutingInterfaceRequest;
import org.openapitools.client.model.CreateNetworkSwitchStackRoutingInterfaceRequest;
import org.openapitools.client.model.GetDeviceSwitchRoutingInterfaces200ResponseInner;
import org.openapitools.client.model.UpdateDeviceSwitchRoutingInterfaceDhcpRequest;
import org.openapitools.client.model.UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest;
import org.openapitools.client.model.UpdateNetworkSwitchStackRoutingInterfaceRequest;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for InterfacesApi
 */
@Disabled
public class InterfacesApiTest {

    private final InterfacesApi api = new InterfacesApi();

    /**
     * Create a layer 3 interface for a switch
     *
     * Create a layer 3 interface for a switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createDeviceSwitchRoutingInterface_2Test() throws ApiException {
        String serial = null;
        CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = null;
        GetDeviceSwitchRoutingInterfaces200ResponseInner response = api.createDeviceSwitchRoutingInterface_2(serial, createDeviceSwitchRoutingInterfaceRequest);
        // TODO: test validations
    }

    /**
     * Create a layer 3 interface for a switch stack
     *
     * Create a layer 3 interface for a switch stack
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNetworkSwitchStackRoutingInterface_3Test() throws ApiException {
        String networkId = null;
        String switchStackId = null;
        CreateNetworkSwitchStackRoutingInterfaceRequest createNetworkSwitchStackRoutingInterfaceRequest = null;
        Object response = api.createNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, createNetworkSwitchStackRoutingInterfaceRequest);
        // TODO: test validations
    }

    /**
     * Delete a layer 3 interface from the switch
     *
     * Delete a layer 3 interface from the switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteDeviceSwitchRoutingInterface_2Test() throws ApiException {
        String serial = null;
        String interfaceId = null;
        api.deleteDeviceSwitchRoutingInterface_2(serial, interfaceId);
        // TODO: test validations
    }

    /**
     * Delete a layer 3 interface from a switch stack
     *
     * Delete a layer 3 interface from a switch stack
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNetworkSwitchStackRoutingInterface_3Test() throws ApiException {
        String networkId = null;
        String switchStackId = null;
        String interfaceId = null;
        api.deleteNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId);
        // TODO: test validations
    }

    /**
     * Return a layer 3 interface DHCP configuration for a switch
     *
     * Return a layer 3 interface DHCP configuration for a switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDeviceSwitchRoutingInterfaceDhcp_2Test() throws ApiException {
        String serial = null;
        String interfaceId = null;
        Object response = api.getDeviceSwitchRoutingInterfaceDhcp_2(serial, interfaceId);
        // TODO: test validations
    }

    /**
     * Return a layer 3 interface for a switch
     *
     * Return a layer 3 interface for a switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDeviceSwitchRoutingInterface_2Test() throws ApiException {
        String serial = null;
        String interfaceId = null;
        GetDeviceSwitchRoutingInterfaces200ResponseInner response = api.getDeviceSwitchRoutingInterface_2(serial, interfaceId);
        // TODO: test validations
    }

    /**
     * List layer 3 interfaces for a switch
     *
     * List layer 3 interfaces for a switch. Those for a stack may be found under switch stack routing.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDeviceSwitchRoutingInterfaces_2Test() throws ApiException {
        String serial = null;
        List<GetDeviceSwitchRoutingInterfaces200ResponseInner> response = api.getDeviceSwitchRoutingInterfaces_2(serial);
        // TODO: test validations
    }

    /**
     * Return a layer 3 interface DHCP configuration for a switch stack
     *
     * Return a layer 3 interface DHCP configuration for a switch stack
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSwitchStackRoutingInterfaceDhcp_3Test() throws ApiException {
        String networkId = null;
        String switchStackId = null;
        String interfaceId = null;
        Object response = api.getNetworkSwitchStackRoutingInterfaceDhcp_3(networkId, switchStackId, interfaceId);
        // TODO: test validations
    }

    /**
     * Return a layer 3 interface from a switch stack
     *
     * Return a layer 3 interface from a switch stack
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSwitchStackRoutingInterface_3Test() throws ApiException {
        String networkId = null;
        String switchStackId = null;
        String interfaceId = null;
        Object response = api.getNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId);
        // TODO: test validations
    }

    /**
     * List layer 3 interfaces for a switch stack
     *
     * List layer 3 interfaces for a switch stack
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkSwitchStackRoutingInterfaces_3Test() throws ApiException {
        String networkId = null;
        String switchStackId = null;
        List<Object> response = api.getNetworkSwitchStackRoutingInterfaces_3(networkId, switchStackId);
        // TODO: test validations
    }

    /**
     * Update a layer 3 interface DHCP configuration for a switch
     *
     * Update a layer 3 interface DHCP configuration for a switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateDeviceSwitchRoutingInterfaceDhcp_2Test() throws ApiException {
        String serial = null;
        String interfaceId = null;
        UpdateDeviceSwitchRoutingInterfaceDhcpRequest updateDeviceSwitchRoutingInterfaceDhcpRequest = null;
        Object response = api.updateDeviceSwitchRoutingInterfaceDhcp_2(serial, interfaceId, updateDeviceSwitchRoutingInterfaceDhcpRequest);
        // TODO: test validations
    }

    /**
     * Update a layer 3 interface for a switch
     *
     * Update a layer 3 interface for a switch
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateDeviceSwitchRoutingInterface_2Test() throws ApiException {
        String serial = null;
        String interfaceId = null;
        CreateDeviceSwitchRoutingInterfaceRequest createDeviceSwitchRoutingInterfaceRequest = null;
        GetDeviceSwitchRoutingInterfaces200ResponseInner response = api.updateDeviceSwitchRoutingInterface_2(serial, interfaceId, createDeviceSwitchRoutingInterfaceRequest);
        // TODO: test validations
    }

    /**
     * Update a layer 3 interface DHCP configuration for a switch stack
     *
     * Update a layer 3 interface DHCP configuration for a switch stack
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkSwitchStackRoutingInterfaceDhcp_3Test() throws ApiException {
        String networkId = null;
        String switchStackId = null;
        String interfaceId = null;
        UpdateNetworkSwitchStackRoutingInterfaceDhcpRequest updateNetworkSwitchStackRoutingInterfaceDhcpRequest = null;
        Object response = api.updateNetworkSwitchStackRoutingInterfaceDhcp_3(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceDhcpRequest);
        // TODO: test validations
    }

    /**
     * Update a layer 3 interface for a switch stack
     *
     * Update a layer 3 interface for a switch stack
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void updateNetworkSwitchStackRoutingInterface_3Test() throws ApiException {
        String networkId = null;
        String switchStackId = null;
        String interfaceId = null;
        UpdateNetworkSwitchStackRoutingInterfaceRequest updateNetworkSwitchStackRoutingInterfaceRequest = null;
        Object response = api.updateNetworkSwitchStackRoutingInterface_3(networkId, switchStackId, interfaceId, updateNetworkSwitchStackRoutingInterfaceRequest);
        // TODO: test validations
    }

}

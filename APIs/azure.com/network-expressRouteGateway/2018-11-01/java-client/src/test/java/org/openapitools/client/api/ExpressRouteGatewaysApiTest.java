/*
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ExpressRouteGateway;
import org.openapitools.client.model.ExpressRouteGatewayList;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ExpressRouteGatewaysApi
 */
@Disabled
public class ExpressRouteGatewaysApiTest {

    private final ExpressRouteGatewaysApi api = new ExpressRouteGatewaysApi();

    /**
     * Creates or updates a ExpressRoute gateway in a specified resource group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void expressRouteGatewaysCreateOrUpdateTest() throws ApiException {
        String resourceGroupName = null;
        String expressRouteGatewayName = null;
        String apiVersion = null;
        String subscriptionId = null;
        ExpressRouteGateway putExpressRouteGatewayParameters = null;
        ExpressRouteGateway response = api.expressRouteGatewaysCreateOrUpdate(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId, putExpressRouteGatewayParameters);
        // TODO: test validations
    }

    /**
     * Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void expressRouteGatewaysDeleteTest() throws ApiException {
        String resourceGroupName = null;
        String expressRouteGatewayName = null;
        String apiVersion = null;
        String subscriptionId = null;
        api.expressRouteGatewaysDelete(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId);
        // TODO: test validations
    }

    /**
     * Fetches the details of a ExpressRoute gateway in a resource group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void expressRouteGatewaysGetTest() throws ApiException {
        String resourceGroupName = null;
        String expressRouteGatewayName = null;
        String apiVersion = null;
        String subscriptionId = null;
        ExpressRouteGateway response = api.expressRouteGatewaysGet(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId);
        // TODO: test validations
    }

    /**
     * Lists ExpressRoute gateways in a given resource group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void expressRouteGatewaysListByResourceGroupTest() throws ApiException {
        String resourceGroupName = null;
        String apiVersion = null;
        String subscriptionId = null;
        ExpressRouteGatewayList response = api.expressRouteGatewaysListByResourceGroup(resourceGroupName, apiVersion, subscriptionId);
        // TODO: test validations
    }

    /**
     * Lists ExpressRoute gateways under a given subscription.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void expressRouteGatewaysListBySubscriptionTest() throws ApiException {
        String apiVersion = null;
        String subscriptionId = null;
        ExpressRouteGatewayList response = api.expressRouteGatewaysListBySubscription(apiVersion, subscriptionId);
        // TODO: test validations
    }

}

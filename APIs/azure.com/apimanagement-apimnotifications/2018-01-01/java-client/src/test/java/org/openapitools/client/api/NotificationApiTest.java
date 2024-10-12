/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2018-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.NotificationCollection;
import org.openapitools.client.model.NotificationContract;
import org.openapitools.client.model.NotificationGetDefaultResponse;
import org.openapitools.client.model.RecipientUserCollection;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for NotificationApi
 */
@Disabled
public class NotificationApiTest {

    private final NotificationApi api = new NotificationApi();

    /**
     * Updates an Notification.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notificationCreateOrUpdateTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String notificationName = null;
        String apiVersion = null;
        String subscriptionId = null;
        String ifMatch = null;
        NotificationContract response = api.notificationCreateOrUpdate(resourceGroupName, serviceName, notificationName, apiVersion, subscriptionId, ifMatch);
        // TODO: test validations
    }

    /**
     * Gets the details of the Notification specified by its identifier.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notificationGetTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String notificationName = null;
        String apiVersion = null;
        String subscriptionId = null;
        NotificationContract response = api.notificationGet(resourceGroupName, serviceName, notificationName, apiVersion, subscriptionId);
        // TODO: test validations
    }

    /**
     * Lists a collection of properties defined within a service instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notificationListByServiceTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String apiVersion = null;
        String subscriptionId = null;
        Integer $top = null;
        Integer $skip = null;
        NotificationCollection response = api.notificationListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, $top, $skip);
        // TODO: test validations
    }

    /**
     * Gets the list of the Notification Recipient User subscribed to the notification.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notificationRecipientUserListByNotificationTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String notificationName = null;
        String apiVersion = null;
        String subscriptionId = null;
        RecipientUserCollection response = api.notificationRecipientUserListByNotification(resourceGroupName, serviceName, notificationName, apiVersion, subscriptionId);
        // TODO: test validations
    }

}

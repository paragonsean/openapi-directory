/*
 * ApiManagementClient
 * Use these REST APIs for performing operations on who is going to receive notifications associated with your Azure API Management deployment.
 *
 * The version of the OpenAPI document: 2019-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.NotificationListByServiceDefaultResponse;
import org.openapitools.client.model.NotificationRecipientUserCreateOrUpdate200Response;
import org.openapitools.client.model.NotificationRecipientUserListByNotification200Response;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for NotificationRecipientUserApi
 */
@Disabled
public class NotificationRecipientUserApiTest {

    private final NotificationRecipientUserApi api = new NotificationRecipientUserApi();

    /**
     * Determine if the Notification Recipient User is subscribed to the notification.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notificationRecipientUserCheckEntityExistsTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String notificationName = null;
        String userId = null;
        String apiVersion = null;
        String subscriptionId = null;
        api.notificationRecipientUserCheckEntityExists(resourceGroupName, serviceName, notificationName, userId, apiVersion, subscriptionId);
        // TODO: test validations
    }

    /**
     * Adds the API Management User to the list of Recipients for the Notification.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notificationRecipientUserCreateOrUpdateTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String notificationName = null;
        String userId = null;
        String apiVersion = null;
        String subscriptionId = null;
        NotificationRecipientUserCreateOrUpdate200Response response = api.notificationRecipientUserCreateOrUpdate(resourceGroupName, serviceName, notificationName, userId, apiVersion, subscriptionId);
        // TODO: test validations
    }

    /**
     * Removes the API Management user from the list of Notification.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void notificationRecipientUserDeleteTest() throws ApiException {
        String resourceGroupName = null;
        String serviceName = null;
        String notificationName = null;
        String userId = null;
        String apiVersion = null;
        String subscriptionId = null;
        api.notificationRecipientUserDelete(resourceGroupName, serviceName, notificationName, userId, apiVersion, subscriptionId);
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
        NotificationRecipientUserListByNotification200Response response = api.notificationRecipientUserListByNotification(resourceGroupName, serviceName, notificationName, apiVersion, subscriptionId);
        // TODO: test validations
    }

}

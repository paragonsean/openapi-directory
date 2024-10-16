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
import org.openapitools.client.model.APIModelsUser;
import org.openapitools.client.model.APIPagedResponseAPIModelsUser;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for UsersApi
 */
@Disabled
public class UsersApiTest {

    private final UsersApi api = new UsersApi();

    /**
     * Get a specific user
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiV2UsersIdGetTest() throws ApiException {
        Integer id = null;
        APIModelsUser response = api.apiV2UsersIdGet(id);
        // TODO: test validations
    }

    /**
     * Delete a user
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usersDeleteTest() throws ApiException {
        Integer id = null;
        api.usersDelete(id);
        // TODO: test validations
    }

    /**
     * Get users
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usersGetTest() throws ApiException {
        String username = null;
        String email = null;
        String name = null;
        String hasRole = null;
        Integer limit = null;
        Integer offset = null;
        APIPagedResponseAPIModelsUser response = api.usersGet(username, email, name, hasRole, limit, offset);
        // TODO: test validations
    }

    /**
     * Gets the current user
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usersGetCurrentUserTest() throws ApiException {
        APIModelsUser response = api.usersGetCurrentUser();
        // TODO: test validations
    }

    /**
     * Create a user
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usersPostTest() throws ApiException {
        APIModelsUser apIModelsUser = null;
        APIModelsUser response = api.usersPost(apIModelsUser);
        // TODO: test validations
    }

    /**
     * Update a user
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usersPutTest() throws ApiException {
        Integer id = null;
        APIModelsUser apIModelsUser = null;
        api.usersPut(id, apIModelsUser);
        // TODO: test validations
    }

    /**
     * Update a user
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void usersPutCurrentUserTest() throws ApiException {
        APIModelsUser apIModelsUser = null;
        api.usersPutCurrentUser(apIModelsUser);
        // TODO: test validations
    }

}

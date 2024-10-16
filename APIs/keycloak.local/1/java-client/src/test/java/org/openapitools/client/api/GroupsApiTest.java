/*
 * Keycloak Admin REST API
 * This is a REST API reference for the Keycloak Admin
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.GroupRepresentation;
import org.openapitools.client.model.ManagementPermissionReference;
import org.openapitools.client.model.UserRepresentation;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for GroupsApi
 */
@Disabled
public class GroupsApiTest {

    private final GroupsApi api = new GroupsApi();

    /**
     * Returns the groups counts.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsCountGetTest() throws ApiException {
        String realm = null;
        String search = null;
        Boolean top = null;
        Map<String, Object> response = api.realmGroupsCountGet(realm, search, top);
        // TODO: test validations
    }

    /**
     * Get group hierarchy.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsGetTest() throws ApiException {
        String realm = null;
        Boolean briefRepresentation = null;
        Integer first = null;
        Integer max = null;
        String search = null;
        List<GroupRepresentation> response = api.realmGroupsGet(realm, briefRepresentation, first, max, search);
        // TODO: test validations
    }

    /**
     * Set or create child.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsIdChildrenPostTest() throws ApiException {
        String realm = null;
        String id = null;
        GroupRepresentation groupRepresentation = null;
        api.realmGroupsIdChildrenPost(realm, id, groupRepresentation);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsIdDeleteTest() throws ApiException {
        String realm = null;
        String id = null;
        api.realmGroupsIdDelete(realm, id);
        // TODO: test validations
    }

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsIdGetTest() throws ApiException {
        String realm = null;
        String id = null;
        GroupRepresentation response = api.realmGroupsIdGet(realm, id);
        // TODO: test validations
    }

    /**
     * Return object stating whether client Authorization permissions have been initialized or not and a reference
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsIdManagementPermissionsGetTest() throws ApiException {
        String realm = null;
        String id = null;
        ManagementPermissionReference response = api.realmGroupsIdManagementPermissionsGet(realm, id);
        // TODO: test validations
    }

    /**
     * Return object stating whether client Authorization permissions have been initialized or not and a reference
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsIdManagementPermissionsPutTest() throws ApiException {
        String realm = null;
        String id = null;
        ManagementPermissionReference managementPermissionReference = null;
        ManagementPermissionReference response = api.realmGroupsIdManagementPermissionsPut(realm, id, managementPermissionReference);
        // TODO: test validations
    }

    /**
     * Get users   Returns a list of users, filtered according to query parameters
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsIdMembersGetTest() throws ApiException {
        String realm = null;
        String id = null;
        Boolean briefRepresentation = null;
        Integer first = null;
        Integer max = null;
        List<UserRepresentation> response = api.realmGroupsIdMembersGet(realm, id, briefRepresentation, first, max);
        // TODO: test validations
    }

    /**
     * Update group, ignores subgroups.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsIdPutTest() throws ApiException {
        String realm = null;
        String id = null;
        GroupRepresentation groupRepresentation = null;
        api.realmGroupsIdPut(realm, id, groupRepresentation);
        // TODO: test validations
    }

    /**
     * create or add a top level realm groupSet or create child.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void realmGroupsPostTest() throws ApiException {
        String realm = null;
        GroupRepresentation groupRepresentation = null;
        api.realmGroupsPost(realm, groupRepresentation);
        // TODO: test validations
    }

}

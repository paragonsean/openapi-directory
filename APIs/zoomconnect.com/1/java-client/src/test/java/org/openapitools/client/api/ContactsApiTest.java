/*
 * www.zoomconnect.com
 * The world's greatest SMS API
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
import org.openapitools.client.model.WebServiceContact;
import org.openapitools.client.model.WebServiceContacts;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ContactsApi
 */
@Disabled
public class ContactsApiTest {

    private final ContactsApi api = new ContactsApi();

    /**
     * all
     *
     * Returns all contacts
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsAllGetTest() throws ApiException {
        WebServiceContacts response = api.apiRestV1ContactsAllGet();
        // TODO: test validations
    }

    /**
     * removeFromGroup
     *
     * Remove a contact from a group
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsContactIdAddFromGroupGroupIdGetTest() throws ApiException {
        String contactId = null;
        String groupId = null;
        api.apiRestV1ContactsContactIdAddFromGroupGroupIdGet(contactId, groupId);
        // TODO: test validations
    }

    /**
     * removeFromGroup
     *
     * Remove a contact from a group
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsContactIdAddFromGroupGroupIdPostTest() throws ApiException {
        String contactId = null;
        String groupId = null;
        api.apiRestV1ContactsContactIdAddFromGroupGroupIdPost(contactId, groupId);
        // TODO: test validations
    }

    /**
     * addToGroup
     *
     * Add a contact to a group
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsContactIdAddToGroupGroupIdGetTest() throws ApiException {
        String contactId = null;
        String groupId = null;
        api.apiRestV1ContactsContactIdAddToGroupGroupIdGet(contactId, groupId);
        // TODO: test validations
    }

    /**
     * addToGroup
     *
     * Add a contact to a group
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsContactIdAddToGroupGroupIdPostTest() throws ApiException {
        String contactId = null;
        String groupId = null;
        api.apiRestV1ContactsContactIdAddToGroupGroupIdPost(contactId, groupId);
        // TODO: test validations
    }

    /**
     * delete
     *
     * Deletes a  contact
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsContactIdDeleteTest() throws ApiException {
        String contactId = null;
        api.apiRestV1ContactsContactIdDelete(contactId);
        // TODO: test validations
    }

    /**
     * get
     *
     * Returns details for a single contact
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsContactIdGetTest() throws ApiException {
        String contactId = null;
        WebServiceContact response = api.apiRestV1ContactsContactIdGet(contactId);
        // TODO: test validations
    }

    /**
     * update
     *
     * Updates a  contact
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsContactIdPostTest() throws ApiException {
        String contactId = null;
        WebServiceContact body = null;
        WebServiceContact response = api.apiRestV1ContactsContactIdPost(contactId, body);
        // TODO: test validations
    }

    /**
     * create
     *
     * Creates a  contact
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void apiRestV1ContactsCreatePostTest() throws ApiException {
        WebServiceContact body = null;
        WebServiceContact response = api.apiRestV1ContactsCreatePost(body);
        // TODO: test validations
    }

}

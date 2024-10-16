/*
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.Schema1;
import org.openapitools.client.model.Schema2;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for NetworkgroupsApi
 */
@Disabled
public class NetworkgroupsApiTest {

    private final NetworkgroupsApi api = new NetworkgroupsApi();

    /**
     * Add external peer
     *
     * Adds an external peer to a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNetworkGroupExternalPeer_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        Object body = null;
        Object response = api.createNetworkGroupExternalPeer_1(ownerId, networkGroupId, body);
        // TODO: test validations
    }

    /**
     * Add member
     *
     * Adds a member to a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNetworkGroupMember_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        Schema2 schema2 = null;
        api.createNetworkGroupMember_1(ownerId, networkGroupId, schema2);
        // TODO: test validations
    }

    /**
     * Create Network Group
     *
     * Creates a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void createNetworkGroup_1Test() throws ApiException {
        String ownerId = null;
        Object body = null;
        Object response = api.createNetworkGroup_1(ownerId, body);
        // TODO: test validations
    }

    /**
     * Remove external peer
     *
     * Removes an external peer from a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNetworkGroupExternalPeer_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        String peerId = null;
        Object body = null;
        api.deleteNetworkGroupExternalPeer_1(ownerId, networkGroupId, peerId, body);
        // TODO: test validations
    }

    /**
     * Remove member
     *
     * Removes a member from a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNetworkGroupMember_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        String memberId = null;
        Object body = null;
        api.deleteNetworkGroupMember_1(ownerId, networkGroupId, memberId, body);
        // TODO: test validations
    }

    /**
     * Remove peer
     *
     * Removes a peer from a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNetworkGroupPeer_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        String peerId = null;
        Object body = null;
        api.deleteNetworkGroupPeer_1(ownerId, networkGroupId, peerId, body);
        // TODO: test validations
    }

    /**
     * Delete Network Group
     *
     * Deletes a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void deleteNetworkGroup_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        Object body = null;
        api.deleteNetworkGroup_1(ownerId, networkGroupId, body);
        // TODO: test validations
    }

    /**
     * Get member
     *
     * Gets details of a Network Group member.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkGroupMember_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        String memberId = null;
        Object body = null;
        Schema1 response = api.getNetworkGroupMember_1(ownerId, networkGroupId, memberId, body);
        // TODO: test validations
    }

    /**
     * Get peer
     *
     * Gets details of a Network Group peer.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkGroupPeer_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        String peerId = null;
        Object body = null;
        Object response = api.getNetworkGroupPeer_1(ownerId, networkGroupId, peerId, body);
        // TODO: test validations
    }

    /**
     * Network Group SSE
     *
     * Retrieves the current Network Group details as a Server Sent Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkGroupStream_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        Object body = null;
        Object response = api.getNetworkGroupStream_1(ownerId, networkGroupId, body);
        // TODO: test validations
    }

    /**
     * Get WireGuard® configuration
     *
     * Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkGroupWireGuardConfigurationStream_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        String peerId = null;
        Object body = null;
        Object response = api.getNetworkGroupWireGuardConfigurationStream_1(ownerId, networkGroupId, peerId, body);
        // TODO: test validations
    }

    /**
     * Get WireGuard® configuration
     *
     * Gets the current WireGuard® tunnel configuration file for a Network Group peer.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkGroupWireGuardConfiguration_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        String peerId = null;
        Object body = null;
        Object response = api.getNetworkGroupWireGuardConfiguration_1(ownerId, networkGroupId, peerId, body);
        // TODO: test validations
    }

    /**
     * Get Network Group
     *
     * Gets details of a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNetworkGroup_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        Object body = null;
        Object response = api.getNetworkGroup_1(ownerId, networkGroupId, body);
        // TODO: test validations
    }

    /**
     * List members
     *
     * Lists members in a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listNetworkGroupMembers_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        Object body = null;
        List<Schema1> response = api.listNetworkGroupMembers_1(ownerId, networkGroupId, body);
        // TODO: test validations
    }

    /**
     * List peers
     *
     * Lists peers in a Network Group.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listNetworkGroupPeers_1Test() throws ApiException {
        String ownerId = null;
        String networkGroupId = null;
        Object body = null;
        List<Object> response = api.listNetworkGroupPeers_1(ownerId, networkGroupId, body);
        // TODO: test validations
    }

    /**
     * List Network Groups
     *
     * Lists Network Groups from an owner.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listNetworkGroups_1Test() throws ApiException {
        String ownerId = null;
        Object body = null;
        List<Object> response = api.listNetworkGroups_1(ownerId, body);
        // TODO: test validations
    }

}

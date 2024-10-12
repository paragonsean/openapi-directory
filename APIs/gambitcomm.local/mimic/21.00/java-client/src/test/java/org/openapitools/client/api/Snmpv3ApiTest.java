/*
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ConfigSNMPv3;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for Snmpv3Api
 */
@Disabled
public class Snmpv3ApiTest {

    private final Snmpv3Api api = new Snmpv3Api();

    /**
     * Adds a new access entry with the specified parameters.
     *
     * Adds a new access entry with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3AccessAddTest() throws ApiException {
        Integer agentNum = null;
        String groupName = null;
        String prefix = null;
        String securityModel = null;
        String securityLevel = null;
        String contextMatch = null;
        String readView = null;
        String writeView = null;
        String notifyView = null;
        String response = api.protocolSnmpv3AccessAdd(agentNum, groupName, prefix, securityModel, securityLevel, contextMatch, readView, writeView, notifyView);
        // TODO: test validations
    }

    /**
     * Clears all access entries.
     *
     * Clears all access entries.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3AccessClearTest() throws ApiException {
        Integer agentNum = null;
        String response = api.protocolSnmpv3AccessClear(agentNum);
        // TODO: test validations
    }

    /**
     * Deletes the specified access entry.
     *
     * Deletes the specified access entry.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3AccessDelTest() throws ApiException {
        Integer agentNum = null;
        String accessName = null;
        String response = api.protocolSnmpv3AccessDel(agentNum, accessName);
        // TODO: test validations
    }

    /**
     * Returns the current acccess entries as an array of strings.
     *
     * Returns the current acccess entries as an array of strings.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3AccessListTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.protocolSnmpv3AccessList(agentNum);
        // TODO: test validations
    }

    /**
     * Returns the SNMPv3 configuration.
     *
     * Returns the SNMPv3 configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GetConfigTest() throws ApiException {
        Integer agentNum = null;
        ConfigSNMPv3 response = api.protocolSnmpv3GetConfig(agentNum);
        // TODO: test validations
    }

    /**
     * Retrieves the contextEngineID for the agent instance.
     *
     * Retrieves the contextEngineID for the agent instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GetContextEngineidTest() throws ApiException {
        Integer agentNum = null;
        String response = api.protocolSnmpv3GetContextEngineid(agentNum);
        // TODO: test validations
    }

    /**
     * Retrieves the number of times the agent has been restarted.
     *
     * Retrieves the number of times the agent has been restarted.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GetEnginebootsTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.protocolSnmpv3GetEngineboots(agentNum);
        // TODO: test validations
    }

    /**
     * For started agents, retrieves the current engineID in use by the snmpv3 module.
     *
     * For stopped agents, this operation is meaningless. If not explicitly set by the user then the autogenerated engineID is returned. The format of the engineID is in the familiar hex format, eg. \\x01 23 45 67 89...
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GetEngineidTest() throws ApiException {
        Integer agentNum = null;
        String response = api.protocolSnmpv3GetEngineid(agentNum);
        // TODO: test validations
    }

    /**
     * Retrieves the time in seconds for which the agent has been running.
     *
     * Retrieves the time in seconds for which the agent has been running.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GetEnginetimeTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.protocolSnmpv3GetEnginetime(agentNum);
        // TODO: test validations
    }

    /**
     * Adds a new group entry with the specified parameters.
     *
     * Adds a new group entry with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GroupAddTest() throws ApiException {
        Integer agentNum = null;
        String groupName = null;
        String securityModel = null;
        String securityName = null;
        String response = api.protocolSnmpv3GroupAdd(agentNum, groupName, securityModel, securityName);
        // TODO: test validations
    }

    /**
     * Clears all group entries.
     *
     * Clears all group entries.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GroupClearTest() throws ApiException {
        Integer agentNum = null;
        String response = api.protocolSnmpv3GroupClear(agentNum);
        // TODO: test validations
    }

    /**
     * Deletes the specified group entry.
     *
     * Deletes the specified group entry.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GroupDelTest() throws ApiException {
        Integer agentNum = null;
        String groupName = null;
        String response = api.protocolSnmpv3GroupDel(agentNum, groupName);
        // TODO: test validations
    }

    /**
     * Returns the current group entries as an array of strings.
     *
     * Returns the current group entries as an array of strings.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3GroupListTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.protocolSnmpv3GroupList(agentNum);
        // TODO: test validations
    }

    /**
     * Changes the SNMPv3 configuration.
     *
     * Changes the SNMPv3 configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3SetConfigTest() throws ApiException {
        Integer agentNum = null;
        String parameter = null;
        String value = null;
        String response = api.protocolSnmpv3SetConfig(agentNum, parameter, value);
        // TODO: test validations
    }

    /**
     * Adds a new user entry with the specified parameters.
     *
     * Adds a new user entry with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3UserAddTest() throws ApiException {
        Integer agentNum = null;
        String userName = null;
        String securityName = null;
        String authProtocol = null;
        String authKey = null;
        String privProtocol = null;
        String privKey = null;
        String response = api.protocolSnmpv3UserAdd(agentNum, userName, securityName, authProtocol, authKey, privProtocol, privKey);
        // TODO: test validations
    }

    /**
     * Clears all user entries.
     *
     * Clears all user entries.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3UserClearTest() throws ApiException {
        Integer agentNum = null;
        String response = api.protocolSnmpv3UserClear(agentNum);
        // TODO: test validations
    }

    /**
     * Deletes the specified user entry.
     *
     * Deletes the specified user entry.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3UserDelTest() throws ApiException {
        Integer agentNum = null;
        String userName = null;
        String response = api.protocolSnmpv3UserDel(agentNum, userName);
        // TODO: test validations
    }

    /**
     * Returns the current user entries as a Tcl list.
     *
     * Returns the current user entries as a Tcl list.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3UserListTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.protocolSnmpv3UserList(agentNum);
        // TODO: test validations
    }

    /**
     * Saves current user settings in the currently loaded USM config file.
     *
     * Saves current user settings in the currently loaded USM config file.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3UsmSaveTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.protocolSnmpv3UsmSave(agentNum);
        // TODO: test validations
    }

    /**
     * Saves current user settings in the specified USM config file.
     *
     * Saves current user settings in the specified USM config file.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3UsmSaveasTest() throws ApiException {
        Integer agentNum = null;
        String filename = null;
        List<String> response = api.protocolSnmpv3UsmSaveas(agentNum, filename);
        // TODO: test validations
    }

    /**
     * Saves current group, access, view settings in the currently loaded VACM config file.
     *
     * Saves current group, access, view settings in the currently loaded VACM config file.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3VacmSaveTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.protocolSnmpv3VacmSave(agentNum);
        // TODO: test validations
    }

    /**
     * Saves current group, access, view settings in the specified VACM config file.
     *
     * Saves current group, access, view settings in the specified VACM config file.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3VacmSaveasTest() throws ApiException {
        Integer agentNum = null;
        String filename = null;
        List<String> response = api.protocolSnmpv3VacmSaveas(agentNum, filename);
        // TODO: test validations
    }

    /**
     * Adds a new view entry with the specified parameters.
     *
     * Adds a new view entry with the specified parameters.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3ViewAddTest() throws ApiException {
        Integer agentNum = null;
        String viewName = null;
        String viewType = null;
        String subtree = null;
        String mask = null;
        String response = api.protocolSnmpv3ViewAdd(agentNum, viewName, viewType, subtree, mask);
        // TODO: test validations
    }

    /**
     * Clears all view entries.
     *
     * Clears all view entries.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3ViewClearTest() throws ApiException {
        Integer agentNum = null;
        String response = api.protocolSnmpv3ViewClear(agentNum);
        // TODO: test validations
    }

    /**
     * Deletes the specified view entry.
     *
     * Deletes the specified view entry.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3ViewDelTest() throws ApiException {
        Integer agentNum = null;
        String viewName = null;
        String response = api.protocolSnmpv3ViewDel(agentNum, viewName);
        // TODO: test validations
    }

    /**
     * Returns the current view entries as an array of strings.
     *
     * Returns the current view entries as an array of strings.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolSnmpv3ViewListTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.protocolSnmpv3ViewList(agentNum);
        // TODO: test validations
    }

}

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
import org.openapitools.client.model.APIModelsApiError;
import org.openapitools.client.model.APIPagedResponseBuildSystemSharedDTOAgent;
import org.openapitools.client.model.BuildSystemSharedDTOActivityRun;
import org.openapitools.client.model.BuildSystemSharedDTOAgent;
import org.openapitools.client.model.BuildSystemSharedDTOAgentStatus;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AgentsApi
 */
@Disabled
public class AgentsApiTest {

    private final AgentsApi api = new AgentsApi();

    /**
     * Delete an Agent
     *
     * Deletes an Agent. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsDeleteAgentTest() throws ApiException {
        Integer agentID = null;
        api.agentsDeleteAgent(agentID);
        // TODO: test validations
    }

    /**
     * Get an Agent&#39;s ActivityRun
     *
     * Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsGetAgentActivityRunTest() throws ApiException {
        Integer agentID = null;
        BuildSystemSharedDTOActivityRun response = api.agentsGetAgentActivityRun(agentID);
        // TODO: test validations
    }

    /**
     * Get Agent
     *
     * Gets an Agent by ID. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsGetAgentAsyncTest() throws ApiException {
        Integer agentID = null;
        BuildSystemSharedDTOAgent response = api.agentsGetAgentAsync(agentID);
        // TODO: test validations
    }

    /**
     * Get Agents
     *
     * Gets a collection of Agents. When successful, the response is a PagedResponse of Agents.                If unsuccessful, an appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsGetAgentsTest() throws ApiException {
        Integer limit = null;
        Integer offset = null;
        APIPagedResponseBuildSystemSharedDTOAgent response = api.agentsGetAgents(limit, offset);
        // TODO: test validations
    }

    /**
     * Get the ActivityRun of Agent associated with the current user
     *
     * Gets the activity run assigned to an agent.  When successful, the response is the ActivityRun              assigned to the Agent.  If unsuccessful, an appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsGetCurrentAgentActivityRunTest() throws ApiException {
        BuildSystemSharedDTOActivityRun response = api.agentsGetCurrentAgentActivityRun();
        // TODO: test validations
    }

    /**
     * Get Agent associated with the current user
     *
     * Gets the Agent associated with the current user. When successful, the response is the requested Agent.  If unsuccessful,              an appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsGetCurrentAgentAsyncTest() throws ApiException {
        BuildSystemSharedDTOAgent response = api.agentsGetCurrentAgentAsync();
        // TODO: test validations
    }

    /**
     * Create an Agent
     *
     * Creates an Agent.  The body of the POST is the Agent to create.  The AgentID will be assigned              on creation of the Agent.  When successful, the response is the AgentID.  If unsuccessful, an              appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsPostAgentTest() throws ApiException {
        BuildSystemSharedDTOAgent buildSystemSharedDTOAgent = null;
        Integer response = api.agentsPostAgent(buildSystemSharedDTOAgent);
        // TODO: test validations
    }

    /**
     * Update an Agent
     *
     * Updates an Agent.  The body of the PUT is the updated Agent.  When successful, the response is empty.              If unsuccessful, an appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsPutAgentTest() throws ApiException {
        Integer agentID = null;
        BuildSystemSharedDTOAgent buildSystemSharedDTOAgent = null;
        api.agentsPutAgent(agentID, buildSystemSharedDTOAgent);
        // TODO: test validations
    }

    /**
     * Update the ActivityRun assigned to the Agent.
     *
     * No Documentation Found.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsPutAgentActivityRunTest() throws ApiException {
        Integer agentID = null;
        BuildSystemSharedDTOActivityRun buildSystemSharedDTOActivityRun = null;
        api.agentsPutAgentActivityRun(agentID, buildSystemSharedDTOActivityRun);
        // TODO: test validations
    }

    /**
     * Update an Agent
     *
     * Updates the status of an Agent.The body of the PUT is the updated Agent status.  When successful,              the response is empty.If unsuccessful, an appropriate ApiError is returned.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentsPutAgentStatusTest() throws ApiException {
        Integer agentID = null;
        BuildSystemSharedDTOAgentStatus buildSystemSharedDTOAgentStatus = null;
        api.agentsPutAgentStatus(agentID, buildSystemSharedDTOAgentStatus);
        // TODO: test validations
    }

}

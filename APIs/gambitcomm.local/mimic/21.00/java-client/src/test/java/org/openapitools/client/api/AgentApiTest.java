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
import org.openapitools.client.model.IPAlias;
import org.openapitools.client.model.IPSource;
import org.openapitools.client.model.TimerScript;
import org.openapitools.client.model.TrapDest;
import org.openapitools.client.model.Triplet;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AgentApi
 */
@Disabled
public class AgentApiTest {

    private final AgentApi api = new AgentApi();

    /**
     * Adds a new ipalias for the agent.
     *
     * port defaults to 161 if not specified. mask defaults to the class-based network mask for the address. interface defaults to the default network interface.  If port is set to 0, the system will automatically select a port number. This is useful for client-mode protocols, such as TFTP or TOD. Upon start of an IP alias with a 0 (auto-assigned) port number, its port will change to contain the value of the selected system port.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addIpaliasTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String mask = null;
        String _interface = null;
        String response = api.addIpalias(agentNum, IP, port, mask, _interface);
        // TODO: test validations
    }

    /**
     * Add a new timer script to be executed at specified interval (in msec) with the specified argument.
     *
     * Add a new timer script to be executed at specified interval (in msec) with the specified argument.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void addTimerScriptTest() throws ApiException {
        Integer agentNum = null;
        String script = null;
        Integer interval = null;
        String arg = null;
        String response = api.addTimerScript(agentNum, script, interval, arg);
        // TODO: test validations
    }

    /**
     * Remove the current agent.
     *
     * For speed, this operation will complete asynchronously. The same synchronization considerations apply as in /mimic/agent/start.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentRemoveTest() throws ApiException {
        Integer agentNum = null;
        String response = api.agentRemove(agentNum);
        // TODO: test validations
    }

    /**
     * This command copies the variable store from the other agent to this agent.
     *
     * This command copies the variable store from the other agent to this agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStoreCopyTest() throws ApiException {
        Integer agentNum = null;
        Integer otherAgent = null;
        String response = api.agentStoreCopy(agentNum, otherAgent);
        // TODO: test validations
    }

    /**
     * This command can be used as a predicate to ascertain the existence of a given variable.
     *
     * It returns \&quot;1\&quot; if the variable exists, else \&quot;0\&quot;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStoreExistsTest() throws ApiException {
        Integer agentNum = null;
        String var = null;
        String response = api.agentStoreExists(agentNum, var);
        // TODO: test validations
    }

    /**
     * Fetches the value associated with a variable.
     *
     * The value will be returned as a string (like all Tcl values).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStoreGetTest() throws ApiException {
        Integer agentNum = null;
        String var = null;
        String response = api.agentStoreGet(agentNum, var);
        // TODO: test validations
    }

    /**
     * This command will return the list of variables in the said scope.
     *
     * The list will be a Tcl format list with curly braces \&quot;{}\&quot; around each list element. These elements in turn are space separated.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStoreListTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.agentStoreList(agentNum);
        // TODO: test validations
    }

    /**
     * These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.
     *
     * These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStoreLreplaceTest() throws ApiException {
        Integer agentNum = null;
        String var = null;
        Integer index = null;
        String body = null;
        String response = api.agentStoreLreplace(agentNum, var, index, body);
        // TODO: test validations
    }

    /**
     * This command can be used as a predicate to ascertain the persistence of a given variable.
     *
     * It returns \&quot;1\&quot; if the variable is persistent, else \&quot;0\&quot;.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStorePersistsTest() throws ApiException {
        Integer agentNum = null;
        String var = null;
        String response = api.agentStorePersists(agentNum, var);
        // TODO: test validations
    }

    /**
     * These commands allow the creation of a new variable, or changing an existing value.
     *
     * The append sub-command will append the value to an existing variable, or create a new one. The set sub-command will overwrite an existing variable, or create a new one. The optional persist flag can be used to indicate if the variable is to be persistent as described above. By default a value of &#39;0&#39; will be implied for the persist flag. To avoid mistakes, for existing variables the persist flag can only be set. If you want to reset it, you first need to unset the variable.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStoreSetTest() throws ApiException {
        Integer agentNum = null;
        String var = null;
        Integer persist = null;
        String body = null;
        String response = api.agentStoreSet(agentNum, var, persist, body);
        // TODO: test validations
    }

    /**
     * Deletes a variable which is currently defined.
     *
     * This will cleanup persistent variables if needed
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void agentStoreUnsetTest() throws ApiException {
        Integer agentNum = null;
        String var = null;
        String response = api.agentStoreUnset(agentNum, var);
        // TODO: test validations
    }

    /**
     * Add an agent.
     *
     * Add an agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void callNewTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        List<Triplet> triplet = null;
        String response = api.callNew(agentNum, IP, triplet);
        // TODO: test validations
    }

    /**
     * Deletes an existing ipalias from the agent.
     *
     * port defaults to 161 if not specified.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void delIpaliasTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.delIpalias(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * Remove a timer script from the execution list.
     *
     * The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void delTimerScriptTest() throws ApiException {
        Integer agentNum = null;
        String script = null;
        Integer interval = null;
        String arg = null;
        String response = api.delTimerScript(agentNum, script, interval, arg);
        // TODO: test validations
    }

    /**
     * Add a source address that the agent will accept messages from.
     *
     * An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void fromAddTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.fromAdd(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * delete a source address that the agent will accept messages from.
     *
     * An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void fromDelTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.fromDel(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * List the source addresses that the agent will accept messages from.
     *
     * This in effect implements source-address-indexing, where 2 agents with the same address can be configured, each accepting messages from different management stations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void fromListTest() throws ApiException {
        Integer agentNum = null;
        List<IPSource> response = api.fromList(agentNum);
        // TODO: test validations
    }

    /**
     * current running state of the agent
     *
     * 0-Unknown 1-Running 2-Stopped 3-Halted 4-Paused 5-Deleted 6-Stopping
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getAgentStateTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getAgentState(agentNum);
        // TODO: test validations
    }

    /**
     * has the agent value space changed?
     *
     * has the agent value space changed?
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getChangedTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getChanged(agentNum);
        // TODO: test validations
    }

    /**
     * has the lab configuration changed?
     *
     * has the lab configuration changed?
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getConfigChangedTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getConfigChanged(agentNum);
        // TODO: test validations
    }

    /**
     * one-way transit delay in msec.
     *
     * The minimum granularity is 10 msec.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDelayTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getDelay(agentNum);
        // TODO: test validations
    }

    /**
     * drop rate (every N-th PDU). 0 means no drops.
     *
     * drop rate (every N-th PDU). 0 means no drops.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getDropsTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getDrops(agentNum);
        // TODO: test validations
    }

    /**
     * host address of the agent.
     *
     * Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getHostTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getHost(agentNum);
        // TODO: test validations
    }

    /**
     * timeout in seconds for retransmitting INFORM PDUs.
     *
     * The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInformTimeoutTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getInformTimeout(agentNum);
        // TODO: test validations
    }

    /**
     * network interface card for the agent.
     *
     * network interface card for the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getInterfaceTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getInterface(agentNum);
        // TODO: test validations
    }

    /**
     * subnet mask of the agent.
     *
     * subnet mask of the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMaskTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getMask(agentNum);
        // TODO: test validations
    }

    /**
     * set of MIBs, simulations and scenarios
     *
     * set of MIBs, simulations and scenarios
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getMibsTest() throws ApiException {
        Integer agentNum = null;
        List<Triplet> response = api.getMibs(agentNum);
        // TODO: test validations
    }

    /**
     * number of starts for the agent.
     *
     * This count is incremented each time an agent starts. It affects the SNMPv3 EngineBoots parameter.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getNumberStartsTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getNumberStarts(agentNum);
        // TODO: test validations
    }

    /**
     * MIB directory of the agent.
     *
     * MIB directory of the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOiddirTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getOiddir(agentNum);
        // TODO: test validations
    }

    /**
     * owner of the agent.
     *
     * owner of the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getOwnerTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getOwner(agentNum);
        // TODO: test validations
    }

    /**
     * maximum PDU size.
     *
     * The limit for this configurable is 65536.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPdusizeTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getPdusize(agentNum);
        // TODO: test validations
    }

    /**
     * port number
     *
     * port number
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPortTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getPort(agentNum);
        // TODO: test validations
    }

    /**
     * private directory of the agent.
     *
     * private directory of the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getPrivdirTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getPrivdir(agentNum);
        // TODO: test validations
    }

    /**
     * protocols supported by agent
     *
     * protocols supported by agent as an array of strings
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getProtocolsTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.getProtocols(agentNum);
        // TODO: test validations
    }

    /**
     * read community string
     *
     * read community string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getReadCommunityTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getReadCommunity(agentNum);
        // TODO: test validations
    }

    /**
     * first scenario name
     *
     * first scenario name
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getScenTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getScen(agentNum);
        // TODO: test validations
    }

    /**
     * first simulation name
     *
     * first simulation name
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getSimTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getSim(agentNum);
        // TODO: test validations
    }

    /**
     * relative start time
     *
     * relative start time
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getStarttimeTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getStarttime(agentNum);
        // TODO: test validations
    }

    /**
     * has the agent state changed?
     *
     * has the agent state changed?
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getStateChangedTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getStateChanged(agentNum);
        // TODO: test validations
    }

    /**
     * current statistics of the agent instance
     *
     * The statistics are returned as 64-bit decimal numbers for the following statistics, total, discarded, error, GET, GETNEXT, SET, GETBULK, trap, GET variables, GETNEXT variables, SET variables, GETBULK variables, INFORM sent, INFORM re-sent, INFORM timed out, INFORM acked, INFORM REPORT
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getStatisticsTest() throws ApiException {
        Integer agentNum = null;
        List<Integer> response = api.getStatistics(agentNum);
        // TODO: test validations
    }

    /**
     * SNMP PDU tracing
     *
     * SNMP PDU tracing
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getTraceTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getTrace(agentNum);
        // TODO: test validations
    }

    /**
     * SNMP SET validation policy.
     *
     * Is a bitmask in which with the following bits (from LSB) check for type, length, range, access
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getValidateTest() throws ApiException {
        Integer agentNum = null;
        Integer response = api.getValidate(agentNum);
        // TODO: test validations
    }

    /**
     * write community string
     *
     * write community string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void getWriteCommunityTest() throws ApiException {
        Integer agentNum = null;
        String response = api.getWriteCommunity(agentNum);
        // TODO: test validations
    }

    /**
     * Halt the current agent.
     *
     * Halt the current agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void haltTest() throws ApiException {
        Integer agentNum = null;
        String response = api.halt(agentNum);
        // TODO: test validations
    }

    /**
     * Lists all the additional ipaliases configured for the agent.
     *
     * The agent host address (set with mimic agent set host) is not in this list, since it is already accessible separately with mimic agent get host.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listIpaliasesTest() throws ApiException {
        Integer agentNum = null;
        List<IPAlias> response = api.listIpaliases(agentNum);
        // TODO: test validations
    }

    /**
     * List the timer scripts currently running along with the their intervals.
     *
     * The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void listTimerScriptsTest() throws ApiException {
        Integer agentNum = null;
        List<TimerScript> response = api.listTimerScripts(agentNum);
        // TODO: test validations
    }

    /**
     * Pause the current agent.
     *
     * Pause the current agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void pauseNowTest() throws ApiException {
        Integer agentNum = null;
        String response = api.pauseNow(agentNum);
        // TODO: test validations
    }

    /**
     * Returns the protocol&#39;s configuration.
     *
     * Returns the protocol&#39;s configuration.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void protocolGetConfigTest() throws ApiException {
        Integer agentNum = null;
        String prot = null;
        Object response = api.protocolGetConfig(agentNum, prot);
        // TODO: test validations
    }

    /**
     * Reload the current agent.
     *
     * This only works for halted agents. The net effect is the same as restarting an agent (ie. stop, start, halt), but without disconnecting the network (and thus existing connections).
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void reloadTest() throws ApiException {
        Integer agentNum = null;
        String response = api.reload(agentNum);
        // TODO: test validations
    }

    /**
     * Resume the current agent.
     *
     * Resume the current agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void resumeTest() throws ApiException {
        Integer agentNum = null;
        String response = api.resume(agentNum);
        // TODO: test validations
    }

    /**
     * Save agent MIB values.
     *
     * Save agent MIB values.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void saveTest() throws ApiException {
        Integer agentNum = null;
        String response = api.save(agentNum);
        // TODO: test validations
    }

    /**
     * one-way transit delay in msec
     *
     * The minimum granularity is 10 msec.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setDelayTest() throws ApiException {
        Integer agentNum = null;
        Integer delay = null;
        Integer response = api.setDelay(agentNum, delay);
        // TODO: test validations
    }

    /**
     * drop rate (every N-th PDU)
     *
     * 0 means no drops
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setDropsTest() throws ApiException {
        Integer agentNum = null;
        Integer drops = null;
        Integer response = api.setDrops(agentNum, drops);
        // TODO: test validations
    }

    /**
     * host address of the agent.
     *
     * Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setHostTest() throws ApiException {
        Integer agentNum = null;
        String host = null;
        String response = api.setHost(agentNum, host);
        // TODO: test validations
    }

    /**
     * timeout in seconds for retransmitting INFORM PDUs
     *
     * The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setInformTimeoutTest() throws ApiException {
        Integer agentNum = null;
        Integer informTimeout = null;
        Integer response = api.setInformTimeout(agentNum, informTimeout);
        // TODO: test validations
    }

    /**
     * network interface card for the agent
     *
     * network interface card for the agent
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setInterfaceTest() throws ApiException {
        Integer agentNum = null;
        String _interface = null;
        String response = api.setInterface(agentNum, _interface);
        // TODO: test validations
    }

    /**
     * subnet mask of the agent.
     *
     * subnet mask of the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setMaskTest() throws ApiException {
        Integer agentNum = null;
        String mask = null;
        String response = api.setMask(agentNum, mask);
        // TODO: test validations
    }

    /**
     * set of MIBs, simulations and scenarios
     *
     * set of MIBs, simulations and scenarios
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setMibsTest() throws ApiException {
        Integer agentNum = null;
        List<Triplet> triplet = null;
        String response = api.setMibs(agentNum, triplet);
        // TODO: test validations
    }

    /**
     * MIB directory of the agent.
     *
     * MIB directory of the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setOiddirTest() throws ApiException {
        Integer agentNum = null;
        String oiddir = null;
        String response = api.setOiddir(agentNum, oiddir);
        // TODO: test validations
    }

    /**
     * owner of the agent
     *
     * owner of the agent
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setOwnerTest() throws ApiException {
        Integer agentNum = null;
        String owner = null;
        String response = api.setOwner(agentNum, owner);
        // TODO: test validations
    }

    /**
     * maximum PDU size
     *
     * The limit for this configurable is 65536
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setPdusizeTest() throws ApiException {
        Integer agentNum = null;
        Integer pdusize = null;
        Integer response = api.setPdusize(agentNum, pdusize);
        // TODO: test validations
    }

    /**
     * port number
     *
     * port number
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setPortTest() throws ApiException {
        Integer agentNum = null;
        Integer port = null;
        String response = api.setPort(agentNum, port);
        // TODO: test validations
    }

    /**
     * private directory of the agent.
     *
     * private directory of the agent.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setPrivdirTest() throws ApiException {
        Integer agentNum = null;
        String privdir = null;
        String response = api.setPrivdir(agentNum, privdir);
        // TODO: test validations
    }

    /**
     * protocols supported by agent as a comma-separated list
     *
     * protocols supported by agent as a comma-separated list
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setProtocolsTest() throws ApiException {
        Integer agentNum = null;
        List<String> requestBody = null;
        List<Integer> response = api.setProtocols(agentNum, requestBody);
        // TODO: test validations
    }

    /**
     * read community string
     *
     * read community string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setReadCommunityTest() throws ApiException {
        Integer agentNum = null;
        String read = null;
        String response = api.setReadCommunity(agentNum, read);
        // TODO: test validations
    }

    /**
     * relative start time
     *
     * relative start time
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setStarttimeTest() throws ApiException {
        Integer agentNum = null;
        Integer start = null;
        String response = api.setStarttime(agentNum, start);
        // TODO: test validations
    }

    /**
     * SNMP PDU tracing
     *
     * SNMP PDU tracing
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setTraceTest() throws ApiException {
        Integer agentNum = null;
        Integer trace = null;
        Integer response = api.setTrace(agentNum, trace);
        // TODO: test validations
    }

    /**
     * SNMP SET validation policy
     *
     * Is a bitmask in which with the following bits (from LSB) check for type, length, range, access. A default value of 65535 does all validation checking.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setValidateTest() throws ApiException {
        Integer agentNum = null;
        Integer validate = null;
        Integer response = api.setValidate(agentNum, validate);
        // TODO: test validations
    }

    /**
     * write community string
     *
     * write community string
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void setWriteCommunityTest() throws ApiException {
        Integer agentNum = null;
        String write = null;
        String response = api.setWriteCommunity(agentNum, write);
        // TODO: test validations
    }

    /**
     * Start the current agent.
     *
     * For speed, this operation will complete asynchronously. A successful return from this command means the starting of the agent is in progress. If you need to rely on the agent to have completed startup, you should wait for it&#39;s state to become RUNNING.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startTest() throws ApiException {
        Integer agentNum = null;
        String response = api.start(agentNum);
        // TODO: test validations
    }

    /**
     * Starts an existing ipalias for the agent.
     *
     * port defaults to 161 if not specified.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void startIpaliasTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.startIpalias(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * Returns the status (0&#x3D;down, 1&#x3D;up) of an existing ipalias for the agent.
     *
     * port defaults to 161 if not specified.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void statusIpaliasTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.statusIpalias(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * Show the agent&#39;s primary IP address
     *
     * Agent primary IP address
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopTest() throws ApiException {
        Integer agentNum = null;
        String response = api.stop(agentNum);
        // TODO: test validations
    }

    /**
     * Stops an existing ipalias for the agent.
     *
     * port defaults to 161 if not specified.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void stopIpaliasTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.stopIpalias(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * Add a trap destination to the set of destinations.
     *
     * Add a trap destination to the set of destinations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void trapConfigAddTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.trapConfigAdd(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * Remove a trap destination from the set of destinations.
     *
     * Remove a trap destination from the set of destinations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void trapConfigDelTest() throws ApiException {
        Integer agentNum = null;
        String IP = null;
        Integer port = null;
        String response = api.trapConfigDel(agentNum, IP, port);
        // TODO: test validations
    }

    /**
     * List the set of trap destinations for this agent instance.
     *
     * Each trap destination is identified with an IP address and a port number. The default port number is the standard SNMP trap port 162.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void trapConfigListTest() throws ApiException {
        Integer agentNum = null;
        List<TrapDest> response = api.trapConfigList(agentNum);
        // TODO: test validations
    }

    /**
     * List the outstanding asynchronous traps for this agent instance.
     *
     * List the outstanding asynchronous traps for this agent instance.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void trapListTest() throws ApiException {
        Integer agentNum = null;
        List<String> response = api.trapList(agentNum);
        // TODO: test validations
    }

}

from typing import List, Dict
from aiohttp import web

from openapi_server.models.ip_alias import IPAlias
from openapi_server.models.ip_source import IPSource
from openapi_server.models.timer_script import TimerScript
from openapi_server.models.trap_dest import TrapDest
from openapi_server.models.triplet import Triplet
from openapi_server import util


async def add_ipalias(request: web.Request, agent_num, ip, port, mask, interface) -> web.Response:
    """Adds a new ipalias for the agent.

    port defaults to 161 if not specified. mask defaults to the class-based network mask for the address. interface defaults to the default network interface.  If port is set to 0, the system will automatically select a port number. This is useful for client-mode protocols, such as TFTP or TOD. Upon start of an IP alias with a 0 (auto-assigned) port number, its port will change to contain the value of the selected system port.

    :param agent_num: Agent to add the IP alias
    :type agent_num: int
    :param ip: IP address , IPv4 or IPv6
    :type ip: str
    :param port: SNMP port , 0 or empty for default
    :type port: int
    :param mask: Netmask, empty for default
    :type mask: str
    :param interface: Interface. Empty for default
    :type interface: str

    """
    return web.Response(status=200)


async def add_timer_script(request: web.Request, agent_num, script, interval, arg) -> web.Response:
    """Add a new timer script to be executed at specified interval (in msec) with the specified argument.

    Add a new timer script to be executed at specified interval (in msec) with the specified argument.

    :param agent_num: Agent to return the timer script list
    :type agent_num: int
    :param script: Script name
    :type script: str
    :param interval: Interval in msec
    :type interval: int
    :param arg: Arguments to the script
    :type arg: str

    """
    return web.Response(status=200)


async def agent_remove(request: web.Request, agent_num) -> web.Response:
    """Remove the current agent.

    For speed, this operation will complete asynchronously. The same synchronization considerations apply as in /mimic/agent/start.

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def agent_store_copy(request: web.Request, agent_num, other_agent) -> web.Response:
    """This command copies the variable store from the other agent to this agent.

    This command copies the variable store from the other agent to this agent.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param other_agent: Agent of the value space
    :type other_agent: int

    """
    return web.Response(status=200)


async def agent_store_exists(request: web.Request, agent_num, var) -> web.Response:
    """This command can be used as a predicate to ascertain the existence of a given variable.

    It returns \&quot;1\&quot; if the variable exists, else \&quot;0\&quot;.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def agent_store_get(request: web.Request, agent_num, var) -> web.Response:
    """Fetches the value associated with a variable.

    The value will be returned as a string (like all Tcl values).

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def agent_store_list(request: web.Request, agent_num) -> web.Response:
    """This command will return the list of variables in the said scope.

    The list will be a Tcl format list with curly braces \&quot;{}\&quot; around each list element. These elements in turn are space separated.

    :param agent_num: Agent of the value space
    :type agent_num: int

    """
    return web.Response(status=200)


async def agent_store_lreplace(request: web.Request, agent_num, var, index, body=None) -> web.Response:
    """These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

    These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param var: Variable name
    :type var: str
    :param index: Index
    :type index: int
    :param body: Value
    :type body: str

    """
    return web.Response(status=200)


async def agent_store_persists(request: web.Request, agent_num, var) -> web.Response:
    """This command can be used as a predicate to ascertain the persistence of a given variable.

    It returns \&quot;1\&quot; if the variable is persistent, else \&quot;0\&quot;.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def agent_store_set(request: web.Request, agent_num, var, persist, body=None) -> web.Response:
    """These commands allow the creation of a new variable, or changing an existing value.

    The append sub-command will append the value to an existing variable, or create a new one. The set sub-command will overwrite an existing variable, or create a new one. The optional persist flag can be used to indicate if the variable is to be persistent as described above. By default a value of &#39;0&#39; will be implied for the persist flag. To avoid mistakes, for existing variables the persist flag can only be set. If you want to reset it, you first need to unset the variable.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param var: Variable name
    :type var: str
    :param persist: Persistent setting
    :type persist: int
    :param body: Value
    :type body: str

    """
    return web.Response(status=200)


async def agent_store_unset(request: web.Request, agent_num, var) -> web.Response:
    """Deletes a variable which is currently defined.

    This will cleanup persistent variables if needed

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def del_ipalias(request: web.Request, agent_num, ip, port) -> web.Response:
    """Deletes an existing ipalias from the agent.

    port defaults to 161 if not specified.

    :param agent_num: Agent to delete the IP alias
    :type agent_num: int
    :param ip: IP address , IPv4 or IPv6
    :type ip: str
    :param port: SNMP port , 0 or empty for default
    :type port: int

    """
    return web.Response(status=200)


async def del_timer_script(request: web.Request, agent_num, script, interval, arg) -> web.Response:
    """Remove a timer script from the execution list.

    The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

    :param agent_num: Agent to return the timer script list
    :type agent_num: int
    :param script: Script name
    :type script: str
    :param interval: Interval in msec
    :type interval: int
    :param arg: Arguments to the script
    :type arg: str

    """
    return web.Response(status=200)


async def from_add(request: web.Request, agent_num, ip, port) -> web.Response:
    """Add a source address that the agent will accept messages from.

    An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

    :param agent_num: Agent to add the IP source
    :type agent_num: int
    :param ip: IP of the port, 0.0.0.0 for any
    :type ip: str
    :param port: port of the source, 0 for any
    :type port: int

    """
    return web.Response(status=200)


async def from_del(request: web.Request, agent_num, ip, port) -> web.Response:
    """delete a source address that the agent will accept messages from.

    An empty ipaddress or 0.0.0.0 both imply any address. Similarly an empty port or 0 both imply any port. For agents with source-address-indexing enabled, messages which do not match any source address will be discarded with an ERROR message, similar to community string mismatches.

    :param agent_num: Agent to delete the IP source
    :type agent_num: int
    :param ip: IP of the source
    :type ip: str
    :param port: port of the source
    :type port: int

    """
    return web.Response(status=200)


async def from_list(request: web.Request, agent_num) -> web.Response:
    """List the source addresses that the agent will accept messages from.

    This in effect implements source-address-indexing, where 2 agents with the same address can be configured, each accepting messages from different management stations.

    :param agent_num: Agent to show the IP sources
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_agent_state(request: web.Request, agent_num) -> web.Response:
    """current running state of the agent

    0-Unknown 1-Running 2-Stopped 3-Halted 4-Paused 5-Deleted 6-Stopping

    :param agent_num: Agent to return the state
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_changed(request: web.Request, agent_num) -> web.Response:
    """has the agent value space changed?

    has the agent value space changed?

    :param agent_num: Agent to return the indicator
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_config_changed(request: web.Request, agent_num) -> web.Response:
    """has the lab configuration changed?

    has the lab configuration changed?

    :param agent_num: Agent to return the indicator
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_delay(request: web.Request, agent_num) -> web.Response:
    """one-way transit delay in msec.

    The minimum granularity is 10 msec.

    :param agent_num: Agent to return the delay time
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_drops(request: web.Request, agent_num) -> web.Response:
    """drop rate (every N-th PDU). 0 means no drops.

    drop rate (every N-th PDU). 0 means no drops.

    :param agent_num: Agent to return the drop rate
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_host(request: web.Request, agent_num) -> web.Response:
    """host address of the agent.

    Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_inform_timeout(request: web.Request, agent_num) -> web.Response:
    """timeout in seconds for retransmitting INFORM PDUs.

    The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

    :param agent_num: Agent to return the timeout setting
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_interface(request: web.Request, agent_num) -> web.Response:
    """network interface card for the agent.

    network interface card for the agent.

    :param agent_num: Agent to return the primary interface
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_mask(request: web.Request, agent_num) -> web.Response:
    """subnet mask of the agent.

    subnet mask of the agent.

    :param agent_num: Agent to return the primary interface
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_mibs(request: web.Request, agent_num) -> web.Response:
    """set of MIBs, simulations and scenarios

    set of MIBs, simulations and scenarios

    :param agent_num: Agent to return the MIB triplets
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_number_starts(request: web.Request, agent_num) -> web.Response:
    """number of starts for the agent.

    This count is incremented each time an agent starts. It affects the SNMPv3 EngineBoots parameter.

    :param agent_num: Agent to return the count
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_oiddir(request: web.Request, agent_num) -> web.Response:
    """MIB directory of the agent.

    MIB directory of the agent.

    :param agent_num: Agent to return the directory path
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_owner(request: web.Request, agent_num) -> web.Response:
    """owner of the agent.

    owner of the agent.

    :param agent_num: Agent to return the owner
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_pdusize(request: web.Request, agent_num) -> web.Response:
    """maximum PDU size.

    The limit for this configurable is 65536.

    :param agent_num: Agent to return the PDU size
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_port(request: web.Request, agent_num) -> web.Response:
    """port number

    port number

    :param agent_num: Agent to return the primary SNMP port
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_privdir(request: web.Request, agent_num) -> web.Response:
    """private directory of the agent.

    private directory of the agent.

    :param agent_num: Agent to return the directory path
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_protocols(request: web.Request, agent_num) -> web.Response:
    """protocols supported by agent

    protocols supported by agent as an array of strings

    :param agent_num: Agent to return the protocols arrary
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_read_community(request: web.Request, agent_num) -> web.Response:
    """read community string

    read community string

    :param agent_num: Agent to return the SNMP read community string
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_scen(request: web.Request, agent_num) -> web.Response:
    """first scenario name

    first scenario name

    :param agent_num: Agent to return the first scenario number
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_sim(request: web.Request, agent_num) -> web.Response:
    """first simulation name

    first simulation name

    :param agent_num: Agent to return the first simulation name
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_starttime(request: web.Request, agent_num) -> web.Response:
    """relative start time

    relative start time

    :param agent_num: Agent to return the relative start time
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_state_changed(request: web.Request, agent_num) -> web.Response:
    """has the agent state changed?

    has the agent state changed?

    :param agent_num: Agent to return the indicator
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_statistics(request: web.Request, agent_num) -> web.Response:
    """current statistics of the agent instance

    The statistics are returned as 64-bit decimal numbers for the following statistics, total, discarded, error, GET, GETNEXT, SET, GETBULK, trap, GET variables, GETNEXT variables, SET variables, GETBULK variables, INFORM sent, INFORM re-sent, INFORM timed out, INFORM acked, INFORM REPORT

    :param agent_num: Agent to return the statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_trace(request: web.Request, agent_num) -> web.Response:
    """SNMP PDU tracing

    SNMP PDU tracing

    :param agent_num: Agent to return the indicator
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_validate(request: web.Request, agent_num) -> web.Response:
    """SNMP SET validation policy.

    Is a bitmask in which with the following bits (from LSB) check for type, length, range, access

    :param agent_num: Agent to return the bitmask integer
    :type agent_num: int

    """
    return web.Response(status=200)


async def get_write_community(request: web.Request, agent_num) -> web.Response:
    """write community string

    write community string

    :param agent_num: Agent to return the SNMP write community string
    :type agent_num: int

    """
    return web.Response(status=200)


async def halt(request: web.Request, agent_num) -> web.Response:
    """Halt the current agent.

    Halt the current agent.

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def list_ipaliases(request: web.Request, agent_num) -> web.Response:
    """Lists all the additional ipaliases configured for the agent.

    The agent host address (set with mimic agent set host) is not in this list, since it is already accessible separately with mimic agent get host.

    :param agent_num: Agent to show the IP alias list
    :type agent_num: int

    """
    return web.Response(status=200)


async def list_timer_scripts(request: web.Request, agent_num) -> web.Response:
    """List the timer scripts currently running along with the their intervals.

    The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.

    :param agent_num: Agent to return the timer script list
    :type agent_num: int

    """
    return web.Response(status=200)


async def new(request: web.Request, agent_num, ip, body) -> web.Response:
    """Add an agent.

    Add an agent.

    :param agent_num: Agent to return the primary IP
    :type agent_num: int
    :param ip: Primary IP
    :type ip: str
    :param body: Created agent object
    :type body: list | bytes

    """
    body = [Triplet.from_dict(d) for d in body]
    return web.Response(status=200)


async def pause_now(request: web.Request, agent_num) -> web.Response:
    """Pause the current agent.

    Pause the current agent.

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_get_config(request: web.Request, agent_num, prot) -> web.Response:
    """Returns the protocol&#39;s configuration.

    Returns the protocol&#39;s configuration.

    :param agent_num: Agent to show the protocol configuration
    :type agent_num: int
    :param prot: Protocol to show configuration
    :type prot: str

    """
    return web.Response(status=200)


async def reload(request: web.Request, agent_num) -> web.Response:
    """Reload the current agent.

    This only works for halted agents. The net effect is the same as restarting an agent (ie. stop, start, halt), but without disconnecting the network (and thus existing connections).

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def resume(request: web.Request, agent_num) -> web.Response:
    """Resume the current agent.

    Resume the current agent.

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def save(request: web.Request, agent_num) -> web.Response:
    """Save agent MIB values.

    Save agent MIB values.

    :param agent_num: Agent to save
    :type agent_num: int

    """
    return web.Response(status=200)


async def set_delay(request: web.Request, agent_num, delay) -> web.Response:
    """one-way transit delay in msec

    The minimum granularity is 10 msec.

    :param agent_num: Agent to set the delay time
    :type agent_num: int
    :param delay: Delay time of the agent
    :type delay: int

    """
    return web.Response(status=200)


async def set_drops(request: web.Request, agent_num, drops) -> web.Response:
    """drop rate (every N-th PDU)

    0 means no drops

    :param agent_num: Agent to set the drop rate
    :type agent_num: int
    :param drops: Drop rate of the agent
    :type drops: int

    """
    return web.Response(status=200)


async def set_host(request: web.Request, agent_num, host) -> web.Response:
    """host address of the agent.

    Currently, only IPv4 addresses are allowed as the main address of the agent, but both IPv4 and IPv6 addresses are allowed as IP aliases for the agent.

    :param agent_num: Agent to set the primary IP
    :type agent_num: int
    :param host: Primary IP of the agent
    :type host: str

    """
    return web.Response(status=200)


async def set_inform_timeout(request: web.Request, agent_num, inform_timeout) -> web.Response:
    """timeout in seconds for retransmitting INFORM PDUs

    The agent will retransmit INFORM PDUs at this interval until it has received a reply from the manager.

    :param agent_num: Agent to set the timeout setting
    :type agent_num: int
    :param inform_timeout: Tmeout setting
    :type inform_timeout: int

    """
    return web.Response(status=200)


async def set_interface(request: web.Request, agent_num, interface) -> web.Response:
    """network interface card for the agent

    network interface card for the agent

    :param agent_num: Agent to set the primary interface
    :type agent_num: int
    :param interface: Primary interface of the agent
    :type interface: str

    """
    return web.Response(status=200)


async def set_mask(request: web.Request, agent_num, mask) -> web.Response:
    """subnet mask of the agent.

    subnet mask of the agent.

    :param agent_num: Agent to set the primary IP address mask
    :type agent_num: int
    :param mask: Mask to set for the agent primary IP address
    :type mask: str

    """
    return web.Response(status=200)


async def set_mibs(request: web.Request, agent_num, body) -> web.Response:
    """set of MIBs, simulations and scenarios

    set of MIBs, simulations and scenarios

    :param agent_num: Agent to return the MIB triplets
    :type agent_num: int
    :param body: 
    :type body: list | bytes

    """
    body = [Triplet.from_dict(d) for d in body]
    return web.Response(status=200)


async def set_oiddir(request: web.Request, agent_num, oiddir) -> web.Response:
    """MIB directory of the agent.

    MIB directory of the agent.

    :param agent_num: Agent to set the directory path
    :type agent_num: int
    :param oiddir: Directory path for the agent
    :type oiddir: str

    """
    return web.Response(status=200)


async def set_owner(request: web.Request, agent_num, owner) -> web.Response:
    """owner of the agent

    owner of the agent

    :param agent_num: Agent to set the owner
    :type agent_num: int
    :param owner: Owner of the agent
    :type owner: str

    """
    return web.Response(status=200)


async def set_pdusize(request: web.Request, agent_num, pdusize) -> web.Response:
    """maximum PDU size

    The limit for this configurable is 65536

    :param agent_num: Agent to return the PDU size
    :type agent_num: int
    :param pdusize: PDU size setting for the agent
    :type pdusize: int

    """
    return web.Response(status=200)


async def set_port(request: web.Request, agent_num, port) -> web.Response:
    """port number

    port number

    :param agent_num: Agent to set the primary SNMP port
    :type agent_num: int
    :param port: Primary SNMP port of the agent
    :type port: int

    """
    return web.Response(status=200)


async def set_privdir(request: web.Request, agent_num, privdir) -> web.Response:
    """private directory of the agent.

    private directory of the agent.

    :param agent_num: Agent to set the directory path
    :type agent_num: int
    :param privdir: Directory path for the agent
    :type privdir: str

    """
    return web.Response(status=200)


async def set_protocols(request: web.Request, agent_num, body) -> web.Response:
    """protocols supported by agent as a comma-separated list

    protocols supported by agent as a comma-separated list

    :param agent_num: Agent to return the protocols arrary
    :type agent_num: int
    :param body: Created agent object
    :type body: List[str]

    """
    return web.Response(status=200)


async def set_read_community(request: web.Request, agent_num, read) -> web.Response:
    """read community string

    read community string

    :param agent_num: Agent to return the SNMP read community string
    :type agent_num: int
    :param read: SNMP read community string
    :type read: str

    """
    return web.Response(status=200)


async def set_starttime(request: web.Request, agent_num, start) -> web.Response:
    """relative start time

    relative start time

    :param agent_num: Agent to return the relative start time
    :type agent_num: int
    :param start: Relative start time of the agent
    :type start: int

    """
    return web.Response(status=200)


async def set_trace(request: web.Request, agent_num, trace) -> web.Response:
    """SNMP PDU tracing

    SNMP PDU tracing

    :param agent_num: Agent to set trace setting
    :type agent_num: int
    :param trace: Trace setting for the agent
    :type trace: int

    """
    return web.Response(status=200)


async def set_validate(request: web.Request, agent_num, validate) -> web.Response:
    """SNMP SET validation policy

    Is a bitmask in which with the following bits (from LSB) check for type, length, range, access. A default value of 65535 does all validation checking.

    :param agent_num: Agent to set the bitmask integer
    :type agent_num: int
    :param validate: Bitmask integer to set
    :type validate: int

    """
    return web.Response(status=200)


async def set_write_community(request: web.Request, agent_num, write) -> web.Response:
    """write community string

    write community string

    :param agent_num: Agent to set the SNMP write community string
    :type agent_num: int
    :param write: SNMP write community string
    :type write: str

    """
    return web.Response(status=200)


async def start(request: web.Request, agent_num) -> web.Response:
    """Start the current agent.

    For speed, this operation will complete asynchronously. A successful return from this command means the starting of the agent is in progress. If you need to rely on the agent to have completed startup, you should wait for it&#39;s state to become RUNNING.

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def start_ipalias(request: web.Request, agent_num, ip, port) -> web.Response:
    """Starts an existing ipalias for the agent.

    port defaults to 161 if not specified.

    :param agent_num: Agent to start the IP alias
    :type agent_num: int
    :param ip: IP address , IPv4 or IPv6
    :type ip: str
    :param port: SNMP port , 0 or empty for default
    :type port: int

    """
    return web.Response(status=200)


async def status_ipalias(request: web.Request, agent_num, ip, port) -> web.Response:
    """Returns the status (0&#x3D;down, 1&#x3D;up) of an existing ipalias for the agent.

    port defaults to 161 if not specified.

    :param agent_num: Agent to show status of the IP alias
    :type agent_num: int
    :param ip: IP address , IPv4 or IPv6
    :type ip: str
    :param port: SNMP port , 0 or empty for default
    :type port: int

    """
    return web.Response(status=200)


async def stop(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s primary IP address

    Agent primary IP address

    :param agent_num: Agent to return the primary IP
    :type agent_num: int

    """
    return web.Response(status=200)


async def stop_ipalias(request: web.Request, agent_num, ip, port) -> web.Response:
    """Stops an existing ipalias for the agent.

    port defaults to 161 if not specified.

    :param agent_num: Agent to stop the IP alias
    :type agent_num: int
    :param ip: IP address , IPv4 or IPv6
    :type ip: str
    :param port: SNMP port , 0 or empty for default
    :type port: int

    """
    return web.Response(status=200)


async def trap_config_add(request: web.Request, agent_num, ip, port) -> web.Response:
    """Add a trap destination to the set of destinations.

    Add a trap destination to the set of destinations.

    :param agent_num: Agent to add the destination
    :type agent_num: int
    :param ip: IP of the destination
    :type ip: str
    :param port: port of the destination
    :type port: int

    """
    return web.Response(status=200)


async def trap_config_del(request: web.Request, agent_num, ip, port) -> web.Response:
    """Remove a trap destination from the set of destinations.

    Remove a trap destination from the set of destinations.

    :param agent_num: Agent to delete the destination
    :type agent_num: int
    :param ip: IP of the destination
    :type ip: str
    :param port: port of the destination
    :type port: int

    """
    return web.Response(status=200)


async def trap_config_list(request: web.Request, agent_num) -> web.Response:
    """List the set of trap destinations for this agent instance.

    Each trap destination is identified with an IP address and a port number. The default port number is the standard SNMP trap port 162.

    :param agent_num: Agent to show the IP alias list
    :type agent_num: int

    """
    return web.Response(status=200)


async def trap_list(request: web.Request, agent_num) -> web.Response:
    """List the outstanding asynchronous traps for this agent instance.

    List the outstanding asynchronous traps for this agent instance.

    :param agent_num: Agent to list the traps
    :type agent_num: int

    """
    return web.Response(status=200)

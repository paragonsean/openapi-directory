from typing import List, Dict
from aiohttp import web

from openapi_server.models.agent_state import AgentState
from openapi_server.models.timer_script import TimerScript
from openapi_server import util


async def add_daemon_timer_script(request: web.Request, script, interval, arg) -> web.Response:
    """Add a new timer script to be executed at specified interval (in msec) with the specified argument.

    Add a new timer script to be executed at specified interval (in msec) with the specified argument.

    :param script: Script name
    :type script: str
    :param interval: Interval in msec
    :type interval: int
    :param arg: Arguments to the script
    :type arg: str

    """
    return web.Response(status=200)


async def cfg_load(request: web.Request, cfg_file, first_agent_num, last_agent_num, start_agent_num) -> web.Response:
    """Load the lab configuration file file.

    Load agents in cfgFile from firstAgentNum to lastAgentNum on startAgentNum of current configuration

    :param cfg_file: MIMIC agent configuration file to load
    :type cfg_file: str
    :param first_agent_num: Agent number in cfgFile to start the loading
    :type first_agent_num: int
    :param last_agent_num: Agent number in cfgFile to end the loading
    :type last_agent_num: int
    :param start_agent_num: Agent number in current configuration to start placing the new agents
    :type start_agent_num: int

    """
    return web.Response(status=200)


async def cfg_new(request: web.Request, first_agent_num, last_agent_num) -> web.Response:
    """Clear the lab configuration.

    Clear the lab configuration.

    :param first_agent_num: Agent number to start clearing
    :type first_agent_num: int
    :param last_agent_num: Agent number to end the clearing
    :type last_agent_num: int

    """
    return web.Response(status=200)


async def cfg_save(request: web.Request, ) -> web.Response:
    """Save the lab configuration.

    Save the lab configuration.


    """
    return web.Response(status=200)


async def cfg_saveas(request: web.Request, cfg_file, first_agent_num, last_agent_num) -> web.Response:
    """Save the lab configuration in file.

    Save the lab configuration in file.

    :param cfg_file: MIMIC agent configuration file to save
    :type cfg_file: str
    :param first_agent_num: Agent number in cfgFile to start the loading
    :type first_agent_num: int
    :param last_agent_num: Agent number in cfgFile to end the loading
    :type last_agent_num: int

    """
    return web.Response(status=200)


async def del_daemon_timer_script(request: web.Request, script, interval, arg) -> web.Response:
    """Remove a timer script from the execution list.

    The first scheduled script that matches the script name, and optionally the interval and argument will be deleted.

    :param script: Script name
    :type script: str
    :param interval: Interval in msec
    :type interval: int
    :param arg: Arguments to the script
    :type arg: str

    """
    return web.Response(status=200)


async def get_active_data_list(request: web.Request, ) -> web.Response:
    """The list of {agentnum {statistics}} for agents that are currently active and whose statistics have changed since the last invocation of this command.

    This list is guaranteed to be sorted into increasing order.


    """
    return web.Response(status=200)


async def get_active_list(request: web.Request, ) -> web.Response:
    """The list of {agentnum} that are currently active (running or paused).

    This list is guaranteed to be sorted into increasing order.


    """
    return web.Response(status=200)


async def get_cfg_file_changed(request: web.Request, ) -> web.Response:
    """This predicate indicates if the currently loaded agent configuration file has changed.

    Whether the loaded agent configuration file has changed since the last time this predicate was queried. This allows for a client to detect agent configuration changes and to synchronize those changes from the MIMIC daemon.


    """
    return web.Response(status=200)


async def get_cfgfile(request: web.Request, ) -> web.Response:
    """The currently loaded lab configuration file for the particular user.

    In the case of multi-user access this command returns a different configuration file loaded for each user.


    """
    return web.Response(status=200)


async def get_changed_config_list(request: web.Request, ) -> web.Response:
    """The list of {agentnum} for which a configurable parameter changed.

    This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.


    """
    return web.Response(status=200)


async def get_changed_state_list(request: web.Request, ) -> web.Response:
    """The list of {agentnum state} for which the state changed.

    This list contains at most 5000 agent(s), and is guaranteed to be sorted into increasing order.


    """
    return web.Response(status=200)


async def get_clients(request: web.Request, ) -> web.Response:
    """The number of clients currently connected to the daemon.

    The number of clients currently connected to the daemon.


    """
    return web.Response(status=200)


async def get_configured_list(request: web.Request, ) -> web.Response:
    """The list of {agentnum} that are currently configured.

    This list is guaranteed to be sorted into increasing order.


    """
    return web.Response(status=200)


async def get_daemon_protocols(request: web.Request, ) -> web.Response:
    """The set of protocols supported by the Simulator.

    The set of protocols supported by the Simulator.


    """
    return web.Response(status=200)


async def get_interfaces(request: web.Request, ) -> web.Response:
    """The set of network interfaces that can be used for simulations.

    The set of network interfaces that can be used for simulations.


    """
    return web.Response(status=200)


async def get_last(request: web.Request, ) -> web.Response:
    """The last configured agent instance.

    The last configured agent instance.


    """
    return web.Response(status=200)


async def get_log(request: web.Request, ) -> web.Response:
    """The current log file for the Simulator.

    The current log file for the Simulator.


    """
    return web.Response(status=200)


async def get_max(request: web.Request, ) -> web.Response:
    """The maximum number of agent instances.

    The maximum number of agent instances.


    """
    return web.Response(status=200)


async def get_netaddr(request: web.Request, ) -> web.Response:
    """The network address of the host where the MIMIC simulator is running.

    The network address of the host where the MIMIC simulator is running.


    """
    return web.Response(status=200)


async def get_netdev(request: web.Request, ) -> web.Response:
    """The default network device to be used for agent addresses.

    The default network device to be used for agent addresses if the interface is not explicitly specified for an agent.


    """
    return web.Response(status=200)


async def get_product(request: web.Request, ) -> web.Response:
    """The product number that is licensed.

    The product number that is licensed.


    """
    return web.Response(status=200)


async def get_return(request: web.Request, ) -> web.Response:
    """The return mode.

    The OpenAPI daemon operates in two modes, nocatch, where error returns from MIMIC operations return error; or catch, where the TCL catch semantics are used (these are similar to C++ exceptions)


    """
    return web.Response(status=200)


async def get_version(request: web.Request, ) -> web.Response:
    """The version of the MIMIC command interface.

    The version of the MIMIC command interface.


    """
    return web.Response(status=200)


async def list_daemon_timer_scripts(request: web.Request, ) -> web.Response:
    """List the timer scripts currently running along with the their intervals.

    The command mimic timer script list lists global timer scripts, the command /mimic/timer/script/{agentNum}/list is the per-agent equivalent NOTE Global timer scripts run globally but within them you can address individual agents using {agentNum}. To schedule timerscripts for an individual agent, use /mimic/timer/script/{agentNum}.


    """
    return web.Response(status=200)


async def mget_info(request: web.Request, info_array) -> web.Response:
    """Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

    Get multiple sets of information about MIMIC, where infoArray is one of the parameters defined in the mimic get command.

    :param info_array: Multiple strings of info.
    :type info_array: List[str]

    """
    return web.Response(status=200)


async def set_log(request: web.Request, body) -> web.Response:
    """The current log file for the Simulator.

    The current log file for the Simulator.

    :param body: The file name of the new log file
    :type body: str

    """
    return web.Response(status=200)


async def set_netdev(request: web.Request, ) -> web.Response:
    """The network address of the host where the MIMIC simulator is running.

    The network address of the host where the MIMIC simulator is running.


    """
    return web.Response(status=200)


async def start_all_agents(request: web.Request, ) -> web.Response:
    """Start MIMIC.

    Start MIMIC.


    """
    return web.Response(status=200)


async def stop_all_agents(request: web.Request, ) -> web.Response:
    """Stop MIMIC.

    Stop MIMIC.


    """
    return web.Response(status=200)


async def store_exists(request: web.Request, var) -> web.Response:
    """This command can be used as a predicate to ascertain the existence of a given variable.

    It returns \&quot;1\&quot; if the variable exists, else \&quot;0\&quot;.

    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def store_get(request: web.Request, var) -> web.Response:
    """Fetches the value associated with a variable.

    The value will be returned as a string (like all Tcl values).

    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def store_list(request: web.Request, ) -> web.Response:
    """This command will return the list of variables in the said scope.

    The list will be a Tcl format list with curly braces \&quot;{}\&quot; around each list element. These elements in turn are space separated.


    """
    return web.Response(status=200)


async def store_lreplace(request: web.Request, var, index, body=None) -> web.Response:
    """These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

    These commands treat the variable as a list, and allow to replace an entry in the list at the specified index with the specified value. The variable has to already exist.

    :param var: Variable name
    :type var: str
    :param index: Index
    :type index: int
    :param body: Value
    :type body: str

    """
    return web.Response(status=200)


async def store_persists(request: web.Request, var) -> web.Response:
    """This command can be used as a predicate to ascertain the persistence of a given variable.

    It returns \&quot;1\&quot; if the variable is persistent, else \&quot;0\&quot;.

    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def store_save(request: web.Request, ) -> web.Response:
    """This operation flushes all global objects which need to be made persistent to disk.

    The MIMIC daemon caches persistent objects and their changes, and writes them to disk at program termination. If it were to crash, these changes would be lost. This operation allows to checkpoint the cache, ie. write changes to persistent objects to disk. To save the lab configuration with per-agent persistent information the mimic save operation needs to be used.


    """
    return web.Response(status=200)


async def store_set(request: web.Request, var, persist, body=None) -> web.Response:
    """Set the variable store for the global storage

    Persist 1 means persistent , 0 means non-persistent

    :param var: Variable name
    :type var: str
    :param persist: Persistent setting
    :type persist: int
    :param body: Value
    :type body: str

    """
    return web.Response(status=200)


async def store_unset(request: web.Request, var) -> web.Response:
    """Deletes a variable which is currently defined.

    This will cleanup persistent variables if needed

    :param var: Variable name
    :type var: str

    """
    return web.Response(status=200)


async def terminate(request: web.Request, ) -> web.Response:
    """Terminate the MIMIC daemon.

    Terminate the MIMIC daemon.


    """
    return web.Response(status=200)

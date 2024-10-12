from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def add(request: web.Request, agent_num, object, instance) -> web.Response:
    """Add an entry to a table.

    The object needs to specify the MIB object with the INDEX clause, usually an object whose name ends with Entry.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Object (column) of the table in the agent&#39;s value space
    :type object: str
    :param instance: Object (column) of the table in the agent&#39;s value space
    :type instance: str

    """
    return web.Response(status=200)


async def eval_value(request: web.Request, agent_num, object, instance) -> web.Response:
    """Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

    Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Single instance object or object (column) of the table in the agent&#39;s value space.
    :type object: str
    :param instance: Row of the table in the agent&#39;s value space. 0 for single instance objects
    :type instance: str

    """
    return web.Response(status=200)


async def get_info(request: web.Request, agent_num, object) -> web.Response:
    """Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.

    Return the syntactical information for the specified object, such as type, size, range, enumerations, and ACCESS.

    :param agent_num: Agent to show the information of the object
    :type agent_num: int
    :param object: Object
    :type object: str

    """
    return web.Response(status=200)


async def get_instances(request: web.Request, agent_num, object) -> web.Response:
    """Display the MIB object instances for the specified object.

    This enables MIB browsing of the MIB on the current agent.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Object (column) of the table in the agent&#39;s value space
    :type object: str

    """
    return web.Response(status=200)


async def get_mib(request: web.Request, agent_num, object) -> web.Response:
    """Return the MIB that defines the specified object.

    This will only return a MIB name if the object is unmistakeably defined in a MIB.

    :param agent_num: Agent to show the MIB
    :type agent_num: int
    :param object: Object
    :type object: str

    """
    return web.Response(status=200)


async def get_name(request: web.Request, agent_num, oid) -> web.Response:
    """Return the symbolic name of the specified object identifier.

    Return the symbolic name of the specified object identifier.

    :param agent_num: Agent to show the object
    :type agent_num: int
    :param oid: OID
    :type oid: str

    """
    return web.Response(status=200)


async def get_objects(request: web.Request, agent_num, oid) -> web.Response:
    """Display the MIB objects below the current position

    This command is similar to the ls or dir operating system commands to list filesystem directories.

    :param agent_num: Agent to show the OID branches
    :type agent_num: int
    :param oid: Current OID
    :type oid: str

    """
    return web.Response(status=200)


async def get_oid(request: web.Request, agent_num, object) -> web.Response:
    """Return the numeric OID of the specified object.

    Return the numeric OID of the specified object.

    :param agent_num: Agent to show the OID
    :type agent_num: int
    :param object: Object
    :type object: str

    """
    return web.Response(status=200)


async def get_state(request: web.Request, agent_num, object) -> web.Response:
    """Get the state of a MIB object object.

    To disable traversal into a MIB object and any subtree underneath, set the state to 0, else set the state to 1.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Object
    :type object: str

    """
    return web.Response(status=200)


async def get_value(request: web.Request, agent_num, object, instance, variable) -> web.Response:
    """Get a variable in the Value Space.

    Get a variable in the Value Space.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Object (column) of the table in the agent&#39;s value space
    :type object: str
    :param instance: Object (column) of the table in the agent&#39;s value space
    :type instance: str
    :param variable: Object (column) of the table in the agent&#39;s value space
    :type variable: str

    """
    return web.Response(status=200)


async def get_variables(request: web.Request, agent_num, object, instance) -> web.Response:
    """Display the variables for the specified instance instance for the specified MIB object object

    This enables variable browsing of the MIB on the current agent.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Single instance object or object (column) of the table in the agent&#39;s value space.
    :type object: str
    :param instance: Row of the table in the agent&#39;s value space. 0 for single instance objects
    :type instance: str

    """
    return web.Response(status=200)


async def meval_value(request: web.Request, agent_num, obj_ins_array) -> web.Response:
    """Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

    Evaluate the values of the specified instance instance for each specified MIB object object and return it as it would through SNMP requests.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param obj_ins_array: Multiple objects or object (column) of the table in the agent&#39;s value space.
    :type obj_ins_array: List[]

    """
    return web.Response(status=200)


async def mget_value(request: web.Request, agent_num, obj_ins_var_array) -> web.Response:
    """Get multiple variables in the Value Space.

    This is a performance optimization of the mimic value get command, to be used when many variables are requested.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param obj_ins_var_array: Multiple objects or object (column) of the table in the agent&#39;s value space.
    :type obj_ins_var_array: List[]

    """
    return web.Response(status=200)


async def mset_value(request: web.Request, agent_num, body=None) -> web.Response:
    """Set multiple variables in the Value Space.

    This is a performance optimization of the mimic value set command, to be used when many variables are to be set.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param body: objInsVarValArray
    :type body: List[]

    """
    return web.Response(status=200)


async def munset_value(request: web.Request, agent_num, body=None) -> web.Response:
    """Unset multiple variables in the Value Space

    This is a performance optimization of the mimic value unset command, to be used when many variables are to be unset.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param body: objInsVarArray
    :type body: List[]

    """
    return web.Response(status=200)


async def remove(request: web.Request, agent_num, object, instance) -> web.Response:
    """Remove an entry from a table.

    The object needs to specify the MIB object with the INDEX clause, usually an object whose name ends with Entry.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Object (column) of the table in the agent&#39;s value space
    :type object: str
    :param instance: Object (column) of the table in the agent&#39;s value space
    :type instance: str

    """
    return web.Response(status=200)


async def set_state(request: web.Request, agent_num, object, state) -> web.Response:
    """Set the state of a MIB object object

    To disable traversal into a MIB object and any subtree underneath, set the state to 0, else set the state to 1.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Object
    :type object: str
    :param state: State
    :type state: int

    """
    return web.Response(status=200)


async def set_value(request: web.Request, agent_num, object, instance, variable, body=None) -> web.Response:
    """Set a variable in the Value Space.

    NOTE to set a binary string value, specify a string starting with \\\\x followed by pairs of hexadecimal digits, eg. \&quot;\\\\x 01 23 45\&quot;. This command also assigns SNMP PDU action scripts for GET* and SET requests on a MIB object. The instance parameter must be 0. The following variables enable actions, g - The specified TCL script will be run on GET or GETNEXT requests. It has to exist under the simulation directory. s - The specified script will be run on SET requests. It has to exist under the simulation directory. This command also controls advanced trap generation functionality. The following variables control trap generation r, tu, c - These variables together represent the rate settings for the trap. r and tu is the actual per second rate and c represents the total duration in seconds for which the trap is sent. As soon as the c variable is set, the trap generation begins, for this reason it should be the last variable set for a particular trap. The following variables have to be set before setting the c variable to modify the behavior of the generated trap(s). OBJECT - An object name when used as a variable is looked up during the trap send and the value of that variable is included in the PDU. OBJECT.i - This type of variable will be used to assign an optional instance for the specified object in the traps varbind. The value of this variable identifies the index. e.g. The commands below will send ifIndex.2 with a value of 5 in the linkUp trap PDU. i - This variable is used to specify any extra version specific information to the trap generation code. Here is what it can be used to represent for various SNMP versions SNMPv1 - [community_string][,[enterprise][,agent_addr]] SNMPv2c - community_string SNMPv2 - source_party,destination_party,context SNMPv3 - user_name,context v - This variable lets the user override the version of the PDU being generated. The possible values are - \&quot;1\&quot;, \&quot;2c\&quot;, \&quot;2\&quot; and \&quot;3\&quot;. o - This variable is used for traps that need extra variables to be added to the PDU along with the ones defined in the MIB as its variables. This lets the user force extra objects (along with instances if needed). All variables to be sent need to be assigned to the o variable. O - To omit any variables which are defined in the MIB you can use the O (capital o) variable. This needs to be set to the list of OIDs of the variable bindings in the order defined in the MIB. ip - The variable ip is used for generating the trap from the N-th IP alias address. a - This variable associates an action script to the trap or INFORM request. The action script specified in the value of this variable has to exist in the simulation directory. It will be executed before each instance of the trap is sent out. I - This optional variable controls the generation of INFORM PDUs. An INFORM is sent only if the variable is non-zero, else a TRAP is generated. R, T, E - This variable associates an action script to the INFORM request. The action script specified in the value of this variable has to exist in the simulation directory. The action script associated with the R variable will be executed on receiving a INFORM RESPONSE, the one associated with the T variable on a timeout (ie. no response), the one associated with the E variable on a report PDU. eid.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine id for the destination specified by IP-ADDRESS and optionally by PORT. eb.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine boots. et.IP-ADDRESS.PORT - control variable allows to configure message authoritative engine time.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Single instance object or object (column) of the table in the agent&#39;s value space.
    :type object: str
    :param instance: Row of the table in the agent&#39;s value space. 0 for single instance objects
    :type instance: str
    :param variable: Variable
    :type variable: str
    :param body: Value
    :type body: str

    """
    return web.Response(status=200)


async def split_oid(request: web.Request, agent_num, oid) -> web.Response:
    """Split the numerical OID into the object OID and instance OID.

    This is useful if you have an OID which is a combination of object and instance.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param oid: OID
    :type oid: str

    """
    return web.Response(status=200)


async def unset_value(request: web.Request, agent_num, object, instance, variable) -> web.Response:
    """Unset a variable in the Value Space in order to free its memory.

    Only variables that have previously been set can be unset.

    :param agent_num: Agent of the value space
    :type agent_num: int
    :param object: Single instance object or object (column) of the table in the agent&#39;s value space.
    :type object: str
    :param instance: Row of the table in the agent&#39;s value space. 0 for single instance objects
    :type instance: str
    :param variable: Variable
    :type variable: str

    """
    return web.Response(status=200)

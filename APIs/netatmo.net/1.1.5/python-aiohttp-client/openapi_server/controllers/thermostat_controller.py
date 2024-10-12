from typing import List, Dict
from aiohttp import web

from openapi_server.models.na_measure_response import NAMeasureResponse
from openapi_server.models.na_new_schedule_response import NANewScheduleResponse
from openapi_server.models.naok_response import NAOkResponse
from openapi_server.models.na_therm_program import NAThermProgram
from openapi_server.models.na_thermostat_data_response import NAThermostatDataResponse
from openapi_server import util


async def createnewschedule(request: web.Request, device_id, module_id, body) -> web.Response:
    """createnewschedule

    The method createnewschedule creates a new schedule stored in the backup list.

    :param device_id: The relay id
    :type device_id: str
    :param module_id: The thermostat id
    :type module_id: str
    :param body: The thermostat program (zones and timetable)
    :type body: dict | bytes

    """
    body = NAThermProgram.from_dict(body)
    return web.Response(status=200)


async def getmeasure_0(request: web.Request, device_id, scale, type, module_id=None, date_begin=None, date_end=None, limit=None, optimize=None, real_time=None) -> web.Response:
    """getmeasure_0

    The method getmeasure returns the measurements of a device or a module. 

    :param device_id: Id of the device whose module&#39;s measurements you want to retrieve. This _id can be found in the user&#39;s devices field.
    :type device_id: str
    :param scale: Defines the time interval between two measurements. Possible values : max -&gt; every value stored will be returned 30min -&gt; 1 value every 30 minutes 1hour -&gt; 1 value every hour 3hours -&gt; 1 value every 3 hours 1day -&gt; 1 value per day 1week -&gt; 1 value per week 1month -&gt; 1 value per month 
    :type scale: str
    :param type: Measures you are interested in. Data you can request depends on the scale. **For Weather Station:**   * max -&gt; Temperature (°C), CO2 (ppm), Humidity (%), Pressure (mbar), Noise (db), Rain (mm), WindStrength (km/h), WindAngle (angles), Guststrength (km/h), GustAngle (angles)   * 30min, 1hour, 3hours -&gt; Same as above + min_temp, max_temp, min_hum, max_hum, min_pressure, max_pressure, min_noise, max_noise, sum_rain, date_max_gust   * 1day, 1week, 1month -&gt; Same as above + date_min_temp, date_max_temp, date_min_hum, date_max_hum, date_min_pressure, date_max_pressure, date_min_noise, date_max_noise, date_min_co2, date_max_co2  **For Thermostat:**   * max -&gt; temperature (°C), sp_temperature (°C), boileron (sec), boileroff (sec)   * 30min, 1hour, 3hours -&gt; temperature, sp_temperature, min_temp, max_temp, sum_boiler_on, sum_boiler_off   * 1day, 1week, 1month -&gt; temperature, min_temp, date_min_temp, max_temp, sum_boiler_on, sum_boiler_off 
    :type type: List[str]
    :param module_id: If you don&#39;t specify any module_id you will retrieve the device&#39;s measurements. If you specify a module_id you will retrieve the module&#39;s measurements.
    :type module_id: str
    :param date_begin: Starting timestamp (utc) of the requested measurements. Please note measurement retrieving is limited to 1024 measurements. 
    :type date_begin: int
    :param date_end: Ending timestamp (utc) of the request measurements. If you want only the last measurement, do not provide date_begin, and set date_end to &#x60;last&#x60;. 
    :type date_end: str
    :param limit: Limits the number of measurements returned (default &amp; max is 1024)
    :type limit: int
    :param optimize: Allows you to choose the format of the answer. If you build a mobile app and bandwith usage is an issue, use &#x60;optimize &#x3D; true&#x60;. Use &#x60;optimize &#x3D; false&#x60;, for an easier parse. In this case, values are indexed by sorted timestamp. Example of un-optimized response : &#x60;&#x60;&#x60;json {\&quot;status\&quot;: \&quot;ok\&quot;,    \&quot;body\&quot;: {     \&quot;1347575400\&quot;: [18.3,39],     \&quot;1347586200\&quot;: [20.6,48]   }, \&quot;time_exec\&quot;: 0.012136936187744} &#x60;&#x60;&#x60; If optimize is set true, measurements are returned as an array of series of regularly spaced measurements. Each series is defined by a beginning time beg_time and a step between measurements, step_time: &#x60;&#x60;&#x60;json {\&quot;status\&quot;: \&quot;ok\&quot;,   \&quot;body\&quot;: [     {\&quot;beg_time\&quot;: 1347575400,      \&quot;step_time\&quot;: 10800,      \&quot;value\&quot;:          [[18.3,39],         [ 20.6,48]]     }], \&quot;time_exec\&quot;: 0.014238119125366} &#x60;&#x60;&#x60; Default value is &#x60;true&#x60;. 
    :type optimize: bool
    :param real_time: In scales higher than max, since the data is aggregated, the timestamps returned are by default offset by +(scale/2). For instance, if you ask for measurements at a daily scale, you will receive data timestamped at 12:00 if real_time is set to &#x60;false&#x60; (default case), and timestamped at 00:00 if real_time is set to &#x60;true&#x60;. NB : The servers always store data with real_time set to &#x60;true&#x60; and data are offset by this parameter AFTER having being time-filtered, thus you could have data after date_end if real_time is set to &#x60;false&#x60;. 
    :type real_time: bool

    """
    return web.Response(status=200)


async def getthermostatsdata(request: web.Request, device_id=None) -> web.Response:
    """getthermostatsdata

    The method getthermostatsdata returns information about user&#39;s thermostats such as their last measurements.

    :param device_id: Id of the device you want to retrieve information of
    :type device_id: str

    """
    return web.Response(status=200)


async def setthermpoint(request: web.Request, device_id, module_id, setpoint_mode, setpoint_endtime=None, setpoint_temp=None) -> web.Response:
    """setthermpoint

    The method setthermpoint changes the Thermostat manual temperature setpoint.

    :param device_id: The relay id
    :type device_id: str
    :param module_id: The thermostat id
    :type module_id: str
    :param setpoint_mode: Chosen setpoint_mode
    :type setpoint_mode: str
    :param setpoint_endtime: When using the manual or max setpoint_mode, this parameter defines when the setpoint expires.
    :type setpoint_endtime: int
    :param setpoint_temp: When using the manual setpoint_mode, this parameter defines the temperature setpoint (in Celcius) to use.
    :type setpoint_temp: float

    """
    return web.Response(status=200)


async def switchschedule(request: web.Request, device_id, module_id, schedule_id) -> web.Response:
    """switchschedule

    The method switchschedule switches the Thermostat&#39;s schedule to another existing schedule.

    :param device_id: The relay id
    :type device_id: str
    :param module_id: The thermostat id
    :type module_id: str
    :param schedule_id: The schedule id. It can be found in the getthermstate response, under the keys &#x60;therm_program_backup&#x60; and &#x60;therm_program&#x60;. 
    :type schedule_id: str

    """
    return web.Response(status=200)


async def syncschedule(request: web.Request, device_id, module_id, body) -> web.Response:
    """syncschedule

    The method syncschedule changes the Thermostat weekly schedule.

    :param device_id: The relay id
    :type device_id: str
    :param module_id: The thermostat id
    :type module_id: str
    :param body: The thermostat program (zones, timetable and name)
    :type body: dict | bytes

    """
    body = NAThermProgram.from_dict(body)
    return web.Response(status=200)

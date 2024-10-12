from typing import List, Dict
from aiohttp import web

from openapi_server.models.alarm_type import AlarmType
from openapi_server.models.anomaly_detector_type import AnomalyDetectorType
from openapi_server.models.delete_alarms_input import DeleteAlarmsInput
from openapi_server.models.delete_anomaly_detector_input import DeleteAnomalyDetectorInput
from openapi_server.models.delete_dashboards_input import DeleteDashboardsInput
from openapi_server.models.delete_insight_rules_input import DeleteInsightRulesInput
from openapi_server.models.delete_insight_rules_output import DeleteInsightRulesOutput
from openapi_server.models.delete_metric_stream_input import DeleteMetricStreamInput
from openapi_server.models.describe_alarm_history_input import DescribeAlarmHistoryInput
from openapi_server.models.describe_alarm_history_output import DescribeAlarmHistoryOutput
from openapi_server.models.describe_alarms_for_metric_input import DescribeAlarmsForMetricInput
from openapi_server.models.describe_alarms_for_metric_output import DescribeAlarmsForMetricOutput
from openapi_server.models.describe_alarms_input import DescribeAlarmsInput
from openapi_server.models.describe_alarms_output import DescribeAlarmsOutput
from openapi_server.models.describe_anomaly_detectors_input import DescribeAnomalyDetectorsInput
from openapi_server.models.describe_anomaly_detectors_output import DescribeAnomalyDetectorsOutput
from openapi_server.models.describe_insight_rules_input import DescribeInsightRulesInput
from openapi_server.models.describe_insight_rules_output import DescribeInsightRulesOutput
from openapi_server.models.dimension import Dimension
from openapi_server.models.dimension_filter import DimensionFilter
from openapi_server.models.disable_alarm_actions_input import DisableAlarmActionsInput
from openapi_server.models.disable_insight_rules_input import DisableInsightRulesInput
from openapi_server.models.disable_insight_rules_output import DisableInsightRulesOutput
from openapi_server.models.enable_alarm_actions_input import EnableAlarmActionsInput
from openapi_server.models.enable_insight_rules_input import EnableInsightRulesInput
from openapi_server.models.enable_insight_rules_output import EnableInsightRulesOutput
from openapi_server.models.get_delete_anomaly_detector_metric_math_anomaly_detector_parameter import GETDeleteAnomalyDetectorMetricMathAnomalyDetectorParameter
from openapi_server.models.get_delete_anomaly_detector_single_metric_anomaly_detector_parameter import GETDeleteAnomalyDetectorSingleMetricAnomalyDetectorParameter
from openapi_server.models.get_get_metric_data_label_options_parameter import GETGetMetricDataLabelOptionsParameter
from openapi_server.models.get_put_anomaly_detector_configuration_parameter import GETPutAnomalyDetectorConfigurationParameter
from openapi_server.models.get_dashboard_input import GetDashboardInput
from openapi_server.models.get_dashboard_output import GetDashboardOutput
from openapi_server.models.get_insight_rule_report_input import GetInsightRuleReportInput
from openapi_server.models.get_insight_rule_report_output import GetInsightRuleReportOutput
from openapi_server.models.get_metric_data_input import GetMetricDataInput
from openapi_server.models.get_metric_data_output import GetMetricDataOutput
from openapi_server.models.get_metric_statistics_input import GetMetricStatisticsInput
from openapi_server.models.get_metric_statistics_output import GetMetricStatisticsOutput
from openapi_server.models.get_metric_stream_input import GetMetricStreamInput
from openapi_server.models.get_metric_stream_output import GetMetricStreamOutput
from openapi_server.models.get_metric_widget_image_input import GetMetricWidgetImageInput
from openapi_server.models.get_metric_widget_image_output import GetMetricWidgetImageOutput
from openapi_server.models.list_dashboards_input import ListDashboardsInput
from openapi_server.models.list_dashboards_output import ListDashboardsOutput
from openapi_server.models.list_managed_insight_rules_input import ListManagedInsightRulesInput
from openapi_server.models.list_managed_insight_rules_output import ListManagedInsightRulesOutput
from openapi_server.models.list_metric_streams_input import ListMetricStreamsInput
from openapi_server.models.list_metric_streams_output import ListMetricStreamsOutput
from openapi_server.models.list_metrics_input import ListMetricsInput
from openapi_server.models.list_metrics_output import ListMetricsOutput
from openapi_server.models.list_tags_for_resource_input import ListTagsForResourceInput
from openapi_server.models.list_tags_for_resource_output import ListTagsForResourceOutput
from openapi_server.models.managed_rule import ManagedRule
from openapi_server.models.metric_data_query import MetricDataQuery
from openapi_server.models.metric_datum import MetricDatum
from openapi_server.models.metric_stream_filter import MetricStreamFilter
from openapi_server.models.metric_stream_statistics_configuration import MetricStreamStatisticsConfiguration
from openapi_server.models.put_anomaly_detector_input import PutAnomalyDetectorInput
from openapi_server.models.put_composite_alarm_input import PutCompositeAlarmInput
from openapi_server.models.put_dashboard_input import PutDashboardInput
from openapi_server.models.put_dashboard_output import PutDashboardOutput
from openapi_server.models.put_insight_rule_input import PutInsightRuleInput
from openapi_server.models.put_managed_insight_rules_input import PutManagedInsightRulesInput
from openapi_server.models.put_managed_insight_rules_output import PutManagedInsightRulesOutput
from openapi_server.models.put_metric_alarm_input import PutMetricAlarmInput
from openapi_server.models.put_metric_data_input import PutMetricDataInput
from openapi_server.models.put_metric_stream_input import PutMetricStreamInput
from openapi_server.models.put_metric_stream_output import PutMetricStreamOutput
from openapi_server.models.set_alarm_state_input import SetAlarmStateInput
from openapi_server.models.start_metric_streams_input import StartMetricStreamsInput
from openapi_server.models.statistic import Statistic
from openapi_server.models.stop_metric_streams_input import StopMetricStreamsInput
from openapi_server.models.tag import Tag
from openapi_server.models.tag_resource_input import TagResourceInput
from openapi_server.models.untag_resource_input import UntagResourceInput
from openapi_server import util


async def g_et_delete_alarms(request: web.Request, alarm_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_alarms

    &lt;p&gt;Deletes the specified alarms. You can delete up to 100 alarms in one operation. However, this total can include no more than one composite alarm. For example, you could delete 99 metric alarms and one composite alarms with one operation, but you can&#39;t delete two composite alarms with one operation.&lt;/p&gt; &lt;p&gt; If you specify an incorrect alarm name or make any other error in the operation, no alarms are deleted. To confirm that alarms were deleted successfully, you can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html\&quot;&gt;DescribeAlarms&lt;/a&gt; operation after using &lt;code&gt;DeleteAlarms&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can&#39;t delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.&lt;/p&gt; &lt;p&gt;To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the &lt;code&gt;AlarmRule&lt;/code&gt; of one of the alarms to &lt;code&gt;false&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. &lt;/p&gt; &lt;/note&gt;

    :param alarm_names: The alarms to be deleted. Do not enclose the alarm names in quote marks.
    :type alarm_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_anomaly_detector(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, namespace=None, metric_name=None, dimensions=None, stat=None, single_metric_anomaly_detector=None, metric_math_anomaly_detector=None) -> web.Response:
    """g_et_delete_anomaly_detector

     Deletes the specified anomaly detection model from your account. For more information about how to delete an anomaly detection model, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html#Delete_Anomaly_Detection_Model\&quot;&gt;Deleting an anomaly detection model&lt;/a&gt; in the &lt;i&gt;CloudWatch User Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param namespace: The namespace associated with the anomaly detection model to delete.
    :type namespace: str
    :param metric_name: The metric name associated with the anomaly detection model to delete.
    :type metric_name: str
    :param dimensions: The metric dimensions associated with the anomaly detection model to delete.
    :type dimensions: list | bytes
    :param stat: The statistic associated with the anomaly detection model to delete.
    :type stat: str
    :param single_metric_anomaly_detector: &lt;p&gt;A single metric anomaly detector to be deleted.&lt;/p&gt; &lt;p&gt;When using &lt;code&gt;SingleMetricAnomalyDetector&lt;/code&gt;, you cannot include the following parameters in the same operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Dimensions&lt;/code&gt;,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MetricName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Namespace&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Stat&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;the &lt;code&gt;MetricMathAnomalyDetector&lt;/code&gt; parameters of &lt;code&gt;DeleteAnomalyDetectorInput&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Instead, specify the single metric anomaly detector attributes as part of the &lt;code&gt;SingleMetricAnomalyDetector&lt;/code&gt; property.&lt;/p&gt;
    :type single_metric_anomaly_detector: dict | bytes
    :param metric_math_anomaly_detector: &lt;p&gt;The metric math anomaly detector to be deleted.&lt;/p&gt; &lt;p&gt;When using &lt;code&gt;MetricMathAnomalyDetector&lt;/code&gt;, you cannot include following parameters in the same operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Dimensions&lt;/code&gt;,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MetricName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Namespace&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Stat&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;the &lt;code&gt;SingleMetricAnomalyDetector&lt;/code&gt; parameters of &lt;code&gt;DeleteAnomalyDetectorInput&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Instead, specify the metric math anomaly detector attributes as part of the &lt;code&gt;MetricMathAnomalyDetector&lt;/code&gt; property.&lt;/p&gt;
    :type metric_math_anomaly_detector: dict | bytes

    """
    dimensions = [Dimension.from_dict(d) for d in dimensions]
    single_metric_anomaly_detector = .from_dict(single_metric_anomaly_detector)
    metric_math_anomaly_detector = .from_dict(metric_math_anomaly_detector)
    return web.Response(status=200)


async def g_et_delete_dashboards(request: web.Request, dashboard_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_dashboards

    Deletes all dashboards that you specify. You can specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.

    :param dashboard_names: The dashboards to be deleted. This parameter is required.
    :type dashboard_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_insight_rules(request: web.Request, rule_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_insight_rules

    &lt;p&gt;Permanently deletes the specified Contributor Insights rules.&lt;/p&gt; &lt;p&gt;If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created might not be available.&lt;/p&gt;

    :param rule_names: An array of the rule names to delete. If you need to find out the names of your rules, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html\&quot;&gt;DescribeInsightRules&lt;/a&gt;.
    :type rule_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_delete_metric_stream(request: web.Request, name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_delete_metric_stream

    Permanently deletes the metric stream that you specify.

    :param name: The name of the metric stream to delete.
    :type name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_describe_alarm_history(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, alarm_name=None, alarm_types=None, history_item_type=None, start_date=None, end_date=None, max_records=None, next_token=None, scan_by=None) -> web.Response:
    """g_et_describe_alarm_history

    &lt;p&gt;Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for either all metric alarms or all composite alarms are returned.&lt;/p&gt; &lt;p&gt;CloudWatch retains the history of an alarm even if you delete the alarm.&lt;/p&gt; &lt;p&gt;To use this operation and return information about a composite alarm, you must be signed on with the &lt;code&gt;cloudwatch:DescribeAlarmHistory&lt;/code&gt; permission that is scoped to &lt;code&gt;*&lt;/code&gt;. You can&#39;t return information about composite alarms if your &lt;code&gt;cloudwatch:DescribeAlarmHistory&lt;/code&gt; permission has a narrower scope.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param alarm_name: The name of the alarm.
    :type alarm_name: str
    :param alarm_types: Use this parameter to specify whether you want the operation to return metric alarms or composite alarms. If you omit this parameter, only metric alarms are returned.
    :type alarm_types: list | bytes
    :param history_item_type: The type of alarm histories to retrieve.
    :type history_item_type: str
    :param start_date: The starting date to retrieve alarm history.
    :type start_date: str
    :param end_date: The ending date to retrieve alarm history.
    :type end_date: str
    :param max_records: The maximum number of alarm history records to retrieve.
    :type max_records: int
    :param next_token: The token returned by a previous call to indicate that there is more data available.
    :type next_token: str
    :param scan_by: Specified whether to return the newest or oldest alarm history first. Specify &lt;code&gt;TimestampDescending&lt;/code&gt; to have the newest event history returned first, and specify &lt;code&gt;TimestampAscending&lt;/code&gt; to have the oldest history returned first.
    :type scan_by: str

    """
    alarm_types = [AlarmType.from_dict(d) for d in alarm_types]
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def g_et_describe_alarms(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, alarm_names=None, alarm_name_prefix=None, alarm_types=None, children_of_alarm_name=None, parents_of_alarm_name=None, state_value=None, action_prefix=None, max_records=None, next_token=None) -> web.Response:
    """g_et_describe_alarms

    &lt;p&gt;Retrieves the specified alarms. You can filter the results by specifying a prefix for the alarm name, the alarm state, or a prefix for any action.&lt;/p&gt; &lt;p&gt;To use this operation and return information about composite alarms, you must be signed on with the &lt;code&gt;cloudwatch:DescribeAlarms&lt;/code&gt; permission that is scoped to &lt;code&gt;*&lt;/code&gt;. You can&#39;t return information about composite alarms if your &lt;code&gt;cloudwatch:DescribeAlarms&lt;/code&gt; permission has a narrower scope.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param alarm_names: The names of the alarms to retrieve information about.
    :type alarm_names: List[str]
    :param alarm_name_prefix: &lt;p&gt;An alarm name prefix. If you specify this parameter, you receive information about all alarms that have names that start with this prefix.&lt;/p&gt; &lt;p&gt;If this parameter is specified, you cannot specify &lt;code&gt;AlarmNames&lt;/code&gt;.&lt;/p&gt;
    :type alarm_name_prefix: str
    :param alarm_types: Use this parameter to specify whether you want the operation to return metric alarms or composite alarms. If you omit this parameter, only metric alarms are returned.
    :type alarm_types: list | bytes
    :param children_of_alarm_name: &lt;p&gt;If you use this parameter and specify the name of a composite alarm, the operation returns information about the \&quot;children\&quot; alarms of the alarm you specify. These are the metric alarms and composite alarms referenced in the &lt;code&gt;AlarmRule&lt;/code&gt; field of the composite alarm that you specify in &lt;code&gt;ChildrenOfAlarmName&lt;/code&gt;. Information about the composite alarm that you name in &lt;code&gt;ChildrenOfAlarmName&lt;/code&gt; is not returned.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;ChildrenOfAlarmName&lt;/code&gt;, you cannot specify any other parameters in the request except for &lt;code&gt;MaxRecords&lt;/code&gt; and &lt;code&gt;NextToken&lt;/code&gt;. If you do so, you receive a validation error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the &lt;code&gt;Alarm Name&lt;/code&gt;, &lt;code&gt;ARN&lt;/code&gt;, &lt;code&gt;StateValue&lt;/code&gt; (OK/ALARM/INSUFFICIENT_DATA), and &lt;code&gt;StateUpdatedTimestamp&lt;/code&gt; information are returned by this operation when you use this parameter. To get complete information about these alarms, perform another &lt;code&gt;DescribeAlarms&lt;/code&gt; operation and specify the parent alarm names in the &lt;code&gt;AlarmNames&lt;/code&gt; parameter.&lt;/p&gt; &lt;/note&gt;
    :type children_of_alarm_name: str
    :param parents_of_alarm_name: &lt;p&gt;If you use this parameter and specify the name of a metric or composite alarm, the operation returns information about the \&quot;parent\&quot; alarms of the alarm you specify. These are the composite alarms that have &lt;code&gt;AlarmRule&lt;/code&gt; parameters that reference the alarm named in &lt;code&gt;ParentsOfAlarmName&lt;/code&gt;. Information about the alarm that you specify in &lt;code&gt;ParentsOfAlarmName&lt;/code&gt; is not returned.&lt;/p&gt; &lt;p&gt;If you specify &lt;code&gt;ParentsOfAlarmName&lt;/code&gt;, you cannot specify any other parameters in the request except for &lt;code&gt;MaxRecords&lt;/code&gt; and &lt;code&gt;NextToken&lt;/code&gt;. If you do so, you receive a validation error.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the Alarm Name and ARN are returned by this operation when you use this parameter. To get complete information about these alarms, perform another &lt;code&gt;DescribeAlarms&lt;/code&gt; operation and specify the parent alarm names in the &lt;code&gt;AlarmNames&lt;/code&gt; parameter.&lt;/p&gt; &lt;/note&gt;
    :type parents_of_alarm_name: str
    :param state_value: Specify this parameter to receive information only about alarms that are currently in the state that you specify.
    :type state_value: str
    :param action_prefix: Use this parameter to filter the results of the operation to only those alarms that use a certain alarm action. For example, you could specify the ARN of an SNS topic to find all alarms that send notifications to that topic.
    :type action_prefix: str
    :param max_records: The maximum number of alarm descriptions to retrieve.
    :type max_records: int
    :param next_token: The token returned by a previous call to indicate that there is more data available.
    :type next_token: str

    """
    alarm_types = [AlarmType.from_dict(d) for d in alarm_types]
    return web.Response(status=200)


async def g_et_describe_alarms_for_metric(request: web.Request, metric_name, namespace, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, statistic=None, extended_statistic=None, dimensions=None, period=None, unit=None) -> web.Response:
    """g_et_describe_alarms_for_metric

    &lt;p&gt;Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.&lt;/p&gt; &lt;p&gt;This operation retrieves only standard alarms that are based on the specified metric. It does not return alarms based on math expressions that use the specified metric, or composite alarms that use the specified metric.&lt;/p&gt;

    :param metric_name: The name of the metric.
    :type metric_name: str
    :param namespace: The namespace of the metric.
    :type namespace: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param statistic: The statistic for the metric, other than percentiles. For percentile statistics, use &lt;code&gt;ExtendedStatistics&lt;/code&gt;.
    :type statistic: str
    :param extended_statistic: The percentile statistic for the metric. Specify a value between p0.0 and p100.
    :type extended_statistic: str
    :param dimensions: The dimensions associated with the metric. If the metric has any associated dimensions, you must specify them in order for the call to succeed.
    :type dimensions: list | bytes
    :param period: The period, in seconds, over which the statistic is applied.
    :type period: int
    :param unit: The unit for the metric.
    :type unit: str

    """
    dimensions = [Dimension.from_dict(d) for d in dimensions]
    return web.Response(status=200)


async def g_et_describe_anomaly_detectors(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, namespace=None, metric_name=None, dimensions=None, anomaly_detector_types=None) -> web.Response:
    """g_et_describe_anomaly_detectors

    Lists the anomaly detection models that you have created in your account. For single metric anomaly detectors, you can list all of the models in your account or filter the results to only the models that are related to a certain namespace, metric name, or metric dimension. For metric math anomaly detectors, you can list them by adding &lt;code&gt;METRIC_MATH&lt;/code&gt; to the &lt;code&gt;AnomalyDetectorTypes&lt;/code&gt; array. This will return all metric math anomaly detectors in your account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Use the token returned by the previous operation to request the next page of results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return in one operation. The maximum value that you can specify is 100.&lt;/p&gt; &lt;p&gt;To retrieve the remaining results, make another call with the returned &lt;code&gt;NextToken&lt;/code&gt; value. &lt;/p&gt;
    :type max_results: int
    :param namespace: Limits the results to only the anomaly detection models that are associated with the specified namespace.
    :type namespace: str
    :param metric_name: Limits the results to only the anomaly detection models that are associated with the specified metric name. If there are multiple metrics with this name in different namespaces that have anomaly detection models, they&#39;re all returned.
    :type metric_name: str
    :param dimensions: Limits the results to only the anomaly detection models that are associated with the specified metric dimensions. If there are multiple metrics that have these dimensions and have anomaly detection models associated, they&#39;re all returned.
    :type dimensions: list | bytes
    :param anomaly_detector_types: The anomaly detector types to request when using &lt;code&gt;DescribeAnomalyDetectorsInput&lt;/code&gt;. If empty, defaults to &lt;code&gt;SINGLE_METRIC&lt;/code&gt;.
    :type anomaly_detector_types: list | bytes

    """
    dimensions = [Dimension.from_dict(d) for d in dimensions]
    anomaly_detector_types = [AnomalyDetectorType.from_dict(d) for d in anomaly_detector_types]
    return web.Response(status=200)


async def g_et_describe_insight_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """g_et_describe_insight_rules

    &lt;p&gt;Returns a list of all the Contributor Insights rules in your account.&lt;/p&gt; &lt;p&gt;For more information about Contributor Insights, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html\&quot;&gt;Using Contributor Insights to Analyze High-Cardinality Data&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Include this value, if it was returned by the previous operation, to get the next set of rules.
    :type next_token: str
    :param max_results: The maximum number of results to return in one operation. If you omit this parameter, the default of 500 is used.
    :type max_results: int

    """
    return web.Response(status=200)


async def g_et_disable_alarm_actions(request: web.Request, alarm_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_disable_alarm_actions

    Disables the actions for the specified alarms. When an alarm&#39;s actions are disabled, the alarm actions do not execute when the alarm state changes.

    :param alarm_names: The names of the alarms.
    :type alarm_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_disable_insight_rules(request: web.Request, rule_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_disable_insight_rules

    Disables the specified Contributor Insights rules. When rules are disabled, they do not analyze log groups and do not incur costs.

    :param rule_names: An array of the rule names to disable. If you need to find out the names of your rules, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html\&quot;&gt;DescribeInsightRules&lt;/a&gt;.
    :type rule_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_enable_alarm_actions(request: web.Request, alarm_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_enable_alarm_actions

    Enables the actions for the specified alarms.

    :param alarm_names: The names of the alarms.
    :type alarm_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_enable_insight_rules(request: web.Request, rule_names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_enable_insight_rules

    Enables the specified Contributor Insights rules. When rules are enabled, they immediately begin analyzing log data.

    :param rule_names: An array of the rule names to enable. If you need to find out the names of your rules, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeInsightRules.html\&quot;&gt;DescribeInsightRules&lt;/a&gt;.
    :type rule_names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_dashboard(request: web.Request, dashboard_name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_dashboard

    &lt;p&gt;Displays the details of the dashboard that you specify.&lt;/p&gt; &lt;p&gt;To copy an existing dashboard, use &lt;code&gt;GetDashboard&lt;/code&gt;, and then use the data returned within &lt;code&gt;DashboardBody&lt;/code&gt; as the template for the new dashboard when you call &lt;code&gt;PutDashboard&lt;/code&gt; to create the copy.&lt;/p&gt;

    :param dashboard_name: The name of the dashboard to be described.
    :type dashboard_name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_insight_rule_report(request: web.Request, rule_name, start_time, end_time, period, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_contributor_count=None, metrics=None, order_by=None) -> web.Response:
    """g_et_get_insight_rule_report

    &lt;p&gt;This operation returns the time series data collected by a Contributor Insights rule. The data includes the identity and number of contributors to the log group.&lt;/p&gt; &lt;p&gt;You can also optionally return one or more statistics about each data point in the time series. These statistics can include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UniqueContributors&lt;/code&gt; -- the number of unique contributors for each data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MaxContributorValue&lt;/code&gt; -- the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph.&lt;/p&gt; &lt;p&gt;If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule&#39;s &lt;code&gt;Value&lt;/code&gt;, during that period.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SampleCount&lt;/code&gt; -- the number of data points matched by the rule.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Sum&lt;/code&gt; -- the sum of the values from all contributors during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Minimum&lt;/code&gt; -- the minimum value from a single observation during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Maximum&lt;/code&gt; -- the maximum value from a single observation during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Average&lt;/code&gt; -- the average value from all contributors during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param rule_name: The name of the rule that you want to see data from.
    :type rule_name: str
    :param start_time: The start time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as &lt;code&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss&lt;/code&gt;. For example, &lt;code&gt;2019-07-01T23:59:59&lt;/code&gt;.
    :type start_time: str
    :param end_time: The end time of the data to use in the report. When used in a raw HTTP Query API, it is formatted as &lt;code&gt;yyyy-MM-dd&#39;T&#39;HH:mm:ss&lt;/code&gt;. For example, &lt;code&gt;2019-07-01T23:59:59&lt;/code&gt;.
    :type end_time: str
    :param period: The period, in seconds, to use for the statistics in the &lt;code&gt;InsightRuleMetricDatapoint&lt;/code&gt; results.
    :type period: int
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_contributor_count: The maximum number of contributors to include in the report. The range is 1 to 100. If you omit this, the default of 10 is used.
    :type max_contributor_count: int
    :param metrics: &lt;p&gt;Specifies which metrics to use for aggregation of contributor values for the report. You can specify one or more of the following metrics:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UniqueContributors&lt;/code&gt; -- the number of unique contributors for each data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MaxContributorValue&lt;/code&gt; -- the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph.&lt;/p&gt; &lt;p&gt;If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule&#39;s &lt;code&gt;Value&lt;/code&gt;, during that period.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SampleCount&lt;/code&gt; -- the number of data points matched by the rule.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Sum&lt;/code&gt; -- the sum of the values from all contributors during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Minimum&lt;/code&gt; -- the minimum value from a single observation during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Maximum&lt;/code&gt; -- the maximum value from a single observation during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Average&lt;/code&gt; -- the average value from all contributors during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type metrics: List[str]
    :param order_by: Determines what statistic to use to rank the contributors. Valid values are SUM and MAXIMUM.
    :type order_by: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    return web.Response(status=200)


async def g_et_get_metric_data(request: web.Request, metric_data_queries, start_time, end_time, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, scan_by=None, max_datapoints=None, label_options=None) -> web.Response:
    """g_et_get_metric_data

    &lt;p&gt;You can use the &lt;code&gt;GetMetricData&lt;/code&gt; API to retrieve CloudWatch metric values. The operation can also include a CloudWatch Metrics Insights query, and one or more metric math functions.&lt;/p&gt; &lt;p&gt;A &lt;code&gt;GetMetricData&lt;/code&gt; operation that does not include a query can retrieve as many as 500 different metrics in a single request, with a total of as many as 100,800 data points. You can also optionally perform metric math expressions on the values of the returned statistics, to create new time series that represent new insights into your data. For example, using Lambda metrics, you could divide the Errors metric by the Invocations metric to get an error rate time series. For more information about metric math expressions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax\&quot;&gt;Metric Math Syntax and Functions&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you include a Metrics Insights query, each &lt;code&gt;GetMetricData&lt;/code&gt; operation can include only one query. But the same &lt;code&gt;GetMetricData&lt;/code&gt; operation can also retrieve other metrics. Metrics Insights queries can query only the most recent three hours of metric data. For more information about Metrics Insights, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html\&quot;&gt;Query your metrics with CloudWatch Metrics Insights&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Calls to the &lt;code&gt;GetMetricData&lt;/code&gt; API have a different pricing structure than calls to &lt;code&gt;GetMetricStatistics&lt;/code&gt;. For more information about pricing, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Amazon CloudWatch retains metric data as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a &lt;code&gt;StorageResolution&lt;/code&gt; of 1.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 60 seconds (1-minute) are available for 15 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 300 seconds (5-minute) are available for 63 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.&lt;/p&gt; &lt;p&gt;If you omit &lt;code&gt;Unit&lt;/code&gt; in your request, all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Using Metrics Insights queries with metric math&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can&#39;t mix a Metric Insights query and metric math syntax in the same expression, but you can reference results from a Metrics Insights query within other Metric math expressions. A Metrics Insights query without a &lt;b&gt;GROUP BY&lt;/b&gt; clause returns a single time-series (TS), and can be used as input for a metric math expression that expects a single time series. A Metrics Insights query with a &lt;b&gt;GROUP BY&lt;/b&gt; clause returns an array of time-series (TS[]), and can be used as input for a metric math expression that expects an array of time series. &lt;/p&gt;

    :param metric_data_queries: The metric queries to be returned. A single &lt;code&gt;GetMetricData&lt;/code&gt; call can include as many as 500 &lt;code&gt;MetricDataQuery&lt;/code&gt; structures. Each of these structures can specify either a metric to retrieve, a Metrics Insights query, or a math expression to perform on retrieved data. 
    :type metric_data_queries: list | bytes
    :param start_time: &lt;p&gt;The time stamp indicating the earliest data to be returned.&lt;/p&gt; &lt;p&gt;The value specified is inclusive; results include data points with the specified time stamp. &lt;/p&gt; &lt;p&gt;CloudWatch rounds the specified time stamp as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you set &lt;code&gt;Period&lt;/code&gt; to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. &lt;/p&gt; &lt;p&gt;For better performance, specify &lt;code&gt;StartTime&lt;/code&gt; and &lt;code&gt;EndTime&lt;/code&gt; values that align with the value of the metric&#39;s &lt;code&gt;Period&lt;/code&gt; and sync up with the beginning and end of an hour. For example, if the &lt;code&gt;Period&lt;/code&gt; of a metric is 5 minutes, specifying 12:05 or 12:30 as &lt;code&gt;StartTime&lt;/code&gt; can get a faster response from CloudWatch than setting 12:07 or 12:29 as the &lt;code&gt;StartTime&lt;/code&gt;.&lt;/p&gt;
    :type start_time: str
    :param end_time: &lt;p&gt;The time stamp indicating the latest data to be returned.&lt;/p&gt; &lt;p&gt;The value specified is exclusive; results include data points up to the specified time stamp.&lt;/p&gt; &lt;p&gt;For better performance, specify &lt;code&gt;StartTime&lt;/code&gt; and &lt;code&gt;EndTime&lt;/code&gt; values that align with the value of the metric&#39;s &lt;code&gt;Period&lt;/code&gt; and sync up with the beginning and end of an hour. For example, if the &lt;code&gt;Period&lt;/code&gt; of a metric is 5 minutes, specifying 12:05 or 12:30 as &lt;code&gt;EndTime&lt;/code&gt; can get a faster response from CloudWatch than setting 12:07 or 12:29 as the &lt;code&gt;EndTime&lt;/code&gt;.&lt;/p&gt;
    :type end_time: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Include this value, if it was returned by the previous &lt;code&gt;GetMetricData&lt;/code&gt; operation, to get the next set of data points.
    :type next_token: str
    :param scan_by: The order in which data points should be returned. &lt;code&gt;TimestampDescending&lt;/code&gt; returns the newest data first and paginates when the &lt;code&gt;MaxDatapoints&lt;/code&gt; limit is reached. &lt;code&gt;TimestampAscending&lt;/code&gt; returns the oldest data first and paginates when the &lt;code&gt;MaxDatapoints&lt;/code&gt; limit is reached.
    :type scan_by: str
    :param max_datapoints: The maximum number of data points the request should return before paginating. If you omit this, the default of 100,800 is used.
    :type max_datapoints: int
    :param label_options: This structure includes the &lt;code&gt;Timezone&lt;/code&gt; parameter, which you can use to specify your time zone so that the labels of returned data display the correct time for your time zone. 
    :type label_options: dict | bytes

    """
    metric_data_queries = [MetricDataQuery.from_dict(d) for d in metric_data_queries]
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    label_options = .from_dict(label_options)
    return web.Response(status=200)


async def g_et_get_metric_statistics(request: web.Request, namespace, metric_name, start_time, end_time, period, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, dimensions=None, statistics=None, extended_statistics=None, unit=None) -> web.Response:
    """g_et_get_metric_statistics

    &lt;p&gt;Gets statistics for the specified metric.&lt;/p&gt; &lt;p&gt;The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.&lt;/p&gt; &lt;p&gt;CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.&lt;/p&gt; &lt;p&gt;CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The SampleCount value of the statistic set is 1.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Min and the Max values of the statistic set are equal.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Percentile statistics are not available for metrics when any of the metric values are negative numbers.&lt;/p&gt; &lt;p&gt;Amazon CloudWatch retains metric data as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a &lt;code&gt;StorageResolution&lt;/code&gt; of 1.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 60 seconds (1-minute) are available for 15 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 300 seconds (5-minute) are available for 63 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.&lt;/p&gt; &lt;p&gt;CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.&lt;/p&gt; &lt;p&gt;For information about metrics and dimensions supported by Amazon Web Services services, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html\&quot;&gt;Amazon CloudWatch Metrics and Dimensions Reference&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.&lt;/p&gt;

    :param namespace: The namespace of the metric, with or without spaces.
    :type namespace: str
    :param metric_name: The name of the metric, with or without spaces.
    :type metric_name: str
    :param start_time: &lt;p&gt;The time stamp that determines the first data point to return. Start times are evaluated relative to the time that CloudWatch receives the request.&lt;/p&gt; &lt;p&gt;The value specified is inclusive; results include data points with the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-03T23:00:00Z).&lt;/p&gt; &lt;p&gt;CloudWatch rounds the specified time stamp as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Start time less than 15 days ago - Round down to the nearest whole minute. For example, 12:32:34 is rounded down to 12:32:00.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start time between 15 and 63 days ago - Round down to the nearest 5-minute clock interval. For example, 12:32:34 is rounded down to 12:30:00.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start time greater than 63 days ago - Round down to the nearest 1-hour clock interval. For example, 12:32:34 is rounded down to 12:00:00.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you set &lt;code&gt;Period&lt;/code&gt; to 5, 10, or 30, the start time of your request is rounded down to the nearest time that corresponds to even 5-, 10-, or 30-second divisions of a minute. For example, if you make a query at (HH:mm:ss) 01:05:23 for the previous 10-second period, the start time of your request is rounded down and you receive data from 01:05:10 to 01:05:20. If you make a query at 15:07:17 for the previous 5 minutes of data, using a period of 5 seconds, you receive data timestamped between 15:02:15 and 15:07:15. &lt;/p&gt;
    :type start_time: str
    :param end_time: &lt;p&gt;The time stamp that determines the last data point to return.&lt;/p&gt; &lt;p&gt;The value specified is exclusive; results include data points up to the specified time stamp. In a raw HTTP query, the time stamp must be in ISO 8601 UTC format (for example, 2016-10-10T23:00:00Z).&lt;/p&gt;
    :type end_time: str
    :param period: &lt;p&gt;The granularity, in seconds, of the returned data points. For metrics with regular resolution, a period can be as short as one minute (60 seconds) and must be a multiple of 60. For high-resolution metrics that are collected at intervals of less than one minute, the period can be 1, 5, 10, 30, 60, or any multiple of 60. High-resolution metrics are those metrics stored by a &lt;code&gt;PutMetricData&lt;/code&gt; call that includes a &lt;code&gt;StorageResolution&lt;/code&gt; of 1 second.&lt;/p&gt; &lt;p&gt;If the &lt;code&gt;StartTime&lt;/code&gt; parameter specifies a time stamp that is greater than 3 hours ago, you must specify the period as follows or no data points in that time range is returned:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds (1 minute).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5 minutes).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Start time greater than 63 days ago - Use a multiple of 3600 seconds (1 hour).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type period: int
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param dimensions: The dimensions. If the metric contains multiple dimensions, you must include a value for each dimension. CloudWatch treats each unique combination of dimensions as a separate metric. If a specific combination of dimensions was not published, you can&#39;t retrieve statistics for it. You must specify the same dimensions that were used when the metrics were created. For an example, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#dimension-combinations\&quot;&gt;Dimension Combinations&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;. For more information about specifying dimensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html\&quot;&gt;Publishing Metrics&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.
    :type dimensions: list | bytes
    :param statistics: The metric statistics, other than percentile. For percentile statistics, use &lt;code&gt;ExtendedStatistics&lt;/code&gt;. When calling &lt;code&gt;GetMetricStatistics&lt;/code&gt;, you must specify either &lt;code&gt;Statistics&lt;/code&gt; or &lt;code&gt;ExtendedStatistics&lt;/code&gt;, but not both.
    :type statistics: list | bytes
    :param extended_statistics: The percentile statistics. Specify values between p0.0 and p100. When calling &lt;code&gt;GetMetricStatistics&lt;/code&gt;, you must specify either &lt;code&gt;Statistics&lt;/code&gt; or &lt;code&gt;ExtendedStatistics&lt;/code&gt;, but not both. Percentile statistics are not available for metrics when any of the metric values are negative numbers.
    :type extended_statistics: List[str]
    :param unit: The unit for a given metric. If you omit &lt;code&gt;Unit&lt;/code&gt;, all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.
    :type unit: str

    """
    start_time = util.deserialize_datetime(start_time)
    end_time = util.deserialize_datetime(end_time)
    dimensions = [Dimension.from_dict(d) for d in dimensions]
    statistics = [Statistic.from_dict(d) for d in statistics]
    return web.Response(status=200)


async def g_et_get_metric_stream(request: web.Request, name, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_get_metric_stream

    Returns information about the metric stream that you specify.

    :param name: The name of the metric stream to retrieve information about.
    :type name: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_get_metric_widget_image(request: web.Request, metric_widget, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, output_format=None) -> web.Response:
    """g_et_get_metric_widget_image

    &lt;p&gt;You can use the &lt;code&gt;GetMetricWidgetImage&lt;/code&gt; API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard.&lt;/p&gt; &lt;p&gt;The graph you retrieve can include all CloudWatch metric graph features, including metric math and horizontal and vertical annotations.&lt;/p&gt; &lt;p&gt;There is a limit of 20 transactions per second for this API. Each &lt;code&gt;GetMetricWidgetImage&lt;/code&gt; action has the following limits:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;As many as 100 metrics in the graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Up to 100 KB uncompressed payload.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param metric_widget: &lt;p&gt;A JSON string that defines the bitmap graph to be retrieved. The string includes the metrics to include in the graph, statistics, annotations, title, axis limits, and so on. You can include only one &lt;code&gt;MetricWidget&lt;/code&gt; parameter in each &lt;code&gt;GetMetricWidgetImage&lt;/code&gt; call.&lt;/p&gt; &lt;p&gt;For more information about the syntax of &lt;code&gt;MetricWidget&lt;/code&gt; see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Metric-Widget-Structure.html\&quot;&gt;GetMetricWidgetImage: Metric Widget Structure and Syntax&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If any metric on the graph could not load all the requested data points, an orange triangle with an exclamation point appears next to the graph legend.&lt;/p&gt;
    :type metric_widget: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param output_format: &lt;p&gt;The format of the resulting image. Only PNG images are supported.&lt;/p&gt; &lt;p&gt;The default is &lt;code&gt;png&lt;/code&gt;. If you specify &lt;code&gt;png&lt;/code&gt;, the API returns an HTTP response with the content-type set to &lt;code&gt;text/xml&lt;/code&gt;. The image data is in a &lt;code&gt;MetricWidgetImage&lt;/code&gt; field. For example:&lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;GetMetricWidgetImageResponse xmlns&#x3D;&amp;lt;URLstring&amp;gt;&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;GetMetricWidgetImageResult&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;MetricWidgetImage&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;/MetricWidgetImage&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;/GetMetricWidgetImageResult&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;ResponseMetadata&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;RequestId&amp;gt;6f0d4192-4d42-11e8-82c1-f539a07e0e3b&amp;lt;/RequestId&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt; &amp;lt;/ResponseMetadata&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;&amp;lt;/GetMetricWidgetImageResponse&amp;gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The &lt;code&gt;image/png&lt;/code&gt; setting is intended only for custom HTTP requests. For most use cases, and all actions using an Amazon Web Services SDK, you should use &lt;code&gt;png&lt;/code&gt;. If you specify &lt;code&gt;image/png&lt;/code&gt;, the HTTP response has a content-type set to &lt;code&gt;image/png&lt;/code&gt;, and the body of the response is a PNG image. &lt;/p&gt;
    :type output_format: str

    """
    return web.Response(status=200)


async def g_et_list_dashboards(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, dashboard_name_prefix=None, next_token=None) -> web.Response:
    """g_et_list_dashboards

    &lt;p&gt;Returns a list of the dashboards for your account. If you include &lt;code&gt;DashboardNamePrefix&lt;/code&gt;, only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed. &lt;/p&gt; &lt;p&gt; &lt;code&gt;ListDashboards&lt;/code&gt; returns up to 1000 results on one page. If there are more than 1000 dashboards, you can call &lt;code&gt;ListDashboards&lt;/code&gt; again and include the value you received for &lt;code&gt;NextToken&lt;/code&gt; in the first call, to receive the next 1000 results.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param dashboard_name_prefix: If you specify this parameter, only the dashboards with names starting with the specified string are listed. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, \&quot;.\&quot;, \&quot;-\&quot;, and \&quot;_\&quot;. 
    :type dashboard_name_prefix: str
    :param next_token: The token returned by a previous call to indicate that there is more data available.
    :type next_token: str

    """
    return web.Response(status=200)


async def g_et_list_managed_insight_rules(request: web.Request, resource_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """g_et_list_managed_insight_rules

     Returns a list that contains the number of managed Contributor Insights rules in your account. 

    :param resource_arn:  The ARN of an Amazon Web Services resource that has managed Contributor Insights rules. 
    :type resource_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token:  Include this value to get the next set of rules if the value was returned by the previous operation. 
    :type next_token: str
    :param max_results:  The maximum number of results to return in one operation. If you omit this parameter, the default number is used. The default number is &lt;code&gt;100&lt;/code&gt;. 
    :type max_results: int

    """
    return web.Response(status=200)


async def g_et_list_metric_streams(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """g_et_list_metric_streams

    Returns a list of metric streams in this account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Include this value, if it was returned by the previous call, to get the next set of metric streams.
    :type next_token: str
    :param max_results: The maximum number of results to return in one operation.
    :type max_results: int

    """
    return web.Response(status=200)


async def g_et_list_metrics(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, namespace=None, metric_name=None, dimensions=None, next_token=None, recently_active=None, include_linked_accounts=None, owning_account=None) -> web.Response:
    """g_et_list_metrics

    &lt;p&gt;List the specified metrics. You can use the returned metrics with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt; to get statistical data.&lt;/p&gt; &lt;p&gt;Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls.&lt;/p&gt; &lt;p&gt;After you create a metric, allow up to 15 minutes for the metric to appear. To see metric statistics sooner, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view metrics from the linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListMetrics&lt;/code&gt; doesn&#39;t return information about metrics if those metrics haven&#39;t reported data in the past two weeks. To retrieve those metrics, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param namespace: The metric namespace to filter against. Only the namespace that matches exactly will be returned.
    :type namespace: str
    :param metric_name: The name of the metric to filter against. Only the metrics with names that match exactly will be returned.
    :type metric_name: str
    :param dimensions: The dimensions to filter against. Only the dimensions that match exactly will be returned.
    :type dimensions: list | bytes
    :param next_token: The token returned by a previous call to indicate that there is more data available.
    :type next_token: str
    :param recently_active: &lt;p&gt;To filter the results to show only metrics that have had data points published in the past three hours, specify this parameter with a value of &lt;code&gt;PT3H&lt;/code&gt;. This is the only valid value for this parameter.&lt;/p&gt; &lt;p&gt;The results that are returned are an approximation of the value you specify. There is a low probability that the returned results include metrics with last published data as much as 40 minutes more than the specified time interval.&lt;/p&gt;
    :type recently_active: str
    :param include_linked_accounts: &lt;p&gt;If you are using this operation in a monitoring account, specify &lt;code&gt;true&lt;/code&gt; to include metrics from source accounts in the returned data.&lt;/p&gt; &lt;p&gt;The default is &lt;code&gt;false&lt;/code&gt;.&lt;/p&gt;
    :type include_linked_accounts: bool
    :param owning_account: When you use this operation in a monitoring account, use this field to return metrics only from one source account. To do so, specify that source account ID in this field, and also specify &lt;code&gt;true&lt;/code&gt; for &lt;code&gt;IncludeLinkedAccounts&lt;/code&gt;.
    :type owning_account: str

    """
    dimensions = [DimensionFilter.from_dict(d) for d in dimensions]
    return web.Response(status=200)


async def g_et_list_tags_for_resource(request: web.Request, resource_arn, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_list_tags_for_resource

    Displays the tags associated with a CloudWatch resource. Currently, alarms and Contributor Insights rules support tagging.

    :param resource_arn: &lt;p&gt;The ARN of the CloudWatch resource that you want to view tags for.&lt;/p&gt; &lt;p&gt;The ARN format of an alarm is &lt;code&gt;arn:aws:cloudwatch:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:alarm:&lt;i&gt;alarm-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a Contributor Insights rule is &lt;code&gt;arn:aws:cloudwatch:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:insight-rule:&lt;i&gt;insight-rule-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\&quot;&gt; Resource Types Defined by Amazon CloudWatch&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt;
    :type resource_arn: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_put_anomaly_detector(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, namespace=None, metric_name=None, dimensions=None, stat=None, configuration=None, single_metric_anomaly_detector=None, metric_math_anomaly_detector=None) -> web.Response:
    """g_et_put_anomaly_detector

    &lt;p&gt;Creates an anomaly detection model for a CloudWatch metric. You can use the model to display a band of expected normal values when the metric is graphed.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html\&quot;&gt;CloudWatch Anomaly Detection&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param namespace: The namespace of the metric to create the anomaly detection model for.
    :type namespace: str
    :param metric_name: The name of the metric to create the anomaly detection model for.
    :type metric_name: str
    :param dimensions: The metric dimensions to create the anomaly detection model for.
    :type dimensions: list | bytes
    :param stat: The statistic to use for the metric and the anomaly detection model.
    :type stat: str
    :param configuration: &lt;p&gt;The configuration specifies details about how the anomaly detection model is to be trained, including time ranges to exclude when training and updating the model. You can specify as many as 10 time ranges.&lt;/p&gt; &lt;p&gt;The configuration can also include the time zone to use for the metric.&lt;/p&gt;
    :type configuration: dict | bytes
    :param single_metric_anomaly_detector: &lt;p&gt;A single metric anomaly detector to be created.&lt;/p&gt; &lt;p&gt;When using &lt;code&gt;SingleMetricAnomalyDetector&lt;/code&gt;, you cannot include the following parameters in the same operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Dimensions&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MetricName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Namespace&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Stat&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;the &lt;code&gt;MetricMatchAnomalyDetector&lt;/code&gt; parameters of &lt;code&gt;PutAnomalyDetectorInput&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Instead, specify the single metric anomaly detector attributes as part of the property &lt;code&gt;SingleMetricAnomalyDetector&lt;/code&gt;.&lt;/p&gt;
    :type single_metric_anomaly_detector: dict | bytes
    :param metric_math_anomaly_detector: &lt;p&gt;The metric math anomaly detector to be created.&lt;/p&gt; &lt;p&gt;When using &lt;code&gt;MetricMathAnomalyDetector&lt;/code&gt;, you cannot include the following parameters in the same operation:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Dimensions&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MetricName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Namespace&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Stat&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;the &lt;code&gt;SingleMetricAnomalyDetector&lt;/code&gt; parameters of &lt;code&gt;PutAnomalyDetectorInput&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Instead, specify the metric math anomaly detector attributes as part of the property &lt;code&gt;MetricMathAnomalyDetector&lt;/code&gt;.&lt;/p&gt;
    :type metric_math_anomaly_detector: dict | bytes

    """
    dimensions = [Dimension.from_dict(d) for d in dimensions]
    configuration = .from_dict(configuration)
    single_metric_anomaly_detector = .from_dict(single_metric_anomaly_detector)
    metric_math_anomaly_detector = .from_dict(metric_math_anomaly_detector)
    return web.Response(status=200)


async def g_et_put_composite_alarm(request: web.Request, alarm_name, alarm_rule, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, actions_enabled=None, alarm_actions=None, alarm_description=None, insufficient_data_actions=None, ok_actions=None, tags=None, actions_suppressor=None, actions_suppressor_wait_period=None, actions_suppressor_extension_period=None) -> web.Response:
    """g_et_put_composite_alarm

    &lt;p&gt;Creates or updates a &lt;i&gt;composite alarm&lt;/i&gt;. When you create a composite alarm, you specify a rule expression for the alarm that takes into account the alarm states of other alarms that you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met.&lt;/p&gt; &lt;p&gt;The alarms specified in a composite alarm&#39;s rule expression can include metric alarms and other composite alarms. The rule expression of a composite alarm can include as many as 100 underlying alarms. Any single alarm can be included in the rule expressions of as many as 150 composite alarms.&lt;/p&gt; &lt;p&gt;Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create a composite alarm and set up alerts only for the composite alarm. For example, you could create a composite alarm that goes into ALARM state only when more than one of the underlying metric alarms are in ALARM state.&lt;/p&gt; &lt;p&gt;Currently, the only alarm actions that can be taken by composite alarms are notifying SNS topics.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can&#39;t delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.&lt;/p&gt; &lt;p&gt;To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the &lt;code&gt;AlarmRule&lt;/code&gt; of one of the alarms to &lt;code&gt;false&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;When this operation creates an alarm, the alarm state is immediately set to &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt;. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. For a composite alarm, this initial time after creation is the only time that the alarm can be in &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.&lt;/p&gt; &lt;p&gt;To use this operation, you must be signed on with the &lt;code&gt;cloudwatch:PutCompositeAlarm&lt;/code&gt; permission that is scoped to &lt;code&gt;*&lt;/code&gt;. You can&#39;t create a composite alarms if your &lt;code&gt;cloudwatch:PutCompositeAlarm&lt;/code&gt; permission has a narrower scope.&lt;/p&gt; &lt;p&gt;If you are an IAM user, you must have &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; to create a composite alarm that has Systems Manager OpsItem actions.&lt;/p&gt;

    :param alarm_name: The name for the composite alarm. This name must be unique within the Region.
    :type alarm_name: str
    :param alarm_rule: &lt;p&gt;An expression that specifies which other alarms are to be evaluated to determine this composite alarm&#39;s state. For each alarm that you reference, you designate a function that specifies whether that alarm needs to be in ALARM state, OK state, or INSUFFICIENT_DATA state. You can use operators (AND, OR and NOT) to combine multiple functions in a single expression. You can use parenthesis to logically group the functions in your expression.&lt;/p&gt; &lt;p&gt;You can use either alarm names or ARNs to reference the other alarms that are to be evaluated.&lt;/p&gt; &lt;p&gt;Functions can include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALARM(\&quot;&lt;i&gt;alarm-name&lt;/i&gt; or &lt;i&gt;alarm-ARN&lt;/i&gt;\&quot;)&lt;/code&gt; is TRUE if the named alarm is in ALARM state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;OK(\&quot;&lt;i&gt;alarm-name&lt;/i&gt; or &lt;i&gt;alarm-ARN&lt;/i&gt;\&quot;)&lt;/code&gt; is TRUE if the named alarm is in OK state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;INSUFFICIENT_DATA(\&quot;&lt;i&gt;alarm-name&lt;/i&gt; or &lt;i&gt;alarm-ARN&lt;/i&gt;\&quot;)&lt;/code&gt; is TRUE if the named alarm is in INSUFFICIENT_DATA state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TRUE&lt;/code&gt; always evaluates to TRUE.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;FALSE&lt;/code&gt; always evaluates to FALSE.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;TRUE and FALSE are useful for testing a complex &lt;code&gt;AlarmRule&lt;/code&gt; structure, and for testing your alarm actions.&lt;/p&gt; &lt;p&gt;Alarm names specified in &lt;code&gt;AlarmRule&lt;/code&gt; can be surrounded with double-quotes (\&quot;), but do not have to be.&lt;/p&gt; &lt;p&gt;The following are some examples of &lt;code&gt;AlarmRule&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALARM(CPUUtilizationTooHigh) AND ALARM(DiskReadOpsTooHigh)&lt;/code&gt; specifies that the composite alarm goes into ALARM state only if both CPUUtilizationTooHigh and DiskReadOpsTooHigh alarms are in ALARM state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALARM(CPUUtilizationTooHigh) AND NOT ALARM(DeploymentInProgress)&lt;/code&gt; specifies that the alarm goes to ALARM state if CPUUtilizationTooHigh is in ALARM state and DeploymentInProgress is not in ALARM state. This example reduces alarm noise during a known deployment window.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;(ALARM(CPUUtilizationTooHigh) OR ALARM(DiskReadOpsTooHigh)) AND OK(NetworkOutTooHigh)&lt;/code&gt; goes into ALARM state if CPUUtilizationTooHigh OR DiskReadOpsTooHigh is in ALARM state, and if NetworkOutTooHigh is in OK state. This provides another example of using a composite alarm to prevent noise. This rule ensures that you are not notified with an alarm action on high CPU or disk usage if a known network problem is also occurring.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The &lt;code&gt;AlarmRule&lt;/code&gt; can specify as many as 100 \&quot;children\&quot; alarms. The &lt;code&gt;AlarmRule&lt;/code&gt; expression can have as many as 500 elements. Elements are child alarms, TRUE or FALSE statements, and parentheses.&lt;/p&gt;
    :type alarm_rule: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state of the composite alarm. The default is &lt;code&gt;TRUE&lt;/code&gt;.
    :type actions_enabled: bool
    :param alarm_actions: &lt;p&gt;The actions to execute when this alarm transitions to the &lt;code&gt;ALARM&lt;/code&gt; state from any other state. Each action is specified as an Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;arn:aws:sns:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:&lt;i&gt;sns-topic-name&lt;/i&gt; &lt;/code&gt; | &lt;code&gt;arn:aws:ssm:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:opsitem:&lt;i&gt;severity&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;
    :type alarm_actions: List[str]
    :param alarm_description: The description for the composite alarm.
    :type alarm_description: str
    :param insufficient_data_actions: &lt;p&gt;The actions to execute when this alarm transitions to the &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt; state from any other state. Each action is specified as an Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;arn:aws:sns:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:&lt;i&gt;sns-topic-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;
    :type insufficient_data_actions: List[str]
    :param ok_actions: &lt;p&gt;The actions to execute when this alarm transitions to an &lt;code&gt;OK&lt;/code&gt; state from any other state. Each action is specified as an Amazon Resource Name (ARN).&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;arn:aws:sns:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:&lt;i&gt;sns-topic-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt;
    :type ok_actions: List[str]
    :param tags: &lt;p&gt;A list of key-value pairs to associate with the composite alarm. You can associate as many as 50 tags with an alarm.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt;
    :type tags: list | bytes
    :param actions_suppressor:  Actions will be suppressed if the suppressor alarm is in the &lt;code&gt;ALARM&lt;/code&gt; state. &lt;code&gt;ActionsSuppressor&lt;/code&gt; can be an AlarmName or an Amazon Resource Name (ARN) from an existing alarm. 
    :type actions_suppressor: str
    :param actions_suppressor_wait_period: &lt;p&gt; The maximum time in seconds that the composite alarm waits for the suppressor alarm to go into the &lt;code&gt;ALARM&lt;/code&gt; state. After this time, the composite alarm performs its actions. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;code&gt;WaitPeriod&lt;/code&gt; is required only when &lt;code&gt;ActionsSuppressor&lt;/code&gt; is specified. &lt;/p&gt; &lt;/important&gt;
    :type actions_suppressor_wait_period: int
    :param actions_suppressor_extension_period: &lt;p&gt; The maximum time in seconds that the composite alarm waits after suppressor alarm goes out of the &lt;code&gt;ALARM&lt;/code&gt; state. After this time, the composite alarm performs its actions. &lt;/p&gt; &lt;important&gt; &lt;p&gt; &lt;code&gt;ExtensionPeriod&lt;/code&gt; is required only when &lt;code&gt;ActionsSuppressor&lt;/code&gt; is specified. &lt;/p&gt; &lt;/important&gt;
    :type actions_suppressor_extension_period: int

    """
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_put_dashboard(request: web.Request, dashboard_name, dashboard_body, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_put_dashboard

    &lt;p&gt;Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here.&lt;/p&gt; &lt;p&gt;All dashboards in your account are global, not region-specific.&lt;/p&gt; &lt;p&gt;A simple way to create a dashboard using &lt;code&gt;PutDashboard&lt;/code&gt; is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use &lt;code&gt;GetDashboard&lt;/code&gt;, and then use the data returned within &lt;code&gt;DashboardBody&lt;/code&gt; as the template for the new dashboard when you call &lt;code&gt;PutDashboard&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When you create a dashboard with &lt;code&gt;PutDashboard&lt;/code&gt;, a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the &lt;code&gt;DashboardBody&lt;/code&gt; script or the CloudFormation template used to create the dashboard.&lt;/p&gt;

    :param dashboard_name: The name of the dashboard. If a dashboard with this name already exists, this call modifies that dashboard, replacing its current contents. Otherwise, a new dashboard is created. The maximum length is 255, and valid characters are A-Z, a-z, 0-9, \&quot;-\&quot;, and \&quot;_\&quot;. This parameter is required.
    :type dashboard_name: str
    :param dashboard_body: &lt;p&gt;The detailed information about the dashboard in JSON format, including the widgets to include and their location on the dashboard. This parameter is required.&lt;/p&gt; &lt;p&gt;For more information about the syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/CloudWatch-Dashboard-Body-Structure.html\&quot;&gt;Dashboard Body Structure and Syntax&lt;/a&gt;.&lt;/p&gt;
    :type dashboard_body: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_put_insight_rule(request: web.Request, rule_name, rule_definition, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, rule_state=None, tags=None) -> web.Response:
    """g_et_put_insight_rule

    &lt;p&gt;Creates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs log group, enabling you to find contributor data for the log events in that log group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html\&quot;&gt;Using Contributor Insights to Analyze High-Cardinality Data&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created might not be available.&lt;/p&gt;

    :param rule_name: A unique name for the rule.
    :type rule_name: str
    :param rule_definition: The definition of the rule, as a JSON object. For details on the valid syntax, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html\&quot;&gt;Contributor Insights Rule Syntax&lt;/a&gt;.
    :type rule_definition: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param rule_state: The state of the rule. Valid values are ENABLED and DISABLED.
    :type rule_state: str
    :param tags: &lt;p&gt;A list of key-value pairs to associate with the Contributor Insights rule. You can associate as many as 50 tags with a rule.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions, by granting a user permission to access or change only the resources that have certain tag values.&lt;/p&gt; &lt;p&gt;To be able to associate tags with a rule, you must have the &lt;code&gt;cloudwatch:TagResource&lt;/code&gt; permission in addition to the &lt;code&gt;cloudwatch:PutInsightRule&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;If you are using this operation to update an existing Contributor Insights rule, any tags you specify in this parameter are ignored. To change the tags of an existing rule, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;.&lt;/p&gt;
    :type tags: list | bytes

    """
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_put_managed_insight_rules(request: web.Request, managed_rules, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_put_managed_insight_rules

     Creates a managed Contributor Insights rule for a specified Amazon Web Services resource. When you enable a managed rule, you create a Contributor Insights rule that collects data from Amazon Web Services services. You cannot edit these rules with &lt;code&gt;PutInsightRule&lt;/code&gt;. The rules can be enabled, disabled, and deleted using &lt;code&gt;EnableInsightRules&lt;/code&gt;, &lt;code&gt;DisableInsightRules&lt;/code&gt;, and &lt;code&gt;DeleteInsightRules&lt;/code&gt;. If a previously created managed rule is currently disabled, a subsequent call to this API will re-enable it. Use &lt;code&gt;ListManagedInsightRules&lt;/code&gt; to describe all available rules. 

    :param managed_rules:  A list of &lt;code&gt;ManagedRules&lt;/code&gt; to enable. 
    :type managed_rules: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    managed_rules = [ManagedRule.from_dict(d) for d in managed_rules]
    return web.Response(status=200)


async def g_et_put_metric_alarm(request: web.Request, alarm_name, evaluation_periods, comparison_operator, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, alarm_description=None, actions_enabled=None, ok_actions=None, alarm_actions=None, insufficient_data_actions=None, metric_name=None, namespace=None, statistic=None, extended_statistic=None, dimensions=None, period=None, unit=None, datapoints_to_alarm=None, threshold=None, treat_missing_data=None, evaluate_low_sample_count_percentile=None, metrics=None, tags=None, threshold_metric_id=None) -> web.Response:
    """g_et_put_metric_alarm

    &lt;p&gt;Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, or Metrics Insights query. For more information about using a Metrics Insights query for an alarm, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html\&quot;&gt;Create alarms on Metrics Insights queries&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Alarms based on anomaly detection models cannot have Auto Scaling actions.&lt;/p&gt; &lt;p&gt;When this operation creates an alarm, the alarm state is immediately set to &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt;. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.&lt;/p&gt; &lt;p&gt;When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.&lt;/p&gt; &lt;p&gt;If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; permission for all alarms with EC2 actions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; permissions to create an alarm with Systems Manager OpsItem or response plan actions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The first time you create an alarm in the Amazon Web Services Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked roles are called &lt;code&gt;AWSServiceRoleForCloudWatchEvents&lt;/code&gt; and &lt;code&gt;AWSServiceRoleForCloudWatchAlarms_ActionSSM&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role\&quot;&gt;Amazon Web Services service-linked role&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each &lt;code&gt;PutMetricAlarm&lt;/code&gt; action has a maximum uncompressed payload of 120 KB.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Cross-account alarms&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can set an alarm on metrics in the current account, or in another account. To create a cross-account alarm that watches a metric in a different account, you must have completed the following pre-requisites:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The account where the metrics are located (the &lt;i&gt;sharing account&lt;/i&gt;) must already have a sharing role named &lt;b&gt;CloudWatch-CrossAccountSharingRole&lt;/b&gt;. If it does not already have this role, you must create it using the instructions in &lt;b&gt;Set up a sharing account&lt;/b&gt; in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\&quot;&gt; Cross-account cross-Region CloudWatch console&lt;/a&gt;. The policy for that role must grant access to the ID of the account where you are creating the alarm. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The account where you are creating the alarm (the &lt;i&gt;monitoring account&lt;/i&gt;) must already have a service-linked role named &lt;b&gt;AWSServiceRoleForCloudWatchCrossAccount&lt;/b&gt; to allow CloudWatch to assume the sharing role in the sharing account. If it does not, you must create it following the directions in &lt;b&gt;Set up a monitoring account&lt;/b&gt; in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\&quot;&gt; Cross-account cross-Region CloudWatch console&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param alarm_name: &lt;p&gt;The name for the alarm. This name must be unique within the Region.&lt;/p&gt; &lt;p&gt;The name must contain only UTF-8 characters, and can&#39;t contain ASCII control characters&lt;/p&gt;
    :type alarm_name: str
    :param evaluation_periods: &lt;p&gt;The number of periods over which data is compared to the specified threshold. If you are setting an alarm that requires that a number of consecutive data points be breaching to trigger the alarm, this value specifies that number. If you are setting an \&quot;M out of N\&quot; alarm, this value is the N.&lt;/p&gt; &lt;p&gt;An alarm&#39;s total current evaluation period can be no longer than one day, so this number multiplied by &lt;code&gt;Period&lt;/code&gt; cannot be more than 86,400 seconds.&lt;/p&gt;
    :type evaluation_periods: int
    :param comparison_operator: &lt;p&gt; The arithmetic operation to use when comparing the specified statistic and threshold. The specified statistic value is used as the first operand.&lt;/p&gt; &lt;p&gt;The values &lt;code&gt;LessThanLowerOrGreaterThanUpperThreshold&lt;/code&gt;, &lt;code&gt;LessThanLowerThreshold&lt;/code&gt;, and &lt;code&gt;GreaterThanUpperThreshold&lt;/code&gt; are used only for alarms based on anomaly detection models.&lt;/p&gt;
    :type comparison_operator: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param alarm_description: The description for the alarm.
    :type alarm_description: str
    :param actions_enabled: Indicates whether actions should be executed during any changes to the alarm state. The default is &lt;code&gt;TRUE&lt;/code&gt;.
    :type actions_enabled: bool
    :param ok_actions: &lt;p&gt;The actions to execute when this alarm transitions to an &lt;code&gt;OK&lt;/code&gt; state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:&lt;/p&gt; &lt;p&gt; &lt;b&gt;EC2 actions:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:stop&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:terminate&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:reboot&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:recover&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Stop/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Terminate/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Reboot/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Recover/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Autoscaling action:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:autoscaling:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:scalingPolicy:&lt;i&gt;policy-id&lt;/i&gt;:autoScalingGroupName/&lt;i&gt;group-friendly-name&lt;/i&gt;:policyName/&lt;i&gt;policy-friendly-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;SNS notification action:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:sns:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:&lt;i&gt;sns-topic-name&lt;/i&gt;:autoScalingGroupName/&lt;i&gt;group-friendly-name&lt;/i&gt;:policyName/&lt;i&gt;policy-friendly-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;SSM integration actions:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:ssm:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:opsitem:&lt;i&gt;severity&lt;/i&gt;#CATEGORY&#x3D;&lt;i&gt;category-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:ssm-incidents::&lt;i&gt;account-id&lt;/i&gt;:responseplan/&lt;i&gt;response-plan-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type ok_actions: List[str]
    :param alarm_actions: &lt;p&gt;The actions to execute when this alarm transitions to the &lt;code&gt;ALARM&lt;/code&gt; state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:&lt;/p&gt; &lt;p&gt; &lt;b&gt;EC2 actions:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:stop&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:terminate&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:reboot&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:recover&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Stop/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Terminate/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Reboot/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Recover/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Autoscaling action:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:autoscaling:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:scalingPolicy:&lt;i&gt;policy-id&lt;/i&gt;:autoScalingGroupName/&lt;i&gt;group-friendly-name&lt;/i&gt;:policyName/&lt;i&gt;policy-friendly-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;SNS notification action:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:sns:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:&lt;i&gt;sns-topic-name&lt;/i&gt;:autoScalingGroupName/&lt;i&gt;group-friendly-name&lt;/i&gt;:policyName/&lt;i&gt;policy-friendly-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;SSM integration actions:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:ssm:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:opsitem:&lt;i&gt;severity&lt;/i&gt;#CATEGORY&#x3D;&lt;i&gt;category-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:ssm-incidents::&lt;i&gt;account-id&lt;/i&gt;:responseplan/&lt;i&gt;response-plan-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type alarm_actions: List[str]
    :param insufficient_data_actions: &lt;p&gt;The actions to execute when this alarm transitions to the &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt; state from any other state. Each action is specified as an Amazon Resource Name (ARN). Valid values:&lt;/p&gt; &lt;p&gt; &lt;b&gt;EC2 actions:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:stop&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:terminate&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:reboot&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:automate:&lt;i&gt;region&lt;/i&gt;:ec2:recover&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Stop/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Terminate/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Reboot/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:swf:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:action/actions/AWS_EC2.InstanceId.Recover/1.0&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Autoscaling action:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:autoscaling:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:scalingPolicy:&lt;i&gt;policy-id&lt;/i&gt;:autoScalingGroupName/&lt;i&gt;group-friendly-name&lt;/i&gt;:policyName/&lt;i&gt;policy-friendly-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;SNS notification action:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:sns:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:&lt;i&gt;sns-topic-name&lt;/i&gt;:autoScalingGroupName/&lt;i&gt;group-friendly-name&lt;/i&gt;:policyName/&lt;i&gt;policy-friendly-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;SSM integration actions:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:ssm:&lt;i&gt;region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:opsitem:&lt;i&gt;severity&lt;/i&gt;#CATEGORY&#x3D;&lt;i&gt;category-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;arn:aws:ssm-incidents::&lt;i&gt;account-id&lt;/i&gt;:responseplan/&lt;i&gt;response-plan-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type insufficient_data_actions: List[str]
    :param metric_name: &lt;p&gt;The name for the metric associated with the alarm. For each &lt;code&gt;PutMetricAlarm&lt;/code&gt; operation, you must specify either &lt;code&gt;MetricName&lt;/code&gt; or a &lt;code&gt;Metrics&lt;/code&gt; array.&lt;/p&gt; &lt;p&gt;If you are creating an alarm based on a math expression, you cannot specify this parameter, or any of the &lt;code&gt;Dimensions&lt;/code&gt;, &lt;code&gt;Period&lt;/code&gt;, &lt;code&gt;Namespace&lt;/code&gt;, &lt;code&gt;Statistic&lt;/code&gt;, or &lt;code&gt;ExtendedStatistic&lt;/code&gt; parameters. Instead, you specify all this information in the &lt;code&gt;Metrics&lt;/code&gt; array.&lt;/p&gt;
    :type metric_name: str
    :param namespace: The namespace for the metric associated specified in &lt;code&gt;MetricName&lt;/code&gt;.
    :type namespace: str
    :param statistic: The statistic for the metric specified in &lt;code&gt;MetricName&lt;/code&gt;, other than percentile. For percentile statistics, use &lt;code&gt;ExtendedStatistic&lt;/code&gt;. When you call &lt;code&gt;PutMetricAlarm&lt;/code&gt; and specify a &lt;code&gt;MetricName&lt;/code&gt;, you must specify either &lt;code&gt;Statistic&lt;/code&gt; or &lt;code&gt;ExtendedStatistic,&lt;/code&gt; but not both.
    :type statistic: str
    :param extended_statistic: The percentile statistic for the metric specified in &lt;code&gt;MetricName&lt;/code&gt;. Specify a value between p0.0 and p100. When you call &lt;code&gt;PutMetricAlarm&lt;/code&gt; and specify a &lt;code&gt;MetricName&lt;/code&gt;, you must specify either &lt;code&gt;Statistic&lt;/code&gt; or &lt;code&gt;ExtendedStatistic,&lt;/code&gt; but not both.
    :type extended_statistic: str
    :param dimensions: The dimensions for the metric specified in &lt;code&gt;MetricName&lt;/code&gt;.
    :type dimensions: list | bytes
    :param period: &lt;p&gt;The length, in seconds, used each time the metric specified in &lt;code&gt;MetricName&lt;/code&gt; is evaluated. Valid values are 10, 30, and any multiple of 60.&lt;/p&gt; &lt;p&gt; &lt;code&gt;Period&lt;/code&gt; is required for alarms based on static thresholds. If you are creating an alarm based on a metric math expression, you specify the period for each metric within the objects in the &lt;code&gt;Metrics&lt;/code&gt; array.&lt;/p&gt; &lt;p&gt;Be sure to specify 10 or 30 only for metrics that are stored by a &lt;code&gt;PutMetricData&lt;/code&gt; call with a &lt;code&gt;StorageResolution&lt;/code&gt; of 1. If you specify a period of 10 or 30 for a metric that does not have sub-minute resolution, the alarm still attempts to gather data at the period rate that you specify. In this case, it does not receive data for the attempts that do not correspond to a one-minute data resolution, and the alarm might often lapse into INSUFFICENT_DATA status. Specifying 10 or 30 also sets this alarm as a high-resolution alarm, which has a higher charge than other alarms. For more information about pricing, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;An alarm&#39;s total current evaluation period can be no longer than one day, so &lt;code&gt;Period&lt;/code&gt; multiplied by &lt;code&gt;EvaluationPeriods&lt;/code&gt; cannot be more than 86,400 seconds.&lt;/p&gt;
    :type period: int
    :param unit: &lt;p&gt;The unit of measure for the statistic. For example, the units for the Amazon EC2 NetworkIn metric are Bytes because NetworkIn tracks the number of bytes that an instance receives on all network interfaces. You can also specify a unit when you create a custom metric. Units help provide conceptual meaning to your data. Metric data points that specify a unit of measure, such as Percent, are aggregated separately.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify &lt;code&gt;Unit&lt;/code&gt;, CloudWatch retrieves all unit types that have been published for the metric and attempts to evaluate the alarm. Usually, metrics are published with only one unit, so the alarm works as intended.&lt;/p&gt; &lt;p&gt;However, if the metric is published with multiple types of units and you don&#39;t specify a unit, the alarm&#39;s behavior is not defined and it behaves unpredictably.&lt;/p&gt; &lt;p&gt;We recommend omitting &lt;code&gt;Unit&lt;/code&gt; so that you don&#39;t inadvertently specify an incorrect unit that is not published for this metric. Doing so causes the alarm to be stuck in the &lt;code&gt;INSUFFICIENT DATA&lt;/code&gt; state.&lt;/p&gt;
    :type unit: str
    :param datapoints_to_alarm: The number of data points that must be breaching to trigger the alarm. This is used only if you are setting an \&quot;M out of N\&quot; alarm. In that case, this value is the M. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarm-evaluation\&quot;&gt;Evaluating an Alarm&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.
    :type datapoints_to_alarm: int
    :param threshold: &lt;p&gt;The value against which the specified statistic is compared.&lt;/p&gt; &lt;p&gt;This parameter is required for alarms based on static thresholds, but should not be used for alarms based on anomaly detection models.&lt;/p&gt;
    :type threshold: float
    :param treat_missing_data: &lt;p&gt; Sets how this alarm is to handle missing data points. If &lt;code&gt;TreatMissingData&lt;/code&gt; is omitted, the default behavior of &lt;code&gt;missing&lt;/code&gt; is used. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data\&quot;&gt;Configuring How CloudWatch Alarms Treats Missing Data&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;breaching | notBreaching | ignore | missing&lt;/code&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;Alarms that evaluate metrics in the &lt;code&gt;AWS/DynamoDB&lt;/code&gt; namespace always &lt;code&gt;ignore&lt;/code&gt; missing data even if you choose a different option for &lt;code&gt;TreatMissingData&lt;/code&gt;. When an &lt;code&gt;AWS/DynamoDB&lt;/code&gt; metric has missing data, alarms that evaluate that metric remain in their current state.&lt;/p&gt; &lt;/note&gt;
    :type treat_missing_data: str
    :param evaluate_low_sample_count_percentile: &lt;p&gt; Used only for alarms based on percentiles. If you specify &lt;code&gt;ignore&lt;/code&gt;, the alarm state does not change during periods with too few data points to be statistically significant. If you specify &lt;code&gt;evaluate&lt;/code&gt; or omit this parameter, the alarm is always evaluated and possibly changes state no matter how many data points are available. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#percentiles-with-low-samples\&quot;&gt;Percentile-Based CloudWatch Alarms and Low Data Samples&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Valid Values: &lt;code&gt;evaluate | ignore&lt;/code&gt; &lt;/p&gt;
    :type evaluate_low_sample_count_percentile: str
    :param metrics: &lt;p&gt;An array of &lt;code&gt;MetricDataQuery&lt;/code&gt; structures that enable you to create an alarm based on the result of a metric math expression. For each &lt;code&gt;PutMetricAlarm&lt;/code&gt; operation, you must specify either &lt;code&gt;MetricName&lt;/code&gt; or a &lt;code&gt;Metrics&lt;/code&gt; array.&lt;/p&gt; &lt;p&gt;Each item in the &lt;code&gt;Metrics&lt;/code&gt; array either retrieves a metric or performs a math expression.&lt;/p&gt; &lt;p&gt;One item in the &lt;code&gt;Metrics&lt;/code&gt; array is the expression that the alarm watches. You designate this expression by setting &lt;code&gt;ReturnData&lt;/code&gt; to true for this object in the array. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDataQuery.html\&quot;&gt;MetricDataQuery&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you use the &lt;code&gt;Metrics&lt;/code&gt; parameter, you cannot include the &lt;code&gt;MetricName&lt;/code&gt;, &lt;code&gt;Dimensions&lt;/code&gt;, &lt;code&gt;Period&lt;/code&gt;, &lt;code&gt;Namespace&lt;/code&gt;, &lt;code&gt;Statistic&lt;/code&gt;, or &lt;code&gt;ExtendedStatistic&lt;/code&gt; parameters of &lt;code&gt;PutMetricAlarm&lt;/code&gt; in the same operation. Instead, you retrieve the metrics you are using in your math expression as part of the &lt;code&gt;Metrics&lt;/code&gt; array.&lt;/p&gt;
    :type metrics: list | bytes
    :param tags: &lt;p&gt;A list of key-value pairs to associate with the alarm. You can associate as many as 50 tags with an alarm.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;If you are using this operation to update an existing alarm, any tags you specify in this parameter are ignored. To change the tags of an existing alarm, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt;
    :type tags: list | bytes
    :param threshold_metric_id: &lt;p&gt;If this is an alarm based on an anomaly detection model, make this value match the ID of the &lt;code&gt;ANOMALY_DETECTION_BAND&lt;/code&gt; function.&lt;/p&gt; &lt;p&gt;For an example of how to use this parameter, see the &lt;b&gt;Anomaly Detection Model Alarm&lt;/b&gt; example on this page.&lt;/p&gt; &lt;p&gt;If your alarm uses this parameter, it cannot have Auto Scaling actions.&lt;/p&gt;
    :type threshold_metric_id: str

    """
    dimensions = [Dimension.from_dict(d) for d in dimensions]
    metrics = [MetricDataQuery.from_dict(d) for d in metrics]
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_put_metric_data(request: web.Request, namespace, metric_data, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_put_metric_data

    &lt;p&gt;Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html\&quot;&gt;ListMetrics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can publish either individual data points in the &lt;code&gt;Value&lt;/code&gt; field, or arrays of values and the number of times each value occurred during the period by using the &lt;code&gt;Values&lt;/code&gt; and &lt;code&gt;Counts&lt;/code&gt; fields in the &lt;code&gt;MetricDatum&lt;/code&gt; structure. Using the &lt;code&gt;Values&lt;/code&gt; and &lt;code&gt;Counts&lt;/code&gt; method enables you to publish up to 150 values per metric with one &lt;code&gt;PutMetricData&lt;/code&gt; request, and supports retrieving percentile statistics on this data.&lt;/p&gt; &lt;p&gt;Each &lt;code&gt;PutMetricData&lt;/code&gt; request is limited to 1 MB in size for HTTP POST requests. You can send a payload compressed by gzip. Each request is also limited to no more than 1000 different metrics.&lt;/p&gt; &lt;p&gt;Although the &lt;code&gt;Value&lt;/code&gt; parameter accepts numbers of type &lt;code&gt;Double&lt;/code&gt;, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.&lt;/p&gt; &lt;p&gt;You can use up to 30 dimensions per metric to further clarify what data the metric collects. Each dimension consists of a Name and Value pair. For more information about specifying dimensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html\&quot;&gt;Publishing Metrics&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You specify the time stamp to be associated with each data point. You can specify time stamps that are as much as two weeks before the current date, and as much as 2 hours after the current day and time.&lt;/p&gt; &lt;p&gt;Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt; from the time they are submitted. Data points with time stamps between 3 and 24 hours ago can take as much as 2 hours to become available for for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;SampleCount&lt;/code&gt; value of the statistic set is 1 and &lt;code&gt;Min&lt;/code&gt;, &lt;code&gt;Max&lt;/code&gt;, and &lt;code&gt;Sum&lt;/code&gt; are all equal.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Min&lt;/code&gt; and &lt;code&gt;Max&lt;/code&gt; are equal, and &lt;code&gt;Sum&lt;/code&gt; is equal to &lt;code&gt;Min&lt;/code&gt; multiplied by &lt;code&gt;SampleCount&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param namespace: &lt;p&gt;The namespace for the metric data. You can use ASCII characters for the namespace, except for control characters which are not supported.&lt;/p&gt; &lt;p&gt;To avoid conflicts with Amazon Web Services service namespaces, you should not specify a namespace that begins with &lt;code&gt;AWS/&lt;/code&gt; &lt;/p&gt;
    :type namespace: str
    :param metric_data: The data for the metric. The array can include no more than 1000 metrics per call.
    :type metric_data: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    metric_data = [MetricDatum.from_dict(d) for d in metric_data]
    return web.Response(status=200)


async def g_et_put_metric_stream(request: web.Request, name, firehose_arn, role_arn, output_format, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, include_filters=None, exclude_filters=None, tags=None, statistics_configurations=None, include_linked_accounts_metrics=None) -> web.Response:
    """g_et_put_metric_stream

    &lt;p&gt;Creates or updates a metric stream. Metric streams can automatically stream CloudWatch metrics to Amazon Web Services destinations, including Amazon S3, and to many third-party solutions.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html\&quot;&gt; Using Metric Streams&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To create a metric stream, you must be signed in to an account that has the &lt;code&gt;iam:PassRole&lt;/code&gt; permission and either the &lt;code&gt;CloudWatchFullAccess&lt;/code&gt; policy or the &lt;code&gt;cloudwatch:PutMetricStream&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;When you create or update a metric stream, you choose one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Stream metrics from all metric namespaces in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Stream metrics from all metric namespaces in the account, except for the namespaces that you list in &lt;code&gt;ExcludeFilters&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Stream metrics from only the metric namespaces that you list in &lt;code&gt;IncludeFilters&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;By default, a metric stream always sends the &lt;code&gt;MAX&lt;/code&gt;, &lt;code&gt;MIN&lt;/code&gt;, &lt;code&gt;SUM&lt;/code&gt;, and &lt;code&gt;SAMPLECOUNT&lt;/code&gt; statistics for each metric that is streamed. You can use the &lt;code&gt;StatisticsConfigurations&lt;/code&gt; parameter to have the metric stream send additional statistics in the stream. Streaming additional statistics incurs additional costs. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;When you use &lt;code&gt;PutMetricStream&lt;/code&gt; to create a new metric stream, the stream is created in the &lt;code&gt;running&lt;/code&gt; state. If you use it to update an existing stream, the state of the stream is not changed.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability and you create a metric stream in a monitoring account, you can choose whether to include metrics from source accounts in the stream. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt;

    :param name: &lt;p&gt;If you are creating a new metric stream, this is the name for the new stream. The name must be different than the names of other metric streams in this account and Region.&lt;/p&gt; &lt;p&gt;If you are updating a metric stream, specify the name of that stream here.&lt;/p&gt; &lt;p&gt;Valid characters are A-Z, a-z, 0-9, \&quot;-\&quot; and \&quot;_\&quot;.&lt;/p&gt;
    :type name: str
    :param firehose_arn: The ARN of the Amazon Kinesis Data Firehose delivery stream to use for this metric stream. This Amazon Kinesis Data Firehose delivery stream must already exist and must be in the same account as the metric stream.
    :type firehose_arn: str
    :param role_arn: &lt;p&gt;The ARN of an IAM role that this metric stream will use to access Amazon Kinesis Data Firehose resources. This IAM role must already exist and must be in the same account as the metric stream. This IAM role must include the following permissions:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;firehose:PutRecord&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;firehose:PutRecordBatch&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type role_arn: str
    :param output_format: The output format for the stream. Valid values are &lt;code&gt;json&lt;/code&gt; and &lt;code&gt;opentelemetry0.7&lt;/code&gt;. For more information about metric stream output formats, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-metric-streams-formats.html\&quot;&gt; Metric streams output formats&lt;/a&gt;.
    :type output_format: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param include_filters: &lt;p&gt;If you specify this parameter, the stream sends only the metrics from the metric namespaces that you specify here.&lt;/p&gt; &lt;p&gt;You cannot include &lt;code&gt;IncludeFilters&lt;/code&gt; and &lt;code&gt;ExcludeFilters&lt;/code&gt; in the same operation.&lt;/p&gt;
    :type include_filters: list | bytes
    :param exclude_filters: &lt;p&gt;If you specify this parameter, the stream sends metrics from all metric namespaces except for the namespaces that you specify here.&lt;/p&gt; &lt;p&gt;You cannot include &lt;code&gt;ExcludeFilters&lt;/code&gt; and &lt;code&gt;IncludeFilters&lt;/code&gt; in the same operation.&lt;/p&gt;
    :type exclude_filters: list | bytes
    :param tags: &lt;p&gt;A list of key-value pairs to associate with the metric stream. You can associate as many as 50 tags with a metric stream.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;You can use this parameter only when you are creating a new metric stream. If you are using this operation to update an existing metric stream, any tags you specify in this parameter are ignored. To change the tags of an existing metric stream, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt;
    :type tags: list | bytes
    :param statistics_configurations: &lt;p&gt;By default, a metric stream always sends the &lt;code&gt;MAX&lt;/code&gt;, &lt;code&gt;MIN&lt;/code&gt;, &lt;code&gt;SUM&lt;/code&gt;, and &lt;code&gt;SAMPLECOUNT&lt;/code&gt; statistics for each metric that is streamed. You can use this parameter to have the metric stream also send additional statistics in the stream. This array can have up to 100 members.&lt;/p&gt; &lt;p&gt;For each entry in this array, you specify one or more metrics and the list of additional statistics to stream for those metrics. The additional statistics that you can stream depend on the stream&#39;s &lt;code&gt;OutputFormat&lt;/code&gt;. If the &lt;code&gt;OutputFormat&lt;/code&gt; is &lt;code&gt;json&lt;/code&gt;, you can stream any additional statistic that is supported by CloudWatch, listed in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html.html\&quot;&gt; CloudWatch statistics definitions&lt;/a&gt;. If the &lt;code&gt;OutputFormat&lt;/code&gt; is &lt;code&gt;opentelemetry0.7&lt;/code&gt;, you can stream percentile statistics such as p95, p99.9, and so on.&lt;/p&gt;
    :type statistics_configurations: list | bytes
    :param include_linked_accounts_metrics: If you are creating a metric stream in a monitoring account, specify &lt;code&gt;true&lt;/code&gt; to include metrics from source accounts in the metric stream.
    :type include_linked_accounts_metrics: bool

    """
    include_filters = [MetricStreamFilter.from_dict(d) for d in include_filters]
    exclude_filters = [MetricStreamFilter.from_dict(d) for d in exclude_filters]
    tags = [Tag.from_dict(d) for d in tags]
    statistics_configurations = [MetricStreamStatisticsConfiguration.from_dict(d) for d in statistics_configurations]
    return web.Response(status=200)


async def g_et_set_alarm_state(request: web.Request, alarm_name, state_value, state_reason, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, state_reason_data=None) -> web.Response:
    """g_et_set_alarm_state

    &lt;p&gt;Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to &lt;code&gt;ALARM&lt;/code&gt; sends an SNS message.&lt;/p&gt; &lt;p&gt;Metric alarms returns to their actual state quickly, often within seconds. Because the metric alarm state change happens quickly, it is typically only visible in the alarm&#39;s &lt;b&gt;History&lt;/b&gt; tab in the Amazon CloudWatch console or through &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html\&quot;&gt;DescribeAlarmHistory&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you use &lt;code&gt;SetAlarmState&lt;/code&gt; on a composite alarm, the composite alarm is not guaranteed to return to its actual state. It returns to its actual state only once any of its children alarms change state. It is also reevaluated if you update its configuration.&lt;/p&gt; &lt;p&gt;If an alarm triggers EC2 Auto Scaling policies or application Auto Scaling policies, you must include information in the &lt;code&gt;StateReasonData&lt;/code&gt; parameter to enable the policy to take the correct action.&lt;/p&gt;

    :param alarm_name: The name of the alarm.
    :type alarm_name: str
    :param state_value: The value of the state.
    :type state_value: str
    :param state_reason: The reason that this alarm is set to this specific state, in text format.
    :type state_reason: str
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param state_reason_data: &lt;p&gt;The reason that this alarm is set to this specific state, in JSON format.&lt;/p&gt; &lt;p&gt;For SNS or EC2 alarm actions, this is just informational. But for EC2 Auto Scaling or application Auto Scaling alarm actions, the Auto Scaling policy uses the information in this field to take the correct action.&lt;/p&gt;
    :type state_reason_data: str

    """
    return web.Response(status=200)


async def g_et_start_metric_streams(request: web.Request, names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_start_metric_streams

    Starts the streaming of metrics for one or more of your metric streams.

    :param names: &lt;p&gt;The array of the names of metric streams to start streaming.&lt;/p&gt; &lt;p&gt;This is an \&quot;all or nothing\&quot; operation. If you do not have permission to access all of the metric streams that you list here, then none of the streams that you list in the operation will start streaming.&lt;/p&gt;
    :type names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_stop_metric_streams(request: web.Request, names, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_stop_metric_streams

    Stops the streaming of metrics for one or more of your metric streams.

    :param names: &lt;p&gt;The array of the names of metric streams to stop streaming.&lt;/p&gt; &lt;p&gt;This is an \&quot;all or nothing\&quot; operation. If you do not have permission to access all of the metric streams that you list here, then none of the streams that you list in the operation will stop streaming.&lt;/p&gt;
    :type names: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def g_et_tag_resource(request: web.Request, resource_arn, tags, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified CloudWatch resource. Currently, the only CloudWatch resources that can be tagged are alarms and Contributor Insights rules.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with an alarm that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a CloudWatch resource.&lt;/p&gt;

    :param resource_arn: &lt;p&gt;The ARN of the CloudWatch resource that you&#39;re adding tags to.&lt;/p&gt; &lt;p&gt;The ARN format of an alarm is &lt;code&gt;arn:aws:cloudwatch:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:alarm:&lt;i&gt;alarm-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a Contributor Insights rule is &lt;code&gt;arn:aws:cloudwatch:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:insight-rule:&lt;i&gt;insight-rule-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\&quot;&gt; Resource Types Defined by Amazon CloudWatch&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt;
    :type resource_arn: str
    :param tags: The list of key-value pairs to associate with the alarm.
    :type tags: list | bytes
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    tags = [Tag.from_dict(d) for d in tags]
    return web.Response(status=200)


async def g_et_untag_resource(request: web.Request, resource_arn, tag_keys, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """g_et_untag_resource

    Removes one or more tags from the specified resource.

    :param resource_arn: &lt;p&gt;The ARN of the CloudWatch resource that you&#39;re removing tags from.&lt;/p&gt; &lt;p&gt;The ARN format of an alarm is &lt;code&gt;arn:aws:cloudwatch:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:alarm:&lt;i&gt;alarm-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;The ARN format of a Contributor Insights rule is &lt;code&gt;arn:aws:cloudwatch:&lt;i&gt;Region&lt;/i&gt;:&lt;i&gt;account-id&lt;/i&gt;:insight-rule:&lt;i&gt;insight-rule-name&lt;/i&gt; &lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about ARN format, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies\&quot;&gt; Resource Types Defined by Amazon CloudWatch&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt;
    :type resource_arn: str
    :param tag_keys: The list of tag keys to remove from the resource.
    :type tag_keys: List[str]
    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str

    """
    return web.Response(status=200)


async def p_ost_delete_alarms(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_alarms

    &lt;p&gt;Deletes the specified alarms. You can delete up to 100 alarms in one operation. However, this total can include no more than one composite alarm. For example, you could delete 99 metric alarms and one composite alarms with one operation, but you can&#39;t delete two composite alarms with one operation.&lt;/p&gt; &lt;p&gt; If you specify an incorrect alarm name or make any other error in the operation, no alarms are deleted. To confirm that alarms were deleted successfully, you can use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html\&quot;&gt;DescribeAlarms&lt;/a&gt; operation after using &lt;code&gt;DeleteAlarms&lt;/code&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can&#39;t delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.&lt;/p&gt; &lt;p&gt;To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the &lt;code&gt;AlarmRule&lt;/code&gt; of one of the alarms to &lt;code&gt;false&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. &lt;/p&gt; &lt;/note&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAlarmsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_anomaly_detector(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_anomaly_detector

     Deletes the specified anomaly detection model from your account. For more information about how to delete an anomaly detection model, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.html#Delete_Anomaly_Detection_Model\&quot;&gt;Deleting an anomaly detection model&lt;/a&gt; in the &lt;i&gt;CloudWatch User Guide&lt;/i&gt;. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteAnomalyDetectorInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_dashboards(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_dashboards

    Deletes all dashboards that you specify. You can specify up to 100 dashboards to delete. If there is an error during this call, no dashboards are deleted.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteDashboardsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_insight_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_insight_rules

    &lt;p&gt;Permanently deletes the specified Contributor Insights rules.&lt;/p&gt; &lt;p&gt;If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created might not be available.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteInsightRulesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_delete_metric_stream(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_delete_metric_stream

    Permanently deletes the metric stream that you specify.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteMetricStreamInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_alarm_history(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_alarm_history

    &lt;p&gt;Retrieves the history for the specified alarm. You can filter the results by date range or item type. If an alarm name is not specified, the histories for either all metric alarms or all composite alarms are returned.&lt;/p&gt; &lt;p&gt;CloudWatch retains the history of an alarm even if you delete the alarm.&lt;/p&gt; &lt;p&gt;To use this operation and return information about a composite alarm, you must be signed on with the &lt;code&gt;cloudwatch:DescribeAlarmHistory&lt;/code&gt; permission that is scoped to &lt;code&gt;*&lt;/code&gt;. You can&#39;t return information about composite alarms if your &lt;code&gt;cloudwatch:DescribeAlarmHistory&lt;/code&gt; permission has a narrower scope.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_records: Pagination limit
    :type max_records: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAlarmHistoryInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_alarms(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_records=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_alarms

    &lt;p&gt;Retrieves the specified alarms. You can filter the results by specifying a prefix for the alarm name, the alarm state, or a prefix for any action.&lt;/p&gt; &lt;p&gt;To use this operation and return information about composite alarms, you must be signed on with the &lt;code&gt;cloudwatch:DescribeAlarms&lt;/code&gt; permission that is scoped to &lt;code&gt;*&lt;/code&gt;. You can&#39;t return information about composite alarms if your &lt;code&gt;cloudwatch:DescribeAlarms&lt;/code&gt; permission has a narrower scope.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_records: Pagination limit
    :type max_records: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAlarmsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_alarms_for_metric(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_describe_alarms_for_metric

    &lt;p&gt;Retrieves the alarms for the specified metric. To filter the results, specify a statistic, period, or unit.&lt;/p&gt; &lt;p&gt;This operation retrieves only standard alarms that are based on the specified metric. It does not return alarms based on math expressions that use the specified metric, or composite alarms that use the specified metric.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAlarmsForMetricInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_anomaly_detectors(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_anomaly_detectors

    Lists the anomaly detection models that you have created in your account. For single metric anomaly detectors, you can list all of the models in your account or filter the results to only the models that are related to a certain namespace, metric name, or metric dimension. For metric math anomaly detectors, you can list them by adding &lt;code&gt;METRIC_MATH&lt;/code&gt; to the &lt;code&gt;AnomalyDetectorTypes&lt;/code&gt; array. This will return all metric math anomaly detectors in your account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeAnomalyDetectorsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_describe_insight_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_describe_insight_rules

    &lt;p&gt;Returns a list of all the Contributor Insights rules in your account.&lt;/p&gt; &lt;p&gt;For more information about Contributor Insights, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html\&quot;&gt;Using Contributor Insights to Analyze High-Cardinality Data&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = DescribeInsightRulesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_disable_alarm_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disable_alarm_actions

    Disables the actions for the specified alarms. When an alarm&#39;s actions are disabled, the alarm actions do not execute when the alarm state changes.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DisableAlarmActionsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_disable_insight_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_disable_insight_rules

    Disables the specified Contributor Insights rules. When rules are disabled, they do not analyze log groups and do not incur costs.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = DisableInsightRulesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_enable_alarm_actions(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_enable_alarm_actions

    Enables the actions for the specified alarms.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnableAlarmActionsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_enable_insight_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_enable_insight_rules

    Enables the specified Contributor Insights rules. When rules are enabled, they immediately begin analyzing log data.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = EnableInsightRulesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_dashboard(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_dashboard

    &lt;p&gt;Displays the details of the dashboard that you specify.&lt;/p&gt; &lt;p&gt;To copy an existing dashboard, use &lt;code&gt;GetDashboard&lt;/code&gt;, and then use the data returned within &lt;code&gt;DashboardBody&lt;/code&gt; as the template for the new dashboard when you call &lt;code&gt;PutDashboard&lt;/code&gt; to create the copy.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetDashboardInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_insight_rule_report(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_insight_rule_report

    &lt;p&gt;This operation returns the time series data collected by a Contributor Insights rule. The data includes the identity and number of contributors to the log group.&lt;/p&gt; &lt;p&gt;You can also optionally return one or more statistics about each data point in the time series. These statistics can include the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;UniqueContributors&lt;/code&gt; -- the number of unique contributors for each data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;MaxContributorValue&lt;/code&gt; -- the value of the top contributor for each data point. The identity of the contributor might change for each data point in the graph.&lt;/p&gt; &lt;p&gt;If this rule aggregates by COUNT, the top contributor for each data point is the contributor with the most occurrences in that period. If the rule aggregates by SUM, the top contributor is the contributor with the highest sum in the log field specified by the rule&#39;s &lt;code&gt;Value&lt;/code&gt;, during that period.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;SampleCount&lt;/code&gt; -- the number of data points matched by the rule.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Sum&lt;/code&gt; -- the sum of the values from all contributors during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Minimum&lt;/code&gt; -- the minimum value from a single observation during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Maximum&lt;/code&gt; -- the maximum value from a single observation during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Average&lt;/code&gt; -- the average value from all contributors during the time period represented by that data point.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetInsightRuleReportInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_metric_data(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_datapoints=None, next_token=None, body=None) -> web.Response:
    """p_ost_get_metric_data

    &lt;p&gt;You can use the &lt;code&gt;GetMetricData&lt;/code&gt; API to retrieve CloudWatch metric values. The operation can also include a CloudWatch Metrics Insights query, and one or more metric math functions.&lt;/p&gt; &lt;p&gt;A &lt;code&gt;GetMetricData&lt;/code&gt; operation that does not include a query can retrieve as many as 500 different metrics in a single request, with a total of as many as 100,800 data points. You can also optionally perform metric math expressions on the values of the returned statistics, to create new time series that represent new insights into your data. For example, using Lambda metrics, you could divide the Errors metric by the Invocations metric to get an error rate time series. For more information about metric math expressions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax\&quot;&gt;Metric Math Syntax and Functions&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;If you include a Metrics Insights query, each &lt;code&gt;GetMetricData&lt;/code&gt; operation can include only one query. But the same &lt;code&gt;GetMetricData&lt;/code&gt; operation can also retrieve other metrics. Metrics Insights queries can query only the most recent three hours of metric data. For more information about Metrics Insights, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html\&quot;&gt;Query your metrics with CloudWatch Metrics Insights&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Calls to the &lt;code&gt;GetMetricData&lt;/code&gt; API have a different pricing structure than calls to &lt;code&gt;GetMetricStatistics&lt;/code&gt;. For more information about pricing, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Amazon CloudWatch retains metric data as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a &lt;code&gt;StorageResolution&lt;/code&gt; of 1.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 60 seconds (1-minute) are available for 15 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 300 seconds (5-minute) are available for 63 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.&lt;/p&gt; &lt;p&gt;If you omit &lt;code&gt;Unit&lt;/code&gt; in your request, all data that was collected with any unit is returned, along with the corresponding units that were specified when the data was reported to CloudWatch. If you specify a unit, the operation returns only data that was collected with that unit specified. If you specify a unit that does not match the data collected, the results of the operation are null. CloudWatch does not perform unit conversions.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Using Metrics Insights queries with metric math&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can&#39;t mix a Metric Insights query and metric math syntax in the same expression, but you can reference results from a Metrics Insights query within other Metric math expressions. A Metrics Insights query without a &lt;b&gt;GROUP BY&lt;/b&gt; clause returns a single time-series (TS), and can be used as input for a metric math expression that expects a single time series. A Metrics Insights query with a &lt;b&gt;GROUP BY&lt;/b&gt; clause returns an array of time-series (TS[]), and can be used as input for a metric math expression that expects an array of time series. &lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_datapoints: Pagination limit
    :type max_datapoints: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetMetricDataInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_metric_statistics(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_metric_statistics

    &lt;p&gt;Gets statistics for the specified metric.&lt;/p&gt; &lt;p&gt;The maximum number of data points returned from a single call is 1,440. If you request more than 1,440 data points, CloudWatch returns an error. To reduce the number of data points, you can narrow the specified time range and make multiple requests across adjacent time ranges, or you can increase the specified period. Data points are not returned in chronological order.&lt;/p&gt; &lt;p&gt;CloudWatch aggregates data points based on the length of the period that you specify. For example, if you request statistics with a one-hour period, CloudWatch aggregates all data points with time stamps that fall within each one-hour period. Therefore, the number of values aggregated by CloudWatch is larger than the number of data points returned.&lt;/p&gt; &lt;p&gt;CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The SampleCount value of the statistic set is 1.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The Min and the Max values of the statistic set are equal.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Percentile statistics are not available for metrics when any of the metric values are negative numbers.&lt;/p&gt; &lt;p&gt;Amazon CloudWatch retains metric data as follows:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Data points with a period of less than 60 seconds are available for 3 hours. These data points are high-resolution metrics and are available only for custom metrics that have been defined with a &lt;code&gt;StorageResolution&lt;/code&gt; of 1.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 60 seconds (1-minute) are available for 15 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 300 seconds (5-minute) are available for 63 days.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Data points with a period of 3600 seconds (1 hour) are available for 455 days (15 months).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Data points that are initially published with a shorter period are aggregated together for long-term storage. For example, if you collect data using a period of 1 minute, the data remains available for 15 days with 1-minute resolution. After 15 days, this data is still available, but is aggregated and retrievable only with a resolution of 5 minutes. After 63 days, the data is further aggregated and is available with a resolution of 1 hour.&lt;/p&gt; &lt;p&gt;CloudWatch started retaining 5-minute and 1-hour metric data as of July 9, 2016.&lt;/p&gt; &lt;p&gt;For information about metrics and dimensions supported by Amazon Web Services services, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html\&quot;&gt;Amazon CloudWatch Metrics and Dimensions Reference&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetMetricStatisticsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_metric_stream(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_metric_stream

    Returns information about the metric stream that you specify.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetMetricStreamInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_get_metric_widget_image(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_get_metric_widget_image

    &lt;p&gt;You can use the &lt;code&gt;GetMetricWidgetImage&lt;/code&gt; API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this image into your services and products, such as wiki pages, reports, and documents. You could also retrieve images regularly, such as every minute, and create your own custom live dashboard.&lt;/p&gt; &lt;p&gt;The graph you retrieve can include all CloudWatch metric graph features, including metric math and horizontal and vertical annotations.&lt;/p&gt; &lt;p&gt;There is a limit of 20 transactions per second for this API. Each &lt;code&gt;GetMetricWidgetImage&lt;/code&gt; action has the following limits:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;As many as 100 metrics in the graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Up to 100 KB uncompressed payload.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetMetricWidgetImageInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_dashboards(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_dashboards

    &lt;p&gt;Returns a list of the dashboards for your account. If you include &lt;code&gt;DashboardNamePrefix&lt;/code&gt;, only those dashboards with names starting with the prefix are listed. Otherwise, all dashboards in your account are listed. &lt;/p&gt; &lt;p&gt; &lt;code&gt;ListDashboards&lt;/code&gt; returns up to 1000 results on one page. If there are more than 1000 dashboards, you can call &lt;code&gt;ListDashboards&lt;/code&gt; again and include the value you received for &lt;code&gt;NextToken&lt;/code&gt; in the first call, to receive the next 1000 results.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListDashboardsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_managed_insight_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_managed_insight_rules

     Returns a list that contains the number of managed Contributor Insights rules in your account. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListManagedInsightRulesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_metric_streams(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_metric_streams

    Returns a list of metric streams in this account.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param max_results: Pagination limit
    :type max_results: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListMetricStreamsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_metrics(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, body=None) -> web.Response:
    """p_ost_list_metrics

    &lt;p&gt;List the specified metrics. You can use the returned metrics with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt; to get statistical data.&lt;/p&gt; &lt;p&gt;Up to 500 results are returned for any one call. To retrieve additional results, use the returned token with subsequent calls.&lt;/p&gt; &lt;p&gt;After you create a metric, allow up to 15 minutes for the metric to appear. To see metric statistics sooner, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view metrics from the linked source accounts. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ListMetrics&lt;/code&gt; doesn&#39;t return information about metrics if those metrics haven&#39;t reported data in the past two weeks. To retrieve those metrics, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param next_token: Pagination token
    :type next_token: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListMetricsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_list_tags_for_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_list_tags_for_resource

    Displays the tags associated with a CloudWatch resource. Currently, alarms and Contributor Insights rules support tagging.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = ListTagsForResourceInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_anomaly_detector(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_anomaly_detector

    &lt;p&gt;Creates an anomaly detection model for a CloudWatch metric. You can use the model to display a band of expected normal values when the metric is graphed.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html\&quot;&gt;CloudWatch Anomaly Detection&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutAnomalyDetectorInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_composite_alarm(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_composite_alarm

    &lt;p&gt;Creates or updates a &lt;i&gt;composite alarm&lt;/i&gt;. When you create a composite alarm, you specify a rule expression for the alarm that takes into account the alarm states of other alarms that you have created. The composite alarm goes into ALARM state only if all conditions of the rule are met.&lt;/p&gt; &lt;p&gt;The alarms specified in a composite alarm&#39;s rule expression can include metric alarms and other composite alarms. The rule expression of a composite alarm can include as many as 100 underlying alarms. Any single alarm can be included in the rule expressions of as many as 150 composite alarms.&lt;/p&gt; &lt;p&gt;Using composite alarms can reduce alarm noise. You can create multiple metric alarms, and also create a composite alarm and set up alerts only for the composite alarm. For example, you could create a composite alarm that goes into ALARM state only when more than one of the underlying metric alarms are in ALARM state.&lt;/p&gt; &lt;p&gt;Currently, the only alarm actions that can be taken by composite alarms are notifying SNS topics.&lt;/p&gt; &lt;note&gt; &lt;p&gt;It is possible to create a loop or cycle of composite alarms, where composite alarm A depends on composite alarm B, and composite alarm B also depends on composite alarm A. In this scenario, you can&#39;t delete any composite alarm that is part of the cycle because there is always still a composite alarm that depends on that alarm that you want to delete.&lt;/p&gt; &lt;p&gt;To get out of such a situation, you must break the cycle by changing the rule of one of the composite alarms in the cycle to remove a dependency that creates the cycle. The simplest change to make to break a cycle is to change the &lt;code&gt;AlarmRule&lt;/code&gt; of one of the alarms to &lt;code&gt;false&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;Additionally, the evaluation of composite alarms stops if CloudWatch detects a cycle in the evaluation path. &lt;/p&gt; &lt;/note&gt; &lt;p&gt;When this operation creates an alarm, the alarm state is immediately set to &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt;. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed. For a composite alarm, this initial time after creation is the only time that the alarm can be in &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.&lt;/p&gt; &lt;p&gt;To use this operation, you must be signed on with the &lt;code&gt;cloudwatch:PutCompositeAlarm&lt;/code&gt; permission that is scoped to &lt;code&gt;*&lt;/code&gt;. You can&#39;t create a composite alarms if your &lt;code&gt;cloudwatch:PutCompositeAlarm&lt;/code&gt; permission has a narrower scope.&lt;/p&gt; &lt;p&gt;If you are an IAM user, you must have &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; to create a composite alarm that has Systems Manager OpsItem actions.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutCompositeAlarmInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_dashboard(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_dashboard

    &lt;p&gt;Creates a dashboard if it does not already exist, or updates an existing dashboard. If you update a dashboard, the entire contents are replaced with what you specify here.&lt;/p&gt; &lt;p&gt;All dashboards in your account are global, not region-specific.&lt;/p&gt; &lt;p&gt;A simple way to create a dashboard using &lt;code&gt;PutDashboard&lt;/code&gt; is to copy an existing dashboard. To copy an existing dashboard using the console, you can load the dashboard and then use the View/edit source command in the Actions menu to display the JSON block for that dashboard. Another way to copy a dashboard is to use &lt;code&gt;GetDashboard&lt;/code&gt;, and then use the data returned within &lt;code&gt;DashboardBody&lt;/code&gt; as the template for the new dashboard when you call &lt;code&gt;PutDashboard&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;When you create a dashboard with &lt;code&gt;PutDashboard&lt;/code&gt;, a good practice is to add a text widget at the top of the dashboard with a message that the dashboard was created by script and should not be changed in the console. This message could also point console users to the location of the &lt;code&gt;DashboardBody&lt;/code&gt; script or the CloudFormation template used to create the dashboard.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutDashboardInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_insight_rule(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_insight_rule

    &lt;p&gt;Creates a Contributor Insights rule. Rules evaluate log events in a CloudWatch Logs log group, enabling you to find contributor data for the log events in that log group. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html\&quot;&gt;Using Contributor Insights to Analyze High-Cardinality Data&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you create a rule, delete it, and then re-create it with the same name, historical data from the first time the rule was created might not be available.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutInsightRuleInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_managed_insight_rules(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_managed_insight_rules

     Creates a managed Contributor Insights rule for a specified Amazon Web Services resource. When you enable a managed rule, you create a Contributor Insights rule that collects data from Amazon Web Services services. You cannot edit these rules with &lt;code&gt;PutInsightRule&lt;/code&gt;. The rules can be enabled, disabled, and deleted using &lt;code&gt;EnableInsightRules&lt;/code&gt;, &lt;code&gt;DisableInsightRules&lt;/code&gt;, and &lt;code&gt;DeleteInsightRules&lt;/code&gt;. If a previously created managed rule is currently disabled, a subsequent call to this API will re-enable it. Use &lt;code&gt;ListManagedInsightRules&lt;/code&gt; to describe all available rules. 

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutManagedInsightRulesInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_metric_alarm(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_metric_alarm

    &lt;p&gt;Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, or Metrics Insights query. For more information about using a Metrics Insights query for an alarm, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html\&quot;&gt;Create alarms on Metrics Insights queries&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Alarms based on anomaly detection models cannot have Auto Scaling actions.&lt;/p&gt; &lt;p&gt;When this operation creates an alarm, the alarm state is immediately set to &lt;code&gt;INSUFFICIENT_DATA&lt;/code&gt;. The alarm is then evaluated and its state is set appropriately. Any actions associated with the new state are then executed.&lt;/p&gt; &lt;p&gt;When you update an existing alarm, its state is left unchanged, but the update completely overwrites the previous configuration of the alarm.&lt;/p&gt; &lt;p&gt;If you are an IAM user, you must have Amazon EC2 permissions for some alarm operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; permission for all alarms with EC2 actions&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;iam:CreateServiceLinkedRole&lt;/code&gt; permissions to create an alarm with Systems Manager OpsItem or response plan actions.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The first time you create an alarm in the Amazon Web Services Management Console, the CLI, or by using the PutMetricAlarm API, CloudWatch creates the necessary service-linked role for you. The service-linked roles are called &lt;code&gt;AWSServiceRoleForCloudWatchEvents&lt;/code&gt; and &lt;code&gt;AWSServiceRoleForCloudWatchAlarms_ActionSSM&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role\&quot;&gt;Amazon Web Services service-linked role&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Each &lt;code&gt;PutMetricAlarm&lt;/code&gt; action has a maximum uncompressed payload of 120 KB.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Cross-account alarms&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can set an alarm on metrics in the current account, or in another account. To create a cross-account alarm that watches a metric in a different account, you must have completed the following pre-requisites:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The account where the metrics are located (the &lt;i&gt;sharing account&lt;/i&gt;) must already have a sharing role named &lt;b&gt;CloudWatch-CrossAccountSharingRole&lt;/b&gt;. If it does not already have this role, you must create it using the instructions in &lt;b&gt;Set up a sharing account&lt;/b&gt; in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\&quot;&gt; Cross-account cross-Region CloudWatch console&lt;/a&gt;. The policy for that role must grant access to the ID of the account where you are creating the alarm. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The account where you are creating the alarm (the &lt;i&gt;monitoring account&lt;/i&gt;) must already have a service-linked role named &lt;b&gt;AWSServiceRoleForCloudWatchCrossAccount&lt;/b&gt; to allow CloudWatch to assume the sharing role in the sharing account. If it does not, you must create it following the directions in &lt;b&gt;Set up a monitoring account&lt;/b&gt; in &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Cross-Account-Cross-Region.html#enable-cross-account-cross-Region\&quot;&gt; Cross-account cross-Region CloudWatch console&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutMetricAlarmInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_metric_data(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_metric_data

    &lt;p&gt;Publishes metric data points to Amazon CloudWatch. CloudWatch associates the data points with the specified metric. If the specified metric does not exist, CloudWatch creates the metric. When CloudWatch creates a metric, it can take up to fifteen minutes for the metric to appear in calls to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListMetrics.html\&quot;&gt;ListMetrics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can publish either individual data points in the &lt;code&gt;Value&lt;/code&gt; field, or arrays of values and the number of times each value occurred during the period by using the &lt;code&gt;Values&lt;/code&gt; and &lt;code&gt;Counts&lt;/code&gt; fields in the &lt;code&gt;MetricDatum&lt;/code&gt; structure. Using the &lt;code&gt;Values&lt;/code&gt; and &lt;code&gt;Counts&lt;/code&gt; method enables you to publish up to 150 values per metric with one &lt;code&gt;PutMetricData&lt;/code&gt; request, and supports retrieving percentile statistics on this data.&lt;/p&gt; &lt;p&gt;Each &lt;code&gt;PutMetricData&lt;/code&gt; request is limited to 1 MB in size for HTTP POST requests. You can send a payload compressed by gzip. Each request is also limited to no more than 1000 different metrics.&lt;/p&gt; &lt;p&gt;Although the &lt;code&gt;Value&lt;/code&gt; parameter accepts numbers of type &lt;code&gt;Double&lt;/code&gt;, CloudWatch rejects values that are either too small or too large. Values must be in the range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity, -Infinity) are not supported.&lt;/p&gt; &lt;p&gt;You can use up to 30 dimensions per metric to further clarify what data the metric collects. Each dimension consists of a Name and Value pair. For more information about specifying dimensions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html\&quot;&gt;Publishing Metrics&lt;/a&gt; in the &lt;i&gt;Amazon CloudWatch User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You specify the time stamp to be associated with each data point. You can specify time stamps that are as much as two weeks before the current date, and as much as 2 hours after the current day and time.&lt;/p&gt; &lt;p&gt;Data points with time stamps from 24 hours ago or longer can take at least 48 hours to become available for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt; from the time they are submitted. Data points with time stamps between 3 and 24 hours ago can take as much as 2 hours to become available for for &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html\&quot;&gt;GetMetricData&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html\&quot;&gt;GetMetricStatistics&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;CloudWatch needs raw data points to calculate percentile statistics. If you publish data using a statistic set instead, you can only retrieve percentile statistics for this data if one of the following conditions is true:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;SampleCount&lt;/code&gt; value of the statistic set is 1 and &lt;code&gt;Min&lt;/code&gt;, &lt;code&gt;Max&lt;/code&gt;, and &lt;code&gt;Sum&lt;/code&gt; are all equal.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;Min&lt;/code&gt; and &lt;code&gt;Max&lt;/code&gt; are equal, and &lt;code&gt;Sum&lt;/code&gt; is equal to &lt;code&gt;Min&lt;/code&gt; multiplied by &lt;code&gt;SampleCount&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutMetricDataInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_put_metric_stream(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_put_metric_stream

    &lt;p&gt;Creates or updates a metric stream. Metric streams can automatically stream CloudWatch metrics to Amazon Web Services destinations, including Amazon S3, and to many third-party solutions.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html\&quot;&gt; Using Metric Streams&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;To create a metric stream, you must be signed in to an account that has the &lt;code&gt;iam:PassRole&lt;/code&gt; permission and either the &lt;code&gt;CloudWatchFullAccess&lt;/code&gt; policy or the &lt;code&gt;cloudwatch:PutMetricStream&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;When you create or update a metric stream, you choose one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Stream metrics from all metric namespaces in the account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Stream metrics from all metric namespaces in the account, except for the namespaces that you list in &lt;code&gt;ExcludeFilters&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Stream metrics from only the metric namespaces that you list in &lt;code&gt;IncludeFilters&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;By default, a metric stream always sends the &lt;code&gt;MAX&lt;/code&gt;, &lt;code&gt;MIN&lt;/code&gt;, &lt;code&gt;SUM&lt;/code&gt;, and &lt;code&gt;SAMPLECOUNT&lt;/code&gt; statistics for each metric that is streamed. You can use the &lt;code&gt;StatisticsConfigurations&lt;/code&gt; parameter to have the metric stream send additional statistics in the stream. Streaming additional statistics incurs additional costs. For more information, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/cloudwatch/pricing/\&quot;&gt;Amazon CloudWatch Pricing&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;When you use &lt;code&gt;PutMetricStream&lt;/code&gt; to create a new metric stream, the stream is created in the &lt;code&gt;running&lt;/code&gt; state. If you use it to update an existing stream, the state of the stream is not changed.&lt;/p&gt; &lt;p&gt;If you are using CloudWatch cross-account observability and you create a metric stream in a monitoring account, you can choose whether to include metrics from source accounts in the stream. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html\&quot;&gt;CloudWatch cross-account observability&lt;/a&gt;.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = PutMetricStreamInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_set_alarm_state(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_set_alarm_state

    &lt;p&gt;Temporarily sets the state of an alarm for testing purposes. When the updated state differs from the previous value, the action configured for the appropriate state is invoked. For example, if your alarm is configured to send an Amazon SNS message when an alarm is triggered, temporarily changing the alarm state to &lt;code&gt;ALARM&lt;/code&gt; sends an SNS message.&lt;/p&gt; &lt;p&gt;Metric alarms returns to their actual state quickly, often within seconds. Because the metric alarm state change happens quickly, it is typically only visible in the alarm&#39;s &lt;b&gt;History&lt;/b&gt; tab in the Amazon CloudWatch console or through &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarmHistory.html\&quot;&gt;DescribeAlarmHistory&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you use &lt;code&gt;SetAlarmState&lt;/code&gt; on a composite alarm, the composite alarm is not guaranteed to return to its actual state. It returns to its actual state only once any of its children alarms change state. It is also reevaluated if you update its configuration.&lt;/p&gt; &lt;p&gt;If an alarm triggers EC2 Auto Scaling policies or application Auto Scaling policies, you must include information in the &lt;code&gt;StateReasonData&lt;/code&gt; parameter to enable the policy to take the correct action.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = SetAlarmStateInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_start_metric_streams(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_start_metric_streams

    Starts the streaming of metrics for one or more of your metric streams.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = StartMetricStreamsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_stop_metric_streams(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_stop_metric_streams

    Stops the streaming of metrics for one or more of your metric streams.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = StopMetricStreamsInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_tag_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_tag_resource

    &lt;p&gt;Assigns one or more tags (key-value pairs) to the specified CloudWatch resource. Currently, the only CloudWatch resources that can be tagged are alarms and Contributor Insights rules.&lt;/p&gt; &lt;p&gt;Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the &lt;code&gt;TagResource&lt;/code&gt; action with an alarm that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a CloudWatch resource.&lt;/p&gt;

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = TagResourceInput.from_dict(body)
    return web.Response(status=200)


async def p_ost_untag_resource(request: web.Request, action, version, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, body=None) -> web.Response:
    """p_ost_untag_resource

    Removes one or more tags from the specified resource.

    :param action: 
    :type action: str
    :param version: 
    :type version: str
    :param x_amz_content_sha256: 
    :type x_amz_content_sha256: str
    :param x_amz_date: 
    :type x_amz_date: str
    :param x_amz_algorithm: 
    :type x_amz_algorithm: str
    :param x_amz_credential: 
    :type x_amz_credential: str
    :param x_amz_security_token: 
    :type x_amz_security_token: str
    :param x_amz_signature: 
    :type x_amz_signature: str
    :param x_amz_signed_headers: 
    :type x_amz_signed_headers: str
    :param body: 
    :type body: dict | bytes

    """
    body = UntagResourceInput.from_dict(body)
    return web.Response(status=200)

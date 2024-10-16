# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.stackdriver_align_options import StackdriverAlignOptions
from openapi_server.models.target_bucket_aggs_inner import TargetBucketAggsInner
from openapi_server.models.target_group_inner import TargetGroupInner
from openapi_server.models.target_metrics_inner import TargetMetricsInner
from openapi_server.models.target_where_inner import TargetWhereInner
from openapi_server import util


class Target(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alias: str=None, alias_by: str=None, align_options: List[StackdriverAlignOptions]=None, alignment_period: str=None, bucket_aggs: List[TargetBucketAggsInner]=None, cross_series_reducer: str=None, datasource: str=None, dimensions: Dict[str, str]=None, ds_type: str=None, expr: str=None, filters: List[str]=None, format: str=None, group: List[TargetGroupInner]=None, group_bys: List[str]=None, hide: bool=None, instant: bool=None, interval: str=None, interval_factor: int=None, legend_format: str=None, measurement: str=None, metric_column: str=None, metric_kind: str=None, metric_name: str=None, metric_type: str=None, metrics: List[TargetMetricsInner]=None, namespace: str=None, per_series_aligner: str=None, period: str=None, project_name: str=None, query: str=None, raw_query: bool=None, raw_sql: str=None, ref_id: str=None, region: str=None, select: List[List[TargetGroupInner]]=None, statistics: List[str]=None, step: int=None, table: str=None, target: str=None, time_column: str=None, time_field: str=None, value_type: str=None, where: List[TargetWhereInner]=None):
        """Target - a model defined in OpenAPI

        :param alias: The alias of this Target.
        :param alias_by: The alias_by of this Target.
        :param align_options: The align_options of this Target.
        :param alignment_period: The alignment_period of this Target.
        :param bucket_aggs: The bucket_aggs of this Target.
        :param cross_series_reducer: The cross_series_reducer of this Target.
        :param datasource: The datasource of this Target.
        :param dimensions: The dimensions of this Target.
        :param ds_type: The ds_type of this Target.
        :param expr: The expr of this Target.
        :param filters: The filters of this Target.
        :param format: The format of this Target.
        :param group: The group of this Target.
        :param group_bys: The group_bys of this Target.
        :param hide: The hide of this Target.
        :param instant: The instant of this Target.
        :param interval: The interval of this Target.
        :param interval_factor: The interval_factor of this Target.
        :param legend_format: The legend_format of this Target.
        :param measurement: The measurement of this Target.
        :param metric_column: The metric_column of this Target.
        :param metric_kind: The metric_kind of this Target.
        :param metric_name: The metric_name of this Target.
        :param metric_type: The metric_type of this Target.
        :param metrics: The metrics of this Target.
        :param namespace: The namespace of this Target.
        :param per_series_aligner: The per_series_aligner of this Target.
        :param period: The period of this Target.
        :param project_name: The project_name of this Target.
        :param query: The query of this Target.
        :param raw_query: The raw_query of this Target.
        :param raw_sql: The raw_sql of this Target.
        :param ref_id: The ref_id of this Target.
        :param region: The region of this Target.
        :param select: The select of this Target.
        :param statistics: The statistics of this Target.
        :param step: The step of this Target.
        :param table: The table of this Target.
        :param target: The target of this Target.
        :param time_column: The time_column of this Target.
        :param time_field: The time_field of this Target.
        :param value_type: The value_type of this Target.
        :param where: The where of this Target.
        """
        self.openapi_types = {
            'alias': str,
            'alias_by': str,
            'align_options': List[StackdriverAlignOptions],
            'alignment_period': str,
            'bucket_aggs': List[TargetBucketAggsInner],
            'cross_series_reducer': str,
            'datasource': str,
            'dimensions': Dict[str, str],
            'ds_type': str,
            'expr': str,
            'filters': List[str],
            'format': str,
            'group': List[TargetGroupInner],
            'group_bys': List[str],
            'hide': bool,
            'instant': bool,
            'interval': str,
            'interval_factor': int,
            'legend_format': str,
            'measurement': str,
            'metric_column': str,
            'metric_kind': str,
            'metric_name': str,
            'metric_type': str,
            'metrics': List[TargetMetricsInner],
            'namespace': str,
            'per_series_aligner': str,
            'period': str,
            'project_name': str,
            'query': str,
            'raw_query': bool,
            'raw_sql': str,
            'ref_id': str,
            'region': str,
            'select': List[List[TargetGroupInner]],
            'statistics': List[str],
            'step': int,
            'table': str,
            'target': str,
            'time_column': str,
            'time_field': str,
            'value_type': str,
            'where': List[TargetWhereInner]
        }

        self.attribute_map = {
            'alias': 'alias',
            'alias_by': 'aliasBy',
            'align_options': 'alignOptions',
            'alignment_period': 'alignmentPeriod',
            'bucket_aggs': 'bucketAggs',
            'cross_series_reducer': 'crossSeriesReducer',
            'datasource': 'datasource',
            'dimensions': 'dimensions',
            'ds_type': 'dsType',
            'expr': 'expr',
            'filters': 'filters',
            'format': 'format',
            'group': 'group',
            'group_bys': 'groupBys',
            'hide': 'hide',
            'instant': 'instant',
            'interval': 'interval',
            'interval_factor': 'intervalFactor',
            'legend_format': 'legendFormat',
            'measurement': 'measurement',
            'metric_column': 'metricColumn',
            'metric_kind': 'metricKind',
            'metric_name': 'metricName',
            'metric_type': 'metricType',
            'metrics': 'metrics',
            'namespace': 'namespace',
            'per_series_aligner': 'perSeriesAligner',
            'period': 'period',
            'project_name': 'projectName',
            'query': 'query',
            'raw_query': 'rawQuery',
            'raw_sql': 'rawSql',
            'ref_id': 'refId',
            'region': 'region',
            'select': 'select',
            'statistics': 'statistics',
            'step': 'step',
            'table': 'table',
            'target': 'target',
            'time_column': 'timeColumn',
            'time_field': 'timeField',
            'value_type': 'valueType',
            'where': 'where'
        }

        self._alias = alias
        self._alias_by = alias_by
        self._align_options = align_options
        self._alignment_period = alignment_period
        self._bucket_aggs = bucket_aggs
        self._cross_series_reducer = cross_series_reducer
        self._datasource = datasource
        self._dimensions = dimensions
        self._ds_type = ds_type
        self._expr = expr
        self._filters = filters
        self._format = format
        self._group = group
        self._group_bys = group_bys
        self._hide = hide
        self._instant = instant
        self._interval = interval
        self._interval_factor = interval_factor
        self._legend_format = legend_format
        self._measurement = measurement
        self._metric_column = metric_column
        self._metric_kind = metric_kind
        self._metric_name = metric_name
        self._metric_type = metric_type
        self._metrics = metrics
        self._namespace = namespace
        self._per_series_aligner = per_series_aligner
        self._period = period
        self._project_name = project_name
        self._query = query
        self._raw_query = raw_query
        self._raw_sql = raw_sql
        self._ref_id = ref_id
        self._region = region
        self._select = select
        self._statistics = statistics
        self._step = step
        self._table = table
        self._target = target
        self._time_column = time_column
        self._time_field = time_field
        self._value_type = value_type
        self._where = where

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Target':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Target of this Target.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alias(self):
        """Gets the alias of this Target.


        :return: The alias of this Target.
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this Target.


        :param alias: The alias of this Target.
        :type alias: str
        """

        self._alias = alias

    @property
    def alias_by(self):
        """Gets the alias_by of this Target.


        :return: The alias_by of this Target.
        :rtype: str
        """
        return self._alias_by

    @alias_by.setter
    def alias_by(self, alias_by):
        """Sets the alias_by of this Target.


        :param alias_by: The alias_by of this Target.
        :type alias_by: str
        """

        self._alias_by = alias_by

    @property
    def align_options(self):
        """Gets the align_options of this Target.


        :return: The align_options of this Target.
        :rtype: List[StackdriverAlignOptions]
        """
        return self._align_options

    @align_options.setter
    def align_options(self, align_options):
        """Sets the align_options of this Target.


        :param align_options: The align_options of this Target.
        :type align_options: List[StackdriverAlignOptions]
        """

        self._align_options = align_options

    @property
    def alignment_period(self):
        """Gets the alignment_period of this Target.


        :return: The alignment_period of this Target.
        :rtype: str
        """
        return self._alignment_period

    @alignment_period.setter
    def alignment_period(self, alignment_period):
        """Sets the alignment_period of this Target.


        :param alignment_period: The alignment_period of this Target.
        :type alignment_period: str
        """

        self._alignment_period = alignment_period

    @property
    def bucket_aggs(self):
        """Gets the bucket_aggs of this Target.


        :return: The bucket_aggs of this Target.
        :rtype: List[TargetBucketAggsInner]
        """
        return self._bucket_aggs

    @bucket_aggs.setter
    def bucket_aggs(self, bucket_aggs):
        """Sets the bucket_aggs of this Target.


        :param bucket_aggs: The bucket_aggs of this Target.
        :type bucket_aggs: List[TargetBucketAggsInner]
        """

        self._bucket_aggs = bucket_aggs

    @property
    def cross_series_reducer(self):
        """Gets the cross_series_reducer of this Target.


        :return: The cross_series_reducer of this Target.
        :rtype: str
        """
        return self._cross_series_reducer

    @cross_series_reducer.setter
    def cross_series_reducer(self, cross_series_reducer):
        """Sets the cross_series_reducer of this Target.


        :param cross_series_reducer: The cross_series_reducer of this Target.
        :type cross_series_reducer: str
        """

        self._cross_series_reducer = cross_series_reducer

    @property
    def datasource(self):
        """Gets the datasource of this Target.


        :return: The datasource of this Target.
        :rtype: str
        """
        return self._datasource

    @datasource.setter
    def datasource(self, datasource):
        """Sets the datasource of this Target.


        :param datasource: The datasource of this Target.
        :type datasource: str
        """

        self._datasource = datasource

    @property
    def dimensions(self):
        """Gets the dimensions of this Target.


        :return: The dimensions of this Target.
        :rtype: Dict[str, str]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this Target.


        :param dimensions: The dimensions of this Target.
        :type dimensions: Dict[str, str]
        """

        self._dimensions = dimensions

    @property
    def ds_type(self):
        """Gets the ds_type of this Target.

        For Elasticsearch

        :return: The ds_type of this Target.
        :rtype: str
        """
        return self._ds_type

    @ds_type.setter
    def ds_type(self, ds_type):
        """Sets the ds_type of this Target.

        For Elasticsearch

        :param ds_type: The ds_type of this Target.
        :type ds_type: str
        """

        self._ds_type = ds_type

    @property
    def expr(self):
        """Gets the expr of this Target.

        For Prometheus

        :return: The expr of this Target.
        :rtype: str
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """Sets the expr of this Target.

        For Prometheus

        :param expr: The expr of this Target.
        :type expr: str
        """

        self._expr = expr

    @property
    def filters(self):
        """Gets the filters of this Target.


        :return: The filters of this Target.
        :rtype: List[str]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this Target.


        :param filters: The filters of this Target.
        :type filters: List[str]
        """

        self._filters = filters

    @property
    def format(self):
        """Gets the format of this Target.


        :return: The format of this Target.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Target.


        :param format: The format of this Target.
        :type format: str
        """

        self._format = format

    @property
    def group(self):
        """Gets the group of this Target.


        :return: The group of this Target.
        :rtype: List[TargetGroupInner]
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this Target.


        :param group: The group of this Target.
        :type group: List[TargetGroupInner]
        """

        self._group = group

    @property
    def group_bys(self):
        """Gets the group_bys of this Target.


        :return: The group_bys of this Target.
        :rtype: List[str]
        """
        return self._group_bys

    @group_bys.setter
    def group_bys(self, group_bys):
        """Sets the group_bys of this Target.


        :param group_bys: The group_bys of this Target.
        :type group_bys: List[str]
        """

        self._group_bys = group_bys

    @property
    def hide(self):
        """Gets the hide of this Target.


        :return: The hide of this Target.
        :rtype: bool
        """
        return self._hide

    @hide.setter
    def hide(self, hide):
        """Sets the hide of this Target.


        :param hide: The hide of this Target.
        :type hide: bool
        """

        self._hide = hide

    @property
    def instant(self):
        """Gets the instant of this Target.


        :return: The instant of this Target.
        :rtype: bool
        """
        return self._instant

    @instant.setter
    def instant(self, instant):
        """Sets the instant of this Target.


        :param instant: The instant of this Target.
        :type instant: bool
        """

        self._instant = instant

    @property
    def interval(self):
        """Gets the interval of this Target.


        :return: The interval of this Target.
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this Target.


        :param interval: The interval of this Target.
        :type interval: str
        """

        self._interval = interval

    @property
    def interval_factor(self):
        """Gets the interval_factor of this Target.


        :return: The interval_factor of this Target.
        :rtype: int
        """
        return self._interval_factor

    @interval_factor.setter
    def interval_factor(self, interval_factor):
        """Sets the interval_factor of this Target.


        :param interval_factor: The interval_factor of this Target.
        :type interval_factor: int
        """

        self._interval_factor = interval_factor

    @property
    def legend_format(self):
        """Gets the legend_format of this Target.


        :return: The legend_format of this Target.
        :rtype: str
        """
        return self._legend_format

    @legend_format.setter
    def legend_format(self, legend_format):
        """Sets the legend_format of this Target.


        :param legend_format: The legend_format of this Target.
        :type legend_format: str
        """

        self._legend_format = legend_format

    @property
    def measurement(self):
        """Gets the measurement of this Target.

        For InfluxDB

        :return: The measurement of this Target.
        :rtype: str
        """
        return self._measurement

    @measurement.setter
    def measurement(self, measurement):
        """Sets the measurement of this Target.

        For InfluxDB

        :param measurement: The measurement of this Target.
        :type measurement: str
        """

        self._measurement = measurement

    @property
    def metric_column(self):
        """Gets the metric_column of this Target.


        :return: The metric_column of this Target.
        :rtype: str
        """
        return self._metric_column

    @metric_column.setter
    def metric_column(self, metric_column):
        """Sets the metric_column of this Target.


        :param metric_column: The metric_column of this Target.
        :type metric_column: str
        """

        self._metric_column = metric_column

    @property
    def metric_kind(self):
        """Gets the metric_kind of this Target.


        :return: The metric_kind of this Target.
        :rtype: str
        """
        return self._metric_kind

    @metric_kind.setter
    def metric_kind(self, metric_kind):
        """Sets the metric_kind of this Target.


        :param metric_kind: The metric_kind of this Target.
        :type metric_kind: str
        """

        self._metric_kind = metric_kind

    @property
    def metric_name(self):
        """Gets the metric_name of this Target.


        :return: The metric_name of this Target.
        :rtype: str
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this Target.


        :param metric_name: The metric_name of this Target.
        :type metric_name: str
        """

        self._metric_name = metric_name

    @property
    def metric_type(self):
        """Gets the metric_type of this Target.


        :return: The metric_type of this Target.
        :rtype: str
        """
        return self._metric_type

    @metric_type.setter
    def metric_type(self, metric_type):
        """Sets the metric_type of this Target.


        :param metric_type: The metric_type of this Target.
        :type metric_type: str
        """

        self._metric_type = metric_type

    @property
    def metrics(self):
        """Gets the metrics of this Target.


        :return: The metrics of this Target.
        :rtype: List[TargetMetricsInner]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this Target.


        :param metrics: The metrics of this Target.
        :type metrics: List[TargetMetricsInner]
        """

        self._metrics = metrics

    @property
    def namespace(self):
        """Gets the namespace of this Target.

        For CloudWatch

        :return: The namespace of this Target.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this Target.

        For CloudWatch

        :param namespace: The namespace of this Target.
        :type namespace: str
        """

        self._namespace = namespace

    @property
    def per_series_aligner(self):
        """Gets the per_series_aligner of this Target.


        :return: The per_series_aligner of this Target.
        :rtype: str
        """
        return self._per_series_aligner

    @per_series_aligner.setter
    def per_series_aligner(self, per_series_aligner):
        """Sets the per_series_aligner of this Target.


        :param per_series_aligner: The per_series_aligner of this Target.
        :type per_series_aligner: str
        """

        self._per_series_aligner = per_series_aligner

    @property
    def period(self):
        """Gets the period of this Target.


        :return: The period of this Target.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this Target.


        :param period: The period of this Target.
        :type period: str
        """

        self._period = period

    @property
    def project_name(self):
        """Gets the project_name of this Target.

        For the Stackdriver data source. Find out more information at https:/grafana.com/docs/grafana/v6.0/features/datasources/stackdriver/

        :return: The project_name of this Target.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this Target.

        For the Stackdriver data source. Find out more information at https:/grafana.com/docs/grafana/v6.0/features/datasources/stackdriver/

        :param project_name: The project_name of this Target.
        :type project_name: str
        """

        self._project_name = project_name

    @property
    def query(self):
        """Gets the query of this Target.


        :return: The query of this Target.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Target.


        :param query: The query of this Target.
        :type query: str
        """

        self._query = query

    @property
    def raw_query(self):
        """Gets the raw_query of this Target.


        :return: The raw_query of this Target.
        :rtype: bool
        """
        return self._raw_query

    @raw_query.setter
    def raw_query(self, raw_query):
        """Sets the raw_query of this Target.


        :param raw_query: The raw_query of this Target.
        :type raw_query: bool
        """

        self._raw_query = raw_query

    @property
    def raw_sql(self):
        """Gets the raw_sql of this Target.


        :return: The raw_sql of this Target.
        :rtype: str
        """
        return self._raw_sql

    @raw_sql.setter
    def raw_sql(self, raw_sql):
        """Sets the raw_sql of this Target.


        :param raw_sql: The raw_sql of this Target.
        :type raw_sql: str
        """

        self._raw_sql = raw_sql

    @property
    def ref_id(self):
        """Gets the ref_id of this Target.


        :return: The ref_id of this Target.
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id):
        """Sets the ref_id of this Target.


        :param ref_id: The ref_id of this Target.
        :type ref_id: str
        """

        self._ref_id = ref_id

    @property
    def region(self):
        """Gets the region of this Target.


        :return: The region of this Target.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Target.


        :param region: The region of this Target.
        :type region: str
        """

        self._region = region

    @property
    def select(self):
        """Gets the select of this Target.


        :return: The select of this Target.
        :rtype: List[List[TargetGroupInner]]
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this Target.


        :param select: The select of this Target.
        :type select: List[List[TargetGroupInner]]
        """

        self._select = select

    @property
    def statistics(self):
        """Gets the statistics of this Target.


        :return: The statistics of this Target.
        :rtype: List[str]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this Target.


        :param statistics: The statistics of this Target.
        :type statistics: List[str]
        """

        self._statistics = statistics

    @property
    def step(self):
        """Gets the step of this Target.


        :return: The step of this Target.
        :rtype: int
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this Target.


        :param step: The step of this Target.
        :type step: int
        """

        self._step = step

    @property
    def table(self):
        """Gets the table of this Target.

        For PostgreSQL

        :return: The table of this Target.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """Sets the table of this Target.

        For PostgreSQL

        :param table: The table of this Target.
        :type table: str
        """

        self._table = table

    @property
    def target(self):
        """Gets the target of this Target.

        For Graphite

        :return: The target of this Target.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this Target.

        For Graphite

        :param target: The target of this Target.
        :type target: str
        """

        self._target = target

    @property
    def time_column(self):
        """Gets the time_column of this Target.


        :return: The time_column of this Target.
        :rtype: str
        """
        return self._time_column

    @time_column.setter
    def time_column(self, time_column):
        """Sets the time_column of this Target.


        :param time_column: The time_column of this Target.
        :type time_column: str
        """

        self._time_column = time_column

    @property
    def time_field(self):
        """Gets the time_field of this Target.


        :return: The time_field of this Target.
        :rtype: str
        """
        return self._time_field

    @time_field.setter
    def time_field(self, time_field):
        """Sets the time_field of this Target.


        :param time_field: The time_field of this Target.
        :type time_field: str
        """

        self._time_field = time_field

    @property
    def value_type(self):
        """Gets the value_type of this Target.


        :return: The value_type of this Target.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this Target.


        :param value_type: The value_type of this Target.
        :type value_type: str
        """

        self._value_type = value_type

    @property
    def where(self):
        """Gets the where of this Target.


        :return: The where of this Target.
        :rtype: List[TargetWhereInner]
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this Target.


        :param where: The where of this Target.
        :type where: List[TargetWhereInner]
        """

        self._where = where

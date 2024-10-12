from typing import List, Dict
from aiohttp import web

from openapi_server.models.aggregate_type import AggregateType
from openapi_server.models.associate_assets_request import AssociateAssetsRequest
from openapi_server.models.associate_time_series_to_asset_property_request import AssociateTimeSeriesToAssetPropertyRequest
from openapi_server.models.batch_associate_project_assets_request import BatchAssociateProjectAssetsRequest
from openapi_server.models.batch_associate_project_assets_response import BatchAssociateProjectAssetsResponse
from openapi_server.models.batch_disassociate_project_assets_request import BatchDisassociateProjectAssetsRequest
from openapi_server.models.batch_disassociate_project_assets_response import BatchDisassociateProjectAssetsResponse
from openapi_server.models.batch_get_asset_property_aggregates_request import BatchGetAssetPropertyAggregatesRequest
from openapi_server.models.batch_get_asset_property_aggregates_response import BatchGetAssetPropertyAggregatesResponse
from openapi_server.models.batch_get_asset_property_value_history_request import BatchGetAssetPropertyValueHistoryRequest
from openapi_server.models.batch_get_asset_property_value_history_response import BatchGetAssetPropertyValueHistoryResponse
from openapi_server.models.batch_get_asset_property_value_request import BatchGetAssetPropertyValueRequest
from openapi_server.models.batch_get_asset_property_value_response import BatchGetAssetPropertyValueResponse
from openapi_server.models.batch_put_asset_property_value_request import BatchPutAssetPropertyValueRequest
from openapi_server.models.batch_put_asset_property_value_response import BatchPutAssetPropertyValueResponse
from openapi_server.models.create_access_policy_request import CreateAccessPolicyRequest
from openapi_server.models.create_access_policy_response import CreateAccessPolicyResponse
from openapi_server.models.create_asset_model_request import CreateAssetModelRequest
from openapi_server.models.create_asset_model_response import CreateAssetModelResponse
from openapi_server.models.create_asset_request import CreateAssetRequest
from openapi_server.models.create_asset_response import CreateAssetResponse
from openapi_server.models.create_bulk_import_job_request import CreateBulkImportJobRequest
from openapi_server.models.create_bulk_import_job_response import CreateBulkImportJobResponse
from openapi_server.models.create_dashboard_request import CreateDashboardRequest
from openapi_server.models.create_dashboard_response import CreateDashboardResponse
from openapi_server.models.create_gateway_request import CreateGatewayRequest
from openapi_server.models.create_gateway_response import CreateGatewayResponse
from openapi_server.models.create_portal_request import CreatePortalRequest
from openapi_server.models.create_portal_response import CreatePortalResponse
from openapi_server.models.create_project_request import CreateProjectRequest
from openapi_server.models.create_project_response import CreateProjectResponse
from openapi_server.models.delete_asset_model_response import DeleteAssetModelResponse
from openapi_server.models.delete_asset_response import DeleteAssetResponse
from openapi_server.models.delete_portal_response import DeletePortalResponse
from openapi_server.models.describe_access_policy_response import DescribeAccessPolicyResponse
from openapi_server.models.describe_asset_model_response import DescribeAssetModelResponse
from openapi_server.models.describe_asset_property_response import DescribeAssetPropertyResponse
from openapi_server.models.describe_asset_response import DescribeAssetResponse
from openapi_server.models.describe_bulk_import_job_response import DescribeBulkImportJobResponse
from openapi_server.models.describe_dashboard_response import DescribeDashboardResponse
from openapi_server.models.describe_default_encryption_configuration_response import DescribeDefaultEncryptionConfigurationResponse
from openapi_server.models.describe_gateway_capability_configuration_response import DescribeGatewayCapabilityConfigurationResponse
from openapi_server.models.describe_gateway_response import DescribeGatewayResponse
from openapi_server.models.describe_logging_options_response import DescribeLoggingOptionsResponse
from openapi_server.models.describe_portal_response import DescribePortalResponse
from openapi_server.models.describe_project_response import DescribeProjectResponse
from openapi_server.models.describe_storage_configuration_response import DescribeStorageConfigurationResponse
from openapi_server.models.describe_time_series_response import DescribeTimeSeriesResponse
from openapi_server.models.disassociate_assets_request import DisassociateAssetsRequest
from openapi_server.models.get_asset_property_aggregates_response import GetAssetPropertyAggregatesResponse
from openapi_server.models.get_asset_property_value_history_response import GetAssetPropertyValueHistoryResponse
from openapi_server.models.get_asset_property_value_response import GetAssetPropertyValueResponse
from openapi_server.models.get_interpolated_asset_property_values_response import GetInterpolatedAssetPropertyValuesResponse
from openapi_server.models.list_access_policies_response import ListAccessPoliciesResponse
from openapi_server.models.list_asset_model_properties_response import ListAssetModelPropertiesResponse
from openapi_server.models.list_asset_models_response import ListAssetModelsResponse
from openapi_server.models.list_asset_properties_response import ListAssetPropertiesResponse
from openapi_server.models.list_asset_relationships_response import ListAssetRelationshipsResponse
from openapi_server.models.list_assets_response import ListAssetsResponse
from openapi_server.models.list_associated_assets_response import ListAssociatedAssetsResponse
from openapi_server.models.list_bulk_import_jobs_response import ListBulkImportJobsResponse
from openapi_server.models.list_dashboards_response import ListDashboardsResponse
from openapi_server.models.list_gateways_response import ListGatewaysResponse
from openapi_server.models.list_portals_response import ListPortalsResponse
from openapi_server.models.list_project_assets_response import ListProjectAssetsResponse
from openapi_server.models.list_projects_response import ListProjectsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.list_time_series_response import ListTimeSeriesResponse
from openapi_server.models.put_default_encryption_configuration_request import PutDefaultEncryptionConfigurationRequest
from openapi_server.models.put_default_encryption_configuration_response import PutDefaultEncryptionConfigurationResponse
from openapi_server.models.put_logging_options_request import PutLoggingOptionsRequest
from openapi_server.models.put_storage_configuration_request import PutStorageConfigurationRequest
from openapi_server.models.put_storage_configuration_response import PutStorageConfigurationResponse
from openapi_server.models.quality import Quality
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_access_policy_request import UpdateAccessPolicyRequest
from openapi_server.models.update_asset_model_request import UpdateAssetModelRequest
from openapi_server.models.update_asset_model_response import UpdateAssetModelResponse
from openapi_server.models.update_asset_property_request import UpdateAssetPropertyRequest
from openapi_server.models.update_asset_request import UpdateAssetRequest
from openapi_server.models.update_asset_response import UpdateAssetResponse
from openapi_server.models.update_dashboard_request import UpdateDashboardRequest
from openapi_server.models.update_gateway_capability_configuration_request import UpdateGatewayCapabilityConfigurationRequest
from openapi_server.models.update_gateway_capability_configuration_response import UpdateGatewayCapabilityConfigurationResponse
from openapi_server.models.update_gateway_request import UpdateGatewayRequest
from openapi_server.models.update_portal_request import UpdatePortalRequest
from openapi_server.models.update_portal_response import UpdatePortalResponse
from openapi_server.models.update_project_request import UpdateProjectRequest
from openapi_server import util


async def associate_assets(request: web.Request, asset_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_assets

    Associates a child asset with the given parent asset through a hierarchy defined in the parent asset&#39;s model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html\&quot;&gt;Associating assets&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param asset_id: The ID of the parent asset.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes
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
    body = AssociateAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def associate_time_series_to_asset_property(request: web.Request, alias, asset_id, property_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """associate_time_series_to_asset_property

    Associates a time series (data stream) with an asset property.

    :param alias: The alias that identifies the time series.
    :type alias: str
    :param asset_id: The ID of the asset in which the asset property was created.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str
    :param body: 
    :type body: dict | bytes
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
    body = AssociateTimeSeriesToAssetPropertyRequest.from_dict(body)
    return web.Response(status=200)


async def batch_associate_project_assets(request: web.Request, project_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_associate_project_assets

    Associates a group (batch) of assets with an IoT SiteWise Monitor project.

    :param project_id: The ID of the project to which to associate the assets.
    :type project_id: str
    :param body: 
    :type body: dict | bytes
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
    body = BatchAssociateProjectAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_disassociate_project_assets(request: web.Request, project_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_disassociate_project_assets

    Disassociates a group (batch) of assets from an IoT SiteWise Monitor project.

    :param project_id: The ID of the project from which to disassociate the assets.
    :type project_id: str
    :param body: 
    :type body: dict | bytes
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
    body = BatchDisassociateProjectAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_asset_property_aggregates(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """batch_get_asset_property_aggregates

    Gets aggregated values (for example, average, minimum, and maximum) for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\&quot;&gt;Querying aggregates&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
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

    """
    body = BatchGetAssetPropertyAggregatesRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_asset_property_value(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None) -> web.Response:
    """batch_get_asset_property_value

    Gets the current value for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\&quot;&gt;Querying current values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
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

    """
    body = BatchGetAssetPropertyValueRequest.from_dict(body)
    return web.Response(status=200)


async def batch_get_asset_property_value_history(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, max_results=None, next_token=None) -> web.Response:
    """batch_get_asset_property_value_history

    Gets the historical values for one or more asset properties. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\&quot;&gt;Querying historical values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
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

    """
    body = BatchGetAssetPropertyValueHistoryRequest.from_dict(body)
    return web.Response(status=200)


async def batch_put_asset_property_value(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """batch_put_asset_property_value

    &lt;p&gt;Sends a list of asset property values to IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html\&quot;&gt;Ingesting data using the API&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;With respect to Unix epoch time, IoT SiteWise accepts only TQVs that have a timestamp of no more than 7 days in the past and no more than 10 minutes in the future. IoT SiteWise rejects timestamps outside of the inclusive range of [-7 days, +10 minutes] and returns a &lt;code&gt;TimestampOutOfRangeException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;For each asset property, IoT SiteWise overwrites TQVs with duplicate timestamps unless the newer TQV has a different quality. For example, if you store a TQV &lt;code&gt;{T1, GOOD, V1}&lt;/code&gt;, then storing &lt;code&gt;{T1, GOOD, V2}&lt;/code&gt; replaces the existing TQV.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;IoT SiteWise authorizes access to each &lt;code&gt;BatchPutAssetPropertyValue&lt;/code&gt; entry individually. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action\&quot;&gt;BatchPutAssetPropertyValue authorization&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt;

    :param body: 
    :type body: dict | bytes
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
    body = BatchPutAssetPropertyValueRequest.from_dict(body)
    return web.Response(status=200)


async def create_access_policy(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_access_policy

    Creates an access policy that grants the specified identity (IAM Identity Center user, IAM Identity Center group, or IAM user) access to the specified IoT SiteWise Monitor portal or project resource.

    :param body: 
    :type body: dict | bytes
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
    body = CreateAccessPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def create_asset(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_asset

    Creates an asset from an existing asset model. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html\&quot;&gt;Creating assets&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
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
    body = CreateAssetRequest.from_dict(body)
    return web.Response(status=200)


async def create_asset_model(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_asset_model

    Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model&#39;s property and hierarchy definitions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html\&quot;&gt;Defining asset models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
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
    body = CreateAssetModelRequest.from_dict(body)
    return web.Response(status=200)


async def create_bulk_import_job(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_bulk_import_job

    &lt;p&gt;Defines a job to ingest data to IoT SiteWise from Amazon S3. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html\&quot;&gt;Create a bulk import job (CLI)&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;You must enable IoT SiteWise to export data to Amazon S3 before you create a bulk import job. For more information about how to configure storage settings, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html\&quot;&gt;PutStorageConfiguration&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

    :param body: 
    :type body: dict | bytes
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
    body = CreateBulkImportJobRequest.from_dict(body)
    return web.Response(status=200)


async def create_dashboard(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_dashboard

    Creates a dashboard in an IoT SiteWise Monitor project.

    :param body: 
    :type body: dict | bytes
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
    body = CreateDashboardRequest.from_dict(body)
    return web.Response(status=200)


async def create_gateway(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_gateway

    Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to IoT SiteWise. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html\&quot;&gt;Ingesting data using a gateway&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
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
    body = CreateGatewayRequest.from_dict(body)
    return web.Response(status=200)


async def create_portal(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_portal

    &lt;p&gt;Creates a portal, which can contain projects and dashboards. IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins\&quot;&gt;Adding or removing portal administrators&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
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
    body = CreatePortalRequest.from_dict(body)
    return web.Response(status=200)


async def create_project(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """create_project

    &lt;p&gt;Creates a project in the specified portal.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Make sure that the project name and description don&#39;t contain confidential information.&lt;/p&gt; &lt;/note&gt;

    :param body: 
    :type body: dict | bytes
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
    body = CreateProjectRequest.from_dict(body)
    return web.Response(status=200)


async def delete_access_policy(request: web.Request, access_policy_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_access_policy

    Deletes an access policy that grants the specified identity access to the specified IoT SiteWise Monitor resource. You can use this operation to revoke access to an IoT SiteWise Monitor resource.

    :param access_policy_id: The ID of the access policy to be deleted.
    :type access_policy_id: str
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
    :param client_token: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required.
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_asset(request: web.Request, asset_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_asset

    &lt;p&gt;Deletes an asset. This action can&#39;t be undone. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\&quot;&gt;Deleting assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can&#39;t delete an asset that&#39;s associated to another asset. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateAssets.html\&quot;&gt;DisassociateAssets&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

    :param asset_id: The ID of the asset to delete.
    :type asset_id: str
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
    :param client_token: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required.
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_asset_model(request: web.Request, asset_model_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_asset_model

    Deletes an asset model. This action can&#39;t be undone. You must delete all assets created from an asset model before you can delete the model. Also, you can&#39;t delete an asset model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html\&quot;&gt;Deleting assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param asset_model_id: The ID of the asset model to delete.
    :type asset_model_id: str
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
    :param client_token: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required.
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_dashboard(request: web.Request, dashboard_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_dashboard

    Deletes a dashboard from IoT SiteWise Monitor.

    :param dashboard_id: The ID of the dashboard to delete.
    :type dashboard_id: str
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
    :param client_token: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required.
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_gateway(request: web.Request, gateway_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """delete_gateway

    Deletes a gateway from IoT SiteWise. When you delete a gateway, some of the gateway&#39;s files remain in your gateway&#39;s file system.

    :param gateway_id: The ID of the gateway to delete.
    :type gateway_id: str
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


async def delete_portal(request: web.Request, portal_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_portal

    Deletes a portal from IoT SiteWise Monitor.

    :param portal_id: The ID of the portal to delete.
    :type portal_id: str
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
    :param client_token: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required.
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_project(request: web.Request, project_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, client_token=None) -> web.Response:
    """delete_project

    Deletes a project from IoT SiteWise Monitor.

    :param project_id: The ID of the project.
    :type project_id: str
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
    :param client_token: A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don&#39;t reuse this client token if a new idempotent request is required.
    :type client_token: str

    """
    return web.Response(status=200)


async def delete_time_series(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, alias=None, asset_id=None, property_id=None) -> web.Response:
    """delete_time_series

    &lt;p&gt;Deletes a time series (data stream). If you delete a time series that&#39;s associated with an asset property, the asset property still exists, but the time series will no longer be associated with this asset property.&lt;/p&gt; &lt;p&gt;To identify a time series, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the time series isn&#39;t associated with an asset property, specify the &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the time series is associated with an asset property, specify one of the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; that identifies the asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

    :param body: 
    :type body: dict | bytes
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
    :param alias: The alias that identifies the time series.
    :type alias: str
    :param asset_id: The ID of the asset in which the asset property was created.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str

    """
    body = AssociateTimeSeriesToAssetPropertyRequest.from_dict(body)
    return web.Response(status=200)


async def describe_access_policy(request: web.Request, access_policy_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_access_policy

    Describes an access policy, which specifies an identity&#39;s access to an IoT SiteWise Monitor portal or project.

    :param access_policy_id: The ID of the access policy.
    :type access_policy_id: str
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


async def describe_asset(request: web.Request, asset_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, exclude_properties=None) -> web.Response:
    """describe_asset

    Retrieves information about an asset.

    :param asset_id: The ID of the asset.
    :type asset_id: str
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
    :param exclude_properties:  Whether or not to exclude asset properties from the response. 
    :type exclude_properties: bool

    """
    return web.Response(status=200)


async def describe_asset_model(request: web.Request, asset_model_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, exclude_properties=None) -> web.Response:
    """describe_asset_model

    Retrieves information about an asset model.

    :param asset_model_id: The ID of the asset model.
    :type asset_model_id: str
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
    :param exclude_properties:  Whether or not to exclude asset model properties from the response. 
    :type exclude_properties: bool

    """
    return web.Response(status=200)


async def describe_asset_property(request: web.Request, asset_id, property_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_asset_property

    &lt;p&gt;Retrieves information about an asset property.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you call this operation for an attribute property, this response includes the default attribute value that you define in the asset model. If you update the default value in the model, this operation&#39;s response includes the new default value.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This operation doesn&#39;t return the value of the asset property. To get the value of an asset property, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html\&quot;&gt;GetAssetPropertyValue&lt;/a&gt;.&lt;/p&gt;

    :param asset_id: The ID of the asset.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str
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


async def describe_bulk_import_job(request: web.Request, job_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_bulk_import_job

    Retrieves information about a bulk import job request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/DescribeBulkImportJob.html\&quot;&gt;Describe a bulk import job (CLI)&lt;/a&gt; in the &lt;i&gt;Amazon Simple Storage Service User Guide&lt;/i&gt;.

    :param job_id: The ID of the job.
    :type job_id: str
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


async def describe_dashboard(request: web.Request, dashboard_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_dashboard

    Retrieves information about a dashboard.

    :param dashboard_id: The ID of the dashboard.
    :type dashboard_id: str
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


async def describe_default_encryption_configuration(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_default_encryption_configuration

    Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified Region. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\&quot;&gt;Key management&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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


async def describe_gateway(request: web.Request, gateway_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_gateway

    Retrieves information about a gateway.

    :param gateway_id: The ID of the gateway device.
    :type gateway_id: str
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


async def describe_gateway_capability_configuration(request: web.Request, gateway_id, capability_namespace, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_gateway_capability_configuration

    Retrieves information about a gateway capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html\&quot;&gt;DescribeGateway&lt;/a&gt;.

    :param gateway_id: The ID of the gateway that defines the capability configuration.
    :type gateway_id: str
    :param capability_namespace: The namespace of the capability configuration. For example, if you configure OPC-UA sources from the IoT SiteWise console, your OPC-UA capability configuration has the namespace &lt;code&gt;iotsitewise:opcuacollector:version&lt;/code&gt;, where &lt;code&gt;version&lt;/code&gt; is a number such as &lt;code&gt;1&lt;/code&gt;.
    :type capability_namespace: str
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


async def describe_logging_options(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_logging_options

    Retrieves the current IoT SiteWise logging options.

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


async def describe_portal(request: web.Request, portal_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_portal

    Retrieves information about a portal.

    :param portal_id: The ID of the portal.
    :type portal_id: str
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


async def describe_project(request: web.Request, project_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_project

    Retrieves information about a project.

    :param project_id: The ID of the project.
    :type project_id: str
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


async def describe_storage_configuration(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """describe_storage_configuration

    Retrieves information about the storage configuration for IoT SiteWise.

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


async def describe_time_series(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, alias=None, asset_id=None, property_id=None) -> web.Response:
    """describe_time_series

    &lt;p&gt;Retrieves information about a time series (data stream).&lt;/p&gt; &lt;p&gt;To identify a time series, do one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If the time series isn&#39;t associated with an asset property, specify the &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If the time series is associated with an asset property, specify one of the following: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;alias&lt;/code&gt; of the time series.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; that identifies the asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

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
    :param alias: The alias that identifies the time series.
    :type alias: str
    :param asset_id: The ID of the asset in which the asset property was created.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str

    """
    return web.Response(status=200)


async def disassociate_assets(request: web.Request, asset_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_assets

    Disassociates a child asset from the given parent asset through a hierarchy defined in the parent asset&#39;s model.

    :param asset_id: The ID of the parent asset from which to disassociate the child asset.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes
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
    body = DisassociateAssetsRequest.from_dict(body)
    return web.Response(status=200)


async def disassociate_time_series_from_asset_property(request: web.Request, alias, asset_id, property_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """disassociate_time_series_from_asset_property

    Disassociates a time series (data stream) from an asset property.

    :param alias: The alias that identifies the time series.
    :type alias: str
    :param asset_id: The ID of the asset in which the asset property was created.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str
    :param body: 
    :type body: dict | bytes
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
    body = AssociateTimeSeriesToAssetPropertyRequest.from_dict(body)
    return web.Response(status=200)


async def get_asset_property_aggregates(request: web.Request, aggregate_types, resolution, start_date, end_date, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, asset_id=None, property_id=None, property_alias=None, qualities=None, time_ordering=None, next_token=None, max_results=None) -> web.Response:
    """get_asset_property_aggregates

    &lt;p&gt;Gets aggregated values for an asset property. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates\&quot;&gt;Querying aggregates&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param aggregate_types: The data aggregating function.
    :type aggregate_types: list | bytes
    :param resolution: The time interval over which to aggregate data.
    :type resolution: str
    :param start_date: The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
    :type start_date: str
    :param end_date: The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
    :type end_date: str
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
    :param asset_id: The ID of the asset.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str
    :param property_alias: The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.
    :type property_alias: str
    :param qualities: The quality by which to filter asset data.
    :type qualities: list | bytes
    :param time_ordering: &lt;p&gt;The chronological sorting order of the requested information.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;ASCENDING&lt;/code&gt; &lt;/p&gt;
    :type time_ordering: str
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The size of the result set is equal to 1 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of data points in the result set is equal to the value of &lt;code&gt;maxResults&lt;/code&gt;. The maximum value of &lt;code&gt;maxResults&lt;/code&gt; is 250.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type max_results: int

    """
    aggregate_types = [AggregateType.from_dict(d) for d in aggregate_types]
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    qualities = [Quality.from_dict(d) for d in qualities]
    return web.Response(status=200)


async def get_asset_property_value(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, asset_id=None, property_id=None, property_alias=None) -> web.Response:
    """get_asset_property_value

    &lt;p&gt;Gets an asset property&#39;s current value. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values\&quot;&gt;Querying current values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    :param asset_id: The ID of the asset.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str
    :param property_alias: The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.
    :type property_alias: str

    """
    return web.Response(status=200)


async def get_asset_property_value_history(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, asset_id=None, property_id=None, property_alias=None, start_date=None, end_date=None, qualities=None, time_ordering=None, next_token=None, max_results=None) -> web.Response:
    """get_asset_property_value_history

    &lt;p&gt;Gets the history of an asset property&#39;s values. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values\&quot;&gt;Querying historical values&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

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
    :param asset_id: The ID of the asset.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str
    :param property_alias: The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.
    :type property_alias: str
    :param start_date: The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.
    :type start_date: str
    :param end_date: The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.
    :type end_date: str
    :param qualities: The quality by which to filter asset data.
    :type qualities: list | bytes
    :param time_ordering: &lt;p&gt;The chronological sorting order of the requested information.&lt;/p&gt; &lt;p&gt;Default: &lt;code&gt;ASCENDING&lt;/code&gt; &lt;/p&gt;
    :type time_ordering: str
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The size of the result set is equal to 4 MB.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The number of data points in the result set is equal to the value of &lt;code&gt;maxResults&lt;/code&gt;. The maximum value of &lt;code&gt;maxResults&lt;/code&gt; is 20000.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type max_results: int

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    qualities = [Quality.from_dict(d) for d in qualities]
    return web.Response(status=200)


async def get_interpolated_asset_property_values(request: web.Request, start_time_in_seconds, end_time_in_seconds, quality, interval_in_seconds, type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, asset_id=None, property_id=None, property_alias=None, start_time_offset_in_nanos=None, end_time_offset_in_nanos=None, next_token=None, max_results=None, interval_window_in_seconds=None) -> web.Response:
    """get_interpolated_asset_property_values

    &lt;p&gt;Get interpolated values for an asset property for a specified time interval, during a period of time. If your time series is missing data points during the specified time interval, you can use interpolation to estimate the missing data.&lt;/p&gt; &lt;p&gt;For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days.&lt;/p&gt; &lt;p&gt;To identify an asset property, you must specify one of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;assetId&lt;/code&gt; and &lt;code&gt;propertyId&lt;/code&gt; of an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;A &lt;code&gt;propertyAlias&lt;/code&gt;, which is a data stream alias (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). To define an asset property&#39;s alias, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html\&quot;&gt;UpdateAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param start_time_in_seconds: The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.
    :type start_time_in_seconds: int
    :param end_time_in_seconds: The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.
    :type end_time_in_seconds: int
    :param quality: The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.
    :type quality: str
    :param interval_in_seconds: The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.
    :type interval_in_seconds: int
    :param type: &lt;p&gt;The interpolation type.&lt;/p&gt; &lt;p&gt;Valid values: &lt;code&gt;LINEAR_INTERPOLATION | LOCF_INTERPOLATION&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LINEAR_INTERPOLATION&lt;/code&gt; – Estimates missing data using &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/Linear_interpolation\&quot;&gt;linear interpolation&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;LOCF_INTERPOLATION&lt;/code&gt; – Estimates missing data using last observation carried forward interpolation&lt;/p&gt; &lt;p&gt;If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.&lt;/p&gt; &lt;p&gt;For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn&#39;t found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type type: str
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
    :param asset_id: The ID of the asset.
    :type asset_id: str
    :param property_id: The ID of the asset property.
    :type property_id: str
    :param property_alias: The alias that identifies the property, such as an OPC-UA server data stream path (for example, &lt;code&gt;/company/windfarm/3/turbine/7/temperature&lt;/code&gt;). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html\&quot;&gt;Mapping industrial data streams to asset properties&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.
    :type property_alias: str
    :param start_time_offset_in_nanos: The nanosecond offset converted from &lt;code&gt;startTimeInSeconds&lt;/code&gt;.
    :type start_time_offset_in_nanos: int
    :param end_time_offset_in_nanos: The nanosecond offset converted from &lt;code&gt;endTimeInSeconds&lt;/code&gt;.
    :type end_time_offset_in_nanos: int
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: The maximum number of results to return for each paginated request. If not specified, the default value is 10.
    :type max_results: int
    :param interval_window_in_seconds: &lt;p&gt;The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;If you specify a value for the &lt;code&gt;intervalWindowInSeconds&lt;/code&gt; parameter, the value for the &lt;code&gt;type&lt;/code&gt; parameter must be &lt;code&gt;LINEAR_INTERPOLATION&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If a data point isn&#39;t found during the specified query window, IoT SiteWise won&#39;t return an interpolated value for the interval. This indicates that there&#39;s a gap in the ingested data points.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. &lt;/p&gt;
    :type interval_window_in_seconds: int

    """
    return web.Response(status=200)


async def list_access_policies(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, identity_type=None, identity_id=None, resource_type=None, resource_id=None, iam_arn=None, next_token=None, max_results=None) -> web.Response:
    """list_access_policies

    Retrieves a paginated list of access policies for an identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user) or an IoT SiteWise Monitor resource (a portal or project).

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
    :param identity_type: The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify &lt;code&gt;identityId&lt;/code&gt;.
    :type identity_type: str
    :param identity_id: The ID of the identity. This parameter is required if you specify &lt;code&gt;USER&lt;/code&gt; or &lt;code&gt;GROUP&lt;/code&gt; for &lt;code&gt;identityType&lt;/code&gt;.
    :type identity_id: str
    :param resource_type: The type of resource (portal or project). This parameter is required if you specify &lt;code&gt;resourceId&lt;/code&gt;.
    :type resource_type: str
    :param resource_id: The ID of the resource. This parameter is required if you specify &lt;code&gt;resourceType&lt;/code&gt;.
    :type resource_id: str
    :param iam_arn: The ARN of the IAM user. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html\&quot;&gt;IAM ARNs&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. This parameter is required if you specify &lt;code&gt;IAM&lt;/code&gt; for &lt;code&gt;identityType&lt;/code&gt;.
    :type iam_arn: str
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_asset_model_properties(request: web.Request, asset_model_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, filter=None) -> web.Response:
    """list_asset_model_properties

    Retrieves a paginated list of properties associated with an asset model. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.

    :param asset_model_id: The ID of the asset model.
    :type asset_model_id: str
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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: The maximum number of results to return for each paginated request. If not specified, the default value is 50.
    :type max_results: int
    :param filter: &lt;p&gt; Filters the requested list of asset model properties. You can choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all asset model properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASE&lt;/code&gt; – The list includes only base asset model properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;BASE&lt;/code&gt; &lt;/p&gt;
    :type filter: str

    """
    return web.Response(status=200)


async def list_asset_models(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_asset_models

    Retrieves a paginated list of summaries of all asset models.

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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_asset_properties(request: web.Request, asset_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, filter=None) -> web.Response:
    """list_asset_properties

    Retrieves a paginated list of properties associated with an asset. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.

    :param asset_id: The ID of the asset.
    :type asset_id: str
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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: The maximum number of results to return for each paginated request. If not specified, the default value is 50.
    :type max_results: int
    :param filter: &lt;p&gt; Filters the requested list of asset properties. You can choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all asset properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;BASE&lt;/code&gt; – The list includes only base asset properties for a given asset model ID. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;BASE&lt;/code&gt; &lt;/p&gt;
    :type filter: str

    """
    return web.Response(status=200)


async def list_asset_relationships(request: web.Request, asset_id, traversal_type, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_asset_relationships

    Retrieves a paginated list of asset relationships for an asset. You can use this operation to identify an asset&#39;s root asset and all associated assets between that asset and its root.

    :param asset_id: The ID of the asset.
    :type asset_id: str
    :param traversal_type: &lt;p&gt;The type of traversal to use to identify asset relationships. Choose the following option:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PATH_TO_ROOT&lt;/code&gt; – Identify the asset&#39;s parent assets up to the root asset. The asset that you specify in &lt;code&gt;assetId&lt;/code&gt; is the first result in the list of &lt;code&gt;assetRelationshipSummaries&lt;/code&gt;, and the root asset is the last result.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type traversal_type: str
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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: The maximum number of results to return for each paginated request.
    :type max_results: int

    """
    return web.Response(status=200)


async def list_assets(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, asset_model_id=None, filter=None) -> web.Response:
    """list_assets

    &lt;p&gt;Retrieves a paginated list of asset summaries.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List assets based on a specific asset model.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List top-level assets.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can&#39;t use this operation to list all assets. To retrieve summaries for all of your assets, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html\&quot;&gt;ListAssetModels&lt;/a&gt; to get all of your asset model IDs. Then, use ListAssets to get all assets for each asset model.&lt;/p&gt;

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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int
    :param asset_model_id: The ID of the asset model by which to filter the list of assets. This parameter is required if you choose &lt;code&gt;ALL&lt;/code&gt; for &lt;code&gt;filter&lt;/code&gt;.
    :type asset_model_id: str
    :param filter: &lt;p&gt;The filter for the requested list of assets. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ALL&lt;/code&gt; – The list includes all assets for a given asset model ID. The &lt;code&gt;assetModelId&lt;/code&gt; parameter is required if you filter by &lt;code&gt;ALL&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;TOP_LEVEL&lt;/code&gt; – The list includes only top-level assets in the asset hierarchy tree.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;ALL&lt;/code&gt; &lt;/p&gt;
    :type filter: str

    """
    return web.Response(status=200)


async def list_associated_assets(request: web.Request, asset_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, hierarchy_id=None, traversal_direction=None, next_token=None, max_results=None) -> web.Response:
    """list_associated_assets

    &lt;p&gt;Retrieves a paginated list of associated assets.&lt;/p&gt; &lt;p&gt;You can use this operation to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;List child assets associated to a parent asset by a hierarchy that you specify.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;List an asset&#39;s parent asset.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

    :param asset_id: The ID of the asset to query.
    :type asset_id: str
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
    :param hierarchy_id: &lt;p&gt;The ID of the hierarchy by which child assets are associated to the asset. To find a hierarchy ID, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAsset.html\&quot;&gt;DescribeAsset&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\&quot;&gt;DescribeAssetModel&lt;/a&gt; operations. This parameter is required if you choose &lt;code&gt;CHILD&lt;/code&gt; for &lt;code&gt;traversalDirection&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html\&quot;&gt;Asset hierarchies&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt;
    :type hierarchy_id: str
    :param traversal_direction: &lt;p&gt;The direction to list associated assets. Choose one of the following options:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;CHILD&lt;/code&gt; – The list includes all child assets associated to the asset. The &lt;code&gt;hierarchyId&lt;/code&gt; parameter is required if you choose &lt;code&gt;CHILD&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;PARENT&lt;/code&gt; – The list includes the asset&#39;s parent asset.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Default: &lt;code&gt;CHILD&lt;/code&gt; &lt;/p&gt;
    :type traversal_direction: str
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_bulk_import_jobs(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, filter=None) -> web.Response:
    """list_bulk_import_jobs

    Retrieves a paginated list of bulk import job requests. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ListBulkImportJobs.html\&quot;&gt;List bulk import jobs (CLI)&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: The maximum number of results to return for each paginated request.
    :type max_results: int
    :param filter: You can use a filter to select the bulk import jobs that you want to retrieve.
    :type filter: str

    """
    return web.Response(status=200)


async def list_dashboards(request: web.Request, project_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_dashboards

    Retrieves a paginated list of dashboards for an IoT SiteWise Monitor project.

    :param project_id: The ID of the project.
    :type project_id: str
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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_gateways(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_gateways

    Retrieves a paginated list of gateways.

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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_portals(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_portals

    Retrieves a paginated list of IoT SiteWise Monitor portals.

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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_project_assets(request: web.Request, project_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_project_assets

    Retrieves a paginated list of assets associated with an IoT SiteWise Monitor project.

    :param project_id: The ID of the project.
    :type project_id: str
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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_projects(request: web.Request, portal_id, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None) -> web.Response:
    """list_projects

    Retrieves a paginated list of projects for an IoT SiteWise Monitor portal.

    :param portal_id: The ID of the portal.
    :type portal_id: str
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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: &lt;p&gt;The maximum number of results to return for each paginated request.&lt;/p&gt; &lt;p&gt;Default: 50&lt;/p&gt;
    :type max_results: int

    """
    return web.Response(status=200)


async def list_tags_for_resource(request: web.Request, resource_arn, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """list_tags_for_resource

    Retrieves the list of tags for an IoT SiteWise resource.

    :param resource_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource.
    :type resource_arn: str
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


async def list_time_series(request: web.Request, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None, next_token=None, max_results=None, asset_id=None, alias_prefix=None, time_series_type=None) -> web.Response:
    """list_time_series

    Retrieves a paginated list of time series (data streams).

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
    :param next_token: The token to be used for the next set of paginated results.
    :type next_token: str
    :param max_results: The maximum number of results to return for each paginated request.
    :type max_results: int
    :param asset_id: The ID of the asset in which the asset property was created.
    :type asset_id: str
    :param alias_prefix: The alias prefix of the time series.
    :type alias_prefix: str
    :param time_series_type: &lt;p&gt;The type of the time series. The time series type can be one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ASSOCIATED&lt;/code&gt; – The time series is associated with an asset property.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;DISASSOCIATED&lt;/code&gt; – The time series isn&#39;t associated with any asset property.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    :type time_series_type: str

    """
    return web.Response(status=200)


async def put_default_encryption_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_default_encryption_configuration

    Sets the default encryption configuration for the Amazon Web Services account. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html\&quot;&gt;Key management&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param body: 
    :type body: dict | bytes
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
    body = PutDefaultEncryptionConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def put_logging_options(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_logging_options

    Sets logging options for IoT SiteWise.

    :param body: 
    :type body: dict | bytes
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
    body = PutLoggingOptionsRequest.from_dict(body)
    return web.Response(status=200)


async def put_storage_configuration(request: web.Request, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """put_storage_configuration

    Configures storage settings for IoT SiteWise.

    :param body: 
    :type body: dict | bytes
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
    body = PutStorageConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def tag_resource(request: web.Request, resource_arn, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """tag_resource

    Adds tags to an IoT SiteWise resource. If a tag already exists for the resource, this operation updates the tag&#39;s value.

    :param resource_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to tag.
    :type resource_arn: str
    :param body: 
    :type body: dict | bytes
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
    body = TagResourceRequest.from_dict(body)
    return web.Response(status=200)


async def untag_resource(request: web.Request, resource_arn, tag_keys, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """untag_resource

    Removes a tag from an IoT SiteWise resource.

    :param resource_arn: The &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\&quot;&gt;ARN&lt;/a&gt; of the resource to untag.
    :type resource_arn: str
    :param tag_keys: A list of keys for tags to remove from the resource.
    :type tag_keys: List[str]
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


async def update_access_policy(request: web.Request, access_policy_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_access_policy

    Updates an existing access policy that specifies an identity&#39;s access to an IoT SiteWise Monitor portal or project resource.

    :param access_policy_id: The ID of the access policy.
    :type access_policy_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateAccessPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_asset(request: web.Request, asset_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_asset

    Updates an asset&#39;s name. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\&quot;&gt;Updating assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.

    :param asset_id: The ID of the asset to update.
    :type asset_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateAssetRequest.from_dict(body)
    return web.Response(status=200)


async def update_asset_model(request: web.Request, asset_model_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_asset_model

    &lt;p&gt;Updates an asset model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model&#39;s property and hierarchy definitions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html\&quot;&gt;Updating assets and models&lt;/a&gt; in the &lt;i&gt;IoT SiteWise User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation overwrites the existing model with the provided model. To avoid deleting your asset model&#39;s properties or hierarchies, you must include their IDs and definitions in the updated asset model payload. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModel.html\&quot;&gt;DescribeAssetModel&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you remove a property from an asset model, IoT SiteWise deletes all previous data for that property. If you remove a hierarchy definition from an asset model, IoT SiteWise disassociates every asset associated with that hierarchy. You can&#39;t change the type or data type of an existing property.&lt;/p&gt; &lt;/important&gt;

    :param asset_model_id: The ID of the asset model to update.
    :type asset_model_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateAssetModelRequest.from_dict(body)
    return web.Response(status=200)


async def update_asset_property(request: web.Request, asset_id, property_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_asset_property

    &lt;p&gt;Updates an asset property&#39;s alias and notification state.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation overwrites the property&#39;s existing alias and notification state. To keep your existing property&#39;s alias or notification state, you must include the existing values in the UpdateAssetProperty request. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html\&quot;&gt;DescribeAssetProperty&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt;

    :param asset_id: The ID of the asset to be updated.
    :type asset_id: str
    :param property_id: The ID of the asset property to be updated.
    :type property_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateAssetPropertyRequest.from_dict(body)
    return web.Response(status=200)


async def update_dashboard(request: web.Request, dashboard_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_dashboard

    Updates an IoT SiteWise Monitor dashboard.

    :param dashboard_id: The ID of the dashboard to update.
    :type dashboard_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateDashboardRequest.from_dict(body)
    return web.Response(status=200)


async def update_gateway(request: web.Request, gateway_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_gateway

    Updates a gateway&#39;s name.

    :param gateway_id: The ID of the gateway to update.
    :type gateway_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateGatewayRequest.from_dict(body)
    return web.Response(status=200)


async def update_gateway_capability_configuration(request: web.Request, gateway_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_gateway_capability_configuration

    Updates a gateway capability configuration or defines a new capability configuration. Each gateway capability defines data sources for a gateway. A capability configuration can contain multiple data source configurations. If you define OPC-UA sources for a gateway in the IoT SiteWise console, all of your OPC-UA sources are stored in one capability configuration. To list all capability configurations for a gateway, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGateway.html\&quot;&gt;DescribeGateway&lt;/a&gt;.

    :param gateway_id: The ID of the gateway to be updated.
    :type gateway_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateGatewayCapabilityConfigurationRequest.from_dict(body)
    return web.Response(status=200)


async def update_portal(request: web.Request, portal_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_portal

    Updates an IoT SiteWise Monitor portal.

    :param portal_id: The ID of the portal to update.
    :type portal_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdatePortalRequest.from_dict(body)
    return web.Response(status=200)


async def update_project(request: web.Request, project_id, body, x_amz_content_sha256=None, x_amz_date=None, x_amz_algorithm=None, x_amz_credential=None, x_amz_security_token=None, x_amz_signature=None, x_amz_signed_headers=None) -> web.Response:
    """update_project

    Updates an IoT SiteWise Monitor project.

    :param project_id: The ID of the project to update.
    :type project_id: str
    :param body: 
    :type body: dict | bytes
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
    body = UpdateProjectRequest.from_dict(body)
    return web.Response(status=200)

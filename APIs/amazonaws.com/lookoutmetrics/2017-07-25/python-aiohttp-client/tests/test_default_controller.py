# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.activate_anomaly_detector_request import ActivateAnomalyDetectorRequest
from openapi_server.models.back_test_anomaly_detector_request import BackTestAnomalyDetectorRequest
from openapi_server.models.create_alert_request import CreateAlertRequest
from openapi_server.models.create_alert_response import CreateAlertResponse
from openapi_server.models.create_anomaly_detector_request import CreateAnomalyDetectorRequest
from openapi_server.models.create_anomaly_detector_response import CreateAnomalyDetectorResponse
from openapi_server.models.create_metric_set_request import CreateMetricSetRequest
from openapi_server.models.create_metric_set_response import CreateMetricSetResponse
from openapi_server.models.delete_alert_request import DeleteAlertRequest
from openapi_server.models.delete_anomaly_detector_request import DeleteAnomalyDetectorRequest
from openapi_server.models.describe_alert_request import DescribeAlertRequest
from openapi_server.models.describe_alert_response import DescribeAlertResponse
from openapi_server.models.describe_anomaly_detection_executions_request import DescribeAnomalyDetectionExecutionsRequest
from openapi_server.models.describe_anomaly_detection_executions_response import DescribeAnomalyDetectionExecutionsResponse
from openapi_server.models.describe_anomaly_detector_request import DescribeAnomalyDetectorRequest
from openapi_server.models.describe_anomaly_detector_response import DescribeAnomalyDetectorResponse
from openapi_server.models.describe_metric_set_request import DescribeMetricSetRequest
from openapi_server.models.describe_metric_set_response import DescribeMetricSetResponse
from openapi_server.models.detect_metric_set_config_request import DetectMetricSetConfigRequest
from openapi_server.models.detect_metric_set_config_response import DetectMetricSetConfigResponse
from openapi_server.models.get_anomaly_group_request import GetAnomalyGroupRequest
from openapi_server.models.get_anomaly_group_response import GetAnomalyGroupResponse
from openapi_server.models.get_data_quality_metrics_request import GetDataQualityMetricsRequest
from openapi_server.models.get_data_quality_metrics_response import GetDataQualityMetricsResponse
from openapi_server.models.get_feedback_request import GetFeedbackRequest
from openapi_server.models.get_feedback_response import GetFeedbackResponse
from openapi_server.models.get_sample_data_request import GetSampleDataRequest
from openapi_server.models.get_sample_data_response import GetSampleDataResponse
from openapi_server.models.list_alerts_request import ListAlertsRequest
from openapi_server.models.list_alerts_response import ListAlertsResponse
from openapi_server.models.list_anomaly_detectors_request import ListAnomalyDetectorsRequest
from openapi_server.models.list_anomaly_detectors_response import ListAnomalyDetectorsResponse
from openapi_server.models.list_anomaly_group_related_metrics_request import ListAnomalyGroupRelatedMetricsRequest
from openapi_server.models.list_anomaly_group_related_metrics_response import ListAnomalyGroupRelatedMetricsResponse
from openapi_server.models.list_anomaly_group_summaries_request import ListAnomalyGroupSummariesRequest
from openapi_server.models.list_anomaly_group_summaries_response import ListAnomalyGroupSummariesResponse
from openapi_server.models.list_anomaly_group_time_series_request import ListAnomalyGroupTimeSeriesRequest
from openapi_server.models.list_anomaly_group_time_series_response import ListAnomalyGroupTimeSeriesResponse
from openapi_server.models.list_metric_sets_request import ListMetricSetsRequest
from openapi_server.models.list_metric_sets_response import ListMetricSetsResponse
from openapi_server.models.list_tags_for_resource_response import ListTagsForResourceResponse
from openapi_server.models.put_feedback_request import PutFeedbackRequest
from openapi_server.models.tag_resource_request import TagResourceRequest
from openapi_server.models.update_alert_request import UpdateAlertRequest
from openapi_server.models.update_alert_response import UpdateAlertResponse
from openapi_server.models.update_anomaly_detector_request import UpdateAnomalyDetectorRequest
from openapi_server.models.update_anomaly_detector_response import UpdateAnomalyDetectorResponse
from openapi_server.models.update_metric_set_request import UpdateMetricSetRequest
from openapi_server.models.update_metric_set_response import UpdateMetricSetResponse


pytestmark = pytest.mark.asyncio

async def test_activate_anomaly_detector(client):
    """Test case for activate_anomaly_detector

    
    """
    body = {"AnomalyDetectorArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ActivateAnomalyDetector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_back_test_anomaly_detector(client):
    """Test case for back_test_anomaly_detector

    
    """
    body = {"AnomalyDetectorArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/BackTestAnomalyDetector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_alert(client):
    """Test case for create_alert

    
    """
    body = {"AlertDescription":"","Action":{"LambdaConfiguration":{"LambdaArn":"","RoleArn":""},"SNSConfiguration":{"SnsTopicArn":"","SnsFormat":"","RoleArn":""}},"AlertName":"","AlertFilters":{"MetricList":"","DimensionFilterList":""},"AlertSensitivityThreshold":"","AnomalyDetectorArn":"","Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/CreateAlert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_anomaly_detector(client):
    """Test case for create_anomaly_detector

    
    """
    body = {"AnomalyDetectorName":"","KmsKeyArn":"","AnomalyDetectorDescription":"","Tags":"","AnomalyDetectorConfig":{"AnomalyDetectorFrequency":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/CreateAnomalyDetector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_metric_set(client):
    """Test case for create_metric_set

    
    """
    body = {"Timezone":"","MetricSetDescription":"","MetricList":"","MetricSource":{"S3SourceConfig":{"TemplatedPathList":"","HistoricalDataPathList":"","RoleArn":"","FileFormatDescriptor":{"JsonFormatDescriptor":{"Charset":"","FileCompression":""},"CsvFormatDescriptor":{"QuoteSymbol":"","ContainsHeader":"","Delimiter":"","HeaderList":"","Charset":"","FileCompression":""}}},"CloudWatchConfig":{"BackTestConfiguration":{"RunBackTestMode":""},"RoleArn":""},"AthenaSourceConfig":{"DataCatalog":"","TableName":"","S3ResultsPath":"","BackTestConfiguration":{"RunBackTestMode":""},"DatabaseName":"","WorkGroupName":"","RoleArn":""},"RDSSourceConfig":{"TableName":"","DatabasePort":"","DatabaseHost":"","DatabaseName":"","SecretManagerArn":"","VpcConfiguration":{"SubnetIdList":"","SecurityGroupIdList":""},"DBInstanceIdentifier":"","RoleArn":""},"AppFlowConfig":{"FlowName":"","RoleArn":""},"RedshiftSourceConfig":{"TableName":"","DatabasePort":"","DatabaseHost":"","DatabaseName":"","SecretManagerArn":"","VpcConfiguration":{"SubnetIdList":"","SecurityGroupIdList":""},"ClusterIdentifier":"","RoleArn":""}},"TimestampColumn":{"ColumnName":"","ColumnFormat":""},"DimensionList":"","DimensionFilterList":"","AnomalyDetectorArn":"","MetricSetFrequency":"","MetricSetName":"","Tags":"","Offset":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/CreateMetricSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deactivate_anomaly_detector(client):
    """Test case for deactivate_anomaly_detector

    
    """
    body = {"AnomalyDetectorArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DeactivateAnomalyDetector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_alert(client):
    """Test case for delete_alert

    
    """
    body = {"AlertArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DeleteAlert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_anomaly_detector(client):
    """Test case for delete_anomaly_detector

    
    """
    body = {"AnomalyDetectorArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DeleteAnomalyDetector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_alert(client):
    """Test case for describe_alert

    
    """
    body = {"AlertArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DescribeAlert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_anomaly_detection_executions(client):
    """Test case for describe_anomaly_detection_executions

    
    """
    body = {"NextToken":"","MaxResults":"","AnomalyDetectorArn":"","Timestamp":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DescribeAnomalyDetectionExecutions',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_anomaly_detector(client):
    """Test case for describe_anomaly_detector

    
    """
    body = {"AnomalyDetectorArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DescribeAnomalyDetector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_metric_set(client):
    """Test case for describe_metric_set

    
    """
    body = {"MetricSetArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DescribeMetricSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_detect_metric_set_config(client):
    """Test case for detect_metric_set_config

    
    """
    body = {"AnomalyDetectorArn":"","AutoDetectionMetricSource":{"S3SourceConfig":{"TemplatedPathList":"","HistoricalDataPathList":""}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/DetectMetricSetConfig',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_anomaly_group(client):
    """Test case for get_anomaly_group

    
    """
    body = {"AnomalyDetectorArn":"","AnomalyGroupId":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/GetAnomalyGroup',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_data_quality_metrics(client):
    """Test case for get_data_quality_metrics

    
    """
    body = {"AnomalyDetectorArn":"","MetricSetArn":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/GetDataQualityMetrics',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_feedback(client):
    """Test case for get_feedback

    
    """
    body = {"NextToken":"","MaxResults":"","AnomalyDetectorArn":"","AnomalyGroupTimeSeriesFeedback":{"TimeSeriesId":"","AnomalyGroupId":""}}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/GetFeedback',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_sample_data(client):
    """Test case for get_sample_data

    
    """
    body = {"S3SourceConfig":{"TemplatedPathList":"","HistoricalDataPathList":"","RoleArn":"","FileFormatDescriptor":{"JsonFormatDescriptor":{"Charset":"","FileCompression":""},"CsvFormatDescriptor":{"QuoteSymbol":"","ContainsHeader":"","Delimiter":"","HeaderList":"","Charset":"","FileCompression":""}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/GetSampleData',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_alerts(client):
    """Test case for list_alerts

    
    """
    body = {"NextToken":"","MaxResults":"","AnomalyDetectorArn":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ListAlerts',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_anomaly_detectors(client):
    """Test case for list_anomaly_detectors

    
    """
    body = {"NextToken":"","MaxResults":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ListAnomalyDetectors',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_anomaly_group_related_metrics(client):
    """Test case for list_anomaly_group_related_metrics

    
    """
    body = {"NextToken":"","MaxResults":"","RelationshipTypeFilter":"","AnomalyDetectorArn":"","AnomalyGroupId":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ListAnomalyGroupRelatedMetrics',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_anomaly_group_summaries(client):
    """Test case for list_anomaly_group_summaries

    
    """
    body = {"NextToken":"","MaxResults":"","SensitivityThreshold":"","AnomalyDetectorArn":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ListAnomalyGroupSummaries',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_anomaly_group_time_series(client):
    """Test case for list_anomaly_group_time_series

    
    """
    body = {"MetricName":"","NextToken":"","MaxResults":"","AnomalyDetectorArn":"","AnomalyGroupId":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ListAnomalyGroupTimeSeries',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_metric_sets(client):
    """Test case for list_metric_sets

    
    """
    body = {"NextToken":"","MaxResults":"","AnomalyDetectorArn":""}
    params = [('MaxResults', 'max_results_example'),
                    ('NextToken', 'next_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/ListMetricSets',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_tags_for_resource(client):
    """Test case for list_tags_for_resource

    
    """
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_feedback(client):
    """Test case for put_feedback

    
    """
    body = {"AnomalyDetectorArn":"","AnomalyGroupTimeSeriesFeedback":{"TimeSeriesId":"","AnomalyGroupId":"","IsAnomaly":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/PutFeedback',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_tag_resource(client):
    """Test case for tag_resource

    
    """
    body = {"Tags":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/tags/{resource_arn}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untag_resource(client):
    """Test case for untag_resource

    
    """
    params = [('tagKeys', ['tag_keys_example'])]
    headers = { 
        'Accept': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/tags/{resource_arntag_key}'.format(resource_arn='resource_arn_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_alert(client):
    """Test case for update_alert

    
    """
    body = {"AlertDescription":"","AlertArn":"","Action":{"LambdaConfiguration":{"LambdaArn":"","RoleArn":""},"SNSConfiguration":{"SnsTopicArn":"","SnsFormat":"","RoleArn":""}},"AlertFilters":{"MetricList":"","DimensionFilterList":""},"AlertSensitivityThreshold":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/UpdateAlert',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_anomaly_detector(client):
    """Test case for update_anomaly_detector

    
    """
    body = {"KmsKeyArn":"","AnomalyDetectorDescription":"","AnomalyDetectorArn":"","AnomalyDetectorConfig":{"AnomalyDetectorFrequency":""}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/UpdateAnomalyDetector',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_metric_set(client):
    """Test case for update_metric_set

    
    """
    body = {"MetricSetDescription":"","MetricList":"","MetricSource":{"S3SourceConfig":{"TemplatedPathList":"","HistoricalDataPathList":"","RoleArn":"","FileFormatDescriptor":{"JsonFormatDescriptor":{"Charset":"","FileCompression":""},"CsvFormatDescriptor":{"QuoteSymbol":"","ContainsHeader":"","Delimiter":"","HeaderList":"","Charset":"","FileCompression":""}}},"CloudWatchConfig":{"BackTestConfiguration":{"RunBackTestMode":""},"RoleArn":""},"AthenaSourceConfig":{"DataCatalog":"","TableName":"","S3ResultsPath":"","BackTestConfiguration":{"RunBackTestMode":""},"DatabaseName":"","WorkGroupName":"","RoleArn":""},"RDSSourceConfig":{"TableName":"","DatabasePort":"","DatabaseHost":"","DatabaseName":"","SecretManagerArn":"","VpcConfiguration":{"SubnetIdList":"","SecurityGroupIdList":""},"DBInstanceIdentifier":"","RoleArn":""},"AppFlowConfig":{"FlowName":"","RoleArn":""},"RedshiftSourceConfig":{"TableName":"","DatabasePort":"","DatabaseHost":"","DatabaseName":"","SecretManagerArn":"","VpcConfiguration":{"SubnetIdList":"","SecurityGroupIdList":""},"ClusterIdentifier":"","RoleArn":""}},"TimestampColumn":{"ColumnName":"","ColumnFormat":""},"DimensionList":"","DimensionFilterList":"","MetricSetFrequency":"","MetricSetArn":"","Offset":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'x_amz_content_sha256': 'x_amz_content_sha256_example',
        'x_amz_date': 'x_amz_date_example',
        'x_amz_algorithm': 'x_amz_algorithm_example',
        'x_amz_credential': 'x_amz_credential_example',
        'x_amz_security_token': 'x_amz_security_token_example',
        'x_amz_signature': 'x_amz_signature_example',
        'x_amz_signed_headers': 'x_amz_signed_headers_example',
        'hmac': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/UpdateMetricSet',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


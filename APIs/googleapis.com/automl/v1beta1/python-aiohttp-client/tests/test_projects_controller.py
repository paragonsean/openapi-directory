# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_predict_request import BatchPredictRequest
from openapi_server.models.column_spec import ColumnSpec
from openapi_server.models.dataset import Dataset
from openapi_server.models.deploy_model_request import DeployModelRequest
from openapi_server.models.export_data_request import ExportDataRequest
from openapi_server.models.export_evaluated_examples_request import ExportEvaluatedExamplesRequest
from openapi_server.models.export_model_request import ExportModelRequest
from openapi_server.models.import_data_request import ImportDataRequest
from openapi_server.models.list_column_specs_response import ListColumnSpecsResponse
from openapi_server.models.list_datasets_response import ListDatasetsResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.list_model_evaluations_response import ListModelEvaluationsResponse
from openapi_server.models.list_models_response import ListModelsResponse
from openapi_server.models.list_operations_response import ListOperationsResponse
from openapi_server.models.list_table_specs_response import ListTableSpecsResponse
from openapi_server.models.model import Model
from openapi_server.models.operation import Operation
from openapi_server.models.policy import Policy
from openapi_server.models.predict_request import PredictRequest
from openapi_server.models.predict_response import PredictResponse
from openapi_server.models.set_iam_policy_request import SetIamPolicyRequest
from openapi_server.models.test_iam_permissions_request import TestIamPermissionsRequest
from openapi_server.models.test_iam_permissions_response import TestIamPermissionsResponse
from openapi_server.models.wait_operation_request import WaitOperationRequest


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_datasets_create(client):
    """Test case for automl_projects_locations_datasets_create

    
    """
    body = {"displayName":"displayName","exampleCount":0,"textExtractionDatasetMetadata":"{}","description":"description","imageClassificationDatasetMetadata":{"classificationType":"CLASSIFICATION_TYPE_UNSPECIFIED"},"videoClassificationDatasetMetadata":"{}","tablesDatasetMetadata":{"primaryTableSpecId":"primaryTableSpecId","targetColumnCorrelations":{"key":{"cramersV":2.3021358869347655}},"weightColumnSpecId":"weightColumnSpecId","mlUseColumnSpecId":"mlUseColumnSpecId","statsUpdateTime":"statsUpdateTime","targetColumnSpecId":"targetColumnSpecId"},"videoObjectTrackingDatasetMetadata":"{}","textClassificationDatasetMetadata":{"classificationType":"CLASSIFICATION_TYPE_UNSPECIFIED"},"createTime":"createTime","name":"name","translationDatasetMetadata":{"sourceLanguageCode":"sourceLanguageCode","targetLanguageCode":"targetLanguageCode"},"etag":"etag","textSentimentDatasetMetadata":{"sentimentMax":6},"imageObjectDetectionDatasetMetadata":"{}"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_datasets_export_data(client):
    """Test case for automl_projects_locations_datasets_export_data

    
    """
    body = {"outputConfig":{"gcsDestination":{"outputUriPrefix":"outputUriPrefix"},"bigqueryDestination":{"outputUri":"outputUri"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameexport_dat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_datasets_import_data(client):
    """Test case for automl_projects_locations_datasets_import_data

    
    """
    body = {"inputConfig":{"bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"inputUris":["inputUris","inputUris"]},"params":{"key":"params"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameimport_dat}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_datasets_list(client):
    """Test case for automl_projects_locations_datasets_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/datasets'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_datasets_table_specs_column_specs_list(client):
    """Test case for automl_projects_locations_datasets_table_specs_column_specs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('fieldMask', 'field_mask_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/columnSpecs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_datasets_table_specs_column_specs_patch(client):
    """Test case for automl_projects_locations_datasets_table_specs_column_specs_patch

    
    """
    body = {"topCorrelatedColumns":[{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"},{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"}],"displayName":"displayName","dataType":{"nullable":True,"structType":{"fields":{}},"timeFormat":"timeFormat","typeCode":"TYPE_CODE_UNSPECIFIED"},"name":"name","etag":"etag","dataStats":{"float64Stats":{"histogramBuckets":[{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"},{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"}],"quantiles":[5.962133916683182,5.962133916683182],"mean":1.4658129805029452,"standardDeviation":5.637376656633329},"structStats":{"fieldStats":{}},"timestampStats":{"granularStats":{"key":{"buckets":{"key":"buckets"}}}},"arrayStats":{},"categoryStats":{"topCategoryStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"distinctValueCount":"distinctValueCount","nullValueCount":"nullValueCount","stringStats":{"topUnigramStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"validValueCount":"validValueCount"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('updateMask', 'update_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_datasets_table_specs_list(client):
    """Test case for automl_projects_locations_datasets_table_specs_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('fieldMask', 'field_mask_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/tableSpecs'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_list(client):
    """Test case for automl_projects_locations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/locations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_batch_predict(client):
    """Test case for automl_projects_locations_models_batch_predict

    
    """
    body = {"inputConfig":{"bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"inputUris":["inputUris","inputUris"]}},"outputConfig":{"gcsDestination":{"outputUriPrefix":"outputUriPrefix"},"bigqueryDestination":{"outputUri":"outputUri"}},"params":{"key":"params"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namebatch_predic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_create(client):
    """Test case for automl_projects_locations_models_create

    
    """
    body = {"videoObjectTrackingModelMetadata":"{}","displayName":"displayName","validateExampleCount":2,"textSentimentModelMetadata":"{}","textClassificationModelMetadata":{"classificationType":"CLASSIFICATION_TYPE_UNSPECIFIED"},"trainExampleCount":5,"translationModelMetadata":{"baseModel":"baseModel","sourceLanguageCode":"sourceLanguageCode","targetLanguageCode":"targetLanguageCode"},"updateTime":"updateTime","videoClassificationModelMetadata":"{}","imageClassificationModelMetadata":{"stopReason":"stopReason","nodeQps":0.8008281904610115,"trainBudget":"trainBudget","nodeCount":"nodeCount","trainCost":"trainCost","modelType":"modelType","baseModelId":"baseModelId"},"deploymentState":"DEPLOYMENT_STATE_UNSPECIFIED","tablesModelMetadata":{"optimizationObjectivePrecisionValue":1.4658129,"tablesModelColumnInfo":[{"featureImportance":3.6160767,"columnDisplayName":"columnDisplayName","columnSpecName":"columnSpecName"},{"featureImportance":3.6160767,"columnDisplayName":"columnDisplayName","columnSpecName":"columnSpecName"}],"targetColumnSpec":{"topCorrelatedColumns":[{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"},{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"}],"displayName":"displayName","dataType":{"nullable":True,"structType":{"fields":{}},"timeFormat":"timeFormat","typeCode":"TYPE_CODE_UNSPECIFIED"},"name":"name","etag":"etag","dataStats":{"float64Stats":{"histogramBuckets":[{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"},{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"}],"quantiles":[5.962133916683182,5.962133916683182],"mean":1.4658129805029452,"standardDeviation":5.637376656633329},"structStats":{"fieldStats":{}},"timestampStats":{"granularStats":{"key":{"buckets":{"key":"buckets"}}}},"arrayStats":{},"categoryStats":{"topCategoryStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"distinctValueCount":"distinctValueCount","nullValueCount":"nullValueCount","stringStats":{"topUnigramStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"validValueCount":"validValueCount"}},"optimizationObjective":"optimizationObjective","trainBudgetMilliNodeHours":"trainBudgetMilliNodeHours","optimizationObjectiveRecallValue":5.962134,"disableEarlyStopping":True,"inputFeatureColumnSpecs":[{"topCorrelatedColumns":[{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"},{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"}],"displayName":"displayName","dataType":{"nullable":True,"structType":{"fields":{}},"timeFormat":"timeFormat","typeCode":"TYPE_CODE_UNSPECIFIED"},"name":"name","etag":"etag","dataStats":{"float64Stats":{"histogramBuckets":[{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"},{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"}],"quantiles":[5.962133916683182,5.962133916683182],"mean":1.4658129805029452,"standardDeviation":5.637376656633329},"structStats":{"fieldStats":{}},"timestampStats":{"granularStats":{"key":{"buckets":{"key":"buckets"}}}},"arrayStats":{},"categoryStats":{"topCategoryStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"distinctValueCount":"distinctValueCount","nullValueCount":"nullValueCount","stringStats":{"topUnigramStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"validValueCount":"validValueCount"}},{"topCorrelatedColumns":[{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"},{"correlationStats":{"cramersV":2.3021358869347655},"columnSpecId":"columnSpecId"}],"displayName":"displayName","dataType":{"nullable":True,"structType":{"fields":{}},"timeFormat":"timeFormat","typeCode":"TYPE_CODE_UNSPECIFIED"},"name":"name","etag":"etag","dataStats":{"float64Stats":{"histogramBuckets":[{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"},{"min":6.027456183070403,"max":0.8008281904610115,"count":"count"}],"quantiles":[5.962133916683182,5.962133916683182],"mean":1.4658129805029452,"standardDeviation":5.637376656633329},"structStats":{"fieldStats":{}},"timestampStats":{"granularStats":{"key":{"buckets":{"key":"buckets"}}}},"arrayStats":{},"categoryStats":{"topCategoryStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"distinctValueCount":"distinctValueCount","nullValueCount":"nullValueCount","stringStats":{"topUnigramStats":[{"count":"count","value":"value"},{"count":"count","value":"value"}]},"validValueCount":"validValueCount"}}],"trainCostMilliNodeHours":"trainCostMilliNodeHours"},"createTime":"createTime","imageObjectDetectionModelMetadata":{"stopReason":"stopReason","nodeQps":6.027456183070403,"nodeCount":"nodeCount","trainBudgetMilliNodeHours":"trainBudgetMilliNodeHours","modelType":"modelType","trainCostMilliNodeHours":"trainCostMilliNodeHours"},"name":"name","textExtractionModelMetadata":{"modelHint":"modelHint"},"datasetId":"datasetId"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{parent}/models'.format(parent='parent_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_deploy(client):
    """Test case for automl_projects_locations_models_deploy

    
    """
    body = {"imageClassificationModelDeploymentMetadata":{"nodeCount":"nodeCount"},"imageObjectDetectionModelDeploymentMetadata":{"nodeCount":"nodeCount"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namedeplo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_export(client):
    """Test case for automl_projects_locations_models_export

    
    """
    body = {"outputConfig":{"modelFormat":"modelFormat","gcsDestination":{"outputUriPrefix":"outputUriPrefix"},"gcrDestination":{"outputUri":"outputUri"},"params":{"key":"params"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameexpor}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_export_evaluated_examples(client):
    """Test case for automl_projects_locations_models_export_evaluated_examples

    
    """
    body = {"outputConfig":{"bigqueryDestination":{"outputUri":"outputUri"}}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameexport_evaluated_example}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_get_iam_policy(client):
    """Test case for automl_projects_locations_models_get_iam_policy

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('options.requestedPolicyVersion', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{resourceget_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_list(client):
    """Test case for automl_projects_locations_models_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/models'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_model_evaluations_list(client):
    """Test case for automl_projects_locations_models_model_evaluations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{parent}/modelEvaluations'.format(parent='parent_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_predict(client):
    """Test case for automl_projects_locations_models_predict

    
    """
    body = {"payload":{"image":{"inputConfig":{"bigquerySource":{"inputUri":"inputUri"},"gcsSource":{"inputUris":["inputUris","inputUris"]},"params":{"key":"params"}},"imageBytes":"imageBytes","thumbnailUri":"thumbnailUri"},"document":{"layout":[{"textSegment":{"endOffset":"endOffset","startOffset":"startOffset","content":"content"},"pageNumber":1,"textSegmentType":"TEXT_SEGMENT_TYPE_UNSPECIFIED","boundingPoly":{"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]}},{"textSegment":{"endOffset":"endOffset","startOffset":"startOffset","content":"content"},"pageNumber":1,"textSegmentType":"TEXT_SEGMENT_TYPE_UNSPECIFIED","boundingPoly":{"normalizedVertices":[{"x":6.0274563,"y":1.4658129},{"x":6.0274563,"y":1.4658129}]}}],"inputConfig":{"gcsSource":{"inputUris":["inputUris","inputUris"]}},"pageCount":6,"documentDimensions":{"unit":"DOCUMENT_DIMENSION_UNIT_UNSPECIFIED","width":1.0246457,"height":1.2315135},"documentText":{"contentUri":"contentUri","mimeType":"mimeType","content":"content"}},"row":{"columnSpecIds":["columnSpecIds","columnSpecIds"],"values":["",""]},"textSnippet":{"contentUri":"contentUri","mimeType":"mimeType","content":"content"}},"params":{"key":"params"}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namepredic}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_set_iam_policy(client):
    """Test case for automl_projects_locations_models_set_iam_policy

    
    """
    body = {"policy":{"bindings":[{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]},{"condition":{"expression":"expression","description":"description","location":"location","title":"title"},"role":"role","members":["members","members"]}],"etag":"etag","version":0}}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{resourceset_iam_polic}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_models_undeploy(client):
    """Test case for automl_projects_locations_models_undeploy

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{nameundeplo}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_operations_cancel(client):
    """Test case for automl_projects_locations_operations_cancel

    
    """
    body = None
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namecance}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_operations_delete(client):
    """Test case for automl_projects_locations_operations_delete

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_operations_get(client):
    """Test case for automl_projects_locations_operations_get

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('fieldMask', 'field_mask_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_operations_list(client):
    """Test case for automl_projects_locations_operations_list

    
    """
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example'),
                    ('filter', 'filter_example'),
                    ('pageSize', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1beta1/{name}/operations'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_operations_wait(client):
    """Test case for automl_projects_locations_operations_wait

    
    """
    body = {"timeout":"timeout"}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{namewai}'.format(name='name_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_automl_projects_locations_test_iam_permissions(client):
    """Test case for automl_projects_locations_test_iam_permissions

    
    """
    body = {"permissions":["permissions","permissions"]}
    params = [('$.xgafv', 'xgafv_example'),
                    ('access_token', 'access_token_example'),
                    ('alt', 'alt_example'),
                    ('callback', 'param_callback_example'),
                    ('fields', 'fields_example'),
                    ('key', 'key_example'),
                    ('oauth_token', 'oauth_token_example'),
                    ('prettyPrint', True),
                    ('quotaUser', 'quota_user_example'),
                    ('upload_protocol', 'upload_protocol_example'),
                    ('uploadType', 'upload_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1beta1/{resourcetest_iam_permission}'.format(resource='resource_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


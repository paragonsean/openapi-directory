# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.report_definition import ReportDefinition
from openapi_server.models.transform_definition import TransformDefinition


pytestmark = pytest.mark.asyncio

async def test_delete_report_definition(client):
    """Test case for delete_report_definition

    Deletes a report definition
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Report/{report_definition_id}'.format(report_definition_id='report_definition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_transform_definition(client):
    """Test case for delete_transform_definition

    Deletes a transform definition
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Transform/{transform_definition_id}'.format(transform_definition_id='transform_definition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_active_pay_instructions_report_output(client):
    """Test case for get_active_pay_instructions_report_output

    Runs the active pay instructions report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('EmployeeKey', 'employee_key_example'),
                    ('ActiveOn', '2013-10-20'),
                    ('FromDate', '2013-10-20'),
                    ('ToDate', '2013-10-20'),
                    ('Type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/ACTPAYINS/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_aoe_liability_report_ouput(client):
    """Test case for get_aoe_liability_report_ouput

    Runs the AOE liability report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('TaxPeriod', 56),
                    ('TransformDefinitionKey', 'transform_definition_key_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/AOELIABILITY/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dps_message_report_output(client):
    """Test case for get_dps_message_report_output

    Runs the DPS message report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('FromDate', '2013-10-20'),
                    ('ToDate', '2013-10-20'),
                    ('MessageTypes', 'message_types_example'),
                    ('MessageStatuses', 'message_statuses_example'),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/DPSMSG/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employer_summary_report_ouput(client):
    """Test case for get_employer_summary_report_ouput

    Runs the employer summary report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('ContextDate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/EMPSUM/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_gross_to_net_report_output(client):
    """Test case for get_gross_to_net_report_output

    Runs the gross to net report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('TaxPeriod', 56),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/GRO2NET/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_holiday_balance_report_output(client):
    """Test case for get_holiday_balance_report_output

    Runs the holiday balance report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('HolidayYearEnd', '2013-10-20'),
                    ('EmployeeCodes', 'employee_codes_example'),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/HOLBAL/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_journal_report_ouput(client):
    """Test case for get_journal_report_ouput

    Runs the journal report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayFrequency', 'pay_frequency_example'),
                    ('TaxYear', 56),
                    ('TaxPeriod', 56),
                    ('LedgerTarget', 'ledger_target_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/JOURNAL/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_last_pay_date_report_ouput(client):
    """Test case for get_last_pay_date_report_ouput

    Runs the last pay date report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('EmployeeKey', 'employee_key_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/LASTPAYDATE/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_net_pay_report_output(client):
    """Test case for get_net_pay_report_output

    Runs the net pay report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('TaxPeriod', 56),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/NETPAY/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_next_pay_period_dates_report_output(client):
    """Test case for get_next_pay_period_dates_report_output

    Runs the next pay period report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/NEXTPERIOD/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_p11_summary_report_output(client):
    """Test case for get_p11_summary_report_output

    Runs the P11 summary report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/P11SUM/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_p32_net_report_output(client):
    """Test case for get_p32_net_report_output

    Runs the P32 report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('TaxYear', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/P32/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_p32_summary_net_report_output(client):
    """Test case for get_p32_summary_net_report_output

    Runs the P32 summary report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('TaxYear', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/P32SUM/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_p45_report_output(client):
    """Test case for get_p45_report_output

    Runs the P45 report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('EmployeeKey', 'employee_key_example'),
                    ('TransformDefinitionKey', 'transform_definition_key_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/P45/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_p60_report_output(client):
    """Test case for get_p60_report_output

    Runs the P60 report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('TaxYear', 56),
                    ('EmployeeCodes', 'employee_codes_example'),
                    ('TransformDefinitionKey', 'transform_definition_key_example'),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/P60/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_papdis_report_ouput(client):
    """Test case for get_papdis_report_ouput

    Runs the PAPDIS report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('PaymentDate', '2013-10-20'),
                    ('PensionKey', 'pension_key_example'),
                    ('MessageFunctionCode', 'message_function_code_example'),
                    ('TransformDefinitionKey', 'transform_definition_key_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/PAPDIS/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pass_report_ouput(client):
    """Test case for get_pass_report_ouput

    Runs the PASS report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('PaymentDate', '2013-10-20'),
                    ('PensionKey', 'pension_key_example'),
                    ('MessageFunctionCode', 'message_function_code_example'),
                    ('IntermediaryId', 'intermediary_id_example'),
                    ('DocumentId', 'document_id_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/PASS/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_dashboard_payslip_report_ouput(client):
    """Test case for get_pay_dashboard_payslip_report_ouput

    Runs the Pay Dashboard payslips report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('EmployeeCodes', 'employee_codes_example'),
                    ('TransformDefinitionKey', 'transform_definition_key_example'),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example'),
                    ('PaymentDate', '2013-10-20'),
                    ('PublicationDate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/PAYDASHBOARD/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payslip3_report_output(client):
    """Test case for get_payslip3_report_output

    Runs the verbose payslip report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('PayScheduleKey', 'pay_schedule_key_example'),
                    ('TaxYear', 56),
                    ('EmployeeCodes', 'employee_codes_example'),
                    ('TransformDefinitionKey', 'transform_definition_key_example'),
                    ('StartIndex', 'start_index_example'),
                    ('MaxIndex', 'max_index_example'),
                    ('PaymentDate', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/PAYSLIP3/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pension_liability_report_output(client):
    """Test case for get_pension_liability_report_output

    Runs the pension liability report
    """
    params = [('EmployerKey', 'employer_key_example'),
                    ('TaxYear', 56),
                    ('PensionKey', 'pension_key_example')]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/PENLIABILITY/run',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_definition_from_application(client):
    """Test case for get_report_definition_from_application

    Get the report definition
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/{report_definition_id}'.format(report_definition_id='report_definition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_definitions_from_application(client):
    """Test case for get_report_definitions_from_application

    Gets all reports
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Reports',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_output(client):
    """Test case for get_report_output

    Runs the specified report definition
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Report/{report_definition_id}/run'.format(report_definition_id='report_definition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transform_definition_from_application(client):
    """Test case for get_transform_definition_from_application

    Get the transform definition
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Transform/{transform_definition_id}'.format(transform_definition_id='transform_definition_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_transform_definitions_from_application(client):
    """Test case for get_transform_definitions_from_application

    Gets all transform definitions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Transforms',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_report_definition(client):
    """Test case for post_report_definition

    Create a new report definition
    """
    body = {"ReportDefinition":{"Active":True,"Readonly":True,"Version":"Version","ReportQuery":{"Variables":{"Variable":[{"@Name":"@Name","@Value":"@Value"},{"@Name":"@Name","@Value":"@Value"}]},"ExcludeNullOrEmptyElements":True,"Groups":{"Group":[{"Condition":[{"@ValueB":"@ValueB","@ValueA":"@ValueA"},{"@ValueB":"@ValueB","@ValueA":"@ValueA"}],"Order":[{"@Property":"@Property"},{"@Property":"@Property"}],"@UniqueKeyVariable":"@UniqueKeyVariable","@Predicate":"@Predicate","@Selector":"@Selector","Filter":[{"@Property":"@Property","@IsOr":True,"@Value":"@Value"},{"@Property":"@Property","@IsOr":True,"@Value":"@Value"}],"Output":[{"@Output":"Element","@MaxLength":"@MaxLength"},{"@Output":"Element","@MaxLength":"@MaxLength"}],"@LoopExpression":"@LoopExpression","@GroupName":"@GroupName","@ItemName":"@ItemName"},{"Condition":[{"@ValueB":"@ValueB","@ValueA":"@ValueA"},{"@ValueB":"@ValueB","@ValueA":"@ValueA"}],"Order":[{"@Property":"@Property"},{"@Property":"@Property"}],"@UniqueKeyVariable":"@UniqueKeyVariable","@Predicate":"@Predicate","@Selector":"@Selector","Filter":[{"@Property":"@Property","@IsOr":True,"@Value":"@Value"},{"@Property":"@Property","@IsOr":True,"@Value":"@Value"}],"Output":[{"@Output":"Element","@MaxLength":"@MaxLength"},{"@Output":"Element","@MaxLength":"@MaxLength"}],"@LoopExpression":"@LoopExpression","@GroupName":"@GroupName","@ItemName":"@ItemName"}]},"Encoding":"Encoding","RootNodeName":"RootNodeName","SuppressMetricAttributes":True},"Title":"Title","SupportedTransforms":"SupportedTransforms"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Reports',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_transform_definition(client):
    """Test case for post_transform_definition

    Create a new transform definition
    """
    body = {"TransformDefinition":{"Active":True,"Readonly":True,"ContentType":"ContentType","Version":"Version","Definition":"Definition","Title":"Title","DefinitionType":"DefinitionType","SupportedReports":"SupportedReports","TaxYear":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Transforms',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_report_definition(client):
    """Test case for put_report_definition

    Updates a report definition
    """
    body = {"ReportDefinition":{"Active":True,"Readonly":True,"Version":"Version","ReportQuery":{"Variables":{"Variable":[{"@Name":"@Name","@Value":"@Value"},{"@Name":"@Name","@Value":"@Value"}]},"ExcludeNullOrEmptyElements":True,"Groups":{"Group":[{"Condition":[{"@ValueB":"@ValueB","@ValueA":"@ValueA"},{"@ValueB":"@ValueB","@ValueA":"@ValueA"}],"Order":[{"@Property":"@Property"},{"@Property":"@Property"}],"@UniqueKeyVariable":"@UniqueKeyVariable","@Predicate":"@Predicate","@Selector":"@Selector","Filter":[{"@Property":"@Property","@IsOr":True,"@Value":"@Value"},{"@Property":"@Property","@IsOr":True,"@Value":"@Value"}],"Output":[{"@Output":"Element","@MaxLength":"@MaxLength"},{"@Output":"Element","@MaxLength":"@MaxLength"}],"@LoopExpression":"@LoopExpression","@GroupName":"@GroupName","@ItemName":"@ItemName"},{"Condition":[{"@ValueB":"@ValueB","@ValueA":"@ValueA"},{"@ValueB":"@ValueB","@ValueA":"@ValueA"}],"Order":[{"@Property":"@Property"},{"@Property":"@Property"}],"@UniqueKeyVariable":"@UniqueKeyVariable","@Predicate":"@Predicate","@Selector":"@Selector","Filter":[{"@Property":"@Property","@IsOr":True,"@Value":"@Value"},{"@Property":"@Property","@IsOr":True,"@Value":"@Value"}],"Output":[{"@Output":"Element","@MaxLength":"@MaxLength"},{"@Output":"Element","@MaxLength":"@MaxLength"}],"@LoopExpression":"@LoopExpression","@GroupName":"@GroupName","@ItemName":"@ItemName"}]},"Encoding":"Encoding","RootNodeName":"RootNodeName","SuppressMetricAttributes":True},"Title":"Title","SupportedTransforms":"SupportedTransforms"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Report/{report_definition_id}'.format(report_definition_id='report_definition_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_transform_definition(client):
    """Test case for put_transform_definition

    Updates a transform definition
    """
    body = {"TransformDefinition":{"Active":True,"Readonly":True,"ContentType":"ContentType","Version":"Version","Definition":"Definition","Title":"Title","DefinitionType":"DefinitionType","SupportedReports":"SupportedReports","TaxYear":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Transform/{transform_definition_id}'.format(transform_definition_id='transform_definition_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


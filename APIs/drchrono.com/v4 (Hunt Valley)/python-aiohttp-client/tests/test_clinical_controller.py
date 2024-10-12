# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.allergies_list200_response import AllergiesList200Response
from openapi_server.models.amendments_list200_response import AmendmentsList200Response
from openapi_server.models.appointment import Appointment
from openapi_server.models.appointment_profile import AppointmentProfile
from openapi_server.models.appointment_profiles_list200_response import AppointmentProfilesList200Response
from openapi_server.models.appointment_template import AppointmentTemplate
from openapi_server.models.appointment_templates_list200_response import AppointmentTemplatesList200Response
from openapi_server.models.appointments_list200_response import AppointmentsList200Response
from openapi_server.models.care_plan import CarePlan
from openapi_server.models.care_plans_list200_response import CarePlansList200Response
from openapi_server.models.care_team_member import CareTeamMember
from openapi_server.models.care_team_members_list200_response import CareTeamMembersList200Response
from openapi_server.models.claim_billing_notes import ClaimBillingNotes
from openapi_server.models.claim_billing_notes_list200_response import ClaimBillingNotesList200Response
from openapi_server.models.clinical_note import ClinicalNote
from openapi_server.models.clinical_note_field_types_list200_response import ClinicalNoteFieldTypesList200Response
from openapi_server.models.clinical_note_field_values_list200_response import ClinicalNoteFieldValuesList200Response
from openapi_server.models.clinical_note_templates_list200_response import ClinicalNoteTemplatesList200Response
from openapi_server.models.clinical_notes_list200_response import ClinicalNotesList200Response
from openapi_server.models.consent_form import ConsentForm
from openapi_server.models.consent_forms_list200_response import ConsentFormsList200Response
from openapi_server.models.custom_appointment_field_type import CustomAppointmentFieldType
from openapi_server.models.custom_appointment_fields_list200_response import CustomAppointmentFieldsList200Response
from openapi_server.models.custom_demographics_list200_response import CustomDemographicsList200Response
from openapi_server.models.custom_patient_field_type import CustomPatientFieldType
from openapi_server.models.custom_vital_type import CustomVitalType
from openapi_server.models.custom_vitals_list200_response import CustomVitalsList200Response
from openapi_server.models.doctor_fee_schedule import DoctorFeeSchedule
from openapi_server.models.documents_list200_response import DocumentsList200Response
from openapi_server.models.eob_object import EOBObject
from openapi_server.models.eobs_list200_response import EobsList200Response
from openapi_server.models.fee_schedules_list200_response import FeeSchedulesList200Response
from openapi_server.models.implantable_device import ImplantableDevice
from openapi_server.models.implantable_devices_list200_response import ImplantableDevicesList200Response
from openapi_server.models.insurance import Insurance
from openapi_server.models.insurances_list200_response import InsurancesList200Response
from openapi_server.models.lab_documents_list200_response import LabDocumentsList200Response
from openapi_server.models.lab_order import LabOrder
from openapi_server.models.lab_order_document import LabOrderDocument
from openapi_server.models.lab_orders_list200_response import LabOrdersList200Response
from openapi_server.models.lab_result import LabResult
from openapi_server.models.lab_results_list200_response import LabResultsList200Response
from openapi_server.models.lab_test import LabTest
from openapi_server.models.lab_tests_list200_response import LabTestsList200Response
from openapi_server.models.lab_vendor_location import LabVendorLocation
from openapi_server.models.medications_list200_response import MedicationsList200Response
from openapi_server.models.patient import Patient
from openapi_server.models.patient_allergy import PatientAllergy
from openapi_server.models.patient_amendment import PatientAmendment
from openapi_server.models.patient_communication import PatientCommunication
from openapi_server.models.patient_communications_list200_response import PatientCommunicationsList200Response
from openapi_server.models.patient_drug import PatientDrug
from openapi_server.models.patient_flag_type import PatientFlagType
from openapi_server.models.patient_flag_types_list200_response import PatientFlagTypesList200Response
from openapi_server.models.patient_intervention import PatientIntervention
from openapi_server.models.patient_interventions_list200_response import PatientInterventionsList200Response
from openapi_server.models.patient_lab_result_set import PatientLabResultSet
from openapi_server.models.patient_lab_results_list200_response import PatientLabResultsList200Response
from openapi_server.models.patient_message import PatientMessage
from openapi_server.models.patient_messages_list200_response import PatientMessagesList200Response
from openapi_server.models.patient_physical_exam import PatientPhysicalExam
from openapi_server.models.patient_physical_exams_list200_response import PatientPhysicalExamsList200Response
from openapi_server.models.patient_problem import PatientProblem
from openapi_server.models.patient_risk_assessment import PatientRiskAssessment
from openapi_server.models.patient_risk_assessments_list200_response import PatientRiskAssessmentsList200Response
from openapi_server.models.patient_vaccine_record import PatientVaccineRecord
from openapi_server.models.patient_vaccine_records_list200_response import PatientVaccineRecordsList200Response
from openapi_server.models.patients_list200_response import PatientsList200Response
from openapi_server.models.prescription_message import PrescriptionMessage
from openapi_server.models.prescription_messages_list200_response import PrescriptionMessagesList200Response
from openapi_server.models.problems_list200_response import ProblemsList200Response
from openapi_server.models.reminder_profile import ReminderProfile
from openapi_server.models.reminder_profiles_list200_response import ReminderProfilesList200Response
from openapi_server.models.scanned_clinical_document import ScannedClinicalDocument
from openapi_server.models.soap_note_custom_report import SoapNoteCustomReport
from openapi_server.models.soap_note_line_item_field_type import SoapNoteLineItemFieldType
from openapi_server.models.soap_note_line_item_field_value import SoapNoteLineItemFieldValue
from openapi_server.models.sublabs_list200_response import SublabsList200Response


pytestmark = pytest.mark.asyncio

async def test_allergies_create(client):
    """Test case for allergies_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/allergies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_allergies_list(client):
    """Test case for allergies_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/allergies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_allergies_partial_update(client):
    """Test case for allergies_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/allergies/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_allergies_read(client):
    """Test case for allergies_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/allergies/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_allergies_update(client):
    """Test case for allergies_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/allergies/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_amendments_create(client):
    """Test case for amendments_create

    
    """
    params = [('appointment', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/amendments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_amendments_delete(client):
    """Test case for amendments_delete

    
    """
    params = [('appointment', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/amendments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_amendments_list(client):
    """Test case for amendments_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('appointment', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/amendments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_amendments_partial_update(client):
    """Test case for amendments_partial_update

    
    """
    params = [('appointment', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/amendments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_amendments_read(client):
    """Test case for amendments_read

    
    """
    params = [('appointment', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/amendments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_amendments_update(client):
    """Test case for amendments_update

    
    """
    params = [('appointment', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/amendments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_profiles_create(client):
    """Test case for appointment_profiles_create

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/appointment_profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_profiles_delete(client):
    """Test case for appointment_profiles_delete

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/appointment_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_profiles_list(client):
    """Test case for appointment_profiles_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/appointment_profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_profiles_partial_update(client):
    """Test case for appointment_profiles_partial_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/appointment_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_profiles_read(client):
    """Test case for appointment_profiles_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/appointment_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_profiles_update(client):
    """Test case for appointment_profiles_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/appointment_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_templates_create(client):
    """Test case for appointment_templates_create

    
    """
    params = [('profile', 56),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/appointment_templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_templates_delete(client):
    """Test case for appointment_templates_delete

    
    """
    params = [('profile', 56),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/appointment_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_templates_list(client):
    """Test case for appointment_templates_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('profile', 56),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/appointment_templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_templates_partial_update(client):
    """Test case for appointment_templates_partial_update

    
    """
    params = [('profile', 56),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/appointment_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_templates_read(client):
    """Test case for appointment_templates_read

    
    """
    params = [('profile', 56),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/appointment_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointment_templates_update(client):
    """Test case for appointment_templates_update

    
    """
    params = [('profile', 56),
                    ('office', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/appointment_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointments_create(client):
    """Test case for appointments_create

    
    """
    params = [('status', 'status_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/appointments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointments_delete(client):
    """Test case for appointments_delete

    
    """
    params = [('status', 'status_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/appointments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointments_list(client):
    """Test case for appointments_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('status', 'status_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/appointments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointments_partial_update(client):
    """Test case for appointments_partial_update

    
    """
    params = [('status', 'status_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/appointments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointments_read(client):
    """Test case for appointments_read

    
    """
    params = [('status', 'status_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/appointments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_appointments_update(client):
    """Test case for appointments_update

    
    """
    params = [('status', 'status_example'),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/appointments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_care_plans_list(client):
    """Test case for care_plans_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('plan_type', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/care_plans',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_care_plans_read(client):
    """Test case for care_plans_read

    
    """
    params = [('patient', 56),
                    ('plan_type', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/care_plans/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_care_team_members_list(client):
    """Test case for care_team_members_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('appointment', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/care_team_members',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_care_team_members_read(client):
    """Test case for care_team_members_read

    
    """
    params = [('patient', 56),
                    ('appointment', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/care_team_members/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_claim_billing_notes_create(client):
    """Test case for claim_billing_notes_create

    
    """
    params = [('appointment', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/claim_billing_notes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_claim_billing_notes_list(client):
    """Test case for claim_billing_notes_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('appointment', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/claim_billing_notes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_claim_billing_notes_read(client):
    """Test case for claim_billing_notes_read

    
    """
    params = [('appointment', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/claim_billing_notes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_field_types_list(client):
    """Test case for clinical_note_field_types_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('clinical_note_template', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_note_field_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_field_types_read(client):
    """Test case for clinical_note_field_types_read

    
    """
    params = [('clinical_note_template', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_note_field_types/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_field_values_create(client):
    """Test case for clinical_note_field_values_create

    
    """
    params = [('clinical_note_field', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('clinical_note_template', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/clinical_note_field_values',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_field_values_list(client):
    """Test case for clinical_note_field_values_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('clinical_note_field', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('clinical_note_template', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_note_field_values',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_field_values_partial_update(client):
    """Test case for clinical_note_field_values_partial_update

    
    """
    params = [('clinical_note_field', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('clinical_note_template', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/clinical_note_field_values/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_field_values_read(client):
    """Test case for clinical_note_field_values_read

    
    """
    params = [('clinical_note_field', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('clinical_note_template', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_note_field_values/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_field_values_update(client):
    """Test case for clinical_note_field_values_update

    
    """
    params = [('clinical_note_field', 56),
                    ('since', 'since_example'),
                    ('appointment', 56),
                    ('clinical_note_template', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/clinical_note_field_values/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_templates_list(client):
    """Test case for clinical_note_templates_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_note_templates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_note_templates_read(client):
    """Test case for clinical_note_templates_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_note_templates/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_notes_list(client):
    """Test case for clinical_notes_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_notes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clinical_notes_read(client):
    """Test case for clinical_notes_read

    
    """
    params = [('patient', 56),
                    ('office', 56),
                    ('doctor', 56),
                    ('since', 'since_example'),
                    ('date_range', 'date_range_example'),
                    ('date', '_date_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/clinical_notes/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consent_forms_apply_to_appointment(client):
    """Test case for consent_forms_apply_to_appointment

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/consent_forms/{id}/apply_to_appointment'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consent_forms_create(client):
    """Test case for consent_forms_create

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/consent_forms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consent_forms_list(client):
    """Test case for consent_forms_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/consent_forms',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consent_forms_partial_update(client):
    """Test case for consent_forms_partial_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/consent_forms/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consent_forms_read(client):
    """Test case for consent_forms_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/consent_forms/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consent_forms_unapply_from_appointment(client):
    """Test case for consent_forms_unapply_from_appointment

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/consent_forms/{id}/unapply_from_appointment'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_consent_forms_update(client):
    """Test case for consent_forms_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/consent_forms/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_appointment_fields_create(client):
    """Test case for custom_appointment_fields_create

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/custom_appointment_fields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_appointment_fields_list(client):
    """Test case for custom_appointment_fields_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_appointment_fields',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_appointment_fields_partial_update(client):
    """Test case for custom_appointment_fields_partial_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/custom_appointment_fields/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_appointment_fields_read(client):
    """Test case for custom_appointment_fields_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_appointment_fields/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_appointment_fields_update(client):
    """Test case for custom_appointment_fields_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/custom_appointment_fields/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_demographics_create(client):
    """Test case for custom_demographics_create

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/custom_demographics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_demographics_list(client):
    """Test case for custom_demographics_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_demographics',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_demographics_partial_update(client):
    """Test case for custom_demographics_partial_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/custom_demographics/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_demographics_read(client):
    """Test case for custom_demographics_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_demographics/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_demographics_update(client):
    """Test case for custom_demographics_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/custom_demographics/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_vitals_list(client):
    """Test case for custom_vitals_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_vitals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_vitals_read(client):
    """Test case for custom_vitals_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/custom_vitals/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_create(client):
    """Test case for documents_create

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_delete(client):
    """Test case for documents_delete

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_list(client):
    """Test case for documents_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_partial_update(client):
    """Test case for documents_partial_update

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_read(client):
    """Test case for documents_read

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_update(client):
    """Test case for documents_update

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eobs_create(client):
    """Test case for eobs_create

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/eobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eobs_list(client):
    """Test case for eobs_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/eobs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_eobs_read(client):
    """Test case for eobs_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/eobs/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fee_schedules_list(client):
    """Test case for fee_schedules_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('code', 'code_example'),
                    ('code_type', 'code_type_example'),
                    ('since', 'since_example'),
                    ('payer_id', 'payer_id_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/fee_schedules',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fee_schedules_read(client):
    """Test case for fee_schedules_read

    
    """
    params = [('code', 'code_example'),
                    ('code_type', 'code_type_example'),
                    ('since', 'since_example'),
                    ('payer_id', 'payer_id_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/fee_schedules/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_implantable_devices_list(client):
    """Test case for implantable_devices_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('mu_date', 'mu_date_example'),
                    ('patient', 56),
                    ('mu_date_range', 'mu_date_range_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/implantable_devices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_implantable_devices_read(client):
    """Test case for implantable_devices_read

    
    """
    params = [('mu_date', 'mu_date_example'),
                    ('patient', 56),
                    ('mu_date_range', 'mu_date_range_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/implantable_devices/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_insurances_list(client):
    """Test case for insurances_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('payer_type', 'payer_type_example'),
                    ('term', 'term_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/insurances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_insurances_read(client):
    """Test case for insurances_read

    
    """
    params = [('payer_type', 'payer_type_example'),
                    ('term', 'term_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/insurances/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_documents_create(client):
    """Test case for lab_documents_create

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/lab_documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_documents_delete(client):
    """Test case for lab_documents_delete

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/lab_documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_documents_list(client):
    """Test case for lab_documents_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_documents_partial_update(client):
    """Test case for lab_documents_partial_update

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/lab_documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_documents_read(client):
    """Test case for lab_documents_read

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_documents_update(client):
    """Test case for lab_documents_update

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/lab_documents/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_create(client):
    """Test case for lab_orders_create

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/lab_orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_delete(client):
    """Test case for lab_orders_delete

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/lab_orders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_list(client):
    """Test case for lab_orders_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_orders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_partial_update(client):
    """Test case for lab_orders_partial_update

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/lab_orders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_read(client):
    """Test case for lab_orders_read

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_orders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_summary_list(client):
    """Test case for lab_orders_summary_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_orders_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_summary_read(client):
    """Test case for lab_orders_summary_read

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_orders_summary/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_orders_update(client):
    """Test case for lab_orders_update

    
    """
    params = [('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/lab_orders/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_results_create(client):
    """Test case for lab_results_create

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/lab_results',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_results_delete(client):
    """Test case for lab_results_delete

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_results_list(client):
    """Test case for lab_results_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_results',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_results_partial_update(client):
    """Test case for lab_results_partial_update

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_results_read(client):
    """Test case for lab_results_read

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_results_update(client):
    """Test case for lab_results_update

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_tests_create(client):
    """Test case for lab_tests_create

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/lab_tests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_tests_delete(client):
    """Test case for lab_tests_delete

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/lab_tests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_tests_list(client):
    """Test case for lab_tests_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_tests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_tests_partial_update(client):
    """Test case for lab_tests_partial_update

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/lab_tests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_tests_read(client):
    """Test case for lab_tests_read

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/lab_tests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_lab_tests_update(client):
    """Test case for lab_tests_update

    
    """
    params = [('order', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/lab_tests/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_medications_append_to_pharmacy_note(client):
    """Test case for medications_append_to_pharmacy_note

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/medications/{id}/append_to_pharmacy_note'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_medications_create(client):
    """Test case for medications_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/medications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_medications_list(client):
    """Test case for medications_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/medications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_medications_partial_update(client):
    """Test case for medications_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/medications/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_medications_read(client):
    """Test case for medications_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/medications/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_medications_update(client):
    """Test case for medications_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/medications/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_communications_create(client):
    """Test case for patient_communications_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_communications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_communications_list(client):
    """Test case for patient_communications_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_communications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_communications_partial_update(client):
    """Test case for patient_communications_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_communications/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_communications_read(client):
    """Test case for patient_communications_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_communications/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_communications_update(client):
    """Test case for patient_communications_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_communications/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_flag_types_create(client):
    """Test case for patient_flag_types_create

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_flag_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_flag_types_list(client):
    """Test case for patient_flag_types_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_flag_types',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_flag_types_partial_update(client):
    """Test case for patient_flag_types_partial_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_flag_types/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_flag_types_read(client):
    """Test case for patient_flag_types_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_flag_types/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_flag_types_update(client):
    """Test case for patient_flag_types_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_flag_types/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_interventions_create(client):
    """Test case for patient_interventions_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_interventions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_interventions_list(client):
    """Test case for patient_interventions_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_interventions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_interventions_partial_update(client):
    """Test case for patient_interventions_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_interventions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_interventions_read(client):
    """Test case for patient_interventions_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_interventions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_interventions_update(client):
    """Test case for patient_interventions_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_interventions/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_lab_results_create(client):
    """Test case for patient_lab_results_create

    
    """
    params = [('ordering_doctor', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_lab_results',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_lab_results_delete(client):
    """Test case for patient_lab_results_delete

    
    """
    params = [('ordering_doctor', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/patient_lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_lab_results_list(client):
    """Test case for patient_lab_results_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('ordering_doctor', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_lab_results',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_lab_results_partial_update(client):
    """Test case for patient_lab_results_partial_update

    
    """
    params = [('ordering_doctor', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_lab_results_read(client):
    """Test case for patient_lab_results_read

    
    """
    params = [('ordering_doctor', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_lab_results_update(client):
    """Test case for patient_lab_results_update

    
    """
    params = [('ordering_doctor', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_lab_results/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_messages_create(client):
    """Test case for patient_messages_create

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_messages_list(client):
    """Test case for patient_messages_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_messages_partial_update(client):
    """Test case for patient_messages_partial_update

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_messages_read(client):
    """Test case for patient_messages_read

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_messages_update(client):
    """Test case for patient_messages_update

    
    """
    params = [('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_physical_exams_create(client):
    """Test case for patient_physical_exams_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_physical_exams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_physical_exams_list(client):
    """Test case for patient_physical_exams_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_physical_exams',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_physical_exams_partial_update(client):
    """Test case for patient_physical_exams_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_physical_exams/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_physical_exams_read(client):
    """Test case for patient_physical_exams_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_physical_exams/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_physical_exams_update(client):
    """Test case for patient_physical_exams_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_physical_exams/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_risk_assessments_create(client):
    """Test case for patient_risk_assessments_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_risk_assessments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_risk_assessments_list(client):
    """Test case for patient_risk_assessments_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_risk_assessments',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_risk_assessments_partial_update(client):
    """Test case for patient_risk_assessments_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_risk_assessments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_risk_assessments_read(client):
    """Test case for patient_risk_assessments_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_risk_assessments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_risk_assessments_update(client):
    """Test case for patient_risk_assessments_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_risk_assessments/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_vaccine_records_create(client):
    """Test case for patient_vaccine_records_create

    
    """
    params = [('cvx_code', 'cvx_code_example'),
                    ('patient', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patient_vaccine_records',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_vaccine_records_list(client):
    """Test case for patient_vaccine_records_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('cvx_code', 'cvx_code_example'),
                    ('patient', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_vaccine_records',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_vaccine_records_partial_update(client):
    """Test case for patient_vaccine_records_partial_update

    
    """
    params = [('cvx_code', 'cvx_code_example'),
                    ('patient', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patient_vaccine_records/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_vaccine_records_read(client):
    """Test case for patient_vaccine_records_read

    
    """
    params = [('cvx_code', 'cvx_code_example'),
                    ('patient', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patient_vaccine_records/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patient_vaccine_records_update(client):
    """Test case for patient_vaccine_records_update

    
    """
    params = [('cvx_code', 'cvx_code_example'),
                    ('patient', 56),
                    ('since', 'since_example'),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patient_vaccine_records/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_ccda(client):
    """Test case for patients_ccda

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Accept': 'application/xml',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patients/{id}/ccda'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_create(client):
    """Test case for patients_create

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_delete(client):
    """Test case for patients_delete

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/patients/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_list(client):
    """Test case for patients_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patients',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_onpatient_access_create(client):
    """Test case for patients_onpatient_access_create

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patients/{id}/onpatient_access'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_onpatient_access_delete(client):
    """Test case for patients_onpatient_access_delete

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/patients/{id}/onpatient_access'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_onpatient_access_read(client):
    """Test case for patients_onpatient_access_read

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patients/{id}/onpatient_access'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_partial_update(client):
    """Test case for patients_partial_update

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patients/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_qrda1(client):
    """Test case for patients_qrda1

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Accept': 'application/xml',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patients/{id}/qrda1'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_read(client):
    """Test case for patients_read

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patients/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_summary_create(client):
    """Test case for patients_summary_create

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/patients_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_summary_delete(client):
    """Test case for patients_summary_delete

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/patients_summary/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_summary_list(client):
    """Test case for patients_summary_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patients_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_summary_partial_update(client):
    """Test case for patients_summary_partial_update

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/patients_summary/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_summary_read(client):
    """Test case for patients_summary_read

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/patients_summary/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_summary_update(client):
    """Test case for patients_summary_update

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patients_summary/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patients_update(client):
    """Test case for patients_update

    
    """
    params = [('first_name', 'first_name_example'),
                    ('last_name', 'last_name_example'),
                    ('preferred_language', 'preferred_language_example'),
                    ('doctor', 56),
                    ('gender', 'gender_example'),
                    ('since', 'since_example'),
                    ('date_of_birth', 'date_of_birth_example'),
                    ('race', 'race_example'),
                    ('chart_id', 'chart_id_example'),
                    ('email', 'email_example'),
                    ('ethnicity', 'ethnicity_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/patients/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prescription_messages_list(client):
    """Test case for prescription_messages_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('parent_message', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/prescription_messages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_prescription_messages_read(client):
    """Test case for prescription_messages_read

    
    """
    params = [('parent_message', 56),
                    ('since', 'since_example'),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/prescription_messages/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_problems_create(client):
    """Test case for problems_create

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/problems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_problems_list(client):
    """Test case for problems_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/problems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_problems_partial_update(client):
    """Test case for problems_partial_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/problems/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_problems_read(client):
    """Test case for problems_read

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/problems/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_problems_update(client):
    """Test case for problems_update

    
    """
    params = [('patient', 56),
                    ('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/problems/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminder_profiles_create(client):
    """Test case for reminder_profiles_create

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/reminder_profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminder_profiles_delete(client):
    """Test case for reminder_profiles_delete

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/reminder_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminder_profiles_list(client):
    """Test case for reminder_profiles_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56),
                    ('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/reminder_profiles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminder_profiles_partial_update(client):
    """Test case for reminder_profiles_partial_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/reminder_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminder_profiles_read(client):
    """Test case for reminder_profiles_read

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/reminder_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reminder_profiles_update(client):
    """Test case for reminder_profiles_update

    
    """
    params = [('doctor', 56)]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/reminder_profiles/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sublabs_create(client):
    """Test case for sublabs_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/sublabs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sublabs_delete(client):
    """Test case for sublabs_delete

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/sublabs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sublabs_list(client):
    """Test case for sublabs_list

    
    """
    params = [('cursor', 'cursor_example'),
                    ('page_size', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/sublabs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sublabs_partial_update(client):
    """Test case for sublabs_partial_update

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/sublabs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sublabs_read(client):
    """Test case for sublabs_read

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/sublabs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sublabs_update(client):
    """Test case for sublabs_update

    
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/sublabs/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


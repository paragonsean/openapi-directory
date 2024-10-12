from typing import List, Dict
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
from openapi_server import util


async def allergies_create(request: web.Request, patient=None, doctor=None) -> web.Response:
    """allergies_create

    Create patient allergy

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def allergies_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None) -> web.Response:
    """allergies_list

    Retrieve or search patient allergies

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def allergies_partial_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """allergies_partial_update

    Update an existing patient allergy

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def allergies_read(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """allergies_read

    Retrieve an existing patient allergy

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def allergies_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """allergies_update

    Update an existing patient allergy

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def amendments_create(request: web.Request, appointment=None, patient=None, doctor=None) -> web.Response:
    """amendments_create

    Create patient amendments to a patient&#39;s clinical records

    :param appointment: 
    :type appointment: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def amendments_delete(request: web.Request, id, appointment=None, patient=None, doctor=None) -> web.Response:
    """amendments_delete

    Delete an existing patient amendment, you can only interact with amendments created by your API application

    :param id: 
    :type id: str
    :param appointment: 
    :type appointment: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def amendments_list(request: web.Request, cursor=None, page_size=None, appointment=None, patient=None, doctor=None) -> web.Response:
    """amendments_list

    Retrieve or search patient amendments. You can only interact with amendments created by your API application

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param appointment: 
    :type appointment: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def amendments_partial_update(request: web.Request, id, appointment=None, patient=None, doctor=None) -> web.Response:
    """amendments_partial_update

    Update an existing patient amendment, you can only interact with amendments created by your API application

    :param id: 
    :type id: str
    :param appointment: 
    :type appointment: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def amendments_read(request: web.Request, id, appointment=None, patient=None, doctor=None) -> web.Response:
    """amendments_read

    Retrieve an existing patient amendment, you can only interact with amendments created by your API application

    :param id: 
    :type id: str
    :param appointment: 
    :type appointment: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def amendments_update(request: web.Request, id, appointment=None, patient=None, doctor=None) -> web.Response:
    """amendments_update

    Update an existing patient amendment, you can only interact with amendments created by your API application

    :param id: 
    :type id: str
    :param appointment: 
    :type appointment: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_profiles_create(request: web.Request, doctor=None) -> web.Response:
    """appointment_profiles_create

    Create appointment profiles for a doctor&#39;s calendar

    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_profiles_delete(request: web.Request, id, doctor=None) -> web.Response:
    """appointment_profiles_delete

    Delete an existing appointment profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_profiles_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """appointment_profiles_list

    Retrieve or search appointment profiles for a doctor&#39;s calendar

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_profiles_partial_update(request: web.Request, id, doctor=None) -> web.Response:
    """appointment_profiles_partial_update

    Update an existing appointment profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_profiles_read(request: web.Request, id, doctor=None) -> web.Response:
    """appointment_profiles_read

    Retrieve an existing appointment profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_profiles_update(request: web.Request, id, doctor=None) -> web.Response:
    """appointment_profiles_update

    Update an existing appointment profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_templates_create(request: web.Request, profile=None, office=None, doctor=None) -> web.Response:
    """appointment_templates_create

    Create appointment templates for a doctor&#39;s calendar

    :param profile: 
    :type profile: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_templates_delete(request: web.Request, id, profile=None, office=None, doctor=None) -> web.Response:
    """appointment_templates_delete

    Delete an existing appointment template

    :param id: 
    :type id: str
    :param profile: 
    :type profile: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_templates_list(request: web.Request, cursor=None, page_size=None, profile=None, office=None, doctor=None) -> web.Response:
    """appointment_templates_list

    Retrieve or search appointment templates for a doctor&#39;s calendar

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param profile: 
    :type profile: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_templates_partial_update(request: web.Request, id, profile=None, office=None, doctor=None) -> web.Response:
    """appointment_templates_partial_update

    Update an existing appointment template

    :param id: 
    :type id: str
    :param profile: 
    :type profile: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_templates_read(request: web.Request, id, profile=None, office=None, doctor=None) -> web.Response:
    """appointment_templates_read

    Retrieve an existing appointment template

    :param id: 
    :type id: str
    :param profile: 
    :type profile: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointment_templates_update(request: web.Request, id, profile=None, office=None, doctor=None) -> web.Response:
    """appointment_templates_update

    Update an existing appointment template

    :param id: 
    :type id: str
    :param profile: 
    :type profile: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def appointments_create(request: web.Request, status=None, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """appointments_create

    Create a new appointment or break on doctor&#39;s calendar

    :param status: 
    :type status: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def appointments_delete(request: web.Request, id, status=None, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """appointments_delete

    Delete an existing appointment or break

    :param id: 
    :type id: str
    :param status: 
    :type status: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def appointments_list(request: web.Request, cursor=None, page_size=None, status=None, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """appointments_list

    Retrieve or search appointment or breaks. &lt;b&gt;Note:&lt;/b&gt; Either &#x60;since&#x60;, &#x60;date&#x60; or &#x60;date_range&#x60; parameter must be specified.             

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param status: 
    :type status: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def appointments_partial_update(request: web.Request, id, status=None, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """appointments_partial_update

    Update an existing appointment or break

    :param id: 
    :type id: str
    :param status: 
    :type status: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def appointments_read(request: web.Request, id, status=None, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """appointments_read

    Retrieve an existing appointment or break

    :param id: 
    :type id: str
    :param status: 
    :type status: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def appointments_update(request: web.Request, id, status=None, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """appointments_update

    Update an existing appointment or break

    :param id: 
    :type id: str
    :param status: 
    :type status: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def care_plans_list(request: web.Request, cursor=None, page_size=None, patient=None, plan_type=None, doctor=None) -> web.Response:
    """care_plans_list

    Retrieve or search care plans

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param plan_type: 
    :type plan_type: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def care_plans_read(request: web.Request, id, patient=None, plan_type=None, doctor=None) -> web.Response:
    """care_plans_read

    Retrieve an existing care plan

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param plan_type: 
    :type plan_type: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def care_team_members_list(request: web.Request, cursor=None, page_size=None, patient=None, appointment=None, doctor=None) -> web.Response:
    """care_team_members_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param appointment: 
    :type appointment: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def care_team_members_read(request: web.Request, id, patient=None, appointment=None, doctor=None) -> web.Response:
    """care_team_members_read

    

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param appointment: 
    :type appointment: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def claim_billing_notes_create(request: web.Request, appointment=None, doctor=None) -> web.Response:
    """claim_billing_notes_create

    Create a new billing note

    :param appointment: 
    :type appointment: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def claim_billing_notes_list(request: web.Request, cursor=None, page_size=None, appointment=None, doctor=None) -> web.Response:
    """claim_billing_notes_list

    Retrieve or search billing notes

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param appointment: 
    :type appointment: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def claim_billing_notes_read(request: web.Request, id, appointment=None, doctor=None) -> web.Response:
    """claim_billing_notes_read

    Retrieve an existing billing note

    :param id: 
    :type id: str
    :param appointment: 
    :type appointment: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_field_types_list(request: web.Request, cursor=None, page_size=None, clinical_note_template=None, doctor=None) -> web.Response:
    """clinical_note_field_types_list

    Retrieve or search clinical note field types

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param clinical_note_template: 
    :type clinical_note_template: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_field_types_read(request: web.Request, id, clinical_note_template=None, doctor=None) -> web.Response:
    """clinical_note_field_types_read

    Retrieve an existing clinial note field type

    :param id: 
    :type id: str
    :param clinical_note_template: 
    :type clinical_note_template: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_field_values_create(request: web.Request, clinical_note_field=None, since=None, appointment=None, clinical_note_template=None, doctor=None) -> web.Response:
    """clinical_note_field_values_create

    Create clinical note field value

    :param clinical_note_field: 
    :type clinical_note_field: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param clinical_note_template: 
    :type clinical_note_template: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_field_values_list(request: web.Request, cursor=None, page_size=None, clinical_note_field=None, since=None, appointment=None, clinical_note_template=None, doctor=None) -> web.Response:
    """clinical_note_field_values_list

    Retrieve or search clinical note field values

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param clinical_note_field: 
    :type clinical_note_field: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param clinical_note_template: 
    :type clinical_note_template: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_field_values_partial_update(request: web.Request, id, clinical_note_field=None, since=None, appointment=None, clinical_note_template=None, doctor=None) -> web.Response:
    """clinical_note_field_values_partial_update

    Update an existing clinical note field value

    :param id: 
    :type id: str
    :param clinical_note_field: 
    :type clinical_note_field: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param clinical_note_template: 
    :type clinical_note_template: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_field_values_read(request: web.Request, id, clinical_note_field=None, since=None, appointment=None, clinical_note_template=None, doctor=None) -> web.Response:
    """clinical_note_field_values_read

    Retrieve an existing clinical note field value

    :param id: 
    :type id: str
    :param clinical_note_field: 
    :type clinical_note_field: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param clinical_note_template: 
    :type clinical_note_template: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_field_values_update(request: web.Request, id, clinical_note_field=None, since=None, appointment=None, clinical_note_template=None, doctor=None) -> web.Response:
    """clinical_note_field_values_update

    Update an existing clinical note field value

    :param id: 
    :type id: str
    :param clinical_note_field: 
    :type clinical_note_field: int
    :param since: 
    :type since: str
    :param appointment: 
    :type appointment: int
    :param clinical_note_template: 
    :type clinical_note_template: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_templates_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """clinical_note_templates_list

    Retrieve or search clinical note templates

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_note_templates_read(request: web.Request, id, doctor=None) -> web.Response:
    """clinical_note_templates_read

    Retrieve an existing clinical note tempalte

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def clinical_notes_list(request: web.Request, cursor=None, page_size=None, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """clinical_notes_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def clinical_notes_read(request: web.Request, id, patient=None, office=None, doctor=None, since=None, date_range=None, _date=None) -> web.Response:
    """clinical_notes_read

    

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param office: 
    :type office: int
    :param doctor: 
    :type doctor: int
    :param since: 
    :type since: str
    :param date_range: 
    :type date_range: str
    :param _date: 
    :type _date: str

    """
    return web.Response(status=200)


async def consent_forms_apply_to_appointment(request: web.Request, id, doctor=None) -> web.Response:
    """consent_forms_apply_to_appointment

    Assign (apply) a consent form to appointment

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def consent_forms_create(request: web.Request, doctor=None) -> web.Response:
    """consent_forms_create

    Create a patient consent form

    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def consent_forms_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """consent_forms_list

    Retrieve or search patient consent forms

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def consent_forms_partial_update(request: web.Request, id, doctor=None) -> web.Response:
    """consent_forms_partial_update

    Update an existing patient consent form

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def consent_forms_read(request: web.Request, id, doctor=None) -> web.Response:
    """consent_forms_read

    Retrieve an existing patient consent form

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def consent_forms_unapply_from_appointment(request: web.Request, id, doctor=None) -> web.Response:
    """consent_forms_unapply_from_appointment

    Unassign (unapply) a consent form from appointment

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def consent_forms_update(request: web.Request, id, doctor=None) -> web.Response:
    """consent_forms_update

    Update an existing patient consent form

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_appointment_fields_create(request: web.Request, doctor=None) -> web.Response:
    """custom_appointment_fields_create

    Create custom appointment fields

    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_appointment_fields_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """custom_appointment_fields_list

    Retrieve or search custom appointment fields

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_appointment_fields_partial_update(request: web.Request, id, doctor=None) -> web.Response:
    """custom_appointment_fields_partial_update

    Update an existing custom appointment field

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_appointment_fields_read(request: web.Request, id, doctor=None) -> web.Response:
    """custom_appointment_fields_read

    Retrieve an existing custom appointment field

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_appointment_fields_update(request: web.Request, id, doctor=None) -> web.Response:
    """custom_appointment_fields_update

    Update an existing custom appointment field

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_demographics_create(request: web.Request, doctor=None) -> web.Response:
    """custom_demographics_create

    Create custom demographics fields

    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_demographics_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """custom_demographics_list

    Retrieve or search custom demographics fields

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_demographics_partial_update(request: web.Request, id, doctor=None) -> web.Response:
    """custom_demographics_partial_update

    Update an existing custom demographics field

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_demographics_read(request: web.Request, id, doctor=None) -> web.Response:
    """custom_demographics_read

    Retrieve an existing custom demographics field

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_demographics_update(request: web.Request, id, doctor=None) -> web.Response:
    """custom_demographics_update

    Update an existing custom demographics field

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_vitals_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """custom_vitals_list

    Retrieve or search custom vital types

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def custom_vitals_read(request: web.Request, id, doctor=None) -> web.Response:
    """custom_vitals_read

    Retrieve an existing custom vital type

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def documents_create(request: web.Request, since=None, patient=None, doctor=None) -> web.Response:
    """documents_create

    Create documents

    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def documents_delete(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """documents_delete

    Delete an existing appointment template

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def documents_list(request: web.Request, cursor=None, page_size=None, since=None, patient=None, doctor=None) -> web.Response:
    """documents_list

    Retrieve or search documents

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def documents_partial_update(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """documents_partial_update

    Update an existing appointment template

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def documents_read(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """documents_read

    Retrieve an existing appointment template

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def documents_update(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """documents_update

    Update an existing appointment template

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def eobs_create(request: web.Request, doctor=None) -> web.Response:
    """eobs_create

    Create EOB object

    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def eobs_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """eobs_list

    Retrieve or search EOB objects

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def eobs_read(request: web.Request, id, doctor=None) -> web.Response:
    """eobs_read

    Retrieve an existing EOB object

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def fee_schedules_list(request: web.Request, cursor=None, page_size=None, code=None, code_type=None, since=None, payer_id=None, doctor=None) -> web.Response:
    """fee_schedules_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param code: 
    :type code: str
    :param code_type: 
    :type code_type: str
    :param since: 
    :type since: str
    :param payer_id: 
    :type payer_id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def fee_schedules_read(request: web.Request, id, code=None, code_type=None, since=None, payer_id=None, doctor=None) -> web.Response:
    """fee_schedules_read

    

    :param id: 
    :type id: str
    :param code: 
    :type code: str
    :param code_type: 
    :type code_type: str
    :param since: 
    :type since: str
    :param payer_id: 
    :type payer_id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def implantable_devices_list(request: web.Request, cursor=None, page_size=None, mu_date=None, patient=None, mu_date_range=None, doctor=None) -> web.Response:
    """implantable_devices_list

    Retrieve or search implantable devices

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param mu_date: 
    :type mu_date: str
    :param patient: 
    :type patient: int
    :param mu_date_range: 
    :type mu_date_range: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def implantable_devices_read(request: web.Request, id, mu_date=None, patient=None, mu_date_range=None, doctor=None) -> web.Response:
    """implantable_devices_read

    Retrieve an existing implantable device

    :param id: 
    :type id: str
    :param mu_date: 
    :type mu_date: str
    :param patient: 
    :type patient: int
    :param mu_date_range: 
    :type mu_date_range: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def insurances_list(request: web.Request, payer_type, cursor=None, page_size=None, term=None) -> web.Response:
    """insurances_list

    

    :param payer_type: One of &#x60;\&quot;emdeon\&quot;&#x60;, &#x60;\&quot;gateway\&quot;&#x60;, &#x60;\&quot;ihcfa\&quot;&#x60;
    :type payer_type: str
    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param term: Search term, which can be either a partial name, partial ID or the state.
    :type term: str

    """
    return web.Response(status=200)


async def insurances_read(request: web.Request, id, payer_type, term=None) -> web.Response:
    """insurances_read

    

    :param id: 
    :type id: str
    :param payer_type: One of &#x60;\&quot;emdeon\&quot;&#x60;, &#x60;\&quot;gateway\&quot;&#x60;, &#x60;\&quot;ihcfa\&quot;&#x60;
    :type payer_type: str
    :param term: Search term, which can be either a partial name, partial ID or the state.
    :type term: str

    """
    return web.Response(status=200)


async def lab_documents_create(request: web.Request, since=None, doctor=None) -> web.Response:
    """lab_documents_create

    Create lab order documents. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 

    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_documents_delete(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_documents_delete

    Delete an existing lab order document

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_documents_list(request: web.Request, cursor=None, page_size=None, since=None, doctor=None) -> web.Response:
    """lab_documents_list

    Retrieve or search lab order documents

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_documents_partial_update(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_documents_partial_update

    Update an existing lab order document

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_documents_read(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_documents_read

    Retrieve an existing lab order document

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_documents_update(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_documents_update

    Update an existing lab order document

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_create(request: web.Request, since=None, doctor=None) -> web.Response:
    """lab_orders_create

    Create lab orders. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 

    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_delete(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_orders_delete

    Delete an existing lab order

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_list(request: web.Request, cursor=None, page_size=None, since=None, doctor=None) -> web.Response:
    """lab_orders_list

    Retrieve or search lab orders

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_partial_update(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_orders_partial_update

    Update an existing lab order

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_read(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_orders_read

    Retrieve an existing lab order

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_summary_list(request: web.Request, cursor=None, page_size=None, since=None, patient=None, doctor=None) -> web.Response:
    """lab_orders_summary_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_summary_read(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """lab_orders_summary_read

    

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_orders_update(request: web.Request, id, since=None, doctor=None) -> web.Response:
    """lab_orders_update

    Update an existing lab order

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_results_create(request: web.Request, order=None, doctor=None) -> web.Response:
    """lab_results_create

    Create lab results. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 

    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_results_delete(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_results_delete

    Delete an existing lab result

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_results_list(request: web.Request, cursor=None, page_size=None, order=None, doctor=None) -> web.Response:
    """lab_results_list

    Retrieve or search lab results

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_results_partial_update(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_results_partial_update

    Update an existing lab result

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_results_read(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_results_read

    Retrieve an existing lab result

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_results_update(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_results_update

    Update an existing lab result

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_tests_create(request: web.Request, order=None, doctor=None) -> web.Response:
    """lab_tests_create

    Create lab tests. An example lab workflow is as following:  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 

    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_tests_delete(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_tests_delete

    Delete an existing lab test

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_tests_list(request: web.Request, cursor=None, page_size=None, order=None, doctor=None) -> web.Response:
    """lab_tests_list

    Retrieve or search lab tests

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_tests_partial_update(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_tests_partial_update

    Update an existing lab test

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_tests_read(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_tests_read

    Retrieve an existing lab test

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def lab_tests_update(request: web.Request, id, order=None, doctor=None) -> web.Response:
    """lab_tests_update

    Update an existing lab test

    :param id: 
    :type id: str
    :param order: 
    :type order: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def medications_append_to_pharmacy_note(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """medications_append_to_pharmacy_note

    Append a message to the \&quot;pharmacy_note\&quot; section of the prescription, in a new paragraph

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def medications_create(request: web.Request, patient=None, doctor=None) -> web.Response:
    """medications_create

    Create patient medications

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def medications_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None) -> web.Response:
    """medications_list

    Retrieve or search patient medications

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def medications_partial_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """medications_partial_update

    Update an existing patient medications

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def medications_read(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """medications_read

    Retrieve an existing patient medications

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def medications_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """medications_update

    Update an existing patient medications

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_communications_create(request: web.Request, patient=None, doctor=None) -> web.Response:
    """patient_communications_create

    Create patient communication for CQM

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_communications_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None) -> web.Response:
    """patient_communications_list

    Retrieve or search patient communications for CQM

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_communications_partial_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_communications_partial_update

    Update an existing patient communication for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_communications_read(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_communications_read

    Retrieve an existing patient communication for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_communications_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_communications_update

    Update an existing patient communication for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_flag_types_create(request: web.Request, doctor=None) -> web.Response:
    """patient_flag_types_create

    Create patient flag types

    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_flag_types_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """patient_flag_types_list

    Retrieve or search patient flag types

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_flag_types_partial_update(request: web.Request, id, doctor=None) -> web.Response:
    """patient_flag_types_partial_update

    Update an existing patient flag type

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_flag_types_read(request: web.Request, id, doctor=None) -> web.Response:
    """patient_flag_types_read

    Retrieve an existing patient flag type

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_flag_types_update(request: web.Request, id, doctor=None) -> web.Response:
    """patient_flag_types_update

    Update an existing patient flag type

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_interventions_create(request: web.Request, patient=None, doctor=None) -> web.Response:
    """patient_interventions_create

    Create patient intervention for CQM

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_interventions_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None) -> web.Response:
    """patient_interventions_list

    Retrieve or search patient interventions for CQM

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_interventions_partial_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_interventions_partial_update

    Update an existing patient intervention for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_interventions_read(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_interventions_read

    Retrieve an existing patient intervention for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_interventions_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_interventions_update

    Update an existing patient intervention for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_lab_results_create(request: web.Request, ordering_doctor=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_lab_results_create

    

    :param ordering_doctor: 
    :type ordering_doctor: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_lab_results_delete(request: web.Request, id, ordering_doctor=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_lab_results_delete

    

    :param id: 
    :type id: str
    :param ordering_doctor: 
    :type ordering_doctor: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_lab_results_list(request: web.Request, cursor=None, page_size=None, ordering_doctor=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_lab_results_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param ordering_doctor: 
    :type ordering_doctor: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_lab_results_partial_update(request: web.Request, id, ordering_doctor=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_lab_results_partial_update

    

    :param id: 
    :type id: str
    :param ordering_doctor: 
    :type ordering_doctor: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_lab_results_read(request: web.Request, id, ordering_doctor=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_lab_results_read

    

    :param id: 
    :type id: str
    :param ordering_doctor: 
    :type ordering_doctor: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_lab_results_update(request: web.Request, id, ordering_doctor=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_lab_results_update

    

    :param id: 
    :type id: str
    :param ordering_doctor: 
    :type ordering_doctor: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_messages_create(request: web.Request, since=None, patient=None, doctor=None) -> web.Response:
    """patient_messages_create

    

    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_messages_list(request: web.Request, cursor=None, page_size=None, since=None, patient=None, doctor=None) -> web.Response:
    """patient_messages_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_messages_partial_update(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """patient_messages_partial_update

    

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_messages_read(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """patient_messages_read

    

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_messages_update(request: web.Request, id, since=None, patient=None, doctor=None) -> web.Response:
    """patient_messages_update

    

    :param id: 
    :type id: str
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_physical_exams_create(request: web.Request, patient=None, doctor=None) -> web.Response:
    """patient_physical_exams_create

    Create patient physical exam for CQM

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_physical_exams_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None) -> web.Response:
    """patient_physical_exams_list

    Retrieve or search patient physical exams for CQM

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_physical_exams_partial_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_physical_exams_partial_update

    Update an existing patient physical exam for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_physical_exams_read(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_physical_exams_read

    Retrieve an existing patient physical exam for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_physical_exams_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_physical_exams_update

    Update an existing patient physical exam for CQM

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_risk_assessments_create(request: web.Request, patient=None, doctor=None) -> web.Response:
    """patient_risk_assessments_create

    

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_risk_assessments_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None) -> web.Response:
    """patient_risk_assessments_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_risk_assessments_partial_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_risk_assessments_partial_update

    

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_risk_assessments_read(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_risk_assessments_read

    

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_risk_assessments_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """patient_risk_assessments_update

    

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_vaccine_records_create(request: web.Request, cvx_code=None, patient=None, since=None, doctor=None) -> web.Response:
    """patient_vaccine_records_create

    Create patient vaccine records

    :param cvx_code: 
    :type cvx_code: str
    :param patient: 
    :type patient: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_vaccine_records_list(request: web.Request, cursor=None, page_size=None, cvx_code=None, patient=None, since=None, doctor=None) -> web.Response:
    """patient_vaccine_records_list

    Retrieve or search patient vaccine records

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param cvx_code: 
    :type cvx_code: str
    :param patient: 
    :type patient: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_vaccine_records_partial_update(request: web.Request, id, cvx_code=None, patient=None, since=None, doctor=None) -> web.Response:
    """patient_vaccine_records_partial_update

    Update an existing patient vaccine records

    :param id: 
    :type id: str
    :param cvx_code: 
    :type cvx_code: str
    :param patient: 
    :type patient: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_vaccine_records_read(request: web.Request, id, cvx_code=None, patient=None, since=None, doctor=None) -> web.Response:
    """patient_vaccine_records_read

    Retrieve an existing patient vaccine records

    :param id: 
    :type id: str
    :param cvx_code: 
    :type cvx_code: str
    :param patient: 
    :type patient: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patient_vaccine_records_update(request: web.Request, id, cvx_code=None, patient=None, since=None, doctor=None) -> web.Response:
    """patient_vaccine_records_update

    Update an existing patient vaccine records

    :param id: 
    :type id: str
    :param cvx_code: 
    :type cvx_code: str
    :param patient: 
    :type patient: int
    :param since: 
    :type since: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def patients_ccda(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_ccda

    Retrieve patient CCDA

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_create(request: web.Request, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_create

    Create patient

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_delete(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_delete

    Delete an existing patient

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_list(request: web.Request, cursor=None, page_size=None, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_list

    Retrieve or search patients

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_onpatient_access_create(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_onpatient_access_create

    Send new onpatient invite to patient

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_onpatient_access_delete(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_onpatient_access_delete

    Revoke sent onpatient invites

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_onpatient_access_read(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_onpatient_access_read

    Retrieve or search existing onpatient access invites

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_partial_update(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_partial_update

    Update an existing patient

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_qrda1(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_qrda1

    Retrieve patient QRDA1

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_read(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_read

    Retrieve an existing patient

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def patients_summary_create(request: web.Request, first_name=None, last_name=None, doctor=None, gender=None, since=None, date_of_birth=None) -> web.Response:
    """patients_summary_create

    

    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str

    """
    return web.Response(status=200)


async def patients_summary_delete(request: web.Request, id, first_name=None, last_name=None, doctor=None, gender=None, since=None, date_of_birth=None) -> web.Response:
    """patients_summary_delete

    

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str

    """
    return web.Response(status=200)


async def patients_summary_list(request: web.Request, cursor=None, page_size=None, first_name=None, last_name=None, doctor=None, gender=None, since=None, date_of_birth=None) -> web.Response:
    """patients_summary_list

    

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str

    """
    return web.Response(status=200)


async def patients_summary_partial_update(request: web.Request, id, first_name=None, last_name=None, doctor=None, gender=None, since=None, date_of_birth=None) -> web.Response:
    """patients_summary_partial_update

    

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str

    """
    return web.Response(status=200)


async def patients_summary_read(request: web.Request, id, first_name=None, last_name=None, doctor=None, gender=None, since=None, date_of_birth=None) -> web.Response:
    """patients_summary_read

    

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str

    """
    return web.Response(status=200)


async def patients_summary_update(request: web.Request, id, first_name=None, last_name=None, doctor=None, gender=None, since=None, date_of_birth=None) -> web.Response:
    """patients_summary_update

    

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str

    """
    return web.Response(status=200)


async def patients_update(request: web.Request, id, first_name=None, last_name=None, preferred_language=None, doctor=None, gender=None, since=None, date_of_birth=None, race=None, chart_id=None, email=None, ethnicity=None) -> web.Response:
    """patients_update

    Update an existing patient

    :param id: 
    :type id: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param preferred_language: 
    :type preferred_language: str
    :param doctor: 
    :type doctor: int
    :param gender: 
    :type gender: str
    :param since: 
    :type since: str
    :param date_of_birth: 
    :type date_of_birth: str
    :param race: 
    :type race: str
    :param chart_id: 
    :type chart_id: str
    :param email: 
    :type email: str
    :param ethnicity: 
    :type ethnicity: str

    """
    return web.Response(status=200)


async def prescription_messages_list(request: web.Request, cursor=None, page_size=None, parent_message=None, since=None, patient=None, doctor=None) -> web.Response:
    """prescription_messages_list

    Retrieve or search prescription messages

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param parent_message: 
    :type parent_message: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def prescription_messages_read(request: web.Request, id, parent_message=None, since=None, patient=None, doctor=None) -> web.Response:
    """prescription_messages_read

    Retrieve an existing prescription message

    :param id: 
    :type id: str
    :param parent_message: 
    :type parent_message: int
    :param since: 
    :type since: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def problems_create(request: web.Request, patient=None, doctor=None) -> web.Response:
    """problems_create

    Create patient problems

    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def problems_list(request: web.Request, cursor=None, page_size=None, patient=None, doctor=None) -> web.Response:
    """problems_list

    Retrieve or search patient problems

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def problems_partial_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """problems_partial_update

    Update an existing patient problems

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def problems_read(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """problems_read

    Retrieve an existing patient problems

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def problems_update(request: web.Request, id, patient=None, doctor=None) -> web.Response:
    """problems_update

    Update an existing patient problems

    :param id: 
    :type id: str
    :param patient: 
    :type patient: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def reminder_profiles_create(request: web.Request, doctor=None) -> web.Response:
    """reminder_profiles_create

    Create reminder profile

    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def reminder_profiles_delete(request: web.Request, id, doctor=None) -> web.Response:
    """reminder_profiles_delete

    Delete an existing reminder profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def reminder_profiles_list(request: web.Request, cursor=None, page_size=None, doctor=None) -> web.Response:
    """reminder_profiles_list

    Retrieve or search reminder profiles

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def reminder_profiles_partial_update(request: web.Request, id, doctor=None) -> web.Response:
    """reminder_profiles_partial_update

    Update an existing reminder profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def reminder_profiles_read(request: web.Request, id, doctor=None) -> web.Response:
    """reminder_profiles_read

    Retrieve an existing reminder profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def reminder_profiles_update(request: web.Request, id, doctor=None) -> web.Response:
    """reminder_profiles_update

    Update an existing reminder profile

    :param id: 
    :type id: str
    :param doctor: 
    :type doctor: int

    """
    return web.Response(status=200)


async def sublabs_create(request: web.Request, ) -> web.Response:
    """sublabs_create

    Create sub-vendors  - When you get orders, submit them via &#x60;/api/lab_orders&#x60;, such that doctors can see them in drchrono.  - When results come in, submit the result document PDF via &#x60;/api/lab_documents&#x60; and submit the results data via &#x60;/api/lab_results&#x60;  - Update &#x60;/api/lab_orders&#x60; status 


    """
    return web.Response(status=200)


async def sublabs_delete(request: web.Request, id) -> web.Response:
    """sublabs_delete

    Delete an existing sub vendor

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def sublabs_list(request: web.Request, cursor=None, page_size=None) -> web.Response:
    """sublabs_list

    Retrieve or search sub vendors

    :param cursor: 
    :type cursor: str
    :param page_size: 
    :type page_size: int

    """
    return web.Response(status=200)


async def sublabs_partial_update(request: web.Request, id) -> web.Response:
    """sublabs_partial_update

    Update an existing sub vendor

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def sublabs_read(request: web.Request, id) -> web.Response:
    """sublabs_read

    Retrieve an existing sub vendor

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def sublabs_update(request: web.Request, id) -> web.Response:
    """sublabs_update

    Update an existing sub vendor

    :param id: 
    :type id: int

    """
    return web.Response(status=200)

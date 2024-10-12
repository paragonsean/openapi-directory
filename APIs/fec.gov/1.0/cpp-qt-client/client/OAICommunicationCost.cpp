/**
 * OpenFEC
 * This application programming interface (API) allows you to explore the way candidates and committees fund their campaigns.    The Federal Election Commission (FEC) API is a RESTful web service supporting full-text and field-specific searches on FEC data. [Bulk downloads](https://www.fec.gov/data/advanced/?tab=bulk-data) are available on the current site. Information is tied to the underlying forms by file ID and image ID. Data is updated nightly.    There are a lot of data, and a good place to start is to use search to find interesting candidates and committees. Then, you can use their IDs to find report or line item details with the other endpoints. If you are interested in individual donors, check out contributor information in the `/schedule_a/` endpoints.    <b class=\"body\" id=\"getting_started_head\">Getting started with the openFEC API</b><br>    If you would like to use the FEC's API programmatically, you can sign up for your own API key using our form. Alternatively, you can still try out our API without an API key by using the web interface and using DEMO_KEY. Note that when you use the openFEC API you are subject to the [Terms of Service](https://github.com/fecgov/FEC/blob/master/TERMS-OF-SERVICE.md) and [Acceptable Use policy](https://github.com/fecgov/FEC/blob/master/ACCEPTABLE-USE-POLICY.md).    Signing up for an API key will enable you to place up to 1,000 calls an hour. Each call is limited to 100 results per page. You can email questions, comments or a request to get a key for 7,200 calls an hour (120 calls per minute) to <a href=\"mailto:APIinfo@fec.gov\">APIinfo@fec.gov</a>. You can also ask questions and discuss the data in a community led [group](https://groups.google.com/forum/#!forum/fec-data).    The model definitions and schema are available at [/swagger](/swagger/). This is useful for making wrappers and exploring the data.    A few restrictions limit the way you can use FEC data. For example, you can’t use contributor lists for commercial purposes or to solicit donations. [Learn more here](https://www.fec.gov/updates/sale-or-use-contributor-information/).    [Inspect our source code](https://github.com/fecgov/openFEC). We welcome issues and pull requests!    <p><br></p> <h2 class=\"title\" id=\"signup_head\">Sign up for an API key</h2> <div id=\"apidatagov_signup\">Loading signup form...</div>
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICommunicationCost.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICommunicationCost::OAICommunicationCost(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICommunicationCost::OAICommunicationCost() {
    this->initializeModel();
}

OAICommunicationCost::~OAICommunicationCost() {}

void OAICommunicationCost::initializeModel() {

    m_action_code_isSet = false;
    m_action_code_isValid = false;

    m_action_code_full_isSet = false;
    m_action_code_full_isValid = false;

    m_candidate_first_name_isSet = false;
    m_candidate_first_name_isValid = false;

    m_candidate_id_isSet = false;
    m_candidate_id_isValid = false;

    m_candidate_last_name_isSet = false;
    m_candidate_last_name_isValid = false;

    m_candidate_middle_name_isSet = false;
    m_candidate_middle_name_isValid = false;

    m_candidate_name_isSet = false;
    m_candidate_name_isValid = false;

    m_candidate_office_isSet = false;
    m_candidate_office_isValid = false;

    m_candidate_office_district_isSet = false;
    m_candidate_office_district_isValid = false;

    m_candidate_office_full_isSet = false;
    m_candidate_office_full_isValid = false;

    m_candidate_office_state_isSet = false;
    m_candidate_office_state_isValid = false;

    m_committee_id_isSet = false;
    m_committee_id_isValid = false;

    m_committee_name_isSet = false;
    m_committee_name_isValid = false;

    m_communication_class_isSet = false;
    m_communication_class_isValid = false;

    m_communication_type_isSet = false;
    m_communication_type_isValid = false;

    m_communication_type_full_isSet = false;
    m_communication_type_full_isValid = false;

    m_cycle_isSet = false;
    m_cycle_isValid = false;

    m_file_number_isSet = false;
    m_file_number_isValid = false;

    m_form_type_code_isSet = false;
    m_form_type_code_isValid = false;

    m_image_number_isSet = false;
    m_image_number_isValid = false;

    m_original_sub_id_isSet = false;
    m_original_sub_id_isValid = false;

    m_pdf_url_isSet = false;
    m_pdf_url_isValid = false;

    m_primary_general_indicator_isSet = false;
    m_primary_general_indicator_isValid = false;

    m_primary_general_indicator_description_isSet = false;
    m_primary_general_indicator_description_isValid = false;

    m_purpose_isSet = false;
    m_purpose_isValid = false;

    m_report_type_isSet = false;
    m_report_type_isValid = false;

    m_report_year_isSet = false;
    m_report_year_isValid = false;

    m_schedule_type_isSet = false;
    m_schedule_type_isValid = false;

    m_schedule_type_full_isSet = false;
    m_schedule_type_full_isValid = false;

    m_state_full_isSet = false;
    m_state_full_isValid = false;

    m_sub_id_isSet = false;
    m_sub_id_isValid = false;

    m_support_oppose_indicator_isSet = false;
    m_support_oppose_indicator_isValid = false;

    m_tran_id_isSet = false;
    m_tran_id_isValid = false;

    m_transaction_amount_isSet = false;
    m_transaction_amount_isValid = false;

    m_transaction_date_isSet = false;
    m_transaction_date_isValid = false;

    m_transaction_type_isSet = false;
    m_transaction_type_isValid = false;
}

void OAICommunicationCost::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICommunicationCost::fromJsonObject(QJsonObject json) {

    m_action_code_isValid = ::OpenAPI::fromJsonValue(m_action_code, json[QString("action_code")]);
    m_action_code_isSet = !json[QString("action_code")].isNull() && m_action_code_isValid;

    m_action_code_full_isValid = ::OpenAPI::fromJsonValue(m_action_code_full, json[QString("action_code_full")]);
    m_action_code_full_isSet = !json[QString("action_code_full")].isNull() && m_action_code_full_isValid;

    m_candidate_first_name_isValid = ::OpenAPI::fromJsonValue(m_candidate_first_name, json[QString("candidate_first_name")]);
    m_candidate_first_name_isSet = !json[QString("candidate_first_name")].isNull() && m_candidate_first_name_isValid;

    m_candidate_id_isValid = ::OpenAPI::fromJsonValue(m_candidate_id, json[QString("candidate_id")]);
    m_candidate_id_isSet = !json[QString("candidate_id")].isNull() && m_candidate_id_isValid;

    m_candidate_last_name_isValid = ::OpenAPI::fromJsonValue(m_candidate_last_name, json[QString("candidate_last_name")]);
    m_candidate_last_name_isSet = !json[QString("candidate_last_name")].isNull() && m_candidate_last_name_isValid;

    m_candidate_middle_name_isValid = ::OpenAPI::fromJsonValue(m_candidate_middle_name, json[QString("candidate_middle_name")]);
    m_candidate_middle_name_isSet = !json[QString("candidate_middle_name")].isNull() && m_candidate_middle_name_isValid;

    m_candidate_name_isValid = ::OpenAPI::fromJsonValue(m_candidate_name, json[QString("candidate_name")]);
    m_candidate_name_isSet = !json[QString("candidate_name")].isNull() && m_candidate_name_isValid;

    m_candidate_office_isValid = ::OpenAPI::fromJsonValue(m_candidate_office, json[QString("candidate_office")]);
    m_candidate_office_isSet = !json[QString("candidate_office")].isNull() && m_candidate_office_isValid;

    m_candidate_office_district_isValid = ::OpenAPI::fromJsonValue(m_candidate_office_district, json[QString("candidate_office_district")]);
    m_candidate_office_district_isSet = !json[QString("candidate_office_district")].isNull() && m_candidate_office_district_isValid;

    m_candidate_office_full_isValid = ::OpenAPI::fromJsonValue(m_candidate_office_full, json[QString("candidate_office_full")]);
    m_candidate_office_full_isSet = !json[QString("candidate_office_full")].isNull() && m_candidate_office_full_isValid;

    m_candidate_office_state_isValid = ::OpenAPI::fromJsonValue(m_candidate_office_state, json[QString("candidate_office_state")]);
    m_candidate_office_state_isSet = !json[QString("candidate_office_state")].isNull() && m_candidate_office_state_isValid;

    m_committee_id_isValid = ::OpenAPI::fromJsonValue(m_committee_id, json[QString("committee_id")]);
    m_committee_id_isSet = !json[QString("committee_id")].isNull() && m_committee_id_isValid;

    m_committee_name_isValid = ::OpenAPI::fromJsonValue(m_committee_name, json[QString("committee_name")]);
    m_committee_name_isSet = !json[QString("committee_name")].isNull() && m_committee_name_isValid;

    m_communication_class_isValid = ::OpenAPI::fromJsonValue(m_communication_class, json[QString("communication_class")]);
    m_communication_class_isSet = !json[QString("communication_class")].isNull() && m_communication_class_isValid;

    m_communication_type_isValid = ::OpenAPI::fromJsonValue(m_communication_type, json[QString("communication_type")]);
    m_communication_type_isSet = !json[QString("communication_type")].isNull() && m_communication_type_isValid;

    m_communication_type_full_isValid = ::OpenAPI::fromJsonValue(m_communication_type_full, json[QString("communication_type_full")]);
    m_communication_type_full_isSet = !json[QString("communication_type_full")].isNull() && m_communication_type_full_isValid;

    m_cycle_isValid = ::OpenAPI::fromJsonValue(m_cycle, json[QString("cycle")]);
    m_cycle_isSet = !json[QString("cycle")].isNull() && m_cycle_isValid;

    m_file_number_isValid = ::OpenAPI::fromJsonValue(m_file_number, json[QString("file_number")]);
    m_file_number_isSet = !json[QString("file_number")].isNull() && m_file_number_isValid;

    m_form_type_code_isValid = ::OpenAPI::fromJsonValue(m_form_type_code, json[QString("form_type_code")]);
    m_form_type_code_isSet = !json[QString("form_type_code")].isNull() && m_form_type_code_isValid;

    m_image_number_isValid = ::OpenAPI::fromJsonValue(m_image_number, json[QString("image_number")]);
    m_image_number_isSet = !json[QString("image_number")].isNull() && m_image_number_isValid;

    m_original_sub_id_isValid = ::OpenAPI::fromJsonValue(m_original_sub_id, json[QString("original_sub_id")]);
    m_original_sub_id_isSet = !json[QString("original_sub_id")].isNull() && m_original_sub_id_isValid;

    m_pdf_url_isValid = ::OpenAPI::fromJsonValue(m_pdf_url, json[QString("pdf_url")]);
    m_pdf_url_isSet = !json[QString("pdf_url")].isNull() && m_pdf_url_isValid;

    m_primary_general_indicator_isValid = ::OpenAPI::fromJsonValue(m_primary_general_indicator, json[QString("primary_general_indicator")]);
    m_primary_general_indicator_isSet = !json[QString("primary_general_indicator")].isNull() && m_primary_general_indicator_isValid;

    m_primary_general_indicator_description_isValid = ::OpenAPI::fromJsonValue(m_primary_general_indicator_description, json[QString("primary_general_indicator_description")]);
    m_primary_general_indicator_description_isSet = !json[QString("primary_general_indicator_description")].isNull() && m_primary_general_indicator_description_isValid;

    m_purpose_isValid = ::OpenAPI::fromJsonValue(m_purpose, json[QString("purpose")]);
    m_purpose_isSet = !json[QString("purpose")].isNull() && m_purpose_isValid;

    m_report_type_isValid = ::OpenAPI::fromJsonValue(m_report_type, json[QString("report_type")]);
    m_report_type_isSet = !json[QString("report_type")].isNull() && m_report_type_isValid;

    m_report_year_isValid = ::OpenAPI::fromJsonValue(m_report_year, json[QString("report_year")]);
    m_report_year_isSet = !json[QString("report_year")].isNull() && m_report_year_isValid;

    m_schedule_type_isValid = ::OpenAPI::fromJsonValue(m_schedule_type, json[QString("schedule_type")]);
    m_schedule_type_isSet = !json[QString("schedule_type")].isNull() && m_schedule_type_isValid;

    m_schedule_type_full_isValid = ::OpenAPI::fromJsonValue(m_schedule_type_full, json[QString("schedule_type_full")]);
    m_schedule_type_full_isSet = !json[QString("schedule_type_full")].isNull() && m_schedule_type_full_isValid;

    m_state_full_isValid = ::OpenAPI::fromJsonValue(m_state_full, json[QString("state_full")]);
    m_state_full_isSet = !json[QString("state_full")].isNull() && m_state_full_isValid;

    m_sub_id_isValid = ::OpenAPI::fromJsonValue(m_sub_id, json[QString("sub_id")]);
    m_sub_id_isSet = !json[QString("sub_id")].isNull() && m_sub_id_isValid;

    m_support_oppose_indicator_isValid = ::OpenAPI::fromJsonValue(m_support_oppose_indicator, json[QString("support_oppose_indicator")]);
    m_support_oppose_indicator_isSet = !json[QString("support_oppose_indicator")].isNull() && m_support_oppose_indicator_isValid;

    m_tran_id_isValid = ::OpenAPI::fromJsonValue(m_tran_id, json[QString("tran_id")]);
    m_tran_id_isSet = !json[QString("tran_id")].isNull() && m_tran_id_isValid;

    m_transaction_amount_isValid = ::OpenAPI::fromJsonValue(m_transaction_amount, json[QString("transaction_amount")]);
    m_transaction_amount_isSet = !json[QString("transaction_amount")].isNull() && m_transaction_amount_isValid;

    m_transaction_date_isValid = ::OpenAPI::fromJsonValue(m_transaction_date, json[QString("transaction_date")]);
    m_transaction_date_isSet = !json[QString("transaction_date")].isNull() && m_transaction_date_isValid;

    m_transaction_type_isValid = ::OpenAPI::fromJsonValue(m_transaction_type, json[QString("transaction_type")]);
    m_transaction_type_isSet = !json[QString("transaction_type")].isNull() && m_transaction_type_isValid;
}

QString OAICommunicationCost::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICommunicationCost::asJsonObject() const {
    QJsonObject obj;
    if (m_action_code_isSet) {
        obj.insert(QString("action_code"), ::OpenAPI::toJsonValue(m_action_code));
    }
    if (m_action_code_full_isSet) {
        obj.insert(QString("action_code_full"), ::OpenAPI::toJsonValue(m_action_code_full));
    }
    if (m_candidate_first_name_isSet) {
        obj.insert(QString("candidate_first_name"), ::OpenAPI::toJsonValue(m_candidate_first_name));
    }
    if (m_candidate_id_isSet) {
        obj.insert(QString("candidate_id"), ::OpenAPI::toJsonValue(m_candidate_id));
    }
    if (m_candidate_last_name_isSet) {
        obj.insert(QString("candidate_last_name"), ::OpenAPI::toJsonValue(m_candidate_last_name));
    }
    if (m_candidate_middle_name_isSet) {
        obj.insert(QString("candidate_middle_name"), ::OpenAPI::toJsonValue(m_candidate_middle_name));
    }
    if (m_candidate_name_isSet) {
        obj.insert(QString("candidate_name"), ::OpenAPI::toJsonValue(m_candidate_name));
    }
    if (m_candidate_office_isSet) {
        obj.insert(QString("candidate_office"), ::OpenAPI::toJsonValue(m_candidate_office));
    }
    if (m_candidate_office_district_isSet) {
        obj.insert(QString("candidate_office_district"), ::OpenAPI::toJsonValue(m_candidate_office_district));
    }
    if (m_candidate_office_full_isSet) {
        obj.insert(QString("candidate_office_full"), ::OpenAPI::toJsonValue(m_candidate_office_full));
    }
    if (m_candidate_office_state_isSet) {
        obj.insert(QString("candidate_office_state"), ::OpenAPI::toJsonValue(m_candidate_office_state));
    }
    if (m_committee_id_isSet) {
        obj.insert(QString("committee_id"), ::OpenAPI::toJsonValue(m_committee_id));
    }
    if (m_committee_name_isSet) {
        obj.insert(QString("committee_name"), ::OpenAPI::toJsonValue(m_committee_name));
    }
    if (m_communication_class_isSet) {
        obj.insert(QString("communication_class"), ::OpenAPI::toJsonValue(m_communication_class));
    }
    if (m_communication_type_isSet) {
        obj.insert(QString("communication_type"), ::OpenAPI::toJsonValue(m_communication_type));
    }
    if (m_communication_type_full_isSet) {
        obj.insert(QString("communication_type_full"), ::OpenAPI::toJsonValue(m_communication_type_full));
    }
    if (m_cycle_isSet) {
        obj.insert(QString("cycle"), ::OpenAPI::toJsonValue(m_cycle));
    }
    if (m_file_number_isSet) {
        obj.insert(QString("file_number"), ::OpenAPI::toJsonValue(m_file_number));
    }
    if (m_form_type_code_isSet) {
        obj.insert(QString("form_type_code"), ::OpenAPI::toJsonValue(m_form_type_code));
    }
    if (m_image_number_isSet) {
        obj.insert(QString("image_number"), ::OpenAPI::toJsonValue(m_image_number));
    }
    if (m_original_sub_id_isSet) {
        obj.insert(QString("original_sub_id"), ::OpenAPI::toJsonValue(m_original_sub_id));
    }
    if (m_pdf_url_isSet) {
        obj.insert(QString("pdf_url"), ::OpenAPI::toJsonValue(m_pdf_url));
    }
    if (m_primary_general_indicator_isSet) {
        obj.insert(QString("primary_general_indicator"), ::OpenAPI::toJsonValue(m_primary_general_indicator));
    }
    if (m_primary_general_indicator_description_isSet) {
        obj.insert(QString("primary_general_indicator_description"), ::OpenAPI::toJsonValue(m_primary_general_indicator_description));
    }
    if (m_purpose_isSet) {
        obj.insert(QString("purpose"), ::OpenAPI::toJsonValue(m_purpose));
    }
    if (m_report_type_isSet) {
        obj.insert(QString("report_type"), ::OpenAPI::toJsonValue(m_report_type));
    }
    if (m_report_year_isSet) {
        obj.insert(QString("report_year"), ::OpenAPI::toJsonValue(m_report_year));
    }
    if (m_schedule_type_isSet) {
        obj.insert(QString("schedule_type"), ::OpenAPI::toJsonValue(m_schedule_type));
    }
    if (m_schedule_type_full_isSet) {
        obj.insert(QString("schedule_type_full"), ::OpenAPI::toJsonValue(m_schedule_type_full));
    }
    if (m_state_full_isSet) {
        obj.insert(QString("state_full"), ::OpenAPI::toJsonValue(m_state_full));
    }
    if (m_sub_id_isSet) {
        obj.insert(QString("sub_id"), ::OpenAPI::toJsonValue(m_sub_id));
    }
    if (m_support_oppose_indicator_isSet) {
        obj.insert(QString("support_oppose_indicator"), ::OpenAPI::toJsonValue(m_support_oppose_indicator));
    }
    if (m_tran_id_isSet) {
        obj.insert(QString("tran_id"), ::OpenAPI::toJsonValue(m_tran_id));
    }
    if (m_transaction_amount_isSet) {
        obj.insert(QString("transaction_amount"), ::OpenAPI::toJsonValue(m_transaction_amount));
    }
    if (m_transaction_date_isSet) {
        obj.insert(QString("transaction_date"), ::OpenAPI::toJsonValue(m_transaction_date));
    }
    if (m_transaction_type_isSet) {
        obj.insert(QString("transaction_type"), ::OpenAPI::toJsonValue(m_transaction_type));
    }
    return obj;
}

QString OAICommunicationCost::getActionCode() const {
    return m_action_code;
}
void OAICommunicationCost::setActionCode(const QString &action_code) {
    m_action_code = action_code;
    m_action_code_isSet = true;
}

bool OAICommunicationCost::is_action_code_Set() const{
    return m_action_code_isSet;
}

bool OAICommunicationCost::is_action_code_Valid() const{
    return m_action_code_isValid;
}

QString OAICommunicationCost::getActionCodeFull() const {
    return m_action_code_full;
}
void OAICommunicationCost::setActionCodeFull(const QString &action_code_full) {
    m_action_code_full = action_code_full;
    m_action_code_full_isSet = true;
}

bool OAICommunicationCost::is_action_code_full_Set() const{
    return m_action_code_full_isSet;
}

bool OAICommunicationCost::is_action_code_full_Valid() const{
    return m_action_code_full_isValid;
}

QString OAICommunicationCost::getCandidateFirstName() const {
    return m_candidate_first_name;
}
void OAICommunicationCost::setCandidateFirstName(const QString &candidate_first_name) {
    m_candidate_first_name = candidate_first_name;
    m_candidate_first_name_isSet = true;
}

bool OAICommunicationCost::is_candidate_first_name_Set() const{
    return m_candidate_first_name_isSet;
}

bool OAICommunicationCost::is_candidate_first_name_Valid() const{
    return m_candidate_first_name_isValid;
}

QString OAICommunicationCost::getCandidateId() const {
    return m_candidate_id;
}
void OAICommunicationCost::setCandidateId(const QString &candidate_id) {
    m_candidate_id = candidate_id;
    m_candidate_id_isSet = true;
}

bool OAICommunicationCost::is_candidate_id_Set() const{
    return m_candidate_id_isSet;
}

bool OAICommunicationCost::is_candidate_id_Valid() const{
    return m_candidate_id_isValid;
}

QString OAICommunicationCost::getCandidateLastName() const {
    return m_candidate_last_name;
}
void OAICommunicationCost::setCandidateLastName(const QString &candidate_last_name) {
    m_candidate_last_name = candidate_last_name;
    m_candidate_last_name_isSet = true;
}

bool OAICommunicationCost::is_candidate_last_name_Set() const{
    return m_candidate_last_name_isSet;
}

bool OAICommunicationCost::is_candidate_last_name_Valid() const{
    return m_candidate_last_name_isValid;
}

QString OAICommunicationCost::getCandidateMiddleName() const {
    return m_candidate_middle_name;
}
void OAICommunicationCost::setCandidateMiddleName(const QString &candidate_middle_name) {
    m_candidate_middle_name = candidate_middle_name;
    m_candidate_middle_name_isSet = true;
}

bool OAICommunicationCost::is_candidate_middle_name_Set() const{
    return m_candidate_middle_name_isSet;
}

bool OAICommunicationCost::is_candidate_middle_name_Valid() const{
    return m_candidate_middle_name_isValid;
}

QString OAICommunicationCost::getCandidateName() const {
    return m_candidate_name;
}
void OAICommunicationCost::setCandidateName(const QString &candidate_name) {
    m_candidate_name = candidate_name;
    m_candidate_name_isSet = true;
}

bool OAICommunicationCost::is_candidate_name_Set() const{
    return m_candidate_name_isSet;
}

bool OAICommunicationCost::is_candidate_name_Valid() const{
    return m_candidate_name_isValid;
}

QString OAICommunicationCost::getCandidateOffice() const {
    return m_candidate_office;
}
void OAICommunicationCost::setCandidateOffice(const QString &candidate_office) {
    m_candidate_office = candidate_office;
    m_candidate_office_isSet = true;
}

bool OAICommunicationCost::is_candidate_office_Set() const{
    return m_candidate_office_isSet;
}

bool OAICommunicationCost::is_candidate_office_Valid() const{
    return m_candidate_office_isValid;
}

QString OAICommunicationCost::getCandidateOfficeDistrict() const {
    return m_candidate_office_district;
}
void OAICommunicationCost::setCandidateOfficeDistrict(const QString &candidate_office_district) {
    m_candidate_office_district = candidate_office_district;
    m_candidate_office_district_isSet = true;
}

bool OAICommunicationCost::is_candidate_office_district_Set() const{
    return m_candidate_office_district_isSet;
}

bool OAICommunicationCost::is_candidate_office_district_Valid() const{
    return m_candidate_office_district_isValid;
}

QString OAICommunicationCost::getCandidateOfficeFull() const {
    return m_candidate_office_full;
}
void OAICommunicationCost::setCandidateOfficeFull(const QString &candidate_office_full) {
    m_candidate_office_full = candidate_office_full;
    m_candidate_office_full_isSet = true;
}

bool OAICommunicationCost::is_candidate_office_full_Set() const{
    return m_candidate_office_full_isSet;
}

bool OAICommunicationCost::is_candidate_office_full_Valid() const{
    return m_candidate_office_full_isValid;
}

QString OAICommunicationCost::getCandidateOfficeState() const {
    return m_candidate_office_state;
}
void OAICommunicationCost::setCandidateOfficeState(const QString &candidate_office_state) {
    m_candidate_office_state = candidate_office_state;
    m_candidate_office_state_isSet = true;
}

bool OAICommunicationCost::is_candidate_office_state_Set() const{
    return m_candidate_office_state_isSet;
}

bool OAICommunicationCost::is_candidate_office_state_Valid() const{
    return m_candidate_office_state_isValid;
}

QString OAICommunicationCost::getCommitteeId() const {
    return m_committee_id;
}
void OAICommunicationCost::setCommitteeId(const QString &committee_id) {
    m_committee_id = committee_id;
    m_committee_id_isSet = true;
}

bool OAICommunicationCost::is_committee_id_Set() const{
    return m_committee_id_isSet;
}

bool OAICommunicationCost::is_committee_id_Valid() const{
    return m_committee_id_isValid;
}

QString OAICommunicationCost::getCommitteeName() const {
    return m_committee_name;
}
void OAICommunicationCost::setCommitteeName(const QString &committee_name) {
    m_committee_name = committee_name;
    m_committee_name_isSet = true;
}

bool OAICommunicationCost::is_committee_name_Set() const{
    return m_committee_name_isSet;
}

bool OAICommunicationCost::is_committee_name_Valid() const{
    return m_committee_name_isValid;
}

QString OAICommunicationCost::getCommunicationClass() const {
    return m_communication_class;
}
void OAICommunicationCost::setCommunicationClass(const QString &communication_class) {
    m_communication_class = communication_class;
    m_communication_class_isSet = true;
}

bool OAICommunicationCost::is_communication_class_Set() const{
    return m_communication_class_isSet;
}

bool OAICommunicationCost::is_communication_class_Valid() const{
    return m_communication_class_isValid;
}

QString OAICommunicationCost::getCommunicationType() const {
    return m_communication_type;
}
void OAICommunicationCost::setCommunicationType(const QString &communication_type) {
    m_communication_type = communication_type;
    m_communication_type_isSet = true;
}

bool OAICommunicationCost::is_communication_type_Set() const{
    return m_communication_type_isSet;
}

bool OAICommunicationCost::is_communication_type_Valid() const{
    return m_communication_type_isValid;
}

QString OAICommunicationCost::getCommunicationTypeFull() const {
    return m_communication_type_full;
}
void OAICommunicationCost::setCommunicationTypeFull(const QString &communication_type_full) {
    m_communication_type_full = communication_type_full;
    m_communication_type_full_isSet = true;
}

bool OAICommunicationCost::is_communication_type_full_Set() const{
    return m_communication_type_full_isSet;
}

bool OAICommunicationCost::is_communication_type_full_Valid() const{
    return m_communication_type_full_isValid;
}

qint32 OAICommunicationCost::getCycle() const {
    return m_cycle;
}
void OAICommunicationCost::setCycle(const qint32 &cycle) {
    m_cycle = cycle;
    m_cycle_isSet = true;
}

bool OAICommunicationCost::is_cycle_Set() const{
    return m_cycle_isSet;
}

bool OAICommunicationCost::is_cycle_Valid() const{
    return m_cycle_isValid;
}

qint32 OAICommunicationCost::getFileNumber() const {
    return m_file_number;
}
void OAICommunicationCost::setFileNumber(const qint32 &file_number) {
    m_file_number = file_number;
    m_file_number_isSet = true;
}

bool OAICommunicationCost::is_file_number_Set() const{
    return m_file_number_isSet;
}

bool OAICommunicationCost::is_file_number_Valid() const{
    return m_file_number_isValid;
}

QString OAICommunicationCost::getFormTypeCode() const {
    return m_form_type_code;
}
void OAICommunicationCost::setFormTypeCode(const QString &form_type_code) {
    m_form_type_code = form_type_code;
    m_form_type_code_isSet = true;
}

bool OAICommunicationCost::is_form_type_code_Set() const{
    return m_form_type_code_isSet;
}

bool OAICommunicationCost::is_form_type_code_Valid() const{
    return m_form_type_code_isValid;
}

QString OAICommunicationCost::getImageNumber() const {
    return m_image_number;
}
void OAICommunicationCost::setImageNumber(const QString &image_number) {
    m_image_number = image_number;
    m_image_number_isSet = true;
}

bool OAICommunicationCost::is_image_number_Set() const{
    return m_image_number_isSet;
}

bool OAICommunicationCost::is_image_number_Valid() const{
    return m_image_number_isValid;
}

qint32 OAICommunicationCost::getOriginalSubId() const {
    return m_original_sub_id;
}
void OAICommunicationCost::setOriginalSubId(const qint32 &original_sub_id) {
    m_original_sub_id = original_sub_id;
    m_original_sub_id_isSet = true;
}

bool OAICommunicationCost::is_original_sub_id_Set() const{
    return m_original_sub_id_isSet;
}

bool OAICommunicationCost::is_original_sub_id_Valid() const{
    return m_original_sub_id_isValid;
}

QString OAICommunicationCost::getPdfUrl() const {
    return m_pdf_url;
}
void OAICommunicationCost::setPdfUrl(const QString &pdf_url) {
    m_pdf_url = pdf_url;
    m_pdf_url_isSet = true;
}

bool OAICommunicationCost::is_pdf_url_Set() const{
    return m_pdf_url_isSet;
}

bool OAICommunicationCost::is_pdf_url_Valid() const{
    return m_pdf_url_isValid;
}

QString OAICommunicationCost::getPrimaryGeneralIndicator() const {
    return m_primary_general_indicator;
}
void OAICommunicationCost::setPrimaryGeneralIndicator(const QString &primary_general_indicator) {
    m_primary_general_indicator = primary_general_indicator;
    m_primary_general_indicator_isSet = true;
}

bool OAICommunicationCost::is_primary_general_indicator_Set() const{
    return m_primary_general_indicator_isSet;
}

bool OAICommunicationCost::is_primary_general_indicator_Valid() const{
    return m_primary_general_indicator_isValid;
}

QString OAICommunicationCost::getPrimaryGeneralIndicatorDescription() const {
    return m_primary_general_indicator_description;
}
void OAICommunicationCost::setPrimaryGeneralIndicatorDescription(const QString &primary_general_indicator_description) {
    m_primary_general_indicator_description = primary_general_indicator_description;
    m_primary_general_indicator_description_isSet = true;
}

bool OAICommunicationCost::is_primary_general_indicator_description_Set() const{
    return m_primary_general_indicator_description_isSet;
}

bool OAICommunicationCost::is_primary_general_indicator_description_Valid() const{
    return m_primary_general_indicator_description_isValid;
}

QString OAICommunicationCost::getPurpose() const {
    return m_purpose;
}
void OAICommunicationCost::setPurpose(const QString &purpose) {
    m_purpose = purpose;
    m_purpose_isSet = true;
}

bool OAICommunicationCost::is_purpose_Set() const{
    return m_purpose_isSet;
}

bool OAICommunicationCost::is_purpose_Valid() const{
    return m_purpose_isValid;
}

QString OAICommunicationCost::getReportType() const {
    return m_report_type;
}
void OAICommunicationCost::setReportType(const QString &report_type) {
    m_report_type = report_type;
    m_report_type_isSet = true;
}

bool OAICommunicationCost::is_report_type_Set() const{
    return m_report_type_isSet;
}

bool OAICommunicationCost::is_report_type_Valid() const{
    return m_report_type_isValid;
}

qint32 OAICommunicationCost::getReportYear() const {
    return m_report_year;
}
void OAICommunicationCost::setReportYear(const qint32 &report_year) {
    m_report_year = report_year;
    m_report_year_isSet = true;
}

bool OAICommunicationCost::is_report_year_Set() const{
    return m_report_year_isSet;
}

bool OAICommunicationCost::is_report_year_Valid() const{
    return m_report_year_isValid;
}

QString OAICommunicationCost::getScheduleType() const {
    return m_schedule_type;
}
void OAICommunicationCost::setScheduleType(const QString &schedule_type) {
    m_schedule_type = schedule_type;
    m_schedule_type_isSet = true;
}

bool OAICommunicationCost::is_schedule_type_Set() const{
    return m_schedule_type_isSet;
}

bool OAICommunicationCost::is_schedule_type_Valid() const{
    return m_schedule_type_isValid;
}

QString OAICommunicationCost::getScheduleTypeFull() const {
    return m_schedule_type_full;
}
void OAICommunicationCost::setScheduleTypeFull(const QString &schedule_type_full) {
    m_schedule_type_full = schedule_type_full;
    m_schedule_type_full_isSet = true;
}

bool OAICommunicationCost::is_schedule_type_full_Set() const{
    return m_schedule_type_full_isSet;
}

bool OAICommunicationCost::is_schedule_type_full_Valid() const{
    return m_schedule_type_full_isValid;
}

QString OAICommunicationCost::getStateFull() const {
    return m_state_full;
}
void OAICommunicationCost::setStateFull(const QString &state_full) {
    m_state_full = state_full;
    m_state_full_isSet = true;
}

bool OAICommunicationCost::is_state_full_Set() const{
    return m_state_full_isSet;
}

bool OAICommunicationCost::is_state_full_Valid() const{
    return m_state_full_isValid;
}

qint32 OAICommunicationCost::getSubId() const {
    return m_sub_id;
}
void OAICommunicationCost::setSubId(const qint32 &sub_id) {
    m_sub_id = sub_id;
    m_sub_id_isSet = true;
}

bool OAICommunicationCost::is_sub_id_Set() const{
    return m_sub_id_isSet;
}

bool OAICommunicationCost::is_sub_id_Valid() const{
    return m_sub_id_isValid;
}

QString OAICommunicationCost::getSupportOpposeIndicator() const {
    return m_support_oppose_indicator;
}
void OAICommunicationCost::setSupportOpposeIndicator(const QString &support_oppose_indicator) {
    m_support_oppose_indicator = support_oppose_indicator;
    m_support_oppose_indicator_isSet = true;
}

bool OAICommunicationCost::is_support_oppose_indicator_Set() const{
    return m_support_oppose_indicator_isSet;
}

bool OAICommunicationCost::is_support_oppose_indicator_Valid() const{
    return m_support_oppose_indicator_isValid;
}

QString OAICommunicationCost::getTranId() const {
    return m_tran_id;
}
void OAICommunicationCost::setTranId(const QString &tran_id) {
    m_tran_id = tran_id;
    m_tran_id_isSet = true;
}

bool OAICommunicationCost::is_tran_id_Set() const{
    return m_tran_id_isSet;
}

bool OAICommunicationCost::is_tran_id_Valid() const{
    return m_tran_id_isValid;
}

double OAICommunicationCost::getTransactionAmount() const {
    return m_transaction_amount;
}
void OAICommunicationCost::setTransactionAmount(const double &transaction_amount) {
    m_transaction_amount = transaction_amount;
    m_transaction_amount_isSet = true;
}

bool OAICommunicationCost::is_transaction_amount_Set() const{
    return m_transaction_amount_isSet;
}

bool OAICommunicationCost::is_transaction_amount_Valid() const{
    return m_transaction_amount_isValid;
}

QDate OAICommunicationCost::getTransactionDate() const {
    return m_transaction_date;
}
void OAICommunicationCost::setTransactionDate(const QDate &transaction_date) {
    m_transaction_date = transaction_date;
    m_transaction_date_isSet = true;
}

bool OAICommunicationCost::is_transaction_date_Set() const{
    return m_transaction_date_isSet;
}

bool OAICommunicationCost::is_transaction_date_Valid() const{
    return m_transaction_date_isValid;
}

QString OAICommunicationCost::getTransactionType() const {
    return m_transaction_type;
}
void OAICommunicationCost::setTransactionType(const QString &transaction_type) {
    m_transaction_type = transaction_type;
    m_transaction_type_isSet = true;
}

bool OAICommunicationCost::is_transaction_type_Set() const{
    return m_transaction_type_isSet;
}

bool OAICommunicationCost::is_transaction_type_Valid() const{
    return m_transaction_type_isValid;
}

bool OAICommunicationCost::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_action_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_action_code_full_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_first_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_last_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_middle_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_office_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_office_district_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_office_full_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_candidate_office_state_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_committee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_committee_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_communication_class_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_communication_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_communication_type_full_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cycle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_type_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_image_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_original_sub_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pdf_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_general_indicator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_general_indicator_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_purpose_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_report_year_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_schedule_type_full_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_state_full_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_support_oppose_indicator_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_tran_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_amount_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_transaction_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICommunicationCost::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

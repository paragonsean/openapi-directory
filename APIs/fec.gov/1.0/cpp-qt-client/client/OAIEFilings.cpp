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

#include "OAIEFilings.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEFilings::OAIEFilings(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEFilings::OAIEFilings() {
    this->initializeModel();
}

OAIEFilings::~OAIEFilings() {}

void OAIEFilings::initializeModel() {

    m_amended_by_isSet = false;
    m_amended_by_isValid = false;

    m_amendment_chain_isSet = false;
    m_amendment_chain_isValid = false;

    m_amendment_number_isSet = false;
    m_amendment_number_isValid = false;

    m_amends_file_isSet = false;
    m_amends_file_isValid = false;

    m_beginning_image_number_isSet = false;
    m_beginning_image_number_isValid = false;

    m_committee_id_isSet = false;
    m_committee_id_isValid = false;

    m_committee_name_isSet = false;
    m_committee_name_isValid = false;

    m_coverage_end_date_isSet = false;
    m_coverage_end_date_isValid = false;

    m_coverage_start_date_isSet = false;
    m_coverage_start_date_isValid = false;

    m_csv_url_isSet = false;
    m_csv_url_isValid = false;

    m_document_description_isSet = false;
    m_document_description_isValid = false;

    m_ending_image_number_isSet = false;
    m_ending_image_number_isValid = false;

    m_fec_file_id_isSet = false;
    m_fec_file_id_isValid = false;

    m_fec_url_isSet = false;
    m_fec_url_isValid = false;

    m_file_number_isSet = false;
    m_file_number_isValid = false;

    m_filed_date_isSet = false;
    m_filed_date_isValid = false;

    m_form_type_isSet = false;
    m_form_type_isValid = false;

    m_html_url_isSet = false;
    m_html_url_isValid = false;

    m_is_amended_isSet = false;
    m_is_amended_isValid = false;

    m_load_timestamp_isSet = false;
    m_load_timestamp_isValid = false;

    m_most_recent_isSet = false;
    m_most_recent_isValid = false;

    m_most_recent_filing_isSet = false;
    m_most_recent_filing_isValid = false;

    m_pdf_url_isSet = false;
    m_pdf_url_isValid = false;

    m_receipt_date_isSet = false;
    m_receipt_date_isValid = false;
}

void OAIEFilings::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEFilings::fromJsonObject(QJsonObject json) {

    m_amended_by_isValid = ::OpenAPI::fromJsonValue(m_amended_by, json[QString("amended_by")]);
    m_amended_by_isSet = !json[QString("amended_by")].isNull() && m_amended_by_isValid;

    m_amendment_chain_isValid = ::OpenAPI::fromJsonValue(m_amendment_chain, json[QString("amendment_chain")]);
    m_amendment_chain_isSet = !json[QString("amendment_chain")].isNull() && m_amendment_chain_isValid;

    m_amendment_number_isValid = ::OpenAPI::fromJsonValue(m_amendment_number, json[QString("amendment_number")]);
    m_amendment_number_isSet = !json[QString("amendment_number")].isNull() && m_amendment_number_isValid;

    m_amends_file_isValid = ::OpenAPI::fromJsonValue(m_amends_file, json[QString("amends_file")]);
    m_amends_file_isSet = !json[QString("amends_file")].isNull() && m_amends_file_isValid;

    m_beginning_image_number_isValid = ::OpenAPI::fromJsonValue(m_beginning_image_number, json[QString("beginning_image_number")]);
    m_beginning_image_number_isSet = !json[QString("beginning_image_number")].isNull() && m_beginning_image_number_isValid;

    m_committee_id_isValid = ::OpenAPI::fromJsonValue(m_committee_id, json[QString("committee_id")]);
    m_committee_id_isSet = !json[QString("committee_id")].isNull() && m_committee_id_isValid;

    m_committee_name_isValid = ::OpenAPI::fromJsonValue(m_committee_name, json[QString("committee_name")]);
    m_committee_name_isSet = !json[QString("committee_name")].isNull() && m_committee_name_isValid;

    m_coverage_end_date_isValid = ::OpenAPI::fromJsonValue(m_coverage_end_date, json[QString("coverage_end_date")]);
    m_coverage_end_date_isSet = !json[QString("coverage_end_date")].isNull() && m_coverage_end_date_isValid;

    m_coverage_start_date_isValid = ::OpenAPI::fromJsonValue(m_coverage_start_date, json[QString("coverage_start_date")]);
    m_coverage_start_date_isSet = !json[QString("coverage_start_date")].isNull() && m_coverage_start_date_isValid;

    m_csv_url_isValid = ::OpenAPI::fromJsonValue(m_csv_url, json[QString("csv_url")]);
    m_csv_url_isSet = !json[QString("csv_url")].isNull() && m_csv_url_isValid;

    m_document_description_isValid = ::OpenAPI::fromJsonValue(m_document_description, json[QString("document_description")]);
    m_document_description_isSet = !json[QString("document_description")].isNull() && m_document_description_isValid;

    m_ending_image_number_isValid = ::OpenAPI::fromJsonValue(m_ending_image_number, json[QString("ending_image_number")]);
    m_ending_image_number_isSet = !json[QString("ending_image_number")].isNull() && m_ending_image_number_isValid;

    m_fec_file_id_isValid = ::OpenAPI::fromJsonValue(m_fec_file_id, json[QString("fec_file_id")]);
    m_fec_file_id_isSet = !json[QString("fec_file_id")].isNull() && m_fec_file_id_isValid;

    m_fec_url_isValid = ::OpenAPI::fromJsonValue(m_fec_url, json[QString("fec_url")]);
    m_fec_url_isSet = !json[QString("fec_url")].isNull() && m_fec_url_isValid;

    m_file_number_isValid = ::OpenAPI::fromJsonValue(m_file_number, json[QString("file_number")]);
    m_file_number_isSet = !json[QString("file_number")].isNull() && m_file_number_isValid;

    m_filed_date_isValid = ::OpenAPI::fromJsonValue(m_filed_date, json[QString("filed_date")]);
    m_filed_date_isSet = !json[QString("filed_date")].isNull() && m_filed_date_isValid;

    m_form_type_isValid = ::OpenAPI::fromJsonValue(m_form_type, json[QString("form_type")]);
    m_form_type_isSet = !json[QString("form_type")].isNull() && m_form_type_isValid;

    m_html_url_isValid = ::OpenAPI::fromJsonValue(m_html_url, json[QString("html_url")]);
    m_html_url_isSet = !json[QString("html_url")].isNull() && m_html_url_isValid;

    m_is_amended_isValid = ::OpenAPI::fromJsonValue(m_is_amended, json[QString("is_amended")]);
    m_is_amended_isSet = !json[QString("is_amended")].isNull() && m_is_amended_isValid;

    m_load_timestamp_isValid = ::OpenAPI::fromJsonValue(m_load_timestamp, json[QString("load_timestamp")]);
    m_load_timestamp_isSet = !json[QString("load_timestamp")].isNull() && m_load_timestamp_isValid;

    m_most_recent_isValid = ::OpenAPI::fromJsonValue(m_most_recent, json[QString("most_recent")]);
    m_most_recent_isSet = !json[QString("most_recent")].isNull() && m_most_recent_isValid;

    m_most_recent_filing_isValid = ::OpenAPI::fromJsonValue(m_most_recent_filing, json[QString("most_recent_filing")]);
    m_most_recent_filing_isSet = !json[QString("most_recent_filing")].isNull() && m_most_recent_filing_isValid;

    m_pdf_url_isValid = ::OpenAPI::fromJsonValue(m_pdf_url, json[QString("pdf_url")]);
    m_pdf_url_isSet = !json[QString("pdf_url")].isNull() && m_pdf_url_isValid;

    m_receipt_date_isValid = ::OpenAPI::fromJsonValue(m_receipt_date, json[QString("receipt_date")]);
    m_receipt_date_isSet = !json[QString("receipt_date")].isNull() && m_receipt_date_isValid;
}

QString OAIEFilings::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEFilings::asJsonObject() const {
    QJsonObject obj;
    if (m_amended_by_isSet) {
        obj.insert(QString("amended_by"), ::OpenAPI::toJsonValue(m_amended_by));
    }
    if (m_amendment_chain.size() > 0) {
        obj.insert(QString("amendment_chain"), ::OpenAPI::toJsonValue(m_amendment_chain));
    }
    if (m_amendment_number_isSet) {
        obj.insert(QString("amendment_number"), ::OpenAPI::toJsonValue(m_amendment_number));
    }
    if (m_amends_file_isSet) {
        obj.insert(QString("amends_file"), ::OpenAPI::toJsonValue(m_amends_file));
    }
    if (m_beginning_image_number_isSet) {
        obj.insert(QString("beginning_image_number"), ::OpenAPI::toJsonValue(m_beginning_image_number));
    }
    if (m_committee_id_isSet) {
        obj.insert(QString("committee_id"), ::OpenAPI::toJsonValue(m_committee_id));
    }
    if (m_committee_name_isSet) {
        obj.insert(QString("committee_name"), ::OpenAPI::toJsonValue(m_committee_name));
    }
    if (m_coverage_end_date_isSet) {
        obj.insert(QString("coverage_end_date"), ::OpenAPI::toJsonValue(m_coverage_end_date));
    }
    if (m_coverage_start_date_isSet) {
        obj.insert(QString("coverage_start_date"), ::OpenAPI::toJsonValue(m_coverage_start_date));
    }
    if (m_csv_url_isSet) {
        obj.insert(QString("csv_url"), ::OpenAPI::toJsonValue(m_csv_url));
    }
    if (m_document_description_isSet) {
        obj.insert(QString("document_description"), ::OpenAPI::toJsonValue(m_document_description));
    }
    if (m_ending_image_number_isSet) {
        obj.insert(QString("ending_image_number"), ::OpenAPI::toJsonValue(m_ending_image_number));
    }
    if (m_fec_file_id_isSet) {
        obj.insert(QString("fec_file_id"), ::OpenAPI::toJsonValue(m_fec_file_id));
    }
    if (m_fec_url_isSet) {
        obj.insert(QString("fec_url"), ::OpenAPI::toJsonValue(m_fec_url));
    }
    if (m_file_number_isSet) {
        obj.insert(QString("file_number"), ::OpenAPI::toJsonValue(m_file_number));
    }
    if (m_filed_date_isSet) {
        obj.insert(QString("filed_date"), ::OpenAPI::toJsonValue(m_filed_date));
    }
    if (m_form_type_isSet) {
        obj.insert(QString("form_type"), ::OpenAPI::toJsonValue(m_form_type));
    }
    if (m_html_url_isSet) {
        obj.insert(QString("html_url"), ::OpenAPI::toJsonValue(m_html_url));
    }
    if (m_is_amended_isSet) {
        obj.insert(QString("is_amended"), ::OpenAPI::toJsonValue(m_is_amended));
    }
    if (m_load_timestamp_isSet) {
        obj.insert(QString("load_timestamp"), ::OpenAPI::toJsonValue(m_load_timestamp));
    }
    if (m_most_recent_isSet) {
        obj.insert(QString("most_recent"), ::OpenAPI::toJsonValue(m_most_recent));
    }
    if (m_most_recent_filing_isSet) {
        obj.insert(QString("most_recent_filing"), ::OpenAPI::toJsonValue(m_most_recent_filing));
    }
    if (m_pdf_url_isSet) {
        obj.insert(QString("pdf_url"), ::OpenAPI::toJsonValue(m_pdf_url));
    }
    if (m_receipt_date_isSet) {
        obj.insert(QString("receipt_date"), ::OpenAPI::toJsonValue(m_receipt_date));
    }
    return obj;
}

qint32 OAIEFilings::getAmendedBy() const {
    return m_amended_by;
}
void OAIEFilings::setAmendedBy(const qint32 &amended_by) {
    m_amended_by = amended_by;
    m_amended_by_isSet = true;
}

bool OAIEFilings::is_amended_by_Set() const{
    return m_amended_by_isSet;
}

bool OAIEFilings::is_amended_by_Valid() const{
    return m_amended_by_isValid;
}

QList<qint32> OAIEFilings::getAmendmentChain() const {
    return m_amendment_chain;
}
void OAIEFilings::setAmendmentChain(const QList<qint32> &amendment_chain) {
    m_amendment_chain = amendment_chain;
    m_amendment_chain_isSet = true;
}

bool OAIEFilings::is_amendment_chain_Set() const{
    return m_amendment_chain_isSet;
}

bool OAIEFilings::is_amendment_chain_Valid() const{
    return m_amendment_chain_isValid;
}

qint32 OAIEFilings::getAmendmentNumber() const {
    return m_amendment_number;
}
void OAIEFilings::setAmendmentNumber(const qint32 &amendment_number) {
    m_amendment_number = amendment_number;
    m_amendment_number_isSet = true;
}

bool OAIEFilings::is_amendment_number_Set() const{
    return m_amendment_number_isSet;
}

bool OAIEFilings::is_amendment_number_Valid() const{
    return m_amendment_number_isValid;
}

qint32 OAIEFilings::getAmendsFile() const {
    return m_amends_file;
}
void OAIEFilings::setAmendsFile(const qint32 &amends_file) {
    m_amends_file = amends_file;
    m_amends_file_isSet = true;
}

bool OAIEFilings::is_amends_file_Set() const{
    return m_amends_file_isSet;
}

bool OAIEFilings::is_amends_file_Valid() const{
    return m_amends_file_isValid;
}

QString OAIEFilings::getBeginningImageNumber() const {
    return m_beginning_image_number;
}
void OAIEFilings::setBeginningImageNumber(const QString &beginning_image_number) {
    m_beginning_image_number = beginning_image_number;
    m_beginning_image_number_isSet = true;
}

bool OAIEFilings::is_beginning_image_number_Set() const{
    return m_beginning_image_number_isSet;
}

bool OAIEFilings::is_beginning_image_number_Valid() const{
    return m_beginning_image_number_isValid;
}

QString OAIEFilings::getCommitteeId() const {
    return m_committee_id;
}
void OAIEFilings::setCommitteeId(const QString &committee_id) {
    m_committee_id = committee_id;
    m_committee_id_isSet = true;
}

bool OAIEFilings::is_committee_id_Set() const{
    return m_committee_id_isSet;
}

bool OAIEFilings::is_committee_id_Valid() const{
    return m_committee_id_isValid;
}

QString OAIEFilings::getCommitteeName() const {
    return m_committee_name;
}
void OAIEFilings::setCommitteeName(const QString &committee_name) {
    m_committee_name = committee_name;
    m_committee_name_isSet = true;
}

bool OAIEFilings::is_committee_name_Set() const{
    return m_committee_name_isSet;
}

bool OAIEFilings::is_committee_name_Valid() const{
    return m_committee_name_isValid;
}

QDate OAIEFilings::getCoverageEndDate() const {
    return m_coverage_end_date;
}
void OAIEFilings::setCoverageEndDate(const QDate &coverage_end_date) {
    m_coverage_end_date = coverage_end_date;
    m_coverage_end_date_isSet = true;
}

bool OAIEFilings::is_coverage_end_date_Set() const{
    return m_coverage_end_date_isSet;
}

bool OAIEFilings::is_coverage_end_date_Valid() const{
    return m_coverage_end_date_isValid;
}

QDate OAIEFilings::getCoverageStartDate() const {
    return m_coverage_start_date;
}
void OAIEFilings::setCoverageStartDate(const QDate &coverage_start_date) {
    m_coverage_start_date = coverage_start_date;
    m_coverage_start_date_isSet = true;
}

bool OAIEFilings::is_coverage_start_date_Set() const{
    return m_coverage_start_date_isSet;
}

bool OAIEFilings::is_coverage_start_date_Valid() const{
    return m_coverage_start_date_isValid;
}

QString OAIEFilings::getCsvUrl() const {
    return m_csv_url;
}
void OAIEFilings::setCsvUrl(const QString &csv_url) {
    m_csv_url = csv_url;
    m_csv_url_isSet = true;
}

bool OAIEFilings::is_csv_url_Set() const{
    return m_csv_url_isSet;
}

bool OAIEFilings::is_csv_url_Valid() const{
    return m_csv_url_isValid;
}

QString OAIEFilings::getDocumentDescription() const {
    return m_document_description;
}
void OAIEFilings::setDocumentDescription(const QString &document_description) {
    m_document_description = document_description;
    m_document_description_isSet = true;
}

bool OAIEFilings::is_document_description_Set() const{
    return m_document_description_isSet;
}

bool OAIEFilings::is_document_description_Valid() const{
    return m_document_description_isValid;
}

QString OAIEFilings::getEndingImageNumber() const {
    return m_ending_image_number;
}
void OAIEFilings::setEndingImageNumber(const QString &ending_image_number) {
    m_ending_image_number = ending_image_number;
    m_ending_image_number_isSet = true;
}

bool OAIEFilings::is_ending_image_number_Set() const{
    return m_ending_image_number_isSet;
}

bool OAIEFilings::is_ending_image_number_Valid() const{
    return m_ending_image_number_isValid;
}

QString OAIEFilings::getFecFileId() const {
    return m_fec_file_id;
}
void OAIEFilings::setFecFileId(const QString &fec_file_id) {
    m_fec_file_id = fec_file_id;
    m_fec_file_id_isSet = true;
}

bool OAIEFilings::is_fec_file_id_Set() const{
    return m_fec_file_id_isSet;
}

bool OAIEFilings::is_fec_file_id_Valid() const{
    return m_fec_file_id_isValid;
}

QString OAIEFilings::getFecUrl() const {
    return m_fec_url;
}
void OAIEFilings::setFecUrl(const QString &fec_url) {
    m_fec_url = fec_url;
    m_fec_url_isSet = true;
}

bool OAIEFilings::is_fec_url_Set() const{
    return m_fec_url_isSet;
}

bool OAIEFilings::is_fec_url_Valid() const{
    return m_fec_url_isValid;
}

qint32 OAIEFilings::getFileNumber() const {
    return m_file_number;
}
void OAIEFilings::setFileNumber(const qint32 &file_number) {
    m_file_number = file_number;
    m_file_number_isSet = true;
}

bool OAIEFilings::is_file_number_Set() const{
    return m_file_number_isSet;
}

bool OAIEFilings::is_file_number_Valid() const{
    return m_file_number_isValid;
}

QDate OAIEFilings::getFiledDate() const {
    return m_filed_date;
}
void OAIEFilings::setFiledDate(const QDate &filed_date) {
    m_filed_date = filed_date;
    m_filed_date_isSet = true;
}

bool OAIEFilings::is_filed_date_Set() const{
    return m_filed_date_isSet;
}

bool OAIEFilings::is_filed_date_Valid() const{
    return m_filed_date_isValid;
}

QString OAIEFilings::getFormType() const {
    return m_form_type;
}
void OAIEFilings::setFormType(const QString &form_type) {
    m_form_type = form_type;
    m_form_type_isSet = true;
}

bool OAIEFilings::is_form_type_Set() const{
    return m_form_type_isSet;
}

bool OAIEFilings::is_form_type_Valid() const{
    return m_form_type_isValid;
}

QString OAIEFilings::getHtmlUrl() const {
    return m_html_url;
}
void OAIEFilings::setHtmlUrl(const QString &html_url) {
    m_html_url = html_url;
    m_html_url_isSet = true;
}

bool OAIEFilings::is_html_url_Set() const{
    return m_html_url_isSet;
}

bool OAIEFilings::is_html_url_Valid() const{
    return m_html_url_isValid;
}

bool OAIEFilings::isIsAmended() const {
    return m_is_amended;
}
void OAIEFilings::setIsAmended(const bool &is_amended) {
    m_is_amended = is_amended;
    m_is_amended_isSet = true;
}

bool OAIEFilings::is_is_amended_Set() const{
    return m_is_amended_isSet;
}

bool OAIEFilings::is_is_amended_Valid() const{
    return m_is_amended_isValid;
}

QDateTime OAIEFilings::getLoadTimestamp() const {
    return m_load_timestamp;
}
void OAIEFilings::setLoadTimestamp(const QDateTime &load_timestamp) {
    m_load_timestamp = load_timestamp;
    m_load_timestamp_isSet = true;
}

bool OAIEFilings::is_load_timestamp_Set() const{
    return m_load_timestamp_isSet;
}

bool OAIEFilings::is_load_timestamp_Valid() const{
    return m_load_timestamp_isValid;
}

bool OAIEFilings::isMostRecent() const {
    return m_most_recent;
}
void OAIEFilings::setMostRecent(const bool &most_recent) {
    m_most_recent = most_recent;
    m_most_recent_isSet = true;
}

bool OAIEFilings::is_most_recent_Set() const{
    return m_most_recent_isSet;
}

bool OAIEFilings::is_most_recent_Valid() const{
    return m_most_recent_isValid;
}

qint32 OAIEFilings::getMostRecentFiling() const {
    return m_most_recent_filing;
}
void OAIEFilings::setMostRecentFiling(const qint32 &most_recent_filing) {
    m_most_recent_filing = most_recent_filing;
    m_most_recent_filing_isSet = true;
}

bool OAIEFilings::is_most_recent_filing_Set() const{
    return m_most_recent_filing_isSet;
}

bool OAIEFilings::is_most_recent_filing_Valid() const{
    return m_most_recent_filing_isValid;
}

QString OAIEFilings::getPdfUrl() const {
    return m_pdf_url;
}
void OAIEFilings::setPdfUrl(const QString &pdf_url) {
    m_pdf_url = pdf_url;
    m_pdf_url_isSet = true;
}

bool OAIEFilings::is_pdf_url_Set() const{
    return m_pdf_url_isSet;
}

bool OAIEFilings::is_pdf_url_Valid() const{
    return m_pdf_url_isValid;
}

QDateTime OAIEFilings::getReceiptDate() const {
    return m_receipt_date;
}
void OAIEFilings::setReceiptDate(const QDateTime &receipt_date) {
    m_receipt_date = receipt_date;
    m_receipt_date_isSet = true;
}

bool OAIEFilings::is_receipt_date_Set() const{
    return m_receipt_date_isSet;
}

bool OAIEFilings::is_receipt_date_Valid() const{
    return m_receipt_date_isValid;
}

bool OAIEFilings::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_amended_by_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amendment_chain.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_amendment_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_amends_file_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_beginning_image_number_isSet) {
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

        if (m_coverage_end_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_coverage_start_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_csv_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_document_description_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ending_image_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fec_file_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_fec_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_file_number_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filed_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_form_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_html_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_amended_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_load_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_most_recent_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_most_recent_filing_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pdf_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_receipt_date_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIEFilings::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

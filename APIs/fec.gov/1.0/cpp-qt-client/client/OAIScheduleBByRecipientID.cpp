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

#include "OAIScheduleBByRecipientID.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIScheduleBByRecipientID::OAIScheduleBByRecipientID(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIScheduleBByRecipientID::OAIScheduleBByRecipientID() {
    this->initializeModel();
}

OAIScheduleBByRecipientID::~OAIScheduleBByRecipientID() {}

void OAIScheduleBByRecipientID::initializeModel() {

    m_committee_id_isSet = false;
    m_committee_id_isValid = false;

    m_committee_name_isSet = false;
    m_committee_name_isValid = false;

    m_count_isSet = false;
    m_count_isValid = false;

    m_cycle_isSet = false;
    m_cycle_isValid = false;

    m_memo_count_isSet = false;
    m_memo_count_isValid = false;

    m_memo_total_isSet = false;
    m_memo_total_isValid = false;

    m_recipient_id_isSet = false;
    m_recipient_id_isValid = false;

    m_recipient_name_isSet = false;
    m_recipient_name_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;
}

void OAIScheduleBByRecipientID::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIScheduleBByRecipientID::fromJsonObject(QJsonObject json) {

    m_committee_id_isValid = ::OpenAPI::fromJsonValue(m_committee_id, json[QString("committee_id")]);
    m_committee_id_isSet = !json[QString("committee_id")].isNull() && m_committee_id_isValid;

    m_committee_name_isValid = ::OpenAPI::fromJsonValue(m_committee_name, json[QString("committee_name")]);
    m_committee_name_isSet = !json[QString("committee_name")].isNull() && m_committee_name_isValid;

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_cycle_isValid = ::OpenAPI::fromJsonValue(m_cycle, json[QString("cycle")]);
    m_cycle_isSet = !json[QString("cycle")].isNull() && m_cycle_isValid;

    m_memo_count_isValid = ::OpenAPI::fromJsonValue(m_memo_count, json[QString("memo_count")]);
    m_memo_count_isSet = !json[QString("memo_count")].isNull() && m_memo_count_isValid;

    m_memo_total_isValid = ::OpenAPI::fromJsonValue(m_memo_total, json[QString("memo_total")]);
    m_memo_total_isSet = !json[QString("memo_total")].isNull() && m_memo_total_isValid;

    m_recipient_id_isValid = ::OpenAPI::fromJsonValue(m_recipient_id, json[QString("recipient_id")]);
    m_recipient_id_isSet = !json[QString("recipient_id")].isNull() && m_recipient_id_isValid;

    m_recipient_name_isValid = ::OpenAPI::fromJsonValue(m_recipient_name, json[QString("recipient_name")]);
    m_recipient_name_isSet = !json[QString("recipient_name")].isNull() && m_recipient_name_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;
}

QString OAIScheduleBByRecipientID::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIScheduleBByRecipientID::asJsonObject() const {
    QJsonObject obj;
    if (m_committee_id_isSet) {
        obj.insert(QString("committee_id"), ::OpenAPI::toJsonValue(m_committee_id));
    }
    if (m_committee_name_isSet) {
        obj.insert(QString("committee_name"), ::OpenAPI::toJsonValue(m_committee_name));
    }
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_cycle_isSet) {
        obj.insert(QString("cycle"), ::OpenAPI::toJsonValue(m_cycle));
    }
    if (m_memo_count_isSet) {
        obj.insert(QString("memo_count"), ::OpenAPI::toJsonValue(m_memo_count));
    }
    if (m_memo_total_isSet) {
        obj.insert(QString("memo_total"), ::OpenAPI::toJsonValue(m_memo_total));
    }
    if (m_recipient_id_isSet) {
        obj.insert(QString("recipient_id"), ::OpenAPI::toJsonValue(m_recipient_id));
    }
    if (m_recipient_name_isSet) {
        obj.insert(QString("recipient_name"), ::OpenAPI::toJsonValue(m_recipient_name));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    return obj;
}

QString OAIScheduleBByRecipientID::getCommitteeId() const {
    return m_committee_id;
}
void OAIScheduleBByRecipientID::setCommitteeId(const QString &committee_id) {
    m_committee_id = committee_id;
    m_committee_id_isSet = true;
}

bool OAIScheduleBByRecipientID::is_committee_id_Set() const{
    return m_committee_id_isSet;
}

bool OAIScheduleBByRecipientID::is_committee_id_Valid() const{
    return m_committee_id_isValid;
}

QString OAIScheduleBByRecipientID::getCommitteeName() const {
    return m_committee_name;
}
void OAIScheduleBByRecipientID::setCommitteeName(const QString &committee_name) {
    m_committee_name = committee_name;
    m_committee_name_isSet = true;
}

bool OAIScheduleBByRecipientID::is_committee_name_Set() const{
    return m_committee_name_isSet;
}

bool OAIScheduleBByRecipientID::is_committee_name_Valid() const{
    return m_committee_name_isValid;
}

qint32 OAIScheduleBByRecipientID::getCount() const {
    return m_count;
}
void OAIScheduleBByRecipientID::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIScheduleBByRecipientID::is_count_Set() const{
    return m_count_isSet;
}

bool OAIScheduleBByRecipientID::is_count_Valid() const{
    return m_count_isValid;
}

qint32 OAIScheduleBByRecipientID::getCycle() const {
    return m_cycle;
}
void OAIScheduleBByRecipientID::setCycle(const qint32 &cycle) {
    m_cycle = cycle;
    m_cycle_isSet = true;
}

bool OAIScheduleBByRecipientID::is_cycle_Set() const{
    return m_cycle_isSet;
}

bool OAIScheduleBByRecipientID::is_cycle_Valid() const{
    return m_cycle_isValid;
}

qint32 OAIScheduleBByRecipientID::getMemoCount() const {
    return m_memo_count;
}
void OAIScheduleBByRecipientID::setMemoCount(const qint32 &memo_count) {
    m_memo_count = memo_count;
    m_memo_count_isSet = true;
}

bool OAIScheduleBByRecipientID::is_memo_count_Set() const{
    return m_memo_count_isSet;
}

bool OAIScheduleBByRecipientID::is_memo_count_Valid() const{
    return m_memo_count_isValid;
}

double OAIScheduleBByRecipientID::getMemoTotal() const {
    return m_memo_total;
}
void OAIScheduleBByRecipientID::setMemoTotal(const double &memo_total) {
    m_memo_total = memo_total;
    m_memo_total_isSet = true;
}

bool OAIScheduleBByRecipientID::is_memo_total_Set() const{
    return m_memo_total_isSet;
}

bool OAIScheduleBByRecipientID::is_memo_total_Valid() const{
    return m_memo_total_isValid;
}

QString OAIScheduleBByRecipientID::getRecipientId() const {
    return m_recipient_id;
}
void OAIScheduleBByRecipientID::setRecipientId(const QString &recipient_id) {
    m_recipient_id = recipient_id;
    m_recipient_id_isSet = true;
}

bool OAIScheduleBByRecipientID::is_recipient_id_Set() const{
    return m_recipient_id_isSet;
}

bool OAIScheduleBByRecipientID::is_recipient_id_Valid() const{
    return m_recipient_id_isValid;
}

QString OAIScheduleBByRecipientID::getRecipientName() const {
    return m_recipient_name;
}
void OAIScheduleBByRecipientID::setRecipientName(const QString &recipient_name) {
    m_recipient_name = recipient_name;
    m_recipient_name_isSet = true;
}

bool OAIScheduleBByRecipientID::is_recipient_name_Set() const{
    return m_recipient_name_isSet;
}

bool OAIScheduleBByRecipientID::is_recipient_name_Valid() const{
    return m_recipient_name_isValid;
}

double OAIScheduleBByRecipientID::getTotal() const {
    return m_total;
}
void OAIScheduleBByRecipientID::setTotal(const double &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAIScheduleBByRecipientID::is_total_Set() const{
    return m_total_isSet;
}

bool OAIScheduleBByRecipientID::is_total_Valid() const{
    return m_total_isValid;
}

bool OAIScheduleBByRecipientID::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_committee_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_committee_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_cycle_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_memo_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_memo_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipient_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_recipient_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIScheduleBByRecipientID::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_committee_id_isValid && m_cycle_isValid && m_recipient_id_isValid && true;
}

} // namespace OpenAPI

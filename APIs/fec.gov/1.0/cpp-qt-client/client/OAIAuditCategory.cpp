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

#include "OAIAuditCategory.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAuditCategory::OAIAuditCategory(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAuditCategory::OAIAuditCategory() {
    this->initializeModel();
}

OAIAuditCategory::~OAIAuditCategory() {}

void OAIAuditCategory::initializeModel() {

    m_primary_category_id_isSet = false;
    m_primary_category_id_isValid = false;

    m_primary_category_name_isSet = false;
    m_primary_category_name_isValid = false;

    m_sub_category_list_isSet = false;
    m_sub_category_list_isValid = false;
}

void OAIAuditCategory::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAuditCategory::fromJsonObject(QJsonObject json) {

    m_primary_category_id_isValid = ::OpenAPI::fromJsonValue(m_primary_category_id, json[QString("primary_category_id")]);
    m_primary_category_id_isSet = !json[QString("primary_category_id")].isNull() && m_primary_category_id_isValid;

    m_primary_category_name_isValid = ::OpenAPI::fromJsonValue(m_primary_category_name, json[QString("primary_category_name")]);
    m_primary_category_name_isSet = !json[QString("primary_category_name")].isNull() && m_primary_category_name_isValid;

    m_sub_category_list_isValid = ::OpenAPI::fromJsonValue(m_sub_category_list, json[QString("sub_category_list")]);
    m_sub_category_list_isSet = !json[QString("sub_category_list")].isNull() && m_sub_category_list_isValid;
}

QString OAIAuditCategory::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAuditCategory::asJsonObject() const {
    QJsonObject obj;
    if (m_primary_category_id_isSet) {
        obj.insert(QString("primary_category_id"), ::OpenAPI::toJsonValue(m_primary_category_id));
    }
    if (m_primary_category_name_isSet) {
        obj.insert(QString("primary_category_name"), ::OpenAPI::toJsonValue(m_primary_category_name));
    }
    if (m_sub_category_list.size() > 0) {
        obj.insert(QString("sub_category_list"), ::OpenAPI::toJsonValue(m_sub_category_list));
    }
    return obj;
}

QString OAIAuditCategory::getPrimaryCategoryId() const {
    return m_primary_category_id;
}
void OAIAuditCategory::setPrimaryCategoryId(const QString &primary_category_id) {
    m_primary_category_id = primary_category_id;
    m_primary_category_id_isSet = true;
}

bool OAIAuditCategory::is_primary_category_id_Set() const{
    return m_primary_category_id_isSet;
}

bool OAIAuditCategory::is_primary_category_id_Valid() const{
    return m_primary_category_id_isValid;
}

QString OAIAuditCategory::getPrimaryCategoryName() const {
    return m_primary_category_name;
}
void OAIAuditCategory::setPrimaryCategoryName(const QString &primary_category_name) {
    m_primary_category_name = primary_category_name;
    m_primary_category_name_isSet = true;
}

bool OAIAuditCategory::is_primary_category_name_Set() const{
    return m_primary_category_name_isSet;
}

bool OAIAuditCategory::is_primary_category_name_Valid() const{
    return m_primary_category_name_isValid;
}

QList<OAIAuditCategoryRelation> OAIAuditCategory::getSubCategoryList() const {
    return m_sub_category_list;
}
void OAIAuditCategory::setSubCategoryList(const QList<OAIAuditCategoryRelation> &sub_category_list) {
    m_sub_category_list = sub_category_list;
    m_sub_category_list_isSet = true;
}

bool OAIAuditCategory::is_sub_category_list_Set() const{
    return m_sub_category_list_isSet;
}

bool OAIAuditCategory::is_sub_category_list_Valid() const{
    return m_sub_category_list_isValid;
}

bool OAIAuditCategory::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_primary_category_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_primary_category_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_sub_category_list.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAuditCategory::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

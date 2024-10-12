/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPageResult_CompanySettingDto_.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPageResult_CompanySettingDto_::OAIPageResult_CompanySettingDto_(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPageResult_CompanySettingDto_::OAIPageResult_CompanySettingDto_() {
    this->initializeModel();
}

OAIPageResult_CompanySettingDto_::~OAIPageResult_CompanySettingDto_() {}

void OAIPageResult_CompanySettingDto_::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_items_isSet = false;
    m_items_isValid = false;

    m_next_page_link_isSet = false;
    m_next_page_link_isValid = false;
}

void OAIPageResult_CompanySettingDto_::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPageResult_CompanySettingDto_::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("Count")]);
    m_count_isSet = !json[QString("Count")].isNull() && m_count_isValid;

    m_items_isValid = ::OpenAPI::fromJsonValue(m_items, json[QString("Items")]);
    m_items_isSet = !json[QString("Items")].isNull() && m_items_isValid;

    m_next_page_link_isValid = ::OpenAPI::fromJsonValue(m_next_page_link, json[QString("NextPageLink")]);
    m_next_page_link_isSet = !json[QString("NextPageLink")].isNull() && m_next_page_link_isValid;
}

QString OAIPageResult_CompanySettingDto_::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPageResult_CompanySettingDto_::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("Count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_items.size() > 0) {
        obj.insert(QString("Items"), ::OpenAPI::toJsonValue(m_items));
    }
    if (m_next_page_link_isSet) {
        obj.insert(QString("NextPageLink"), ::OpenAPI::toJsonValue(m_next_page_link));
    }
    return obj;
}

qint64 OAIPageResult_CompanySettingDto_::getCount() const {
    return m_count;
}
void OAIPageResult_CompanySettingDto_::setCount(const qint64 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIPageResult_CompanySettingDto_::is_count_Set() const{
    return m_count_isSet;
}

bool OAIPageResult_CompanySettingDto_::is_count_Valid() const{
    return m_count_isValid;
}

QList<OAICompanySettingDto> OAIPageResult_CompanySettingDto_::getItems() const {
    return m_items;
}
void OAIPageResult_CompanySettingDto_::setItems(const QList<OAICompanySettingDto> &items) {
    m_items = items;
    m_items_isSet = true;
}

bool OAIPageResult_CompanySettingDto_::is_items_Set() const{
    return m_items_isSet;
}

bool OAIPageResult_CompanySettingDto_::is_items_Valid() const{
    return m_items_isValid;
}

QString OAIPageResult_CompanySettingDto_::getNextPageLink() const {
    return m_next_page_link;
}
void OAIPageResult_CompanySettingDto_::setNextPageLink(const QString &next_page_link) {
    m_next_page_link = next_page_link;
    m_next_page_link_isSet = true;
}

bool OAIPageResult_CompanySettingDto_::is_next_page_link_Set() const{
    return m_next_page_link_isSet;
}

bool OAIPageResult_CompanySettingDto_::is_next_page_link_Valid() const{
    return m_next_page_link_isValid;
}

bool OAIPageResult_CompanySettingDto_::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_items.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_page_link_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPageResult_CompanySettingDto_::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

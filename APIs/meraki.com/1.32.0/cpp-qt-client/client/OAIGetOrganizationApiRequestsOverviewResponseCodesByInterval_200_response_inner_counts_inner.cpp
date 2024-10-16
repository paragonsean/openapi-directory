/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner() {
    this->initializeModel();
}

OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::~OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner() {}

void OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::initializeModel() {

    m_code_isSet = false;
    m_code_isValid = false;

    m_count_isSet = false;
    m_count_isValid = false;
}

void OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::fromJsonObject(QJsonObject json) {

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;
}

QString OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_code_isSet) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    return obj;
}

qint32 OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::getCode() const {
    return m_code;
}
void OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::setCode(const qint32 &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::is_code_Set() const{
    return m_code_isSet;
}

bool OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::is_code_Valid() const{
    return m_code_isValid;
}

qint32 OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::getCount() const {
    return m_count;
}
void OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::is_count_Set() const{
    return m_count_isSet;
}

bool OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::is_count_Valid() const{
    return m_count_isValid;
}

bool OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetOrganizationApiRequestsOverviewResponseCodesByInterval_200_response_inner_counts_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

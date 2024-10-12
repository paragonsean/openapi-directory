/**
 * AppServicePlans API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2016-09-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIAppServicePlans_ListMetrics_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAppServicePlans_ListMetrics_200_response::OAIAppServicePlans_ListMetrics_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAppServicePlans_ListMetrics_200_response::OAIAppServicePlans_ListMetrics_200_response() {
    this->initializeModel();
}

OAIAppServicePlans_ListMetrics_200_response::~OAIAppServicePlans_ListMetrics_200_response() {}

void OAIAppServicePlans_ListMetrics_200_response::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIAppServicePlans_ListMetrics_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAppServicePlans_ListMetrics_200_response::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIAppServicePlans_ListMetrics_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAppServicePlans_ListMetrics_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIAppServicePlans_ListMetrics_200_response::getNextLink() const {
    return m_next_link;
}
void OAIAppServicePlans_ListMetrics_200_response::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIAppServicePlans_ListMetrics_200_response::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIAppServicePlans_ListMetrics_200_response::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIAppServicePlans_ListMetrics_200_response_value_inner> OAIAppServicePlans_ListMetrics_200_response::getValue() const {
    return m_value;
}
void OAIAppServicePlans_ListMetrics_200_response::setValue(const QList<OAIAppServicePlans_ListMetrics_200_response_value_inner> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIAppServicePlans_ListMetrics_200_response::is_value_Set() const{
    return m_value_isSet;
}

bool OAIAppServicePlans_ListMetrics_200_response::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIAppServicePlans_ListMetrics_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_next_link_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAppServicePlans_ListMetrics_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_value_isValid && true;
}

} // namespace OpenAPI

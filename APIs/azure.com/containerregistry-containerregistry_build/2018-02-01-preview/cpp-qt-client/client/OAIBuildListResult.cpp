/**
 * ContainerRegistryManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBuildListResult.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildListResult::OAIBuildListResult(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildListResult::OAIBuildListResult() {
    this->initializeModel();
}

OAIBuildListResult::~OAIBuildListResult() {}

void OAIBuildListResult::initializeModel() {

    m_next_link_isSet = false;
    m_next_link_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIBuildListResult::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildListResult::fromJsonObject(QJsonObject json) {

    m_next_link_isValid = ::OpenAPI::fromJsonValue(m_next_link, json[QString("nextLink")]);
    m_next_link_isSet = !json[QString("nextLink")].isNull() && m_next_link_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIBuildListResult::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildListResult::asJsonObject() const {
    QJsonObject obj;
    if (m_next_link_isSet) {
        obj.insert(QString("nextLink"), ::OpenAPI::toJsonValue(m_next_link));
    }
    if (m_value.size() > 0) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIBuildListResult::getNextLink() const {
    return m_next_link;
}
void OAIBuildListResult::setNextLink(const QString &next_link) {
    m_next_link = next_link;
    m_next_link_isSet = true;
}

bool OAIBuildListResult::is_next_link_Set() const{
    return m_next_link_isSet;
}

bool OAIBuildListResult::is_next_link_Valid() const{
    return m_next_link_isValid;
}

QList<OAIBuild> OAIBuildListResult::getValue() const {
    return m_value;
}
void OAIBuildListResult::setValue(const QList<OAIBuild> &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIBuildListResult::is_value_Set() const{
    return m_value_isSet;
}

bool OAIBuildListResult::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIBuildListResult::isSet() const {
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

bool OAIBuildListResult::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

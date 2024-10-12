/**
 * FrontDoorManagementClient
 * Use these APIs to manage Azure Front Door resources through the Azure Resource Manager. You must make sure that requests made to these resources are secure.
 *
 * The version of the OpenAPI document: 2019-05-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIValidateCustomDomainInput.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIValidateCustomDomainInput::OAIValidateCustomDomainInput(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIValidateCustomDomainInput::OAIValidateCustomDomainInput() {
    this->initializeModel();
}

OAIValidateCustomDomainInput::~OAIValidateCustomDomainInput() {}

void OAIValidateCustomDomainInput::initializeModel() {

    m_host_name_isSet = false;
    m_host_name_isValid = false;
}

void OAIValidateCustomDomainInput::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIValidateCustomDomainInput::fromJsonObject(QJsonObject json) {

    m_host_name_isValid = ::OpenAPI::fromJsonValue(m_host_name, json[QString("hostName")]);
    m_host_name_isSet = !json[QString("hostName")].isNull() && m_host_name_isValid;
}

QString OAIValidateCustomDomainInput::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIValidateCustomDomainInput::asJsonObject() const {
    QJsonObject obj;
    if (m_host_name_isSet) {
        obj.insert(QString("hostName"), ::OpenAPI::toJsonValue(m_host_name));
    }
    return obj;
}

QString OAIValidateCustomDomainInput::getHostName() const {
    return m_host_name;
}
void OAIValidateCustomDomainInput::setHostName(const QString &host_name) {
    m_host_name = host_name;
    m_host_name_isSet = true;
}

bool OAIValidateCustomDomainInput::is_host_name_Set() const{
    return m_host_name_isSet;
}

bool OAIValidateCustomDomainInput::is_host_name_Valid() const{
    return m_host_name_isValid;
}

bool OAIValidateCustomDomainInput::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_host_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIValidateCustomDomainInput::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_host_name_isValid && true;
}

} // namespace OpenAPI

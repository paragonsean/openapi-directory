/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILegacyDeploymentResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILegacyDeploymentResponse::OAILegacyDeploymentResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILegacyDeploymentResponse::OAILegacyDeploymentResponse() {
    this->initializeModel();
}

OAILegacyDeploymentResponse::~OAILegacyDeploymentResponse() {}

void OAILegacyDeploymentResponse::initializeModel() {

    m_deployment_isSet = false;
    m_deployment_isValid = false;
}

void OAILegacyDeploymentResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILegacyDeploymentResponse::fromJsonObject(QJsonObject json) {

    m_deployment_isValid = ::OpenAPI::fromJsonValue(m_deployment, json[QString("deployment")]);
    m_deployment_isSet = !json[QString("deployment")].isNull() && m_deployment_isValid;
}

QString OAILegacyDeploymentResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILegacyDeploymentResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_deployment.size() > 0) {
        obj.insert(QString("deployment"), ::OpenAPI::toJsonValue(m_deployment));
    }
    return obj;
}

QMap<QString, OAILegacyDeploymentResponse_deployment_value> OAILegacyDeploymentResponse::getDeployment() const {
    return m_deployment;
}
void OAILegacyDeploymentResponse::setDeployment(const QMap<QString, OAILegacyDeploymentResponse_deployment_value> &deployment) {
    m_deployment = deployment;
    m_deployment_isSet = true;
}

bool OAILegacyDeploymentResponse::is_deployment_Set() const{
    return m_deployment_isSet;
}

bool OAILegacyDeploymentResponse::is_deployment_Valid() const{
    return m_deployment_isValid;
}

bool OAILegacyDeploymentResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_deployment.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILegacyDeploymentResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

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

#include "OAILegacyDeploymentsResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILegacyDeploymentsResponse::OAILegacyDeploymentsResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILegacyDeploymentsResponse::OAILegacyDeploymentsResponse() {
    this->initializeModel();
}

OAILegacyDeploymentsResponse::~OAILegacyDeploymentsResponse() {}

void OAILegacyDeploymentsResponse::initializeModel() {

    m_deployments_isSet = false;
    m_deployments_isValid = false;
}

void OAILegacyDeploymentsResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILegacyDeploymentsResponse::fromJsonObject(QJsonObject json) {

    m_deployments_isValid = ::OpenAPI::fromJsonValue(m_deployments, json[QString("deployments")]);
    m_deployments_isSet = !json[QString("deployments")].isNull() && m_deployments_isValid;
}

QString OAILegacyDeploymentsResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILegacyDeploymentsResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_deployments.size() > 0) {
        obj.insert(QString("deployments"), ::OpenAPI::toJsonValue(m_deployments));
    }
    return obj;
}

QList<OAILegacyDeploymentResponse_deployment_value> OAILegacyDeploymentsResponse::getDeployments() const {
    return m_deployments;
}
void OAILegacyDeploymentsResponse::setDeployments(const QList<OAILegacyDeploymentResponse_deployment_value> &deployments) {
    m_deployments = deployments;
    m_deployments_isSet = true;
}

bool OAILegacyDeploymentsResponse::is_deployments_Set() const{
    return m_deployments_isSet;
}

bool OAILegacyDeploymentsResponse::is_deployments_Valid() const{
    return m_deployments_isValid;
}

bool OAILegacyDeploymentsResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_deployments.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILegacyDeploymentsResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

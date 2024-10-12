/**
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2019-06-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOrchestratorVersionProfileProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrchestratorVersionProfileProperties::OAIOrchestratorVersionProfileProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrchestratorVersionProfileProperties::OAIOrchestratorVersionProfileProperties() {
    this->initializeModel();
}

OAIOrchestratorVersionProfileProperties::~OAIOrchestratorVersionProfileProperties() {}

void OAIOrchestratorVersionProfileProperties::initializeModel() {

    m_orchestrators_isSet = false;
    m_orchestrators_isValid = false;
}

void OAIOrchestratorVersionProfileProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrchestratorVersionProfileProperties::fromJsonObject(QJsonObject json) {

    m_orchestrators_isValid = ::OpenAPI::fromJsonValue(m_orchestrators, json[QString("orchestrators")]);
    m_orchestrators_isSet = !json[QString("orchestrators")].isNull() && m_orchestrators_isValid;
}

QString OAIOrchestratorVersionProfileProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrchestratorVersionProfileProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_orchestrators.size() > 0) {
        obj.insert(QString("orchestrators"), ::OpenAPI::toJsonValue(m_orchestrators));
    }
    return obj;
}

QList<OAIOrchestratorVersionProfile> OAIOrchestratorVersionProfileProperties::getOrchestrators() const {
    return m_orchestrators;
}
void OAIOrchestratorVersionProfileProperties::setOrchestrators(const QList<OAIOrchestratorVersionProfile> &orchestrators) {
    m_orchestrators = orchestrators;
    m_orchestrators_isSet = true;
}

bool OAIOrchestratorVersionProfileProperties::is_orchestrators_Set() const{
    return m_orchestrators_isSet;
}

bool OAIOrchestratorVersionProfileProperties::is_orchestrators_Valid() const{
    return m_orchestrators_isValid;
}

bool OAIOrchestratorVersionProfileProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_orchestrators.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrchestratorVersionProfileProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_orchestrators_isValid && true;
}

} // namespace OpenAPI

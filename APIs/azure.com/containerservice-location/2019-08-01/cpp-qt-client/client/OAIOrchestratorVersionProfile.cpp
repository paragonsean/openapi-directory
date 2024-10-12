/**
 * ContainerServiceClient
 * The Container Service Client.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOrchestratorVersionProfile.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOrchestratorVersionProfile::OAIOrchestratorVersionProfile(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOrchestratorVersionProfile::OAIOrchestratorVersionProfile() {
    this->initializeModel();
}

OAIOrchestratorVersionProfile::~OAIOrchestratorVersionProfile() {}

void OAIOrchestratorVersionProfile::initializeModel() {

    m_r_default_isSet = false;
    m_r_default_isValid = false;

    m_is_preview_isSet = false;
    m_is_preview_isValid = false;

    m_orchestrator_type_isSet = false;
    m_orchestrator_type_isValid = false;

    m_orchestrator_version_isSet = false;
    m_orchestrator_version_isValid = false;

    m_upgrades_isSet = false;
    m_upgrades_isValid = false;
}

void OAIOrchestratorVersionProfile::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOrchestratorVersionProfile::fromJsonObject(QJsonObject json) {

    m_r_default_isValid = ::OpenAPI::fromJsonValue(m_r_default, json[QString("default")]);
    m_r_default_isSet = !json[QString("default")].isNull() && m_r_default_isValid;

    m_is_preview_isValid = ::OpenAPI::fromJsonValue(m_is_preview, json[QString("isPreview")]);
    m_is_preview_isSet = !json[QString("isPreview")].isNull() && m_is_preview_isValid;

    m_orchestrator_type_isValid = ::OpenAPI::fromJsonValue(m_orchestrator_type, json[QString("orchestratorType")]);
    m_orchestrator_type_isSet = !json[QString("orchestratorType")].isNull() && m_orchestrator_type_isValid;

    m_orchestrator_version_isValid = ::OpenAPI::fromJsonValue(m_orchestrator_version, json[QString("orchestratorVersion")]);
    m_orchestrator_version_isSet = !json[QString("orchestratorVersion")].isNull() && m_orchestrator_version_isValid;

    m_upgrades_isValid = ::OpenAPI::fromJsonValue(m_upgrades, json[QString("upgrades")]);
    m_upgrades_isSet = !json[QString("upgrades")].isNull() && m_upgrades_isValid;
}

QString OAIOrchestratorVersionProfile::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOrchestratorVersionProfile::asJsonObject() const {
    QJsonObject obj;
    if (m_r_default_isSet) {
        obj.insert(QString("default"), ::OpenAPI::toJsonValue(m_r_default));
    }
    if (m_is_preview_isSet) {
        obj.insert(QString("isPreview"), ::OpenAPI::toJsonValue(m_is_preview));
    }
    if (m_orchestrator_type_isSet) {
        obj.insert(QString("orchestratorType"), ::OpenAPI::toJsonValue(m_orchestrator_type));
    }
    if (m_orchestrator_version_isSet) {
        obj.insert(QString("orchestratorVersion"), ::OpenAPI::toJsonValue(m_orchestrator_version));
    }
    if (m_upgrades.size() > 0) {
        obj.insert(QString("upgrades"), ::OpenAPI::toJsonValue(m_upgrades));
    }
    return obj;
}

bool OAIOrchestratorVersionProfile::isRDefault() const {
    return m_r_default;
}
void OAIOrchestratorVersionProfile::setRDefault(const bool &r_default) {
    m_r_default = r_default;
    m_r_default_isSet = true;
}

bool OAIOrchestratorVersionProfile::is_r_default_Set() const{
    return m_r_default_isSet;
}

bool OAIOrchestratorVersionProfile::is_r_default_Valid() const{
    return m_r_default_isValid;
}

bool OAIOrchestratorVersionProfile::isIsPreview() const {
    return m_is_preview;
}
void OAIOrchestratorVersionProfile::setIsPreview(const bool &is_preview) {
    m_is_preview = is_preview;
    m_is_preview_isSet = true;
}

bool OAIOrchestratorVersionProfile::is_is_preview_Set() const{
    return m_is_preview_isSet;
}

bool OAIOrchestratorVersionProfile::is_is_preview_Valid() const{
    return m_is_preview_isValid;
}

QString OAIOrchestratorVersionProfile::getOrchestratorType() const {
    return m_orchestrator_type;
}
void OAIOrchestratorVersionProfile::setOrchestratorType(const QString &orchestrator_type) {
    m_orchestrator_type = orchestrator_type;
    m_orchestrator_type_isSet = true;
}

bool OAIOrchestratorVersionProfile::is_orchestrator_type_Set() const{
    return m_orchestrator_type_isSet;
}

bool OAIOrchestratorVersionProfile::is_orchestrator_type_Valid() const{
    return m_orchestrator_type_isValid;
}

QString OAIOrchestratorVersionProfile::getOrchestratorVersion() const {
    return m_orchestrator_version;
}
void OAIOrchestratorVersionProfile::setOrchestratorVersion(const QString &orchestrator_version) {
    m_orchestrator_version = orchestrator_version;
    m_orchestrator_version_isSet = true;
}

bool OAIOrchestratorVersionProfile::is_orchestrator_version_Set() const{
    return m_orchestrator_version_isSet;
}

bool OAIOrchestratorVersionProfile::is_orchestrator_version_Valid() const{
    return m_orchestrator_version_isValid;
}

QList<OAIOrchestratorProfile> OAIOrchestratorVersionProfile::getUpgrades() const {
    return m_upgrades;
}
void OAIOrchestratorVersionProfile::setUpgrades(const QList<OAIOrchestratorProfile> &upgrades) {
    m_upgrades = upgrades;
    m_upgrades_isSet = true;
}

bool OAIOrchestratorVersionProfile::is_upgrades_Set() const{
    return m_upgrades_isSet;
}

bool OAIOrchestratorVersionProfile::is_upgrades_Valid() const{
    return m_upgrades_isValid;
}

bool OAIOrchestratorVersionProfile::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_r_default_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_preview_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_orchestrator_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_orchestrator_version_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_upgrades.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOrchestratorVersionProfile::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_orchestrator_type_isValid && m_orchestrator_version_isValid && true;
}

} // namespace OpenAPI

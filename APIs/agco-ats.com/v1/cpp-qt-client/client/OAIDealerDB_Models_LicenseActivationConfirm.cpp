/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIDealerDB_Models_LicenseActivationConfirm.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIDealerDB_Models_LicenseActivationConfirm::OAIDealerDB_Models_LicenseActivationConfirm(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIDealerDB_Models_LicenseActivationConfirm::OAIDealerDB_Models_LicenseActivationConfirm() {
    this->initializeModel();
}

OAIDealerDB_Models_LicenseActivationConfirm::~OAIDealerDB_Models_LicenseActivationConfirm() {}

void OAIDealerDB_Models_LicenseActivationConfirm::initializeModel() {

    m_license_version_isSet = false;
    m_license_version_isValid = false;
}

void OAIDealerDB_Models_LicenseActivationConfirm::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIDealerDB_Models_LicenseActivationConfirm::fromJsonObject(QJsonObject json) {

    m_license_version_isValid = ::OpenAPI::fromJsonValue(m_license_version, json[QString("LicenseVersion")]);
    m_license_version_isSet = !json[QString("LicenseVersion")].isNull() && m_license_version_isValid;
}

QString OAIDealerDB_Models_LicenseActivationConfirm::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIDealerDB_Models_LicenseActivationConfirm::asJsonObject() const {
    QJsonObject obj;
    if (m_license_version_isSet) {
        obj.insert(QString("LicenseVersion"), ::OpenAPI::toJsonValue(m_license_version));
    }
    return obj;
}

QString OAIDealerDB_Models_LicenseActivationConfirm::getLicenseVersion() const {
    return m_license_version;
}
void OAIDealerDB_Models_LicenseActivationConfirm::setLicenseVersion(const QString &license_version) {
    m_license_version = license_version;
    m_license_version_isSet = true;
}

bool OAIDealerDB_Models_LicenseActivationConfirm::is_license_version_Set() const{
    return m_license_version_isSet;
}

bool OAIDealerDB_Models_LicenseActivationConfirm::is_license_version_Valid() const{
    return m_license_version_isValid;
}

bool OAIDealerDB_Models_LicenseActivationConfirm::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_license_version_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIDealerDB_Models_LicenseActivationConfirm::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_license_version_isValid && true;
}

} // namespace OpenAPI

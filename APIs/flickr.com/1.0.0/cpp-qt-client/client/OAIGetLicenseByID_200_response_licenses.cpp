/**
 * Flickr API Schema
 * A subset of Flickr's API defined in Swagger format.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetLicenseByID_200_response_licenses.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetLicenseByID_200_response_licenses::OAIGetLicenseByID_200_response_licenses(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetLicenseByID_200_response_licenses::OAIGetLicenseByID_200_response_licenses() {
    this->initializeModel();
}

OAIGetLicenseByID_200_response_licenses::~OAIGetLicenseByID_200_response_licenses() {}

void OAIGetLicenseByID_200_response_licenses::initializeModel() {

    m_license_isSet = false;
    m_license_isValid = false;
}

void OAIGetLicenseByID_200_response_licenses::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetLicenseByID_200_response_licenses::fromJsonObject(QJsonObject json) {

    m_license_isValid = ::OpenAPI::fromJsonValue(m_license, json[QString("license")]);
    m_license_isSet = !json[QString("license")].isNull() && m_license_isValid;
}

QString OAIGetLicenseByID_200_response_licenses::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetLicenseByID_200_response_licenses::asJsonObject() const {
    QJsonObject obj;
    if (m_license.size() > 0) {
        obj.insert(QString("license"), ::OpenAPI::toJsonValue(m_license));
    }
    return obj;
}

QList<OAIGetLicenseByID_200_response_licenses_license_inner> OAIGetLicenseByID_200_response_licenses::getLicense() const {
    return m_license;
}
void OAIGetLicenseByID_200_response_licenses::setLicense(const QList<OAIGetLicenseByID_200_response_licenses_license_inner> &license) {
    m_license = license;
    m_license_isSet = true;
}

bool OAIGetLicenseByID_200_response_licenses::is_license_Set() const{
    return m_license_isSet;
}

bool OAIGetLicenseByID_200_response_licenses::is_license_Valid() const{
    return m_license_isValid;
}

bool OAIGetLicenseByID_200_response_licenses::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_license.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetLicenseByID_200_response_licenses::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

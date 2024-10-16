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

#include "OAIMoveOrganizationLicensingCotermLicenses_request.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMoveOrganizationLicensingCotermLicenses_request::OAIMoveOrganizationLicensingCotermLicenses_request(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMoveOrganizationLicensingCotermLicenses_request::OAIMoveOrganizationLicensingCotermLicenses_request() {
    this->initializeModel();
}

OAIMoveOrganizationLicensingCotermLicenses_request::~OAIMoveOrganizationLicensingCotermLicenses_request() {}

void OAIMoveOrganizationLicensingCotermLicenses_request::initializeModel() {

    m_destination_isSet = false;
    m_destination_isValid = false;

    m_licenses_isSet = false;
    m_licenses_isValid = false;
}

void OAIMoveOrganizationLicensingCotermLicenses_request::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMoveOrganizationLicensingCotermLicenses_request::fromJsonObject(QJsonObject json) {

    m_destination_isValid = ::OpenAPI::fromJsonValue(m_destination, json[QString("destination")]);
    m_destination_isSet = !json[QString("destination")].isNull() && m_destination_isValid;

    m_licenses_isValid = ::OpenAPI::fromJsonValue(m_licenses, json[QString("licenses")]);
    m_licenses_isSet = !json[QString("licenses")].isNull() && m_licenses_isValid;
}

QString OAIMoveOrganizationLicensingCotermLicenses_request::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMoveOrganizationLicensingCotermLicenses_request::asJsonObject() const {
    QJsonObject obj;
    if (m_destination.isSet()) {
        obj.insert(QString("destination"), ::OpenAPI::toJsonValue(m_destination));
    }
    if (m_licenses.size() > 0) {
        obj.insert(QString("licenses"), ::OpenAPI::toJsonValue(m_licenses));
    }
    return obj;
}

OAIMoveOrganizationLicensingCotermLicenses_request_destination OAIMoveOrganizationLicensingCotermLicenses_request::getDestination() const {
    return m_destination;
}
void OAIMoveOrganizationLicensingCotermLicenses_request::setDestination(const OAIMoveOrganizationLicensingCotermLicenses_request_destination &destination) {
    m_destination = destination;
    m_destination_isSet = true;
}

bool OAIMoveOrganizationLicensingCotermLicenses_request::is_destination_Set() const{
    return m_destination_isSet;
}

bool OAIMoveOrganizationLicensingCotermLicenses_request::is_destination_Valid() const{
    return m_destination_isValid;
}

QList<OAIMoveOrganizationLicensingCotermLicenses_request_licenses_inner> OAIMoveOrganizationLicensingCotermLicenses_request::getLicenses() const {
    return m_licenses;
}
void OAIMoveOrganizationLicensingCotermLicenses_request::setLicenses(const QList<OAIMoveOrganizationLicensingCotermLicenses_request_licenses_inner> &licenses) {
    m_licenses = licenses;
    m_licenses_isSet = true;
}

bool OAIMoveOrganizationLicensingCotermLicenses_request::is_licenses_Set() const{
    return m_licenses_isSet;
}

bool OAIMoveOrganizationLicensingCotermLicenses_request::is_licenses_Valid() const{
    return m_licenses_isValid;
}

bool OAIMoveOrganizationLicensingCotermLicenses_request::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_destination.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_licenses.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMoveOrganizationLicensingCotermLicenses_request::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_destination_isValid && m_licenses_isValid && true;
}

} // namespace OpenAPI

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

#include "OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication() {
    this->initializeModel();
}

OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::~OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication() {}

void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::initializeModel() {

    m_client_root_ca_certificate_isSet = false;
    m_client_root_ca_certificate_isValid = false;

    m_enabled_isSet = false;
    m_enabled_isValid = false;

    m_ocsp_responder_url_isSet = false;
    m_ocsp_responder_url_isValid = false;

    m_use_ldap_isSet = false;
    m_use_ldap_isValid = false;

    m_use_ocsp_isSet = false;
    m_use_ocsp_isValid = false;
}

void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::fromJsonObject(QJsonObject json) {

    m_client_root_ca_certificate_isValid = ::OpenAPI::fromJsonValue(m_client_root_ca_certificate, json[QString("clientRootCaCertificate")]);
    m_client_root_ca_certificate_isSet = !json[QString("clientRootCaCertificate")].isNull() && m_client_root_ca_certificate_isValid;

    m_enabled_isValid = ::OpenAPI::fromJsonValue(m_enabled, json[QString("enabled")]);
    m_enabled_isSet = !json[QString("enabled")].isNull() && m_enabled_isValid;

    m_ocsp_responder_url_isValid = ::OpenAPI::fromJsonValue(m_ocsp_responder_url, json[QString("ocspResponderUrl")]);
    m_ocsp_responder_url_isSet = !json[QString("ocspResponderUrl")].isNull() && m_ocsp_responder_url_isValid;

    m_use_ldap_isValid = ::OpenAPI::fromJsonValue(m_use_ldap, json[QString("useLdap")]);
    m_use_ldap_isSet = !json[QString("useLdap")].isNull() && m_use_ldap_isValid;

    m_use_ocsp_isValid = ::OpenAPI::fromJsonValue(m_use_ocsp, json[QString("useOcsp")]);
    m_use_ocsp_isSet = !json[QString("useOcsp")].isNull() && m_use_ocsp_isValid;
}

QString OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::asJsonObject() const {
    QJsonObject obj;
    if (m_client_root_ca_certificate.isSet()) {
        obj.insert(QString("clientRootCaCertificate"), ::OpenAPI::toJsonValue(m_client_root_ca_certificate));
    }
    if (m_enabled_isSet) {
        obj.insert(QString("enabled"), ::OpenAPI::toJsonValue(m_enabled));
    }
    if (m_ocsp_responder_url_isSet) {
        obj.insert(QString("ocspResponderUrl"), ::OpenAPI::toJsonValue(m_ocsp_responder_url));
    }
    if (m_use_ldap_isSet) {
        obj.insert(QString("useLdap"), ::OpenAPI::toJsonValue(m_use_ldap));
    }
    if (m_use_ocsp_isSet) {
        obj.insert(QString("useOcsp"), ::OpenAPI::toJsonValue(m_use_ocsp));
    }
    return obj;
}

OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication_clientRootCaCertificate OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::getClientRootCaCertificate() const {
    return m_client_root_ca_certificate;
}
void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::setClientRootCaCertificate(const OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication_clientRootCaCertificate &client_root_ca_certificate) {
    m_client_root_ca_certificate = client_root_ca_certificate;
    m_client_root_ca_certificate_isSet = true;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_client_root_ca_certificate_Set() const{
    return m_client_root_ca_certificate_isSet;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_client_root_ca_certificate_Valid() const{
    return m_client_root_ca_certificate_isValid;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::isEnabled() const {
    return m_enabled;
}
void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::setEnabled(const bool &enabled) {
    m_enabled = enabled;
    m_enabled_isSet = true;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_enabled_Set() const{
    return m_enabled_isSet;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_enabled_Valid() const{
    return m_enabled_isValid;
}

QString OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::getOcspResponderUrl() const {
    return m_ocsp_responder_url;
}
void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::setOcspResponderUrl(const QString &ocsp_responder_url) {
    m_ocsp_responder_url = ocsp_responder_url;
    m_ocsp_responder_url_isSet = true;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_ocsp_responder_url_Set() const{
    return m_ocsp_responder_url_isSet;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_ocsp_responder_url_Valid() const{
    return m_ocsp_responder_url_isValid;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::isUseLdap() const {
    return m_use_ldap;
}
void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::setUseLdap(const bool &use_ldap) {
    m_use_ldap = use_ldap;
    m_use_ldap_isSet = true;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_use_ldap_Set() const{
    return m_use_ldap_isSet;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_use_ldap_Valid() const{
    return m_use_ldap_isValid;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::isUseOcsp() const {
    return m_use_ocsp;
}
void OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::setUseOcsp(const bool &use_ocsp) {
    m_use_ocsp = use_ocsp;
    m_use_ocsp_isSet = true;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_use_ocsp_Set() const{
    return m_use_ocsp_isSet;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::is_use_ocsp_Valid() const{
    return m_use_ocsp_isValid;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_client_root_ca_certificate.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_enabled_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ocsp_responder_url_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_ldap_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_ocsp_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateNetworkWirelessSsid_request_localRadius_certificateAuthentication::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

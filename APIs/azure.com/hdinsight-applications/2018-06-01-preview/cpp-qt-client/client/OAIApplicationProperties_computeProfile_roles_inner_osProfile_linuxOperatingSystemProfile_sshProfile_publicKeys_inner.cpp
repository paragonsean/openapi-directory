/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner() {
    this->initializeModel();
}

OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::~OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner() {}

void OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::initializeModel() {

    m_certificate_data_isSet = false;
    m_certificate_data_isValid = false;
}

void OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::fromJsonObject(QJsonObject json) {

    m_certificate_data_isValid = ::OpenAPI::fromJsonValue(m_certificate_data, json[QString("certificateData")]);
    m_certificate_data_isSet = !json[QString("certificateData")].isNull() && m_certificate_data_isValid;
}

QString OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_certificate_data_isSet) {
        obj.insert(QString("certificateData"), ::OpenAPI::toJsonValue(m_certificate_data));
    }
    return obj;
}

QString OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::getCertificateData() const {
    return m_certificate_data;
}
void OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::setCertificateData(const QString &certificate_data) {
    m_certificate_data = certificate_data;
    m_certificate_data_isSet = true;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::is_certificate_data_Set() const{
    return m_certificate_data_isSet;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::is_certificate_data_Valid() const{
    return m_certificate_data_isValid;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_certificate_data_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApplicationProperties_computeProfile_roles_inner_osProfile_linuxOperatingSystemProfile_sshProfile_publicKeys_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

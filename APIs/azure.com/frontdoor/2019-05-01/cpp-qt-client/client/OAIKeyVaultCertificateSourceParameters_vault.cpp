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

#include "OAIKeyVaultCertificateSourceParameters_vault.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIKeyVaultCertificateSourceParameters_vault::OAIKeyVaultCertificateSourceParameters_vault(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIKeyVaultCertificateSourceParameters_vault::OAIKeyVaultCertificateSourceParameters_vault() {
    this->initializeModel();
}

OAIKeyVaultCertificateSourceParameters_vault::~OAIKeyVaultCertificateSourceParameters_vault() {}

void OAIKeyVaultCertificateSourceParameters_vault::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAIKeyVaultCertificateSourceParameters_vault::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIKeyVaultCertificateSourceParameters_vault::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAIKeyVaultCertificateSourceParameters_vault::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIKeyVaultCertificateSourceParameters_vault::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    return obj;
}

QString OAIKeyVaultCertificateSourceParameters_vault::getId() const {
    return m_id;
}
void OAIKeyVaultCertificateSourceParameters_vault::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIKeyVaultCertificateSourceParameters_vault::is_id_Set() const{
    return m_id_isSet;
}

bool OAIKeyVaultCertificateSourceParameters_vault::is_id_Valid() const{
    return m_id_isValid;
}

bool OAIKeyVaultCertificateSourceParameters_vault::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIKeyVaultCertificateSourceParameters_vault::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

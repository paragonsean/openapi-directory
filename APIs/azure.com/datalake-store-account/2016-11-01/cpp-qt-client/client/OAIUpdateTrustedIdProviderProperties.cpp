/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2016-11-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIUpdateTrustedIdProviderProperties.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIUpdateTrustedIdProviderProperties::OAIUpdateTrustedIdProviderProperties(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIUpdateTrustedIdProviderProperties::OAIUpdateTrustedIdProviderProperties() {
    this->initializeModel();
}

OAIUpdateTrustedIdProviderProperties::~OAIUpdateTrustedIdProviderProperties() {}

void OAIUpdateTrustedIdProviderProperties::initializeModel() {

    m_id_provider_isSet = false;
    m_id_provider_isValid = false;
}

void OAIUpdateTrustedIdProviderProperties::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIUpdateTrustedIdProviderProperties::fromJsonObject(QJsonObject json) {

    m_id_provider_isValid = ::OpenAPI::fromJsonValue(m_id_provider, json[QString("idProvider")]);
    m_id_provider_isSet = !json[QString("idProvider")].isNull() && m_id_provider_isValid;
}

QString OAIUpdateTrustedIdProviderProperties::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIUpdateTrustedIdProviderProperties::asJsonObject() const {
    QJsonObject obj;
    if (m_id_provider_isSet) {
        obj.insert(QString("idProvider"), ::OpenAPI::toJsonValue(m_id_provider));
    }
    return obj;
}

QString OAIUpdateTrustedIdProviderProperties::getIdProvider() const {
    return m_id_provider;
}
void OAIUpdateTrustedIdProviderProperties::setIdProvider(const QString &id_provider) {
    m_id_provider = id_provider;
    m_id_provider_isSet = true;
}

bool OAIUpdateTrustedIdProviderProperties::is_id_provider_Set() const{
    return m_id_provider_isSet;
}

bool OAIUpdateTrustedIdProviderProperties::is_id_provider_Valid() const{
    return m_id_provider_isValid;
}

bool OAIUpdateTrustedIdProviderProperties::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_provider_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIUpdateTrustedIdProviderProperties::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

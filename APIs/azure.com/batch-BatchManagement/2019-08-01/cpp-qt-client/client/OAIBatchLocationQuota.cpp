/**
 * BatchManagement
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBatchLocationQuota.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBatchLocationQuota::OAIBatchLocationQuota(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBatchLocationQuota::OAIBatchLocationQuota() {
    this->initializeModel();
}

OAIBatchLocationQuota::~OAIBatchLocationQuota() {}

void OAIBatchLocationQuota::initializeModel() {

    m_account_quota_isSet = false;
    m_account_quota_isValid = false;
}

void OAIBatchLocationQuota::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBatchLocationQuota::fromJsonObject(QJsonObject json) {

    m_account_quota_isValid = ::OpenAPI::fromJsonValue(m_account_quota, json[QString("accountQuota")]);
    m_account_quota_isSet = !json[QString("accountQuota")].isNull() && m_account_quota_isValid;
}

QString OAIBatchLocationQuota::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBatchLocationQuota::asJsonObject() const {
    QJsonObject obj;
    if (m_account_quota_isSet) {
        obj.insert(QString("accountQuota"), ::OpenAPI::toJsonValue(m_account_quota));
    }
    return obj;
}

qint32 OAIBatchLocationQuota::getAccountQuota() const {
    return m_account_quota;
}
void OAIBatchLocationQuota::setAccountQuota(const qint32 &account_quota) {
    m_account_quota = account_quota;
    m_account_quota_isSet = true;
}

bool OAIBatchLocationQuota::is_account_quota_Set() const{
    return m_account_quota_isSet;
}

bool OAIBatchLocationQuota::is_account_quota_Valid() const{
    return m_account_quota_isValid;
}

bool OAIBatchLocationQuota::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_account_quota_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBatchLocationQuota::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

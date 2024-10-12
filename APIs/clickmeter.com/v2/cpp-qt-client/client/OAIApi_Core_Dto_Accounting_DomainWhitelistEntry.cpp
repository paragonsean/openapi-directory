/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIApi_Core_Dto_Accounting_DomainWhitelistEntry.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::OAIApi_Core_Dto_Accounting_DomainWhitelistEntry(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::OAIApi_Core_Dto_Accounting_DomainWhitelistEntry() {
    this->initializeModel();
}

OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::~OAIApi_Core_Dto_Accounting_DomainWhitelistEntry() {}

void OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;
}

void OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;
}

QString OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    return obj;
}

QString OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::getId() const {
    return m_id;
}
void OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::is_id_Set() const{
    return m_id_isSet;
}

bool OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::getName() const {
    return m_name;
}
void OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::is_name_Set() const{
    return m_name_isSet;
}

bool OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::is_name_Valid() const{
    return m_name_isValid;
}

bool OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIApi_Core_Dto_Accounting_DomainWhitelistEntry::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

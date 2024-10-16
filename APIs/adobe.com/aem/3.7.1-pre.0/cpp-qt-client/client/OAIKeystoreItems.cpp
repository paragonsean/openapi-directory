/**
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.7.1-pre.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIKeystoreItems.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIKeystoreItems::OAIKeystoreItems(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIKeystoreItems::OAIKeystoreItems() {
    this->initializeModel();
}

OAIKeystoreItems::~OAIKeystoreItems() {}

void OAIKeystoreItems::initializeModel() {

    m_algorithm_isSet = false;
    m_algorithm_isValid = false;

    m_alias_isSet = false;
    m_alias_isValid = false;

    m_chain_isSet = false;
    m_chain_isValid = false;

    m_entry_type_isSet = false;
    m_entry_type_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;
}

void OAIKeystoreItems::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIKeystoreItems::fromJsonObject(QJsonObject json) {

    m_algorithm_isValid = ::OpenAPI::fromJsonValue(m_algorithm, json[QString("algorithm")]);
    m_algorithm_isSet = !json[QString("algorithm")].isNull() && m_algorithm_isValid;

    m_alias_isValid = ::OpenAPI::fromJsonValue(m_alias, json[QString("alias")]);
    m_alias_isSet = !json[QString("alias")].isNull() && m_alias_isValid;

    m_chain_isValid = ::OpenAPI::fromJsonValue(m_chain, json[QString("chain")]);
    m_chain_isSet = !json[QString("chain")].isNull() && m_chain_isValid;

    m_entry_type_isValid = ::OpenAPI::fromJsonValue(m_entry_type, json[QString("entryType")]);
    m_entry_type_isSet = !json[QString("entryType")].isNull() && m_entry_type_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;
}

QString OAIKeystoreItems::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIKeystoreItems::asJsonObject() const {
    QJsonObject obj;
    if (m_algorithm_isSet) {
        obj.insert(QString("algorithm"), ::OpenAPI::toJsonValue(m_algorithm));
    }
    if (m_alias_isSet) {
        obj.insert(QString("alias"), ::OpenAPI::toJsonValue(m_alias));
    }
    if (m_chain.size() > 0) {
        obj.insert(QString("chain"), ::OpenAPI::toJsonValue(m_chain));
    }
    if (m_entry_type_isSet) {
        obj.insert(QString("entryType"), ::OpenAPI::toJsonValue(m_entry_type));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    return obj;
}

QString OAIKeystoreItems::getAlgorithm() const {
    return m_algorithm;
}
void OAIKeystoreItems::setAlgorithm(const QString &algorithm) {
    m_algorithm = algorithm;
    m_algorithm_isSet = true;
}

bool OAIKeystoreItems::is_algorithm_Set() const{
    return m_algorithm_isSet;
}

bool OAIKeystoreItems::is_algorithm_Valid() const{
    return m_algorithm_isValid;
}

QString OAIKeystoreItems::getAlias() const {
    return m_alias;
}
void OAIKeystoreItems::setAlias(const QString &alias) {
    m_alias = alias;
    m_alias_isSet = true;
}

bool OAIKeystoreItems::is_alias_Set() const{
    return m_alias_isSet;
}

bool OAIKeystoreItems::is_alias_Valid() const{
    return m_alias_isValid;
}

QList<OAIKeystoreChainItems> OAIKeystoreItems::getChain() const {
    return m_chain;
}
void OAIKeystoreItems::setChain(const QList<OAIKeystoreChainItems> &chain) {
    m_chain = chain;
    m_chain_isSet = true;
}

bool OAIKeystoreItems::is_chain_Set() const{
    return m_chain_isSet;
}

bool OAIKeystoreItems::is_chain_Valid() const{
    return m_chain_isValid;
}

QString OAIKeystoreItems::getEntryType() const {
    return m_entry_type;
}
void OAIKeystoreItems::setEntryType(const QString &entry_type) {
    m_entry_type = entry_type;
    m_entry_type_isSet = true;
}

bool OAIKeystoreItems::is_entry_type_Set() const{
    return m_entry_type_isSet;
}

bool OAIKeystoreItems::is_entry_type_Valid() const{
    return m_entry_type_isValid;
}

QString OAIKeystoreItems::getFormat() const {
    return m_format;
}
void OAIKeystoreItems::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAIKeystoreItems::is_format_Set() const{
    return m_format_isSet;
}

bool OAIKeystoreItems::is_format_Valid() const{
    return m_format_isValid;
}

bool OAIKeystoreItems::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_algorithm_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_alias_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_chain.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_entry_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIKeystoreItems::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITransactionResource_relationships_tags_data_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransactionResource_relationships_tags_data_inner::OAITransactionResource_relationships_tags_data_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransactionResource_relationships_tags_data_inner::OAITransactionResource_relationships_tags_data_inner() {
    this->initializeModel();
}

OAITransactionResource_relationships_tags_data_inner::~OAITransactionResource_relationships_tags_data_inner() {}

void OAITransactionResource_relationships_tags_data_inner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAITransactionResource_relationships_tags_data_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransactionResource_relationships_tags_data_inner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAITransactionResource_relationships_tags_data_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransactionResource_relationships_tags_data_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAITransactionResource_relationships_tags_data_inner::getId() const {
    return m_id;
}
void OAITransactionResource_relationships_tags_data_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITransactionResource_relationships_tags_data_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAITransactionResource_relationships_tags_data_inner::is_id_Valid() const{
    return m_id_isValid;
}

QString OAITransactionResource_relationships_tags_data_inner::getType() const {
    return m_type;
}
void OAITransactionResource_relationships_tags_data_inner::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAITransactionResource_relationships_tags_data_inner::is_type_Set() const{
    return m_type_isSet;
}

bool OAITransactionResource_relationships_tags_data_inner::is_type_Valid() const{
    return m_type_isValid;
}

bool OAITransactionResource_relationships_tags_data_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITransactionResource_relationships_tags_data_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_id_isValid && m_type_isValid && true;
}

} // namespace OpenAPI

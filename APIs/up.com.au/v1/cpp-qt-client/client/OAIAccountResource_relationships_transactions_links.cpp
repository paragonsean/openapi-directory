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

#include "OAIAccountResource_relationships_transactions_links.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAccountResource_relationships_transactions_links::OAIAccountResource_relationships_transactions_links(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAccountResource_relationships_transactions_links::OAIAccountResource_relationships_transactions_links() {
    this->initializeModel();
}

OAIAccountResource_relationships_transactions_links::~OAIAccountResource_relationships_transactions_links() {}

void OAIAccountResource_relationships_transactions_links::initializeModel() {

    m_related_isSet = false;
    m_related_isValid = false;
}

void OAIAccountResource_relationships_transactions_links::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAccountResource_relationships_transactions_links::fromJsonObject(QJsonObject json) {

    m_related_isValid = ::OpenAPI::fromJsonValue(m_related, json[QString("related")]);
    m_related_isSet = !json[QString("related")].isNull() && m_related_isValid;
}

QString OAIAccountResource_relationships_transactions_links::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAccountResource_relationships_transactions_links::asJsonObject() const {
    QJsonObject obj;
    if (m_related_isSet) {
        obj.insert(QString("related"), ::OpenAPI::toJsonValue(m_related));
    }
    return obj;
}

QString OAIAccountResource_relationships_transactions_links::getRelated() const {
    return m_related;
}
void OAIAccountResource_relationships_transactions_links::setRelated(const QString &related) {
    m_related = related;
    m_related_isSet = true;
}

bool OAIAccountResource_relationships_transactions_links::is_related_Set() const{
    return m_related_isSet;
}

bool OAIAccountResource_relationships_transactions_links::is_related_Valid() const{
    return m_related_isValid;
}

bool OAIAccountResource_relationships_transactions_links::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_related_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAccountResource_relationships_transactions_links::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_related_isValid && true;
}

} // namespace OpenAPI

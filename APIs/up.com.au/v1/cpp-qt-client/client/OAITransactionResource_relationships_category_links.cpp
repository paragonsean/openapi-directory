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

#include "OAITransactionResource_relationships_category_links.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITransactionResource_relationships_category_links::OAITransactionResource_relationships_category_links(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITransactionResource_relationships_category_links::OAITransactionResource_relationships_category_links() {
    this->initializeModel();
}

OAITransactionResource_relationships_category_links::~OAITransactionResource_relationships_category_links() {}

void OAITransactionResource_relationships_category_links::initializeModel() {

    m_related_isSet = false;
    m_related_isValid = false;

    m_self_isSet = false;
    m_self_isValid = false;
}

void OAITransactionResource_relationships_category_links::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITransactionResource_relationships_category_links::fromJsonObject(QJsonObject json) {

    m_related_isValid = ::OpenAPI::fromJsonValue(m_related, json[QString("related")]);
    m_related_isSet = !json[QString("related")].isNull() && m_related_isValid;

    m_self_isValid = ::OpenAPI::fromJsonValue(m_self, json[QString("self")]);
    m_self_isSet = !json[QString("self")].isNull() && m_self_isValid;
}

QString OAITransactionResource_relationships_category_links::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITransactionResource_relationships_category_links::asJsonObject() const {
    QJsonObject obj;
    if (m_related_isSet) {
        obj.insert(QString("related"), ::OpenAPI::toJsonValue(m_related));
    }
    if (m_self_isSet) {
        obj.insert(QString("self"), ::OpenAPI::toJsonValue(m_self));
    }
    return obj;
}

QString OAITransactionResource_relationships_category_links::getRelated() const {
    return m_related;
}
void OAITransactionResource_relationships_category_links::setRelated(const QString &related) {
    m_related = related;
    m_related_isSet = true;
}

bool OAITransactionResource_relationships_category_links::is_related_Set() const{
    return m_related_isSet;
}

bool OAITransactionResource_relationships_category_links::is_related_Valid() const{
    return m_related_isValid;
}

QString OAITransactionResource_relationships_category_links::getSelf() const {
    return m_self;
}
void OAITransactionResource_relationships_category_links::setSelf(const QString &self) {
    m_self = self;
    m_self_isSet = true;
}

bool OAITransactionResource_relationships_category_links::is_self_Set() const{
    return m_self_isSet;
}

bool OAITransactionResource_relationships_category_links::is_self_Valid() const{
    return m_self_isValid;
}

bool OAITransactionResource_relationships_category_links::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_related_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_self_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITransactionResource_relationships_category_links::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_self_isValid && true;
}

} // namespace OpenAPI

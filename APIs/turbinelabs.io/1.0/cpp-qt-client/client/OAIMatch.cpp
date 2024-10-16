/**
 * Turbine Labs API
 * The Turbine Labs API provides CRUD operations for core object types, and is mostly RESTy. The easiest way to interact with the API is with [tbnctl](https://docs.turbinelabs.io/advanced/tbnctl.html). If you want to make direct HTTP calls, however, you can obtain an access token using tbnctl, and then pass it in the Authorization header, prefixed by `Token `: ```console curl -H \"Authorization: Token <access token>\" https://api.turbinelabs.io/v1.0/cluster ``` 
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMatch.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMatch::OAIMatch(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMatch::OAIMatch() {
    this->initializeModel();
}

OAIMatch::~OAIMatch() {}

void OAIMatch::initializeModel() {

    m_behavior_isSet = false;
    m_behavior_isValid = false;

    m_from_isSet = false;
    m_from_isValid = false;

    m_kind_isSet = false;
    m_kind_isValid = false;

    m_to_isSet = false;
    m_to_isValid = false;
}

void OAIMatch::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMatch::fromJsonObject(QJsonObject json) {

    m_behavior_isValid = ::OpenAPI::fromJsonValue(m_behavior, json[QString("behavior")]);
    m_behavior_isSet = !json[QString("behavior")].isNull() && m_behavior_isValid;

    m_from_isValid = ::OpenAPI::fromJsonValue(m_from, json[QString("from")]);
    m_from_isSet = !json[QString("from")].isNull() && m_from_isValid;

    m_kind_isValid = ::OpenAPI::fromJsonValue(m_kind, json[QString("kind")]);
    m_kind_isSet = !json[QString("kind")].isNull() && m_kind_isValid;

    m_to_isValid = ::OpenAPI::fromJsonValue(m_to, json[QString("to")]);
    m_to_isSet = !json[QString("to")].isNull() && m_to_isValid;
}

QString OAIMatch::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMatch::asJsonObject() const {
    QJsonObject obj;
    if (m_behavior_isSet) {
        obj.insert(QString("behavior"), ::OpenAPI::toJsonValue(m_behavior));
    }
    if (m_from.isSet()) {
        obj.insert(QString("from"), ::OpenAPI::toJsonValue(m_from));
    }
    if (m_kind_isSet) {
        obj.insert(QString("kind"), ::OpenAPI::toJsonValue(m_kind));
    }
    if (m_to.isSet()) {
        obj.insert(QString("to"), ::OpenAPI::toJsonValue(m_to));
    }
    return obj;
}

QString OAIMatch::getBehavior() const {
    return m_behavior;
}
void OAIMatch::setBehavior(const QString &behavior) {
    m_behavior = behavior;
    m_behavior_isSet = true;
}

bool OAIMatch::is_behavior_Set() const{
    return m_behavior_isSet;
}

bool OAIMatch::is_behavior_Valid() const{
    return m_behavior_isValid;
}

OAIMetadatum OAIMatch::getFrom() const {
    return m_from;
}
void OAIMatch::setFrom(const OAIMetadatum &from) {
    m_from = from;
    m_from_isSet = true;
}

bool OAIMatch::is_from_Set() const{
    return m_from_isSet;
}

bool OAIMatch::is_from_Valid() const{
    return m_from_isValid;
}

QString OAIMatch::getKind() const {
    return m_kind;
}
void OAIMatch::setKind(const QString &kind) {
    m_kind = kind;
    m_kind_isSet = true;
}

bool OAIMatch::is_kind_Set() const{
    return m_kind_isSet;
}

bool OAIMatch::is_kind_Valid() const{
    return m_kind_isValid;
}

OAIMetadatum OAIMatch::getTo() const {
    return m_to;
}
void OAIMatch::setTo(const OAIMetadatum &to) {
    m_to = to;
    m_to_isSet = true;
}

bool OAIMatch::is_to_Set() const{
    return m_to_isSet;
}

bool OAIMatch::is_to_Valid() const{
    return m_to_isValid;
}

bool OAIMatch::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_behavior_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_from.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_kind_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_to.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMatch::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

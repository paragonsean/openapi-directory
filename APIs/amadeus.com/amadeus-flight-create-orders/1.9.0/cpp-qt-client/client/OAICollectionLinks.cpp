/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICollectionLinks.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICollectionLinks::OAICollectionLinks(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICollectionLinks::OAICollectionLinks() {
    this->initializeModel();
}

OAICollectionLinks::~OAICollectionLinks() {}

void OAICollectionLinks::initializeModel() {

    m_first_isSet = false;
    m_first_isValid = false;

    m_last_isSet = false;
    m_last_isValid = false;

    m_next_isSet = false;
    m_next_isValid = false;

    m_previous_isSet = false;
    m_previous_isValid = false;

    m_self_isSet = false;
    m_self_isValid = false;

    m_up_isSet = false;
    m_up_isValid = false;
}

void OAICollectionLinks::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICollectionLinks::fromJsonObject(QJsonObject json) {

    m_first_isValid = ::OpenAPI::fromJsonValue(m_first, json[QString("first")]);
    m_first_isSet = !json[QString("first")].isNull() && m_first_isValid;

    m_last_isValid = ::OpenAPI::fromJsonValue(m_last, json[QString("last")]);
    m_last_isSet = !json[QString("last")].isNull() && m_last_isValid;

    m_next_isValid = ::OpenAPI::fromJsonValue(m_next, json[QString("next")]);
    m_next_isSet = !json[QString("next")].isNull() && m_next_isValid;

    m_previous_isValid = ::OpenAPI::fromJsonValue(m_previous, json[QString("previous")]);
    m_previous_isSet = !json[QString("previous")].isNull() && m_previous_isValid;

    m_self_isValid = ::OpenAPI::fromJsonValue(m_self, json[QString("self")]);
    m_self_isSet = !json[QString("self")].isNull() && m_self_isValid;

    m_up_isValid = ::OpenAPI::fromJsonValue(m_up, json[QString("up")]);
    m_up_isSet = !json[QString("up")].isNull() && m_up_isValid;
}

QString OAICollectionLinks::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICollectionLinks::asJsonObject() const {
    QJsonObject obj;
    if (m_first_isSet) {
        obj.insert(QString("first"), ::OpenAPI::toJsonValue(m_first));
    }
    if (m_last_isSet) {
        obj.insert(QString("last"), ::OpenAPI::toJsonValue(m_last));
    }
    if (m_next_isSet) {
        obj.insert(QString("next"), ::OpenAPI::toJsonValue(m_next));
    }
    if (m_previous_isSet) {
        obj.insert(QString("previous"), ::OpenAPI::toJsonValue(m_previous));
    }
    if (m_self_isSet) {
        obj.insert(QString("self"), ::OpenAPI::toJsonValue(m_self));
    }
    if (m_up_isSet) {
        obj.insert(QString("up"), ::OpenAPI::toJsonValue(m_up));
    }
    return obj;
}

QString OAICollectionLinks::getFirst() const {
    return m_first;
}
void OAICollectionLinks::setFirst(const QString &first) {
    m_first = first;
    m_first_isSet = true;
}

bool OAICollectionLinks::is_first_Set() const{
    return m_first_isSet;
}

bool OAICollectionLinks::is_first_Valid() const{
    return m_first_isValid;
}

QString OAICollectionLinks::getLast() const {
    return m_last;
}
void OAICollectionLinks::setLast(const QString &last) {
    m_last = last;
    m_last_isSet = true;
}

bool OAICollectionLinks::is_last_Set() const{
    return m_last_isSet;
}

bool OAICollectionLinks::is_last_Valid() const{
    return m_last_isValid;
}

QString OAICollectionLinks::getNext() const {
    return m_next;
}
void OAICollectionLinks::setNext(const QString &next) {
    m_next = next;
    m_next_isSet = true;
}

bool OAICollectionLinks::is_next_Set() const{
    return m_next_isSet;
}

bool OAICollectionLinks::is_next_Valid() const{
    return m_next_isValid;
}

QString OAICollectionLinks::getPrevious() const {
    return m_previous;
}
void OAICollectionLinks::setPrevious(const QString &previous) {
    m_previous = previous;
    m_previous_isSet = true;
}

bool OAICollectionLinks::is_previous_Set() const{
    return m_previous_isSet;
}

bool OAICollectionLinks::is_previous_Valid() const{
    return m_previous_isValid;
}

QString OAICollectionLinks::getSelf() const {
    return m_self;
}
void OAICollectionLinks::setSelf(const QString &self) {
    m_self = self;
    m_self_isSet = true;
}

bool OAICollectionLinks::is_self_Set() const{
    return m_self_isSet;
}

bool OAICollectionLinks::is_self_Valid() const{
    return m_self_isValid;
}

QString OAICollectionLinks::getUp() const {
    return m_up;
}
void OAICollectionLinks::setUp(const QString &up) {
    m_up = up;
    m_up_isSet = true;
}

bool OAICollectionLinks::is_up_Set() const{
    return m_up_isSet;
}

bool OAICollectionLinks::is_up_Valid() const{
    return m_up_isValid;
}

bool OAICollectionLinks::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_first_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_last_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_next_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_previous_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_self_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_up_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICollectionLinks::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

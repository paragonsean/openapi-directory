/**
 * Seatmap Display
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAILink.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAILink::OAILink(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAILink::OAILink() {
    this->initializeModel();
}

OAILink::~OAILink() {}

void OAILink::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_href_isSet = false;
    m_href_isValid = false;

    m_methods_isSet = false;
    m_methods_isValid = false;
}

void OAILink::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAILink::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_href_isValid = ::OpenAPI::fromJsonValue(m_href, json[QString("href")]);
    m_href_isSet = !json[QString("href")].isNull() && m_href_isValid;

    m_methods_isValid = ::OpenAPI::fromJsonValue(m_methods, json[QString("methods")]);
    m_methods_isSet = !json[QString("methods")].isNull() && m_methods_isValid;
}

QString OAILink::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAILink::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_href_isSet) {
        obj.insert(QString("href"), ::OpenAPI::toJsonValue(m_href));
    }
    if (m_methods.size() > 0) {
        obj.insert(QString("methods"), ::OpenAPI::toJsonValue(m_methods));
    }
    return obj;
}

qint32 OAILink::getCount() const {
    return m_count;
}
void OAILink::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAILink::is_count_Set() const{
    return m_count_isSet;
}

bool OAILink::is_count_Valid() const{
    return m_count_isValid;
}

QString OAILink::getHref() const {
    return m_href;
}
void OAILink::setHref(const QString &href) {
    m_href = href;
    m_href_isSet = true;
}

bool OAILink::is_href_Set() const{
    return m_href_isSet;
}

bool OAILink::is_href_Valid() const{
    return m_href_isValid;
}

QList<QString> OAILink::getMethods() const {
    return m_methods;
}
void OAILink::setMethods(const QList<QString> &methods) {
    m_methods = methods;
    m_methods_isSet = true;
}

bool OAILink::is_methods_Set() const{
    return m_methods_isSet;
}

bool OAILink::is_methods_Valid() const{
    return m_methods_isValid;
}

bool OAILink::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_href_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_methods.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAILink::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_href_isValid && true;
}

} // namespace OpenAPI

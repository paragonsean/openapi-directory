/**
 * Travel Recommendations API
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMeta.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMeta::OAIMeta(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMeta::OAIMeta() {
    this->initializeModel();
}

OAIMeta::~OAIMeta() {}

void OAIMeta::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;
}

void OAIMeta::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMeta::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;
}

QString OAIMeta::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMeta::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_links.isSet()) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    return obj;
}

qint64 OAIMeta::getCount() const {
    return m_count;
}
void OAIMeta::setCount(const qint64 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAIMeta::is_count_Set() const{
    return m_count_isSet;
}

bool OAIMeta::is_count_Valid() const{
    return m_count_isValid;
}

OAILinks OAIMeta::getLinks() const {
    return m_links;
}
void OAIMeta::setLinks(const OAILinks &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIMeta::is_links_Set() const{
    return m_links_isSet;
}

bool OAIMeta::is_links_Valid() const{
    return m_links_isValid;
}

bool OAIMeta::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_count_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_links.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMeta::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

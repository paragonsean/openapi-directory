/**
 * Safe Place
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.     Please also be aware that our test environment is based on a subset of the production, this API in test only returns a few selected cities. You can find the list in our **[data collection](https://github.com/amadeus4dev/data-collection)**.
 *
 * The version of the OpenAPI document: 1.0.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAICollection_Meta.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICollection_Meta::OAICollection_Meta(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICollection_Meta::OAICollection_Meta() {
    this->initializeModel();
}

OAICollection_Meta::~OAICollection_Meta() {}

void OAICollection_Meta::initializeModel() {

    m_count_isSet = false;
    m_count_isValid = false;

    m_links_isSet = false;
    m_links_isValid = false;
}

void OAICollection_Meta::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICollection_Meta::fromJsonObject(QJsonObject json) {

    m_count_isValid = ::OpenAPI::fromJsonValue(m_count, json[QString("count")]);
    m_count_isSet = !json[QString("count")].isNull() && m_count_isValid;

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;
}

QString OAICollection_Meta::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICollection_Meta::asJsonObject() const {
    QJsonObject obj;
    if (m_count_isSet) {
        obj.insert(QString("count"), ::OpenAPI::toJsonValue(m_count));
    }
    if (m_links.isSet()) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    return obj;
}

qint32 OAICollection_Meta::getCount() const {
    return m_count;
}
void OAICollection_Meta::setCount(const qint32 &count) {
    m_count = count;
    m_count_isSet = true;
}

bool OAICollection_Meta::is_count_Set() const{
    return m_count_isSet;
}

bool OAICollection_Meta::is_count_Valid() const{
    return m_count_isValid;
}

OAICollectionLinks OAICollection_Meta::getLinks() const {
    return m_links;
}
void OAICollection_Meta::setLinks(const OAICollectionLinks &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAICollection_Meta::is_links_Set() const{
    return m_links_isSet;
}

bool OAICollection_Meta::is_links_Valid() const{
    return m_links_isValid;
}

bool OAICollection_Meta::isSet() const {
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

bool OAICollection_Meta::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

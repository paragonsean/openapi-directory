/**
 * Image Search Client
 * The Image Search API lets you send a search query to Bing and get back a list of relevant images. This section provides technical details about the query parameters and headers that you use to request images and the JSON response objects that contain them. For examples that show how to make requests, see [Searching the Web for Images](https://docs.microsoft.com/azure/cognitive-services/bing-image-search/search-the-web).
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIIdentifiable.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIIdentifiable::OAIIdentifiable(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIIdentifiable::OAIIdentifiable() {
    this->initializeModel();
}

OAIIdentifiable::~OAIIdentifiable() {}

void OAIIdentifiable::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m__type_isSet = false;
    m__type_isValid = false;
}

void OAIIdentifiable::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIIdentifiable::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m__type_isValid = ::OpenAPI::fromJsonValue(m__type, json[QString("_type")]);
    m__type_isSet = !json[QString("_type")].isNull() && m__type_isValid;
}

QString OAIIdentifiable::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIIdentifiable::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m__type_isSet) {
        obj.insert(QString("_type"), ::OpenAPI::toJsonValue(m__type));
    }
    return obj;
}

QString OAIIdentifiable::getId() const {
    return m_id;
}
void OAIIdentifiable::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIIdentifiable::is_id_Set() const{
    return m_id_isSet;
}

bool OAIIdentifiable::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIIdentifiable::getType() const {
    return m__type;
}
void OAIIdentifiable::setType(const QString &_type) {
    m__type = _type;
    m__type_isSet = true;
}

bool OAIIdentifiable::is__type_Set() const{
    return m__type_isSet;
}

bool OAIIdentifiable::is__type_Valid() const{
    return m__type_isValid;
}

bool OAIIdentifiable::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m__type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIIdentifiable::isValid() const {
    // only required properties are required for the object to be considered valid
    return m__type_isValid && true;
}

} // namespace OpenAPI

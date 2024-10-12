/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITypes_with_id_types_type_inner.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITypes_with_id_types_type_inner::OAITypes_with_id_types_type_inner(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITypes_with_id_types_type_inner::OAITypes_with_id_types_type_inner() {
    this->initializeModel();
}

OAITypes_with_id_types_type_inner::~OAITypes_with_id_types_type_inner() {}

void OAITypes_with_id_types_type_inner::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_types_isSet = false;
    m_types_isValid = false;
}

void OAITypes_with_id_types_type_inner::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITypes_with_id_types_type_inner::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_types_isValid = ::OpenAPI::fromJsonValue(m_types, json[QString("types")]);
    m_types_isSet = !json[QString("types")].isNull() && m_types_isValid;
}

QString OAITypes_with_id_types_type_inner::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITypes_with_id_types_type_inner::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_types.isSet()) {
        obj.insert(QString("types"), ::OpenAPI::toJsonValue(m_types));
    }
    return obj;
}

QString OAITypes_with_id_types_type_inner::getId() const {
    return m_id;
}
void OAITypes_with_id_types_type_inner::setId(const QString &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITypes_with_id_types_type_inner::is_id_Set() const{
    return m_id_isSet;
}

bool OAITypes_with_id_types_type_inner::is_id_Valid() const{
    return m_id_isValid;
}

OAITypes_with_id_types_type_inner_types OAITypes_with_id_types_type_inner::getTypes() const {
    return m_types;
}
void OAITypes_with_id_types_type_inner::setTypes(const OAITypes_with_id_types_type_inner_types &types) {
    m_types = types;
    m_types_isSet = true;
}

bool OAITypes_with_id_types_type_inner::is_types_Set() const{
    return m_types_isSet;
}

bool OAITypes_with_id_types_type_inner::is_types_Valid() const{
    return m_types_isValid;
}

bool OAITypes_with_id_types_type_inner::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_types.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITypes_with_id_types_type_inner::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_types_isValid && true;
}

} // namespace OpenAPI

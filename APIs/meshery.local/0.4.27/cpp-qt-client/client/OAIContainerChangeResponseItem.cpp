/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIContainerChangeResponseItem.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIContainerChangeResponseItem::OAIContainerChangeResponseItem(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIContainerChangeResponseItem::OAIContainerChangeResponseItem() {
    this->initializeModel();
}

OAIContainerChangeResponseItem::~OAIContainerChangeResponseItem() {}

void OAIContainerChangeResponseItem::initializeModel() {

    m_kind_isSet = false;
    m_kind_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;
}

void OAIContainerChangeResponseItem::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIContainerChangeResponseItem::fromJsonObject(QJsonObject json) {

    m_kind_isValid = ::OpenAPI::fromJsonValue(m_kind, json[QString("Kind")]);
    m_kind_isSet = !json[QString("Kind")].isNull() && m_kind_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("Path")]);
    m_path_isSet = !json[QString("Path")].isNull() && m_path_isValid;
}

QString OAIContainerChangeResponseItem::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIContainerChangeResponseItem::asJsonObject() const {
    QJsonObject obj;
    if (m_kind_isSet) {
        obj.insert(QString("Kind"), ::OpenAPI::toJsonValue(m_kind));
    }
    if (m_path_isSet) {
        obj.insert(QString("Path"), ::OpenAPI::toJsonValue(m_path));
    }
    return obj;
}

qint32 OAIContainerChangeResponseItem::getKind() const {
    return m_kind;
}
void OAIContainerChangeResponseItem::setKind(const qint32 &kind) {
    m_kind = kind;
    m_kind_isSet = true;
}

bool OAIContainerChangeResponseItem::is_kind_Set() const{
    return m_kind_isSet;
}

bool OAIContainerChangeResponseItem::is_kind_Valid() const{
    return m_kind_isValid;
}

QString OAIContainerChangeResponseItem::getPath() const {
    return m_path;
}
void OAIContainerChangeResponseItem::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAIContainerChangeResponseItem::is_path_Set() const{
    return m_path_isSet;
}

bool OAIContainerChangeResponseItem::is_path_Valid() const{
    return m_path_isValid;
}

bool OAIContainerChangeResponseItem::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_kind_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIContainerChangeResponseItem::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_kind_isValid && m_path_isValid && true;
}

} // namespace OpenAPI

/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIMasterUser_masterUser_data.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIMasterUser_masterUser_data::OAIMasterUser_masterUser_data(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIMasterUser_masterUser_data::OAIMasterUser_masterUser_data() {
    this->initializeModel();
}

OAIMasterUser_masterUser_data::~OAIMasterUser_masterUser_data() {}

void OAIMasterUser_masterUser_data::initializeModel() {

    m_id_isSet = false;
    m_id_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIMasterUser_masterUser_data::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIMasterUser_masterUser_data::fromJsonObject(QJsonObject json) {

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIMasterUser_masterUser_data::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIMasterUser_masterUser_data::asJsonObject() const {
    QJsonObject obj;
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

qint32 OAIMasterUser_masterUser_data::getId() const {
    return m_id;
}
void OAIMasterUser_masterUser_data::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAIMasterUser_masterUser_data::is_id_Set() const{
    return m_id_isSet;
}

bool OAIMasterUser_masterUser_data::is_id_Valid() const{
    return m_id_isValid;
}

QString OAIMasterUser_masterUser_data::getType() const {
    return m_type;
}
void OAIMasterUser_masterUser_data::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIMasterUser_masterUser_data::is_type_Set() const{
    return m_type_isSet;
}

bool OAIMasterUser_masterUser_data::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIMasterUser_masterUser_data::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIMasterUser_masterUser_data::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

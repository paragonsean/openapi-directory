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

#include "OAICohortSeed.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAICohortSeed::OAICohortSeed(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAICohortSeed::OAICohortSeed() {
    this->initializeModel();
}

OAICohortSeed::~OAICohortSeed() {}

void OAICohortSeed::initializeModel() {

    m_name_isSet = false;
    m_name_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;

    m_use_zero_value_seed_isSet = false;
    m_use_zero_value_seed_isValid = false;
}

void OAICohortSeed::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAICohortSeed::fromJsonObject(QJsonObject json) {

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;

    m_use_zero_value_seed_isValid = ::OpenAPI::fromJsonValue(m_use_zero_value_seed, json[QString("use_zero_value_seed")]);
    m_use_zero_value_seed_isSet = !json[QString("use_zero_value_seed")].isNull() && m_use_zero_value_seed_isValid;
}

QString OAICohortSeed::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAICohortSeed::asJsonObject() const {
    QJsonObject obj;
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    if (m_use_zero_value_seed_isSet) {
        obj.insert(QString("use_zero_value_seed"), ::OpenAPI::toJsonValue(m_use_zero_value_seed));
    }
    return obj;
}

QString OAICohortSeed::getName() const {
    return m_name;
}
void OAICohortSeed::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAICohortSeed::is_name_Set() const{
    return m_name_isSet;
}

bool OAICohortSeed::is_name_Valid() const{
    return m_name_isValid;
}

QString OAICohortSeed::getType() const {
    return m_type;
}
void OAICohortSeed::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAICohortSeed::is_type_Set() const{
    return m_type_isSet;
}

bool OAICohortSeed::is_type_Valid() const{
    return m_type_isValid;
}

bool OAICohortSeed::isUseZeroValueSeed() const {
    return m_use_zero_value_seed;
}
void OAICohortSeed::setUseZeroValueSeed(const bool &use_zero_value_seed) {
    m_use_zero_value_seed = use_zero_value_seed;
    m_use_zero_value_seed_isSet = true;
}

bool OAICohortSeed::is_use_zero_value_seed_Set() const{
    return m_use_zero_value_seed_isSet;
}

bool OAICohortSeed::is_use_zero_value_seed_Valid() const{
    return m_use_zero_value_seed_isValid;
}

bool OAICohortSeed::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_use_zero_value_seed_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAICohortSeed::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

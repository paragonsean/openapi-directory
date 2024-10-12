/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIJsonPatchOperation.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIJsonPatchOperation::OAIJsonPatchOperation(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIJsonPatchOperation::OAIJsonPatchOperation() {
    this->initializeModel();
}

OAIJsonPatchOperation::~OAIJsonPatchOperation() {}

void OAIJsonPatchOperation::initializeModel() {

    m_from_isSet = false;
    m_from_isValid = false;

    m_op_isSet = false;
    m_op_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;

    m_value_isSet = false;
    m_value_isValid = false;
}

void OAIJsonPatchOperation::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIJsonPatchOperation::fromJsonObject(QJsonObject json) {

    m_from_isValid = ::OpenAPI::fromJsonValue(m_from, json[QString("from")]);
    m_from_isSet = !json[QString("from")].isNull() && m_from_isValid;

    m_op_isValid = ::OpenAPI::fromJsonValue(m_op, json[QString("op")]);
    m_op_isSet = !json[QString("op")].isNull() && m_op_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;

    m_value_isValid = ::OpenAPI::fromJsonValue(m_value, json[QString("value")]);
    m_value_isSet = !json[QString("value")].isNull() && m_value_isValid;
}

QString OAIJsonPatchOperation::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIJsonPatchOperation::asJsonObject() const {
    QJsonObject obj;
    if (m_from_isSet) {
        obj.insert(QString("from"), ::OpenAPI::toJsonValue(m_from));
    }
    if (m_op_isSet) {
        obj.insert(QString("op"), ::OpenAPI::toJsonValue(m_op));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    if (m_value_isSet) {
        obj.insert(QString("value"), ::OpenAPI::toJsonValue(m_value));
    }
    return obj;
}

QString OAIJsonPatchOperation::getFrom() const {
    return m_from;
}
void OAIJsonPatchOperation::setFrom(const QString &from) {
    m_from = from;
    m_from_isSet = true;
}

bool OAIJsonPatchOperation::is_from_Set() const{
    return m_from_isSet;
}

bool OAIJsonPatchOperation::is_from_Valid() const{
    return m_from_isValid;
}

QString OAIJsonPatchOperation::getOp() const {
    return m_op;
}
void OAIJsonPatchOperation::setOp(const QString &op) {
    m_op = op;
    m_op_isSet = true;
}

bool OAIJsonPatchOperation::is_op_Set() const{
    return m_op_isSet;
}

bool OAIJsonPatchOperation::is_op_Valid() const{
    return m_op_isValid;
}

QString OAIJsonPatchOperation::getPath() const {
    return m_path;
}
void OAIJsonPatchOperation::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAIJsonPatchOperation::is_path_Set() const{
    return m_path_isSet;
}

bool OAIJsonPatchOperation::is_path_Valid() const{
    return m_path_isValid;
}

OAIObject OAIJsonPatchOperation::getValue() const {
    return m_value;
}
void OAIJsonPatchOperation::setValue(const OAIObject &value) {
    m_value = value;
    m_value_isSet = true;
}

bool OAIJsonPatchOperation::is_value_Set() const{
    return m_value_isSet;
}

bool OAIJsonPatchOperation::is_value_Valid() const{
    return m_value_isValid;
}

bool OAIJsonPatchOperation::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_from_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_op_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_value_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIJsonPatchOperation::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

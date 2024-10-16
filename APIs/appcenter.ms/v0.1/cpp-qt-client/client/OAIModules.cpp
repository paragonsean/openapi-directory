/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIModules.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIModules::OAIModules(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIModules::OAIModules() {
    this->initializeModel();
}

OAIModules::~OAIModules() {}

void OAIModules::initializeModel() {

    m_modules_isSet = false;
    m_modules_isValid = false;
}

void OAIModules::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIModules::fromJsonObject(QJsonObject json) {

    if(json["modules"].isObject()){
        auto varmap = json["modules"].toObject().toVariantMap();
        m_modules_isValid = true;
        if(varmap.count() > 0){
            for(auto val : varmap.keys()){
                QMap<QString, bool> item;
                auto jval = QJsonValue::fromVariant(varmap.value(val));
                m_modules_isValid &= ::OpenAPI::fromJsonValue(item, jval);
                m_modules_isSet &= !jval.isNull() && m_modules_isValid;
                m_modules.insert(m_modules.end(), val, item);
            }
        }
    }
}

QString OAIModules::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIModules::asJsonObject() const {
    QJsonObject obj;
    if (m_modules.size() > 0) {
        
        obj.insert(QString("modules"), toJsonValue(m_modules));
    }
    return obj;
}

QMap<QString, QMap<QString, bool>> OAIModules::getModules() const {
    return m_modules;
}
void OAIModules::setModules(const QMap<QString, QMap<QString, bool>> &modules) {
    m_modules = modules;
    m_modules_isSet = true;
}

bool OAIModules::is_modules_Set() const{
    return m_modules_isSet;
}

bool OAIModules::is_modules_Valid() const{
    return m_modules_isValid;
}

bool OAIModules::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_modules.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIModules::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

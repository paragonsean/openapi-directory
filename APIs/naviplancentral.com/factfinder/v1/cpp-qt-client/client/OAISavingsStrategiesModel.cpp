/**
 * Advicent.FactFinderService
 * An API for accessing the NaviPlan Fact Finder.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISavingsStrategiesModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISavingsStrategiesModel::OAISavingsStrategiesModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISavingsStrategiesModel::OAISavingsStrategiesModel() {
    this->initializeModel();
}

OAISavingsStrategiesModel::~OAISavingsStrategiesModel() {}

void OAISavingsStrategiesModel::initializeModel() {

    m_savings_strategies_isSet = false;
    m_savings_strategies_isValid = false;
}

void OAISavingsStrategiesModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISavingsStrategiesModel::fromJsonObject(QJsonObject json) {

    m_savings_strategies_isValid = ::OpenAPI::fromJsonValue(m_savings_strategies, json[QString("savingsStrategies")]);
    m_savings_strategies_isSet = !json[QString("savingsStrategies")].isNull() && m_savings_strategies_isValid;
}

QString OAISavingsStrategiesModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISavingsStrategiesModel::asJsonObject() const {
    QJsonObject obj;
    if (m_savings_strategies.size() > 0) {
        obj.insert(QString("savingsStrategies"), ::OpenAPI::toJsonValue(m_savings_strategies));
    }
    return obj;
}

QList<OAISavingsStrategyWithIdModel> OAISavingsStrategiesModel::getSavingsStrategies() const {
    return m_savings_strategies;
}
void OAISavingsStrategiesModel::setSavingsStrategies(const QList<OAISavingsStrategyWithIdModel> &savings_strategies) {
    m_savings_strategies = savings_strategies;
    m_savings_strategies_isSet = true;
}

bool OAISavingsStrategiesModel::is_savings_strategies_Set() const{
    return m_savings_strategies_isSet;
}

bool OAISavingsStrategiesModel::is_savings_strategies_Valid() const{
    return m_savings_strategies_isValid;
}

bool OAISavingsStrategiesModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_savings_strategies.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISavingsStrategiesModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

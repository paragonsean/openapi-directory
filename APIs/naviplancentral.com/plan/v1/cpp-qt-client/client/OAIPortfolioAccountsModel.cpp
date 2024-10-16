/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIPortfolioAccountsModel.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIPortfolioAccountsModel::OAIPortfolioAccountsModel(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIPortfolioAccountsModel::OAIPortfolioAccountsModel() {
    this->initializeModel();
}

OAIPortfolioAccountsModel::~OAIPortfolioAccountsModel() {}

void OAIPortfolioAccountsModel::initializeModel() {

    m_links_isSet = false;
    m_links_isValid = false;

    m_portfolio_accounts_isSet = false;
    m_portfolio_accounts_isValid = false;
}

void OAIPortfolioAccountsModel::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIPortfolioAccountsModel::fromJsonObject(QJsonObject json) {

    m_links_isValid = ::OpenAPI::fromJsonValue(m_links, json[QString("links")]);
    m_links_isSet = !json[QString("links")].isNull() && m_links_isValid;

    m_portfolio_accounts_isValid = ::OpenAPI::fromJsonValue(m_portfolio_accounts, json[QString("portfolioAccounts")]);
    m_portfolio_accounts_isSet = !json[QString("portfolioAccounts")].isNull() && m_portfolio_accounts_isValid;
}

QString OAIPortfolioAccountsModel::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIPortfolioAccountsModel::asJsonObject() const {
    QJsonObject obj;
    if (m_links.size() > 0) {
        obj.insert(QString("links"), ::OpenAPI::toJsonValue(m_links));
    }
    if (m_portfolio_accounts.size() > 0) {
        obj.insert(QString("portfolioAccounts"), ::OpenAPI::toJsonValue(m_portfolio_accounts));
    }
    return obj;
}

QList<OAIObjectLink> OAIPortfolioAccountsModel::getLinks() const {
    return m_links;
}
void OAIPortfolioAccountsModel::setLinks(const QList<OAIObjectLink> &links) {
    m_links = links;
    m_links_isSet = true;
}

bool OAIPortfolioAccountsModel::is_links_Set() const{
    return m_links_isSet;
}

bool OAIPortfolioAccountsModel::is_links_Valid() const{
    return m_links_isValid;
}

QList<OAIIPortfolioAccount> OAIPortfolioAccountsModel::getPortfolioAccounts() const {
    return m_portfolio_accounts;
}
void OAIPortfolioAccountsModel::setPortfolioAccounts(const QList<OAIIPortfolioAccount> &portfolio_accounts) {
    m_portfolio_accounts = portfolio_accounts;
    m_portfolio_accounts_isSet = true;
}

bool OAIPortfolioAccountsModel::is_portfolio_accounts_Set() const{
    return m_portfolio_accounts_isSet;
}

bool OAIPortfolioAccountsModel::is_portfolio_accounts_Valid() const{
    return m_portfolio_accounts_isValid;
}

bool OAIPortfolioAccountsModel::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_links.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_portfolio_accounts.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIPortfolioAccountsModel::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI

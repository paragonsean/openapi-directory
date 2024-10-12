/**
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAILoop____times.h
 *
 * Loop action combines a set of actions and executes it as many times as specified in the \&quot;times\&quot; parameter.
 */

#ifndef OAILoop____times_H
#define OAILoop____times_H

#include <QJsonObject>

#include "OAIAction.h"
#include <QList>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {
class OAIAction;

class OAILoop____times : public OAIObject {
public:
    OAILoop____times();
    OAILoop____times(QString json);
    ~OAILoop____times() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QList<OAIAction> getActions() const;
    void setActions(const QList<OAIAction> &actions);
    bool is_actions_Set() const;
    bool is_actions_Valid() const;

    double getTimes() const;
    void setTimes(const double &times);
    bool is_times_Set() const;
    bool is_times_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QList<OAIAction> m_actions;
    bool m_actions_isSet;
    bool m_actions_isValid;

    double m_times;
    bool m_times_isSet;
    bool m_times_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAILoop____times)

#endif // OAILoop____times_H

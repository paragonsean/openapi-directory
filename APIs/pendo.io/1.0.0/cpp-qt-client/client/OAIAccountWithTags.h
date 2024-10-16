/**
 * Pendo Feedback API
 * ## Who is this for?  This documentation is for developers creating their own integration with [Feedback's](https://www.pendo.io/product/feedback/) API. If you are doing a standard integration, there's a really easy [Javascript integration](https://help.receptive.io/hc/en-us/articles/209221969-How-to-integrate-Receptive-with-your-app) that you should know about before you go to the effort of building your own integration.  ## Authentication  API calls generally need to be authenticated. Generate an API Key at https://feedback.pendo.io/app/#/vendor/settings?section=integrate. This key should then be added to every request as a request header named 'auth-token' (preferred), or as a query parameter named 'auth-token'.  ## Endpoint  API endpoint is https://api.feedback.eu.pendo.io / https://api.feedback.us.pendo.io depending where your datacenter is located.  ## Notes  API endpoints are being added to this documentation as needed by customers. If you don't see an endpoint you need please contact support and if it exists we'll publish the docs here. The 'try it out' feature on this documentation page will probably be blocked by your browser because the Access-Control-Allow-Origin header has its value set by the Feedback server depending on your hostname.  ## Generating client code  This documentation is automatically generated from an OpenAPI spec available [here](http://apidoc.receptive.io/receptive.swagger.json). You can use Swagger to auto-generate API client code in many languages using the [Swagger Editor](http://editor.swagger.io/#/)
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@receptive.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

/*
 * OAIAccountWithTags.h
 *
 * 
 */

#ifndef OAIAccountWithTags_H
#define OAIAccountWithTags_H

#include <QJsonObject>

#include "OAIObject.h"
#include <QString>

#include "OAIEnum.h"
#include "OAIObject.h"

namespace OpenAPI {

class OAIAccountWithTags : public OAIObject {
public:
    OAIAccountWithTags();
    OAIAccountWithTags(QString json);
    ~OAIAccountWithTags() override;

    QString asJson() const override;
    QJsonObject asJsonObject() const override;
    void fromJsonObject(QJsonObject json) override;
    void fromJson(QString jsonString) override;

    QString getCreatedAt() const;
    void setCreatedAt(const QString &created_at);
    bool is_created_at_Set() const;
    bool is_created_at_Valid() const;

    QString getId() const;
    void setId(const QString &id);
    bool is_id_Set() const;
    bool is_id_Valid() const;

    bool isIsPaying() const;
    void setIsPaying(const bool &is_paying);
    bool is_is_paying_Set() const;
    bool is_is_paying_Valid() const;

    float getMonthlyValue() const;
    void setMonthlyValue(const float &monthly_value);
    bool is_monthly_value_Set() const;
    bool is_monthly_value_Valid() const;

    QString getName() const;
    void setName(const QString &name);
    bool is_name_Set() const;
    bool is_name_Valid() const;

    QString getStatus() const;
    void setStatus(const QString &status);
    bool is_status_Set() const;
    bool is_status_Valid() const;

    OAIObject getTags() const;
    void setTags(const OAIObject &tags);
    bool is_tags_Set() const;
    bool is_tags_Valid() const;

    virtual bool isSet() const override;
    virtual bool isValid() const override;

private:
    void initializeModel();

    QString m_created_at;
    bool m_created_at_isSet;
    bool m_created_at_isValid;

    QString m_id;
    bool m_id_isSet;
    bool m_id_isValid;

    bool m_is_paying;
    bool m_is_paying_isSet;
    bool m_is_paying_isValid;

    float m_monthly_value;
    bool m_monthly_value_isSet;
    bool m_monthly_value_isValid;

    QString m_name;
    bool m_name_isSet;
    bool m_name_isValid;

    QString m_status;
    bool m_status_isSet;
    bool m_status_isValid;

    OAIObject m_tags;
    bool m_tags_isSet;
    bool m_tags_isValid;
};

} // namespace OpenAPI

Q_DECLARE_METATYPE(OpenAPI::OAIAccountWithTags)

#endif // OAIAccountWithTags_H
